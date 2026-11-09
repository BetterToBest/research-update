# Handoff (Nov 9, 2026): S58 done, a price rule that answers demand and capacity

## Step status
S58 is **done** in one session. S7 stays held until round 2 is ready for release (PLAN.md).

## What shipped
- research-update `prereg/2026-11-s58-price-rule.md` (committed before the build; Amendment 1 before the pilot: a weak pull below normal, κ₂, and one joint regression for κ, κ₂, ρ; Amendment 2 after the first run failed the nesting check: option `rs`, pilot rerun); PLAN.md (S58 done, S63 carries); this file. Pull request: see the ledger log line.
- compassionism-simulation [PR 90](https://github.com/BetterToBest/compassionism-simulation/pull/90): switch `PRICE_RULE` (row option `pr`; off = today's rule) and study option `mf` (money-flow table, reporting only). Main values from FRED data in the rule's own form (`sources/s58_price_rule.py`, inputs `sources/s58_fred/`): κ 0.445, κ₂ 0.051, ρ 0.275, α 0.508, slack 0. Guard identical, lineage linked twice, validate, unit (282), domtest (153) pass. Report `dev/reports/s58-price-rule.md`; tables `dev/runs/s58-price/`; S39 report correction note (conversion tax).
- compassionism-sim-results [PR 25](https://github.com/BetterToBest/compassionism-sim-results/pull/25): `s58-price-74ca1a8` (seeds 1-100, three environments, 16 rows; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot at 100 seeds; intervals unadjusted; 500 of 540 exclude zero, 482 survive Holm)
- No study covers new money of 30-50% of income a year; across 110 countries inflation follows money about one for one (McCandless and Weber 1995).
- The new rule agrees: pass-through after 19 years 0.96-1.04 in every reading; programme inflation within about 2 points a year of today's rule (C2.2 Reference 37.4 → 38.2; release 31.5 → 32.2).
- But the path comes in waves of about 9 years (C2.2 Reference: 14% in year 1, 72% in year 4, 25% in year 9, 45% in year 13), from wage and expectation persistence.
- Basket poverty and the cost of living unchanged (under 0.1 point at the main values). Wealth poverty moves with the wave's phase at year 20: C2.2 Reference +0.7 → −1.8; sweep −17.8 (ρ 0.45) to +1.6.
- Both rules imply demand that output cannot meet (C2.2 Reference 22.5% a year today, 11.3% new); at shadow prices C2.2's wealth-poverty effect is +11.7 and +2.5.
- The conversion tax is withheld from each payout, so it was never in U ($12,300 per adult-year, 23% of gross conversion, C2.2 Reference); no design question.

## In flight
- Nothing.

## Decisions waiting
- None new. S63 files the main-row price-rule decision (Claude's recommendation, fixed before the pilot: `pr: true`, today's rule beside it).

## Next step
**S66** (opus, high): trace the low end of S55's fixed-share curve (no engine change). Then S59 (opus, xhigh). S60 can start too (S56, S58 and S61 are done).

## Pitfalls
- The nesting point must switch off the recession's slack too (`rs: false`); only Adverse seed 39 showed it. A preregistered check caught it; the first run is unpublished.
- Under `pr`, a year-20 wealth reading depends on the inflation wave's phase: read the yearly path.
- A no-programme row's `pd*` keys read the previous run's PTF state (pre-existing, reporting only); after `paUnitSuite` the first study differs on them.
- `no_figure_change.py` fails on any engine change by design; the guard test and lineage are the proof.
- Run pilots from a clean worktree (`git worktree add`); remove `sim-pilot` afterwards.
