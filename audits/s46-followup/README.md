# S46 follow-up (Oct 29, 2026)

Two sessions ran S46 at the same time. The first to land, research-hub PR #9 (note: `audits/formal-model-s46.md`), repaired the mechanism-design paper and three compendium items. Measured against the S29 triage's list of S46 items, it left five open. This follow-up closes them in research-hub PR #11 (merge `ab1a4c7`), using #9's notation and its `tools/build_pdf.js`. The second session's own PDF script (research-hub PR #10) was closed unmerged as a duplicate.

## What changed on the Hub

- **optimal-transfer-design, abstract (A01).** It still said the system "achieves Pareto efficiency improvements", against #9's sec 5.1 and conclusion. It now points to Proposition 1's conditions and says no Pareto improvement is claimed.
- **dual-currency-inflation 3.1-3.4.**
  - The household budget is complete, with sources and uses of primary currency (B013). Its basic-unit line matches the mechanism-design paper: units spent plus units offered for conversion come out of the allocation plus units received as payment, each used once.
  - The conversion ceiling is `(R × Q)_max × min(Σ C, N × B_t)`. It rises with the units issued; the old text said it was independent of them.
  - One capacity per person, the highest across industries, and one rule for the cap (B067, B014). This is a modelling assumption: the papers do not say whether capacities in different industries add up, and this is the cautious reading.
- **economic-modeling-simulation 3.1 (B019, A07).** The utility function is stated: CRRA in γ over a Cobb-Douglas composite of consumption and leisure (share α_leisure), with skill entering through the wage and discount δ. It uses only parameters the paper already declares and is labelled a modelling assumption. Risk aversion now has one distribution: the Beta in 3.1 conflicted with the Uniform[0.5, 3] in 4.1.
- **integrated-digital-governance 4.3 (B108).** The zone equation is one flow per pair of zones, `F_ij = M_ij · Z_i · f(P_i, P_j) · g(Z_i/C_i)`. No one leaves an empty zone, and the total population is conserved. The old outflow term `g(C_k)` was undefined, and its inflow and outflow were separate rules.
- **PDFs and claims ledger.** The four PDFs were rebuilt and `data/claims.csv` regenerated (6,661 figures, all classed by reviewed rules).
  - `tools/extract_claims.py` now reads an "Appendix X" line that pdftotext runs into the next paragraph as a heading. Without this, appendices printed after a reference list were read as references: for example, "CBO Publication 43473" was classed "no basis, remove".

## Files

- `apply_followup.py`: the nine edits. Each must match its passage exactly once. Run on research-hub `3ee1a5a`, it reproduces the merged pages byte for byte.
- `check_followup.py`: four numerical checks, all pass:
  - total conversions stay within `N × B_t` even when received units are spent again;
  - the ceiling holds;
  - the capacity rule;
  - zone flows conserve population.

## Left for S24

dual-currency-inflation 4.3 ("Our analysis shows stability requires", but no analysis exists), Appendix A.2 (a stability "theorem" with no linearized system) and A.3 (`λ* ≈ 0.7 in our calibration`, with no run behind it).
