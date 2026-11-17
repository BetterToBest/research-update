# Second-pass audit of the Simulation's release (v5.9.9), in-house part (Nov 17, 2026)

S13, second pass, part 1. Written by a session that did not build round 2, reading only the specification, the reports, the release data's index and the earlier audits, with the Nov 9 audit's eight findings as the first checklist. It is still the same kind of AI system that built the model, so it is not an independent review. Two outside reviews (Grok, and ChatGPT or Gemini) and possibly a third on NVIDIA's catalogue follow from `audits/2026-11-17-release-audit-prompt.md`; they are triaged in S13 parts 2 and 3.

Read: compassionism-simulation `1d50b19` (v5.9.9): MODEL_SPEC.md sections 6.12 and 14 (by line), the release 2 overview, the question 4 report (backing), the findings-page text (first 30 lines), the S68, S69 and S70 reports (by section), the S69 brief, ECONOMIST-REVIEW.md, the README's opening; research-update: the Nov 9 and Nov 13 audits, the D23 note, the Nov 15 figures audit, the release 2 freeze file (by section). Not rerun: anything. Not read: the engine's code, the question 1-3 and 5-7 reports beyond the overview, the live pages beyond a grep.

## In short

1. **The model has no limit on real goods, and that is why the poverty results "barely depend on backing".** With no backing at all, a programme paying out a third or more of household income with nothing new produced still lowers basket poverty by 31.0 points and raises median real wealth by $86,800 (full coverage, Reference, 20 years). Wages follow prices one for one, the Basic Unit and the cost-of-living basket are indexed, and every household's demand is met: essentials prices rise with demand above the no-programme level (housing 0.6, medical 0.5, food 0), but no one is ever short of goods. So the real goods the programme's recipients gain are taken from no one except holders of nominal savings and lenders. This is the model's structure, not a property of the design, and the reports do not say so.
2. **Full backing costs nothing in the model.** At the main row, output equal to the whole payout appears with no extra work, capital or time, while participation falls 1 to 5 points. The page's footnote says full backing is the design's statement and that the model's own mechanism reaches about 1% of it; it does not say that the backing output has no inputs.
3. **The second implementation checks the translation, not the model.** S69 agreed exactly with the engine on the frozen full-backing row, in every key and seed. But its brief gave it the engine's code excerpts and the engine's per-seed results, as well as the written description. Exact agreement shows the description, the code and a careful port agree; it cannot catch a modelling choice that both share (finding 1 is one).

## The Nov 9 findings, checked against the release

| Nov 9 finding | Status | Evidence | What remains |
|---|---|---|---|
| 1. All wealth is one nominal number | Closed | Asset classes, returns, the creditor side (S59, S71); at the main row under 3% of any wealth figure is erosion of opening balances (overview). | At partial backing, the wealth gain rests on real assets keeping pace with 30-50% inflation (the Nov 13 audit: half-indexing flips the sign in two environments) and on finding 1 above. |
| 2. The capacity price rule | Closed | Today's rule is the main row; the capacity rule a reading (S67; freeze file). | At full backing no price rule is tested: there is no unbacked money (question 4 report: "these readings are inactive at full backing"). "Rests on today's price rule" then says little. |
| 3. Round 2 not in the spec; no independent check | Partly closed | MODEL_SPEC section 14, ODD section 8, TESTBED_SPEC section 7 (S68); S69 rerun exact on the frozen row (S69 report, last section). | The second program had the code and the reference results (S69 brief, files list), so it is a translation check. Finding 1 above is the kind of shared choice it cannot catch. |
| 4. Switches tested alone; state leaks | Closed | 121 rows on together in three environments, run-order test identical, per-run reset of module state (S68 parts 1 and 2). | Nothing found. |
| 5. Seed intervals are not the uncertainty | Partly closed | The page leads with the range across 62 readings (specification curves); the S70 screen moved every reading together. | The screen ran at full backing, where "the box is calm", so the 62 readings are narrow by construction; Stress was not screened (both stated in the reports). Backing, the largest uncertainty, is shown as a separate curve, which is right, but the poverty curve's flatness is finding 1. |
| 6. The financed row | Closed | Financed rows beside the main rows, never led with, the financing identity counting every dollar (S68, S72; overview). | None for the display. |
| 7. Clarity | Open | The README still opens with "see how it does", calls the model agent-based, and describes the page as of v5.2.1 with 500 adults. | One "start here" page; the README's first screen giving both sides; "a dynamic microsimulation with a reduced-form price level". |
| 8. Process | Partly closed | The freeze is registered on OSF (osf.io/msdzk, Nov 14); this pass ran in a fresh session; the pages carry "not yet reviewed by an independent economist". | Every reviewer so far is an AI system. ECONOMIST-REVIEW.md still describes the v5.6 model (rows 7 and 10 say the wealth result rises through the price rule; release 2 reverses it). |

## New findings

Severity: **A** blocks a published claim · **B** fix before the Hub uses the figure (S40, S25, S45) · **C** later.

### 1. No limit on real goods (A, for any sentence that poverty results "do not depend on backing")

**What the model does.** MODEL_SPEC section 6.12: unbacked money moves the general price level one for one; essentials prices move with demand above the no-programme capacity, `P_E = 1 + θ (D − S)/S`, with θ 0 for food, 0.6 housing, 0.5 medical (an unsourced placeholder), multiplied by the general level. Section 6: wages carry the general price level in full (`wIdx` 1). The BU covers the C2.2 needs and is indexed. Nothing caps what households consume when demand exceeds supply under today's rule.

**Why it matters.** In a closed economy with no new output, a transfer that raises some households' real consumption must lower someone else's. In the model, the only losers are holders of nominal assets and lenders (and the creditor side's outside share is left out of the books). Question 4's report says the poverty effects "barely depend on backing" and that at no backing they hold "against prices that rise 35-50% a year: a world no one would run"; the findings page carries the poverty headlines as robust. Both read as facts about the design. They are facts about a model without a resource constraint.

**Fix.** A dated note in question 4's report and the findings-page text: the poverty effects below full backing hold because the model has no limit on real goods, so they are not evidence that the design works without backing. Then, as an engine step after the outside reviews: a reading in which demand above supply is rationed (the capacity rule already computes a rationed share, which, as far as the spec shows, does not enter consumption) or in which wages follow prices only in part, reported for poverty along the backing curve. Wage indexation is already the largest mover at no backing in S70's screen.

### 2. Full backing has no inputs (B)

At the main row the matching output is assumed, not produced: it uses no labour (participation falls 1-5 points), no capital and no time. The design's statement is that the programme is backed; the model shows nothing about how. The card footnote should add one clause: "The model does not show what would produce this output, or with what work."

### 3. The second implementation's independence (B, for how S69 is described)

Describe S69 on the Hub and in the spec as "a second program written from the description, with the engine's code and results to check against", not as an independent model. A from-the-description-only rebuild (no code, no results until the end) of a small part, for example the price and backing block, would test the description; it is optional, after the outside reviews.

### 4. ECONOMIST-REVIEW.md is out of date (C)

Rows 7 and 10 describe the v5.6 model ("too little wealth" rising through the price rule; release 2 reverses it). The rows an economist should see first for release 2 are full backing, finding 1 above, wage indexation, and asset returns under high inflation. Rewrite the checklist for release 2 (S25 or S44).

### 5. Weighted figures (C)

D31 (default proceeds) leaves the engine's own share below 30 days unweighted; by weight it differs by at most 0.61 points in a year. Nothing to change; the outside reviews are asked whether other published figures share the problem S81 found.

## Plan

- No engine change before the outside replies are triaged: findings 1 and 2 are the first things asked of Grok and ChatGPT or Gemini (prompt, part B, items 3 and 4), and their answers decide the shape of the engine step.
- Findings 1 and 2's wording notes go in with the S13 part 2 or 3 triage, so the outside reviews are not shown a page already changed for the questions they are asked.
- Finding 1 is filed for Duke as a ledger decision, because it bears on what the Hub may say about the design: whether the Hub's poverty headlines carry "in a model with no limit on real goods" until an engine step adds one. Default: they do, from S40 on.

## What could not be checked

- Whether the capacity rule's rationed share enters consumption anywhere: the spec does not say it does; the code was not read.
- The question 1-3 and 5-7 reports in full; the live findings page beyond a grep.
- No figure was recomputed: the Nov 15 audit recomputed every main-row effect from the raw files and found them right.

## Amendment (Nov 17, 2026, the same day): Duke's reply, and what it changes

Duke answered findings 1-3 in Chat. His points, and how each changes the note.

**Finding 1.** Duke: households get what they need, not everything they want; a luxury car or a mansion still has to be earned. Goods and services are not limited by design: anyone can provide them through the Creative Collectives and the PTFs and PTH, so the economy could grow to two or three times today's output or more. He sees the poverty and wealth gains as the effect of a foundation that people build on, without the baseline's extraction, and asked whether the no-programme run has the same absence of a limit.

- *Wording corrected.* The chat summary's "every household gets everything it wants to buy" was wrong. Each household buys what its income and BU allow. What has no limit in the model is the economy's total supply: demand never runs into what can be produced, and nothing is rationed.
- *The no-programme run has the same structure.* Its essentials supply is defined as its own demand, so its prices never move. The two runs therefore differ only in what the programme adds.
- *At full backing the model and the design agree.* There, output is assumed to rise with the payout, which is how the model represents the growth Duke expects. The model does not produce that growth itself (its own mechanism reaches 0.2-1.9% of the payout), and the page already says so.
- *The finding narrows.* It does not bear on the main row's headlines. It bears on the readings below full backing, and on the sentence that the poverty effects "barely depend on backing". With no new output at all, the poverty gains in the model are paid for by no one except holders of nominal savings and lenders, because the model has no supply limit to run into. That sentence should say so. Severity falls from A to B, for that sentence and the no-backing figures only.

**Finding 2.** Duke: "This is the point. Work is worth more for less, instead of the current less for more." That is the design's intent: more output per hour. The model assumes the result (full backing) without modelling the productivity gain. It is a model limit, not a contradiction. Severity falls from B to C. A later engine step could model output per hour in PTF, collective and project work, so the growth is shown rather than assumed. The outside reviews are asked for the evidence (prompt, part B, item 4).

**Finding 3.** Duke left this to Claude. S69 was worth doing and stands: it found three gaps between the description and the code, and it proved the code does what the description says, to the last digit. The only change is how it is described: "a second program written from the description, with the engine's code and results to check against", not an independent model. Severity B, for wording only.

**Decision D32, narrowed with Duke's answer.** The main row's headlines stay as they are. A dated note goes on the sentences and figures below full backing (question 4's report, the findings-page paragraph on backing), saying the model has no limit on total supply there. The prompt for the outside reviews was revised the same day, before it was sent, to state the design's reading beside the questions (part B, items 3 and 4).
