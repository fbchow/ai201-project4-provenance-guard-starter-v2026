# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Part I: Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. Allow at most 1 false positive in 10

**Why this target:**
I allow at most 1 false positive in 10 because on a writing site accusation costs more than a missed detection. The user risks losing their job and reputational standing, so we need to be more certain about who we flag.

---

## 2. Text I judge borderline scores between 0.35-0.65 in at least 4 out of 5 cases

*Edit:* I revised the numerical boundary before running the before eval because I originally wrote the incorrect range for what constitutes as an "unsure" label. I changed it from the (0.4-0.6) range to (0.35,0.65) range.

**Why this target:**
I allow 1 in 5 cases because the user whose borderline text falls in the 1 in 5 outside of a 	0.35-0.65 band might be uncertain themselves or use some portion of AI assisted writing.

---

## 3. All 3 labels reachable

Across 3 test inputs I choose, each of `ai`, `human`, and `unsure` is returned at least 1 time.

**Why this target:**
Every submission gets a label, so an unreachable one silently distorts the others. If `ai` can't be returned, the detector never does its job. If `human` can't be returned, writers are never cleared and the appeal path absorbs every incorrect flag. If `unsure` can't be reached, borderline text is forced into an accusation or a clearance. This is a risk because `score_to_label` is still a placeholder and a flat style signal could leave a label out of reach. A single hit per label confirms each one can be produced at all.

---

## 4. Every decision appears in the audit log.

**Why this target:**
When a user wants to appeal their decision, then they will naturally request the log trace for an explanation of how the decision came to be. Every decision the service makes need to be logged. The one time that a decision does not get logged and missing could risk failing to fulfill the one crucial time where data provenance is requested by the user.

In the real world, failing to fulfill compliance could lead to lawsuits and fines.

---

## 5. Malformed text gets marked as a 400 status in 4 of 4 cases.

Examples include: missing, empty text, missing creator_id.

*Edit:* Changed to text input criterion because I can automate testing using the `run_eval.py` script. Before I had the appeal status change as a criterion but I find that is not reliable to perform by hand 15 times.

**Why this target:**
We want to make decisions on complete information. We do not want to make decisions without sufficient information. We want the app to flag explicitly as 400 status to say that the input is incorrect.

### Before: Appeal always changes status
Every appeal changes status and gets recorded with one new record to the audit log.

**Why this target:**

An appeal is the only recourse that a wrongly flagged writer has, so it's important this action gets implemented. If the status doesn't get changed with the service flow, then the writer still sees the "AI" flag. If the appeal fails to be recorded in the log, we can't confirm the appeal happened or if the status was a duplicate entry.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

## Part II: Capstone Project Criteria

## 1. 3 out of 3 text inputs over 5000 words triggers a 400 error and is logged

The text is split by whitespace. Send 3 texts of over 5000 words. Each gets a 400 and `/log` shows a new entry with `event: rejected` and a reason that mentions the word limit.

**Why this target:**
My `eval_bad_huge` test was accepted and scored as 0.9975, so right now nothing stops an enormous input from reaching the model. 3 out of 3 because the check is a simple length comparison. 5000 words, which is about 10 pages, seems like a reasonable limit.

## 2. 3 out of 3 scoring failures log an `error` entry and return a 500

I force the failure by temporarily making each of `model_signal`, `style_signal`, and `combine_signals` raise an exception, one at a time. Each time a caller gets a 500 with a JSON body and `/log` has a new entry with `event: error` and `status: error`.

**Why this target:**
Before this change, a crash in `model_signal`, `style_signal`, or `combine_signals` returned an unlogged 500. A failure left no trace at all. 3 out of 3 because an error handler that works only sometimes would still leave silent gaps, which is the problem it addresses.

## 3. All 4 warm runs are 1000 ms or less

Restart the service, then send the text once to load the model (this first cold request is not counted). Then send the same 200-word text 4 more times. Read `duration_ms` from `/log` on the 4 entries after the cold request. 4 out of 4 warm run is 1000 ms or less.

**Why this target:**
In my trial run, a warm run took about 500 to 535 ms, so 1000 ms leaves roughly 2 times the headroom but would still catch a real slowdown. I'm leaving out the first request, which is a cold start. In my trial, it took 11,627 ms. That first run is about 20 times slower, so it would distort the warm-run result. 4 out of 4 because one slow warm run should count as a miss.

## 4. All 3 labels reachable

Across 3 test inputs I choose, each of `ai`, `human`, and `unsure` is returned at least 1 time.  

**Why this target:**
Every submission gets a label, so an unreachable one silently distorts the others. If `ai` can't be returned, the detector never does its job. If `human` can't be returned, writers are never cleared and the appeal path absorbs every incorrect flag. If `unsure` can't be reached, borderline text is forced into an accusation or a clearance.

## 5. 3 out of 3 valid text submissions log an `input_chars` value equal to the real text length

Send 3 valid text inputs of known length, exactly 50, 500, and 5000 characters. For each, the matching entry in `/log` has `input_chars` equal to that length.

**Why this target:**
My rejected entries for empty, missing, and null text all logged the same reason, so I can't tell the cases apart afterward. A length in every entry lets me spot huge text or empty inputs when diagnosing a failure. 3 out of 3 because the value comes from `len(text)`, so any mismatch means there is a bug.
