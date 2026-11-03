"""
Four calibration inputs for Milestone 4. Prints both signals separately.

    python calibration.py
"""

import scoring
from detector import model_signal
from stylometry import style_signal

INPUTS = {
    "clearly AI": (
        "Artificial intelligence is transforming the way we live and work in "
        "numerous ways. It offers significant benefits across a wide range of "
        "industries, including healthcare, education, and finance. Moreover, "
        "it is important to consider the ethical implications of these "
        "technologies. By fostering collaboration between researchers, "
        "policymakers, and the public, we can ensure that AI develops in a "
        "responsible and beneficial manner. In conclusion, the future of AI "
        "holds immense potential, provided that we approach it with care and "
        "foresight."
    ),
    "clearly human": (
        "ok so the bus was late AGAIN. Third time this week. I stood there "
        "like an idiot for twenty minutes, coffee going cold, watching a "
        "pigeon eat half a bagel off the pavement. Honestly? Best part of my "
        "morning. Got to work, Dev asked why I was grinning, and I couldn't "
        "even explain it. Something about that pigeon's total commitment. "
        "Anyway. Missed the standup. Nobody noticed, which is either "
        "comforting or insulting, I haven't decided."
    ),
    "formal human": (
        "The committee met on Tuesday to review the proposed amendments to the "
        "municipal zoning ordinance. After considerable deliberation, it was "
        "resolved that the height restriction for residential structures in "
        "the northern district shall remain unchanged. Several members "
        "expressed concern regarding the potential impact on existing "
        "property values; however, the majority determined that the "
        "long-term benefits to the community outweighed these considerations. "
        "A follow-up session has been scheduled for the fourteenth of next "
        "month, at which time public comment will be received."
    ),
    "lightly-edited AI": (
        "Remote work has changed how a lot of us think about our days. It "
        "gives people more flexibility, and honestly that's the big win, "
        "since commutes just vanish. But it isn't all good. Many workers say "
        "they feel isolated, and the line between home and office gets "
        "blurry fast. Companies that do it well tend to set clear "
        "expectations, check in often, and make room for real conversation. "
        "Those that don't? They usually see burnout creep in. Balance is the "
        "key, I think, and it takes ongoing effort from everyone."
    ),
}

if __name__ == "__main__":
    print(f"{'input':20} {'model':>7} {'style':>7} {'combined':>9}")
    for name, text in INPUTS.items():
        m, s = model_signal(text), style_signal(text)
        print(f"{name:20} {m:7.3f} {s:7.3f} {scoring.combine_signals(m, s):9.3f}")
