# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 14:36
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `22583f4a-a9b7-403f-b7ab-25ffaa6a6cc0` | human | 0.326 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c4a1c61b-6875-4d60-b4f2-03e8e4d49ca7` | unsure | 0.559 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ed3e7016-2cd1-4242-91d4-cfc1b163feca` | unsure | 0.617 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `7637dd7a-c487-4fe5-86da-ef8410e7591e` | unsure | 0.613 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `a47eb3f7-a9cd-41e7-8b96-4b9b2b3f1770` | unsure | 0.381 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `7e89b5e3-8494-4171-821d-ec56c81883eb` | unsure | 0.553 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0bc73554-fab1-4d34-a660-d4ed4876a293` | unsure | 0.608 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a2872e1f-9935-443f-96ae-fc694b3f53d8` | human | 0.338 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `67102ff0-fb29-4c9f-bb45-51acd6eb39d3` | unsure | 0.642 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0ddcab3e-154a-4c87-89f9-251d8dd3bdc2` | ai | 0.903 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `548c9073-42f3-4b91-ac10-acf077f5678d` | unsure | 0.603 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a96578a6-0a17-4c0b-b60a-9e19892f17c2` | ai | 0.703 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `52520907-670d-4dba-b1dd-2f9b3e171c24` | ai | 0.738 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `63bc1ad4-4f0b-4b21-a9ca-026d3e247a94` | ai | 0.741 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `e92239c4-9985-4e01-a86e-189c24054055` | ai | 0.738 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `4aeb5685-4de1-440d-9b1d-7ba6b2c20ed3` | unsure | 0.640 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0039a612-6348-4f0f-9aa9-da1518113d06` | unsure | 0.640 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `6bc1600b-a842-4739-9fe6-77b9c4439cb5` | human | 0.344 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `da581a2e-fe2e-4446-87ac-57e624be2df3` | unsure | 0.482 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ce238936-22ea-4f81-91a4-90528591b1c8` | human | 0.290 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4119494d-97fd-4a30-b5b9-1fc3ae8e5ee6` | unsure | 0.583 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `7b39d448-636b-48aa-8010-15e3b5f74564` | unsure | 0.480 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `e2e2147c-c94b-43cb-8356-93e5f6518e71` | unsure | 0.547 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `8aa65c7c-7791-4f01-bae7-c94f79599ae8` | unsure | 0.567 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `4824e52e-19ca-4316-a6ce-0718f6c08ac2` | human | 0.174 |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `67d8423a-11ae-4782-b137-8cb5a4842d47` | ai | 0.905 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `396b6d9b-2162-4cae-a302-383738b88b56` | ai | 0.895 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fb56a2e4-074d-4c93-8de0-b2474e7e6ca4` | human | 0.246 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7ce11804-9997-452b-a0c0-7c6658748a0e` | human | 0.246 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d035b82f-51a1-4f49-b141-b09eaccd24fe` | human | 0.246 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9cfb35e3-3439-4415-ad41-0ee0bde6c9c5` | human | 0.246 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3b3af90a-30e1-48f5-bf8a-9cfdb824a105` | human | 0.246 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `236b6aba-9020-4e0d-bdab-a610b5e27ea2` | human | 0.246 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d5c6dfea-a8b3-431b-9f47-9ed6b6ba529c` | human | 0.246 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cc5642d1-9521-4bad-9197-c174482a3dab` | human | 0.246 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3dc86dee-050f-42d3-aa25-477e4dce2d41` | human | 0.246 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c8c31dd1-9e5f-42dc-8c94-befae4b0ffbd` | human | 0.246 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "22583f4a-a9b7-403f-b7ab-25ffaa6a6cc0",
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
  "content_id": "c4a1c61b-6875-4d60-b4f2-03e8e4d49ca7",
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
  "content_id": "ed3e7016-2cd1-4242-91d4-cfc1b163feca",
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
  "content_id": "7637dd7a-c487-4fe5-86da-ef8410e7591e",
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
  "content_id": "a47eb3f7-a9cd-41e7-8b96-4b9b2b3f1770",
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
  "content_id": "7e89b5e3-8494-4171-821d-ec56c81883eb",
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
  "content_id": "0bc73554-fab1-4d34-a660-d4ed4876a293",
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
  "content_id": "a2872e1f-9935-443f-96ae-fc694b3f53d8",
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
  "content_id": "67102ff0-fb29-4c9f-bb45-51acd6eb39d3",
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
  "content_id": "0ddcab3e-154a-4c87-89f9-251d8dd3bdc2",
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
  "content_id": "548c9073-42f3-4b91-ac10-acf077f5678d",
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
  "content_id": "a96578a6-0a17-4c0b-b60a-9e19892f17c2",
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
  "content_id": "52520907-670d-4dba-b1dd-2f9b3e171c24",
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
  "content_id": "63bc1ad4-4f0b-4b21-a9ca-026d3e247a94",
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
  "content_id": "e92239c4-9985-4e01-a86e-189c24054055",
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
  "content_id": "4aeb5685-4de1-440d-9b1d-7ba6b2c20ed3",
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
  "content_id": "0039a612-6348-4f0f-9aa9-da1518113d06",
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
  "content_id": "6bc1600b-a842-4739-9fe6-77b9c4439cb5",
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
  "content_id": "da581a2e-fe2e-4446-87ac-57e624be2df3",
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
  "content_id": "ce238936-22ea-4f81-91a4-90528591b1c8",
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
  "content_id": "4119494d-97fd-4a30-b5b9-1fc3ae8e5ee6",
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
  "content_id": "7b39d448-636b-48aa-8010-15e3b5f74564",
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
  "content_id": "e2e2147c-c94b-43cb-8356-93e5f6518e71",
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
  "content_id": "8aa65c7c-7791-4f01-bae7-c94f79599ae8",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "4824e52e-19ca-4316-a6ce-0718f6c08ac2",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "67d8423a-11ae-4782-b137-8cb5a4842d47",
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
  "content_id": "396b6d9b-2162-4cae-a302-383738b88b56",
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

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
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
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "fb56a2e4-074d-4c93-8de0-b2474e7e6ca4",
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
  "content_id": "7ce11804-9997-452b-a0c0-7c6658748a0e",
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
  "content_id": "d035b82f-51a1-4f49-b141-b09eaccd24fe",
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
  "content_id": "9cfb35e3-3439-4415-ad41-0ee0bde6c9c5",
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
  "content_id": "3b3af90a-30e1-48f5-bf8a-9cfdb824a105",
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
  "content_id": "236b6aba-9020-4e0d-bdab-a610b5e27ea2",
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
  "content_id": "d5c6dfea-a8b3-431b-9f47-9ed6b6ba529c",
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
  "content_id": "cc5642d1-9521-4bad-9197-c174482a3dab",
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
  "content_id": "3dc86dee-050f-42d3-aa25-477e4dce2d41",
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
  "content_id": "c8c31dd1-9e5f-42dc-8c94-befae4b0ffbd",
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
