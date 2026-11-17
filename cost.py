import app as app_module
import audit

CREATOR_ID = "test_cost"
TEXT = "The quick brown fox jumps over the lazy dog."
N_TRIALS = 10
client = app_module.app.test_client()

for i in range(N_TRIALS):
    resp = client.post("/submit", json={"creator_id": CREATOR_ID, "text": TEXT})

rows = audit.read_entries(N_TRIALS)

total_time = 0
for row in rows:
    total_time += row.get("duration_ms")

avg_time = total_time / N_TRIALS
print(f"total_time: {total_time}")
print(f"avg_time: {avg_time}")
