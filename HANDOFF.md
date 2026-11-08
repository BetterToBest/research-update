# Handoff (Nov 8, 2026): S5 done, the participation figure

## Step status
S5 is **done**. S7 now has every input (S36, S38, S5, S55) and can start.

## What shipped
- compassionism-simulation [PR 84](https://github.com/BetterToBest/compassionism-simulation/pull/84) (analysis only, no engine change): report `dev/reports/s5-participation.md`, tool `dev/tools/s5_participation.py` (8 checks pass), tables and every estimate in `dev/runs/s5-participation/`, DECISIONS.md. **Still open at the end of the session: checks (`checks`, `guard`) were running.** Merge it once both are green; nothing else depends on its merge except S7 reading the report.
- research-update: PLAN.md (S5 done; notes for S24/S25/S7) and this file.
- Read from compassionism-sim-results `prog-d-ce8d030` and `prog-d10-ce8d030` (500 seeds each).

## Findings (plain words)
- By the preregistered rule the figure is **2%**, the floor of the grid, in every environment and at 10,000 adults. It is a detection level, not a viability threshold.
- Headline cell (Reference, 500 adults, 20 years, CPS yardstick, raise off): basic living +0.71 and cost of living +2.15 points at 2%; wealth +0.95 at 2%, +0.58 at 5%, then worse: -0.21 at 10%, -22.43 at 90%. Basic living +10.44 and cost of living +18.08 at 90%. Inflation 0.34 points a year and cost $35,736 per adult-year at 90%.
- All three measures improve together only up to 5% of adults joining (headline cell); in other cells 2% to 10%; at 90% in one cell (Reference, 40 years, raise on). With the as-released yardstick several cells find no level where all three improve.
- No threshold of 30%, 55%, 60-65% or 75% can be confirmed or refuted: the engine has no network effect. The grid belongs to the as-released design; under C2.2 everyone is covered.
- 10,000 adults give the same decisions as 500 (one Stress basic-living level differs).

## In flight
- compassionism-simulation PR 84: checks running; merge when green (no job output depends on it).

## Decisions waiting
- None.

## Next step
**S39** (outside engine cross-check; opus, high): next unblocked row of the Order table. **S7** (sonnet, medium) can start now too.

## Pitfalls
- "Detected" at 2% does not mean "works at 2%": the wealth effect reverses. Any Hub sentence about the figure must say so, and keep "stated" apart from "material".
- The "60-65%" statement is in no audit file; S24 must grep the Hub corpus for it (research-hub was not attached this session).
- The results repository is large; clone it shallow with a long timeout. Reading D and D10 takes under a minute.
