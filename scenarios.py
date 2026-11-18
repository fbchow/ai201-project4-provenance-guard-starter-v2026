"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string. 
"""

SCENARIOS = [
    {
        
        "name": "too long",
        "criterion": 1,
        "bodies": [
            {"text": "word " * 5001,  "creator_id": "eval_long_1"},   # just over the limit
            {"text": "word " * 10000, "creator_id": "eval_long_2"},
            {"text": "word " * 50000, "creator_id": "eval_long_3"},
        ],
    },
        # Criterion 2 (scoring failure -> 500) is tested by hand: it needs the
    # signal functions to raise, which no input can cause.
    {
        # Restart app.py first. Request 1 of trial 1 is the cold start and is
        # not counted; judge log_duration_ms on the rest.
        "name": "warm latency",
        "criterion": 3,
        "texts": [
            ("The committee met on Tuesday to review the proposal for the new "
             "community garden. Several neighbors spoke in favor, citing the lack "
             "of green space nearby, while others worried about parking and noise. "
             "After an hour of discussion, the chair suggested a trial season and "
             "a follow-up meeting in the spring. ") * 6
        ] * 5,
    },
    {
        "name": "input_chars",
        "criterion": 5,
        "bodies": [
            {"text": ("word " * 10)[:50],     "creator_id": "eval_chars_50"},
            {"text": ("word " * 100)[:500],   "creator_id": "eval_chars_500"},
            {"text": ("word " * 1000)[:5000], "creator_id": "eval_chars_5000"},
        ],
    },
    {
        "name": "label coverage",
        "criterion": 4,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "That contrast is real — a 3-hour round trip for 2 hours of work and $50 is a rough trade on paper, and it makes sense that it’d throw the old remote setup into relief. At least the bus ride being easy and it only being 3 mornings a week keeps it from eating your whole week.",
            "I don't know who I will be in the future, and this is scary. I think it'll be all right.",
            "To be or not to be, that is the presumptive question.",
        ],
    },
    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
