# Handoff (Nov 14, 2026): S73 done (movement in and out of the labour force, and the participation margin)

## Step status
S73 is **done**. Preregistered first (`prereg/2026-11-s73-participation.md`). Amendment 1 was made before the pilot: changes found while building, none from a result.

## What shipped
- compassionism-simulation [PR 103](https://github.com/BetterToBest/compassionism-simulation/pull/103) (merged, 26d9b47):
  - Options `lf.fl` (yearly exits and returns; 'stock' main, 'panel') and `lf.pm` (0.43: the share of the income effect taken by leaving work).
  - `r2MainRow` carries `lf {fl: 'stock', pm: 0.43}`; `R2_ALT` gains 'lp'.
  - 8 unit tests (358 in all); guard identical; lineage linked; on-together tests 154 rows × 3 environments pass.
  - Report `dev/reports/s73-participation.md`; MODEL_SPEC 14.15.
- compassionism-sim-results [PR 35](https://github.com/BetterToBest/compassionism-sim-results/pull/35) (merged): `s73-participation-d12fd0f` (pilot, 100 seeds).
- research-update: prereg and Amendment 1; PLAN notes for S73, S70 and S63; this file.

## Findings (plain words)
- **Source.** 18,937 adults interviewed in both the March 2025 and March 2026 Census surveys. Each year about 3.6 in 100 working-age adults stop working all year (care, illness, school, early retirement), and 11-44 in 100 of those out come back, depending on the reason.
- **The flows matter.** With people moving in and out, both designs cut basket poverty by 1-2 points more, and programme inflation is 0.6-3.4 points a year lower.
- **The margin passes the check S60 failed.** On the $12,000 test, participation falls 1.3 points (the US experiment: −4.2, interval −7.5 to −0.9; the old engine: 0.0). Expected earnings are unchanged by design.
- **Under the programme**, 1.3-4.4% of adult-years are spent out of work because of it. Basket poverty is 0.1-1.0 point higher, and wealth poverty at most 0.14 points higher. The price rule and the flat contribution's rate (85.1% of wages) barely move.
- **Both go to S70's screen as headline-moving** (preregistered rules C and D).
- **Unpaid work** (Duke's note): Claude's reading is in report section 6. The model counts only the conversion the design pays for (projects). It does not value care of one's own family, community work or new ventures, and says so beside every participation figure. If Duke means family care to convert under the CCO, that is a design change (a ledger decision); none filed, default: not counted.

## In flight
- Nothing running.

## Decisions waiting
- None new. D23 is still to be filed again by S63.

## Next step
**S69** (`/start-session S69`). It waits on S68, S72 and S73, all done. It starts by building the packet (about 40 minutes of 500-seed references; dev/packets/make_s69_reference.js, then build_s69_packet.py). Where possible, run it on a different model from the one that built the switches. S70 and S63 follow.

## Pitfalls
- At 500 adults, one seed's out-of-work share wanders by about 1.7 points: read it over 100 seeds.
- Without ageing, adults have no age or sex, so the flows use tables by household type.
- `fl 'panel'` without ageing drifts the share out toward 28%.
- The key `E` is earnings per adult-year only in rows without a programme.
- An apostrophe inside a single-quoted test name broke harness.js once: run `node -e "require('./harness.js')"` before committing.
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and earlier session branches in research-update still need deleting by hand.
