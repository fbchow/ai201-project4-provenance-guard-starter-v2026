# Provenance Guard

---

## What This Does
1. User submits a JSON paylod with text and a creator_id.
2. The text perlexity score is calculated and converted to an interpretable model signal score.
3. The decision is logged.
4. Calculate style signal attributes: sentence length spread, type token ratio, and punctuation density.
5. Combine the scores into a single style signal store.
6. The style score is logged.
7. The model signal score and style signal score is combined.
8. Post answer
9. Log answer
<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
Perplexity, which is how surprised the model is by te text. A lower perplexity means that the text is more predictable. This signal
rewards common words in short, ordinary sentences. It returns a positive number. Typical values land roughly between 10 and 200, but that range shifts with topic and length, which is one reason the raw number isn't what we score on.

**Why that might differ between human and AI writing:**
AI writing is in general very clean and spotless with less spelling typos and grammatical mistakes.

**What it can't see:**
Some people just naturally write with short concise setences. Some authors, who write English as a second language, may write in a terse way.

### Signal two — the style signal

**What it measures:**
The shape of the text and how much it varies.

**Why that might differ between human and AI writing:**
Human text may be more varied in terms of length, punctuation use, and unique word choice.

**What it can't see:**
Deliberate hacks, like using many instances of random punctuation and chracters with no meaning. Many non-sensical unique words may also be AI generated to deliberately confuse the model.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
A weighted average that leans on the model signal, with one safeguard. If the two signals disagree by a lot, the combined score is capped just below the "AI" threshold, so a split can make us unsure but can never produce a confident AI call on its own. I chose this because a wrong accusation of a real writer costs more than missing some AI text. The style signal also has a known blind spot: it rates formal human writing as the most AI-like input, so it shouldn't be able to condemn a text alone.

**The numbers:**
- `combined = 0.65 × model_score + 0.35 × style_score` (`WEIGHT_MODEL_SIGNAL`, `WEIGHT_STYLE_SIGNAL` in `config.py`)
- If `|model_score − style_score| > 0.3` (`DISAGREEMENT_LIMIT`), then `combined = min(combined, 0.64)`, which is `AI_THRESHOLD − 0.01`.
- Both signals are 0–1, higher means more likely AI, so the output is too.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
Lightly-edited AI: the style signal reads it as 0.48 (the edits add varied punctuation and uneven sentences), while the model signal still sees predictable prose. The model score below (0.85) is illustrative, not measured yet; replace it with the real output of `python calibration.py`.

| model | style | weighted average | split > 0.3? | combined |
|---|---|---|---|---|
| 0.85 | 0.48 | 0.72 | yes (0.37) | **0.64**, capped: "unsure" |

Without the cap this would score as confident AI on a text where one signal was clearly fooled, so the rule downgrades it to "unsure". The cost is that real AI text with a fooled style signal is never flagged as confidently AI.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.0-0.35  | Probably written by a person. |
| unsure | 0.35-0.65 |Not as confident, could be either AI or human.  |
| high-confidence AI |0.65-1.00  | Probably written by AI |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
I wanted to mention being uncertain without accusing the writer.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
 $ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":  "Artificial intelligence is transforming the way we live and work in numerous ways. It offers significant benefits across a wide range of industries, including healthcare, education, and finance.Moreover, it is important to consider the ethical implications of these technologies. By fostering collaboration between researchers,   policymakers, and the public, we can ensure that AI develops in a responsible and beneficial manner. In conclusion, the future of AI holds immense potential, provided that we approach it with care and foresight",
     "creator_id": "intelligentphony67"'

```

```json
{
  "confidence": 0.749869574733391,
  "content_id": "8522e630-e78e-4094-a26d-ee0943f757a4",
  "guess": "ai",
  "label": "Probably written by AI.",
  "model_score": 0.8421,
  "style_score": 0.57858449923826
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "8522e630-e78e-4094-a26d-ee0943f757a4", "reasoning": "Had assistance but still wrote most of the text."}'
```

```json
{
  "content_id": "8522e630-e78e-4094-a26d-ee0943f757a4",
  "creator_id": null,
  "reasoning": "Had assistance but still wrote most of the text.",
  "status": "appeal"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.749869574733391,
      "content_id": "d19c0946-9cff-4bed-931e-22091ae06f25",
      "creator_id": "intelligentphony67",
      "guess": "ai",
      "label": "Probably written by AI.",
      "model_score": 0.8421,
      "status": "decided",
      "style_score": 0.57858449923826,
      "timestamp": "2026-11-04T06:13:48+00:00"
    },
    {
      "combined_score": 0.749869574733391,
      "content_id": "8522e630-e78e-4094-a26d-ee0943f757a4",
      "creator_id": "intelligentphony67",
      "guess": "ai",
      "label": "Probably written by AI.",
      "model_score": 0.8421,
      "status": "decided",
      "style_score": 0.57858449923826,
      "timestamp": "2026-11-04T06:15:02+00:00"
    },
    {
      "content_id": "8522e630-e78e-4094-a26d-ee0943f757a4",
      "creator_id": "intelligentphony67",
      "event": "appeal",
      "reasoning": "Had assistance but still wrote most of the text.",
      "status": "under_review",
      "timestamp": "2026-11-04T06:47:06+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help understanding how the payload gets passed in the Flask framework to each function route.
- *What came back:* Suggestion to directly access payload using json library.
- *What I changed:* Directly parced `creator_id` and `text` in `submit()` function from the user's json payload input.

**Moment 2**

- *What I asked for:* Help normalizing the style metrics. I originally just took the inverse of the metrics to make the direction match the interpretation of "likely AI" and "likely human".
- *What came back:* Multiple suggestions, such as taking the logit.
- *What I changed:* I didn't want to normalize the metrics using so many additional hyperparameters to keep track of and explain. I wanted to keep the scaling of the metrics simpler and interpretable rather than complex and precise.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
