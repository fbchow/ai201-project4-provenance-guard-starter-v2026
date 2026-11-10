# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 16:58
- Auto-marked BROKE (5xx, crash, no response): **5**
- Left for you to judge: **51**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `a8dcf28e-ad82-4b98-9607-37cb7da3dd3d` | human | 0.326 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `bdd66d48-2822-415e-8efb-b0c2bad2404a` | unsure | 0.559 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `27a9ee88-71d8-4318-9034-1c661c61c333` | unsure | 0.617 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f0b2eadd-4078-40d7-a80f-20741909083d` | unsure | 0.613 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `19353dca-d6d1-4b6a-bf44-2650e5c65a63` | unsure | 0.381 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `5b29d808-852c-4b22-86ff-a8a34f293cac` | unsure | 0.553 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `95645627-06b8-4c06-8236-b9e776a0f0bc` | unsure | 0.608 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `162cdf7f-5684-4ea9-a058-07a505c3030a` | human | 0.338 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8b90e61a-4ae7-4c51-9d5e-9024a6ef07c1` | unsure | 0.642 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `17f21a73-efa8-40b5-9ba6-42183487a3a1` | ai | 0.903 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `46cb9029-42e8-4635-8dfb-94698d3e0b5a` | unsure | 0.603 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `d5a4d219-08a4-4264-9994-135e9cc7ba97` | ai | 0.703 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f25f2b3e-db37-4030-aa20-b21d66cee339` | ai | 0.738 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `e8255653-8374-4015-b101-056d385be835` | ai | 0.741 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `87d27ef6-3e45-467d-9c98-ddeaf0f1319b` | ai | 0.738 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `b75c34e1-468a-45de-93db-5d7cb9fa4a73` | unsure | 0.640 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `4b114586-bcdf-4052-a62d-e85885c59f83` | unsure | 0.640 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `deb0bd07-a427-4210-b075-7f9aafb0d3ae` | human | 0.344 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `33e0f93d-09dd-45b8-a243-a2110050a35a` | unsure | 0.482 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d5bc5808-225e-42fc-9dcd-da093c485b9e` | human | 0.290 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `81c6b9f6-40de-479c-8f9a-7a14cc235f51` | unsure | 0.583 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0cfc7906-6bfe-4c0d-9c8e-5e0a76c5438d` | unsure | 0.480 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `34056ea3-b832-4398-9025-8f7b896c01d4` | unsure | 0.547 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6532e017-32fe-46db-935b-cb4f0102855c` | unsure | 0.567 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `551ae467-1a93-4521-b3e4-6f9b38be886b` | human | 0.174 |  |
| MF04 | malformed | text is only punctuation | 200 | `d87becd9-0c81-46da-bd3f-f67cb8eb64f8` | human | 0.223 |  |
| MF05 | malformed | text is a very long single word | 200 | `fadb36f2-e925-4a20-9f56-aea6c2a1660a` | ai | 0.928 |  |
| MF06 | malformed | text is emoji only | 200 | `52ebf576-8b81-414b-87bb-4c1c62fa4522` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `dd76c66c-bbfd-4d62-a55e-b8d6a67a4a04` | ai | 0.905 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `e38972c0-bae5-4753-a64e-42946d34c378` | ai | 0.895 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `b6ce2aa5-6d73-4913-b448-fbaf7f1e0063` | unsure | 0.383 |  |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `e5599b2d-2252-4590-9a73-b60b53a782df` | human | 0.221 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `208feb44-d882-4e10-ad0a-bbd4b8dde014` | human | 0.246 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `12f9ac53-8130-45da-91d7-612532114972` | human | 0.246 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `094dbeb1-6133-4820-b156-2bb11fd5366c` | human | 0.246 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `abb75156-1881-4ff5-94e3-fa9fd11dd701` | human | 0.246 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `daa248b0-a3dd-40e6-bb1d-ea7a7d196621` | human | 0.246 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `028bf153-9a89-4f38-bcb3-9c40d3a44d3d` | human | 0.246 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2207e13c-d357-42c4-ac69-210fd83e55b8` | human | 0.246 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `55277fbd-9b56-450f-a760-ec5859e37dde` | human | 0.246 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `918a4b9d-3331-4437-ab96-92c7bc68d51c` | human | 0.246 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `79a0e120-79cc-4ed6-ae72-3c3830adbe78` | human | 0.246 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 5 | 15 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

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

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "bdd66d48-2822-415e-8efb-b0c2bad2404a",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5586937500214972,
  "model_score": 0.5943,
  "style_score": 0.49256785720427754,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "27a9ee88-71d8-4318-9034-1c661c61c333",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6165113436203202,
  "model_score": 0.6662,
  "style_score": 0.5242324103437719,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "f0b2eadd-4078-40d7-a80f-20741909083d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6126807518304433,
  "model_score": 0.6114,
  "style_score": 0.6150592909441238,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "19353dca-d6d1-4b6a-bf44-2650e5c65a63",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3806580891086859,
  "model_score": 0.3212,
  "style_score": 0.4910802545962455,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "5b29d808-852c-4b22-86ff-a8a34f293cac",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5526245300098527,
  "model_score": 0.5727,
  "style_score": 0.5153415143138649,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "95645627-06b8-4c06-8236-b9e776a0f0bc",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6076461132606483,
  "model_score": 0.5862,
  "style_score": 0.6474746093161381,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "162cdf7f-5684-4ea9-a058-07a505c3030a",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.33762655476101694,
  "model_score": 0.2452,
  "style_score": 0.5092758707457627,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "8b90e61a-4ae7-4c51-9d5e-9024a6ef07c1",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.642203277342265,
  "model_score": 0.7042,
  "style_score": 0.5270665066921856,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "17f21a73-efa8-40b5-9ba6-42183487a3a1",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9027422393925688,
  "model_score": 0.9792,
  "style_score": 0.7607492554073396,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "46cb9029-42e8-4635-8dfb-94698d3e0b5a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6033220439955487,
  "model_score": 0.6175,
  "style_score": 0.5769915542729963,
  "label": "Not as confident, could be either AI or human.",
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

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "b75c34e1-468a-45de-93db-5d7cb9fa4a73",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.8814,
  "style_score": 0.5572463596714635,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "4b114586-bcdf-4052-a62d-e85885c59f83",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.8816,
  "style_score": 0.5505901458851814,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "deb0bd07-a427-4210-b075-7f9aafb0d3ae",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.34425009643413707,
  "model_score": 0.3223,
  "style_score": 0.38501456124039163,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "33e0f93d-09dd-45b8-a243-a2110050a35a",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.48154915758304806,
  "model_score": 0.4625,
  "style_score": 0.5169261645229943,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d5bc5808-225e-42fc-9dcd-da093c485b9e",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2895147582747461,
  "model_score": 0.2044,
  "style_score": 0.4475850236421317,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "81c6b9f6-40de-479c-8f9a-7a14cc235f51",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5833760200729373,
  "model_score": 0.5943,
  "style_score": 0.5630886287798207,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "0cfc7906-6bfe-4c0d-9c8e-5e0a76c5438d",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.48045628351469666,
  "model_score": 0.4998,
  "style_score": 0.44453223861341895,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "34056ea3-b832-4398-9025-8f7b896c01d4",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5474447238349794,
  "model_score": 0.6401,
  "style_score": 0.37537063952851274,
  "label": "Not as confident, could be either AI or human.",
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

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
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

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "fadb36f2-e925-4a20-9f56-aea6c2a1660a",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9284399999999999,
  "model_score": 0.9976,
  "style_score": 0.8,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "52ebf576-8b81-414b-87bb-4c1c62fa4522",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.997985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "Probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "dd76c66c-bbfd-4d62-a55e-b8d6a67a4a04",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9054250602409639,
  "model_score": 0.9064,
  "style_score": 0.9036144578313254,
  "label": "Probably written by AI.",
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

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "b6ce2aa5-6d73-4913-b448-fbaf7f1e0063",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.38284481132075476,
  "model_score": 0.2395,
  "style_score": 0.649056603773585,
  "label": "Not as confident, could be either AI or human.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;int&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=ye",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=y",
  "verdict": "BROKE"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "e5599b2d-2252-4590-9a73-b60b53a782df",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.22107090909090912,
  "model_score": 0.0492,
  "style_score": 0.5402597402597403,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;dict&#39; object has no attribute &#39;strip&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=y",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "208feb44-d882-4e10-ad0a-bbd4b8dde014",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "12f9ac53-8130-45da-91d7-612532114972",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "094dbeb1-6133-4820-b156-2bb11fd5366c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "abb75156-1881-4ff5-94e3-fa9fd11dd701",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "daa248b0-a3dd-40e6-bb1d-ea7a7d196621",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "028bf153-9a89-4f38-bcb3-9c40d3a44d3d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "2207e13c-d357-42c4-ac69-210fd83e55b8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "55277fbd-9b56-450f-a760-ec5859e37dde",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "918a4b9d-3331-4437-ab96-92c7bc68d51c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "79a0e120-79cc-4ed6-ae72-3c3830adbe78",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.24582481132075473,
  "model_score": 0.0287,
  "style_score": 0.649056603773585,
  "label": "Probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
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
