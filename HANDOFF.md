# Handoff (Oct 29, 2026): S46 repair the formal model

Model check (chained session): ran on claude-opus-5-5. The chained prompt asked for effort xhigh, but the session reported effort high: `/model` and `/effort` lines in a chained prompt do not change a running session. The task resumed the same session as S23 and S30.

## Step status
S46 **done.** The formal model is repaired in five Hub papers, their PDFs are rebuilt, and the "what changed" note is `audits/formal-model-s46.md`. Next: **S10**.

## What shipped
- research-hub PR `claude/s46-formal-model` (link and merge commit in the ledger log). In `optimal-transfer-design.html`:
  - one basic-unit budget (each unit counted once);
  - first-order conditions (new 4.4);
  - Phi as a factor on M(q);
  - Proposition 1, a conditional "no one worse off" result, with the v5.6.0 release finding that every group gains real resources but ends with less wealth, so no Pareto improvement is claimed;
  - Lemma 1 (weak monotonicity) and Lemma 2 (one market, partial equilibrium);
  - κ for risk aversion;
  - the $68,500 wealth interval withdrawn.
- The four companion papers:
  - community-monetary: steady states of 11.8% and 7.4% replace "below 5% in 15 years";
  - economic-modeling: unit-free stability index, and the diminishing-returns claim marked unsupported;
  - integrated-digital-governance: V(n) weights labelled as assumed;
  - dual-currency: Theorem 1 scoped to one market.
- `tools/build_pdf.js` (headless Chromium, the page's print styles, no outside requests) rebuilt all five PDFs. `data/claims.csv` was regenerated (6,655 figures).
- research-update: `audits/formal-model-s46.md`.

## In flight
Nothing.

## Decisions waiting
- D2 (chat exports for S31): still waiting; S31 is skipped.

## Next step
S10 (second, independent implementation of the yearly loop in Python), opus, xhigh (or fable, high). It waits on nothing, but it **must start in a new session**. The chained S10 task fired into this session on Oct 29 at 19:46 UTC, and S10 was deliberately not started there. That session had read engine code during S30 (the early engine pages, the current page's `CFG.TARGET_*` constants, the CHANGELOG's fix descriptions). An implementation written in it would not be independent of harness.js internals, which S10 forbids. The chain stops here; Duke starts S10 by hand.

## Pitfalls
- Chained tasks resume the same session (same conversation and container), so later steps inherit everything earlier steps read. For any step that must be independent (S10, outside audits), start a fresh session instead of chaining.
- Rebuilding a PDF from its HTML drops material that existed only in the old PDF (counts in the note). That was intended for these five papers. Do not rebuild citizens-internet-portal or corporate-transformation that way without deciding per paper (I12).
- Modelling assumption, recorded in the paper and the note: conversion may use one's own units or units received as payment, each counted once, and needs a recognised contribution.
- The release reports outcomes by group, not the share of individuals better off on every measure; the study program should add that share (S32/S36).
- New text on a paper page falls into that paper's page-wide fallback rule in `tools/claims_review.py` unless a rule is added above it (done for the S46 text).
