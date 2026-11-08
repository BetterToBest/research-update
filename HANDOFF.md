# Handoff (Nov 8, 2026): S36 done, the synergy report from the full batch

## Step status
S36 is **done**. The synergy report reads studies B (500 adults, 20 and 40 years) and B10 (10,000 adults) from the 500-seed batch at engine `ce8d030`. It covers both designs, three environments, both yardsticks, and the octave raise off and on.

## What shipped
- compassionism-simulation [PR 79](https://github.com/BetterToBest/compassionism-simulation/pull/79), merged `c921e6c` (analysis only): `dev/tools/s36_synergy.py`, the report `dev/reports/s36-synergy.md`, every table in `dev/runs/s36-synergy/tables.md`, every estimate in `estimates.csv` (about 25,600), DECISIONS.md (S36).
- research-update: PLAN.md marks S36 done, with its findings in one paragraph.

## Findings (C2.2 design unless stated)
- The CCO accounts for 97-100% of the gain in basic living and 93-99% of the gain on the cost of living, in all 24 settings. CIP comes next (1-6%). PTF, PTH and SZH stay under 0.33 points each.
- On those two outcomes the parts overlap rather than reinforce each other, mostly CCO x CIP. The whole-design contrast is negative in every setting. A material synergy shows only in Adverse, 40 years, released-wage yardstick.
- Wealth has the largest interactions (for example CCO x PTH +2.3), but their sign changes with the raise, the yardstick, the design and the horizon. No wealth synergy is stated.
- The parts together inflate 0.4-4.3 points a year less than separately. The full effect is 26-89 points a year.
- SZH is never material. Scale: 0 of 510 comparisons pass. Every material contrast survives Holm.
- The Hub's 0.42/0.28/0.18/0.12 split (audit A08) cannot be recomputed in its own four categories. The report's short answer 8 gives the replacement line, by the five parts, for S24/S25.

## Checks
All pass, in tables section 0:
- cells without the CCO are identical under both designs;
- the first 20 years of each 40-year row equal the 20-year row;
- B's 72 shared rows equal study A's, every key and seed;
- Shapley efficiency holds per seed (gap 9e-16).

## In flight
- Nothing.

## Decisions waiting
- None.

## Next step
**S38** (community-layer report; opus, medium): next in the Order table. Studies G, G10, H, I and J at engine `ce8d030`, headline at 10,000 adults. `s36_synergy.py`'s linear maps (Shapley, contrasts, dividends) can be reused for G and G10's layer factorial. S5 and S39 can also start.

## Pitfalls
- My own checks failed at first: the `main` row was counted as a no-CCO cell, and the C2.2-only keys (`c22PY`, `buPY`, `el*`) are null on release rows. Both are fixed in the script; the data were right.
- Shapley shares of a near-zero full effect run to several hundred percent (C2.2 wealth, Reference, year 20). They are shown as preregistered; the report says why they are not meaningful there.
- The PR's branch commit carries a model name in its co-author line, against the no-model-names rule. The squash merge on main does not. Use `Co-Authored-By: Claude <noreply@anthropic.com>`.
- Sparse-clone the results repository (`--filter=blob:none --sparse`, then `sparse-checkout set <folders>`). The whole repository is several GB.
- `s52_shock.py`'s report header still says "PILOT" for any folder; the O report (S7) should relabel batch results.
- **GitHub plugin:** failed to connect again; the built-in GitHub tools worked.
