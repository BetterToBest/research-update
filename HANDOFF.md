# Handoff (Oct 29, 2026): S46 repair the formal model, and its follow-up

Two sessions ran S46 at once. Duke started one by hand at 19:27 UTC; at 19:30 the S30 chain fired S46 into the old S23/S30 session. The chained session landed first (research-hub #9). The hand-started session found that on returning from a worker restart. It closed its duplicate (#10) and landed only the S46 items #9 had left open (#11). Model and effort matched PLAN.md's S46 row.

## Step status
S46 **done.** The formal model is repaired in five Hub papers and their PDFs are rebuilt. The notes are `audits/formal-model-s46.md` (#9) and `audits/s46-followup/README.md` (#11). Next: **S10**, in a new session.

## What shipped
- research-hub #9 `claude/s46-formal-model` (merged), in `optimal-transfer-design`:
  - one basic-unit budget, with each unit counted once, and first-order conditions (4.4);
  - Proposition 1, a conditional "no one worse off" result, with the v5.6.0 finding: every group gains real resources but ends with less wealth, so no Pareto improvement is claimed;
  - Lemma 1 (weak monotonicity) and Lemma 2 (one market, partial equilibrium); κ for risk aversion; the $68,500 wealth interval withdrawn;
  - in the companion papers: steady states of 11.8% and 7.4%, a unit-free stability index, the "diminishing returns" claim marked unsupported, V(n) weights labelled as assumed, and dual-currency Theorem 1 scoped to one market.
  - It also added `tools/build_pdf.js` and regenerated `data/claims.csv`.
- research-hub #10 `claude/s46-pdf-build`: closed unmerged (a duplicate of `build_pdf.js`).
- research-hub #11 `claude/s46-followup` (merge `ab1a4c7`):
  - optimal-transfer-design's abstract no longer claims Pareto improvements (A01);
  - dual-currency-inflation: a complete budget and a conversion ceiling that rises with units issued (B013), and one capacity per person with one cap rule (B067, B014);
  - economic-modeling-simulation: the utility function is stated, with one risk-aversion distribution (B019, A07);
  - integrated-digital-governance: zone flows conserve population (B108);
  - four PDFs rebuilt; claims ledger regenerated (6,661 figures);
  - `extract_claims.py` no longer reads an appendix printed after the references as part of the reference list.
- research-update (this branch): `audits/s46-followup/` (apply script, 4 checks, note).

## In flight
Nothing.

## Decisions waiting
- D2 (chat exports for S31): still waiting; S31 is skipped.

## Next step
S10 (a second, independent implementation of the yearly loop in Python), with the model and effort in PLAN.md's Order table. It waits on nothing, but it **must start in a new session** that has not read engine code. The S23/S30 session read engine pages, so it cannot do S10. The chain is stopped; Duke starts S10 by hand.

## Pitfalls
- **A step can run twice.** If Duke starts a step by hand while a chained task for the same step is armed, both run. Before starting, and again before landing, fetch research-update `main` and read its HANDOFF. Delete a pending chained task (scheduled tasks list) before starting that step by hand.
- Chained tasks resume the same session, so later steps inherit everything earlier steps read. Start any step that must be independent (S10, outside audits) in a fresh session.
- Commit trailers: CLAUDE.md forbids model names in commits. research-update commits up to S30 and research-hub `cbbc54f` (on the closed #10 branch) carry one in the Co-Authored-By line; they cannot be rewritten. Use `Co-Authored-By: Claude <noreply@anthropic.com>`.
- Rebuilding a PDF from its HTML drops material that existed only in the old PDF. Do not rebuild citizens-internet-portal or corporate-transformation that way without deciding per paper (I12).
- PDF figures are classed from pdftotext's layout, so a rebuild can move a figure's 70-character window and change its class. After any rebuild, regenerate `data/claims.csv` and compare classes per page with the previous version.
- New text on a paper page falls into that paper's page-wide fallback rule in `tools/claims_review.py` unless a rule is added above it.
- Left for S24: dual-currency-inflation 4.3, A.2 and A.3 (unproven stability "theorem"; `λ* ≈ 0.7` with no run behind it).
