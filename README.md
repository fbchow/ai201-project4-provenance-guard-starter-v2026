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

**My limits:** 10 per minute, 100 per day

**Why those numbers and not others:**
A user that is pushing the 10 per minute limit would be submitting 5 writing samples in 30 seconds or 1 every 6 seconds. That seems like the upper bound for an technologically savvy human to be submitting their work repeatedly out of frustration or internet network lag. A user at most that is sending 200 writing submissions per day. 100 submissions divided by an average 8 hour workday is 12.5 submissions per hour. That seems like a reasonable upper bound for a person to submit writing samples. If they're submitting with greater frequency just because they make small edits, then we want to discourage that behavior anyways. It's not good practice to just make small writing submission edits and submit with that high of a frequency.
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They faildifferently — one script can look like a thousand callers, and one household. can look like one. -->
per `creator_id`

**The run of status codes when I pushed past it:**
```bash
python run_attacks.py --flood 15

15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 200
  [10/15] 200
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
============================================================

5 of 15 were rate limited. Paste the run above into your README
under **Rate Limiting**, and check GET /log recorded the rejections.

Wrote results/flood_2026-11-04_1526.md

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f04b251f-adf0-45ee-b2cf-2ba47e920878` | human | 0.326 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `e8912c27-f4e6-4be6-8b61-150d6af980de` | unsure | 0.559 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ead02ec2-94dc-4482-94c9-09d8ad239d50` | unsure | 0.617 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `103a5a40-5314-48a1-98eb-08b2e9692240` | unsure | 0.613 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c5462a88-2973-4664-abb0-c6d092e095aa` | unsure | 0.381 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `41c57b0c-8909-47d7-98b5-1fd1caa6ddf4` | unsure | 0.553 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `8570e795-b83a-4d32-b6f9-5a989652b404` | unsure | 0.608 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `259140ef-11ce-42fd-81b2-0349b9ee1496` | human | 0.338 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `910d63f9-ff51-408a-bf2f-c53df3310e72` | unsure | 0.642 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `869cb86d-70f8-496b-9c21-a535de3a3722` | ai | 0.903 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `71c9fd5b-979c-4792-a855-49539895ef10` | unsure | 0.603 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `9279237a-0def-4d80-9a00-ad482ec5ca9e` | ai | 0.703 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `e777da80-31a2-4f20-b8dd-179c3ac2de6c` | ai | 0.738 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c407e25d-b105-4c54-a349-00acdd02293e` | ai | 0.741 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `95f8e6cd-c3b8-44dc-95bb-8f616b574c0f` | ai | 0.738 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `a862cebc-0fb2-4ce7-a2fe-6b14cbca2fab` | unsure | 0.640 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `e319d194-9ce2-4d28-ac7d-7174850d7cfd` | unsure | 0.640 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `e768bfb4-b5b4-47ba-84bd-0cf1ba5b6f8c` | human | 0.344 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1bdd88fc-62bb-4667-85b2-ac7151afba21` | unsure | 0.482 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `9b83fd3b-6f2d-47eb-b035-efbb1dbabfc0` | human | 0.290 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ffe22964-2de8-4d99-92c0-839c1c6f207f` | unsure | 0.583 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d4c5124c-4435-41c0-938e-82edc798bb7e` | unsure | 0.480 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ea399a6d-d3c6-4fe6-8d2f-dc487ed98cb1` | unsure | 0.547 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `49354ac4-b52f-4d05-9e38-c8d6e5a000ea` | unsure | 0.567 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `0d5c2906-f666-46bf-a819-fa09c4465029` | human | 0.174 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `a9a1e146-fa7b-493e-927a-d136bcde27f8` | human | 0.223 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `d3cbed21-6ab7-4bae-85a8-a49bd463c3a2` | ai | 0.928 | HELD |
| MF06 | malformed | text is emoji only | 200 | `b2c67f14-e016-4f75-98a0-541a236faea3` | ai | 0.998 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `abaa171c-5692-4b6f-946b-d75e7421d388` | ai | 0.905 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `c45fc54e-5bee-47d8-ab4a-3d5c8b2a9677` | ai | 0.895 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `8362c161-d0a2-41d6-93f9-46981f727f7a` | unsure | 0.383 | BROKE |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 400 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `8a0d3f15-871a-440c-ab9f-4c764baa90b9` | human | 0.221 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | BROKE |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | BROKE |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6a817b51-d470-41f1-a6de-3185fa0a2154` | human | 0.246 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `28033300-ef24-425b-ae36-fa1f3b4526f3` | human | 0.246 |BROKE  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `de00a469-bea0-497c-b50f-80dcf68ed025` | human | 0.246 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d40d53df-d0d4-46cc-b4c6-42ba4a651e50` | human | 0.246 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1b85843e-29d0-49ef-95a0-6fd53fa8a0bf` | human | 0.246 |BROKE  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aaea6468-8bca-48ac-8447-36fc9d5db338` | human | 0.246 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b156d182-528a-4124-a619-10d59a6f5a11` | human | 0.246 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aff4013c-e9e2-421e-acd7-02680a7a7163` | human | 0.246 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `59065ddb-7f6d-4d97-ae97-c712764f81b7` | human | 0.246 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c90b16fd-71ea-44aa-845c-97b2af378d59` | human | 0.246 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```


### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "a8dcf28e-ad82-4b98-9607-37cb7da3dd3d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3258003695295389,
  "model_score": 0.1635,
  "style_score": 0.6272153415129683,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f25f2b3e-db37-4030-aa20-b21d66cee339",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7379657541025328,
  "model_score": 0.8051,
  "style_score": 0.6132878688643795,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```
### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "d5a4d219-08a4-4264-9994-135e9cc7ba97",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7030878874164761,
  "model_score": 0.7387,
  "style_score": 0.6369511069042174,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "e8255653-8374-4015-b101-056d385be835",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7406778321496121,
  "model_score": 0.8329,
  "style_score": 0.5694080918560347,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```
### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "87d27ef6-3e45-467d-9c98-ddeaf0f1319b",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7383605516391188,
  "model_score": 0.8005,
  "style_score": 0.6229587189689109,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "6532e017-32fe-46db-935b-cb4f0102855c",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5667034980567721,
  "model_score": 0.5583,
  "style_score": 0.5823099944479203,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```
### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "551ae467-1a93-4521-b3e4-6f9b38be886b",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.17353612167300378,
  "model_score": 0.0,
  "style_score": 0.4958174904942966,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "e38972c0-bae5-4753-a64e-42946d34c378",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8950821631023733,
  "model_score": 0.9876,
  "style_score": 0.7232633231496379,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "d87becd9-0c81-46da-bd3f-f67cb8eb64f8",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.22250262334536705,
  "model_score": 0.0112,
  "style_score": 0.614921780986763,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```



**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP02 — `false_positive` human writing in a formal register


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
