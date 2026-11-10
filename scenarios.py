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
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I'm trying my best sometimes. It's so hard :(. Sometimes I get overtaken by sadness and I feel so scared of my future. It all feels so bleak and hopeless.",
            "I wonder what type of person I'll be in the future. It's hard to discern how I will be like in 5 years let alone next month. When it starts become dark and fall comes, we start questioning who we are. and the rush to the holidays begins.",
            "Hey guys! i created a group caht to talk about our performance next week. i posted some example coreo pix. I was hoping that we could do a dark clown vibe aesthetic for our makeup. actually on 2nd thot, lol i was hopeing someone in the grou would be more konwledgeable but a week isn't enough time to youtube it. 🤣",
            "hey gurlie pop! i just was wondering if youd have some time next week to grab boba and hangout. i missed you & I was wondering how ya doing. no pressure if you're busy!",
            "Hi Jane Doe! wassup! we haven't chatted in a hot minute :P, ifyou're free next week, let's grab lunch or coffee. i have been in cavewomen mode for awhile but now i wanna see ya'll!",
            "AFter day light savings, the days rush into a dark abyss. but there is hope and solace that a new future will commence. MAriah Carey starts playing on the radio as if to bludgeon your soul into adapting the christmas vibes. whatever happened to a slow burn towards el otono?",
            "¿Preguntas? ¡hola señorita juanita! Cómo está, bien usted. Altavaz? here you come again! Man I had so many questions for you. I wanted to find the root of it all.",
            "This is my straightforward, robotic voice. Why would I lie to you? I have nothing to hide from you. I'm engaging with you like a human-being. Why would I have anything to hide? I'm being real, really real.",
            "Yesterday, I saw my friend's dance performance. He was spectacular and strong. I admired his artistic spirit.",
            "Yes, I agree to this contract. Yes, I agree to these conditions. Sure, that sounds good."
        ],
    },
        {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "That contrast is real — a 3-hour round trip for 2 hours of work and $50 is a rough trade on paper, and it makes sense that it’d throw the old remote setup into relief. At least the bus ride being easy and it only being 3 mornings a week keeps it from eating your whole week.",
            "I don't know who I will be in the future, and this is scary. I think it'll be all right.",
            "To be or not to be, that is the presumptive question.",
        ],
    },
    {
        "name": "borderline",
        "criterion": 2,
        # text that is considered borderline
        "texts": [
            "That contrast is real — a 3-hour round trip for 2 hours of work and $50 is a rough trade on paper, and it makes sense that it’d throw the old remote setup into relief.",
            "It makes complete sense that this feels hard — asking for help can feel vulnerable, especially after a career break. But you got to try.",
            "Referrals are usually most effective when they’re specific and easy to act on — you’re not asking your colleague to vouch for your whole career, just to forward your resume or say a good word internally. It's not that deep.",
            "You don’t have to do it every day either — even two or three mornings a week with a consistent spot and a consistent time could be enough to break the “don’t know what to do once I’m up” feeling. It's not all or nothing.",
            "To be or not to be, that is the presumptive question.",
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
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
