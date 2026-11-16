from pathlib import Path

import pytest

import app as app_module
import audit

# One log file shared by every test and every run. It is never deleted or
# truncated, so new entries are appended to the bottom on each pytest run.
# The real audit log is never touched.
TEST_LOG_DIR = Path(__file__).parent / "test_output"
TEST_LOG_FILE = TEST_LOG_DIR / "test_audit.jsonl"


@pytest.fixture(scope="session", autouse=True)
def run_log():
    """Redirect the audit log to test_output/test_audit.jsonl for the whole run."""
    TEST_LOG_DIR.mkdir(exist_ok=True)
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(app_module.config, "LOG_DIR", TEST_LOG_DIR)
        mp.setattr(app_module.config, "AUDIT_LOG", TEST_LOG_FILE)
        yield TEST_LOG_FILE


@pytest.mark.parametrize("target", ["model_signal", "style_signal", "combine_signals"])
def test_scoring_crash_logged_as_error(monkeypatch, target):
    # Stub the signals that aren't under test so the real model never loads
    # (slow) and each case isolates exactly one failing function.
    stubs = {
        "model_signal": lambda text: 0.5,
        "style_signal": lambda text: 0.5,
        "combine_signals": lambda m, s: 0.5,
    }
    for name, stub in stubs.items():
        if name != target:
            monkeypatch.setattr(app_module, name, stub)

    def boom(*args, **kwargs):
        raise RuntimeError("simulated crash")

    # Patch the name as app.py sees it (from-imports), not detector.model_signal
    monkeypatch.setattr(app_module, target, boom)

    client = app_module.app.test_client()
    resp = client.post("/submit", json={"creator_id": "tester", "text": "hello there world"})

    # Client gets JSON, not Flask's HTML 500 page, and no exception text leaks
    assert resp.status_code == 500
    body = resp.get_json()
    assert body["error"] == "scoring failed"
    assert "simulated crash" not in resp.get_data(as_text=True)

    # The log accumulates across tests and runs, so find this request's entry
    # by its unique content_id. It must be distinguishable from a 400 rejection.
    matches = [e for e in audit.read_entries() if e.get("content_id") == body["content_id"]]
    assert len(matches) == 1
    e = matches[0]
    assert e["event"] == "error"
    assert e["status"] == "error"
    assert e["http_status"] == 500
    assert e["error"].startswith("RuntimeError")


def test_400_still_rejected():
    client = app_module.app.test_client()
    resp = client.post("/submit", json={"creator_id": "tester", "text": ""})

    assert resp.status_code == 400
    # A 400 response has no content_id, so take the entry just written (the last line).
    e = audit.read_entries()[-1]
    assert e["event"] == "rejected"
    assert e["status"] == "rejected"
