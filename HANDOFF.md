# Handoff (Nov 16, 2026): S74 part 2 done (central-bank engine build and pilot); S40 and S65 done (parallel session, Nov 15)

## Step status
**S74 is partly done: parts 1 and 2 of 3.** Part 2 built the engine, tested it and ran the 100-seed pilot. **Part 3 remains:** build `cb.dm` (refused until built), run the forward sweep (20 seeds, fans) with the new reading `th`, split who gains and who pays by group, run the stability test, write the report (`dev/reports/s74-central-bank.md`), and describe the Fed's governance as the plan says.
**S40 and S65 are done** (parallel session). The Hub's other made-up results belong to S24 and S25.

## What shipped
- [compassionism-simulation PR 123](https://github.com/BetterToBest/compassionism-simulation/pull/123) (merged, 1102b9c): History environment `hx` (`HISTORY_ENV`, `var HX` from `sources/s74_history.json`; `hx.rp 'infl'` is History with no central bank), the policy-rate rule `cb`, forced sales `cb.fs`, and stability measures (study option `stab`, `ST74_KEYS`). 15 unit tests (`s74UnitSuite`). Guard test identical; round-2 main pair identical (`dev/tools/s74_offsig.js`); on-together tests 172 rows x 4 environments pass; engine lineage linked. Decisions are in `dev/DECISIONS.md` (S74). Notes: `dev/reports/s74-design-reading.md` and `dev/reports/s74-pilot.md`.
- [compassionism-sim-results PR 41](https://github.com/BetterToBest/compassionism-sim-results/pull/41) (merged): `s74-cb-5f11ceb`, the pilot (100 seeds, four environments, both designs).
- research-update: prereg Amendment 1 (Nov 15, before the pilot).
- S40 (parallel): research-hub PRs 13 and 14 (merged; generator and withdrawn figures); compassionism-simulation PR 121 (merged) and PR 122 (audit wording; merge once green).

## Pilot findings (plain words; part 3 confirms them)
- Both designs cut the share of households pushed below the basket line in a recession year: C2.2 from about 10% to about 1%; the release design to about 5.5%. C2.2 also cuts the median household's largest wealth fall. Both raise year-to-year income swings in dollars.
- The design's claim that its share of essentials damps what the central bank does to the cost of basic living is **not supported**. The rule has no channel to essential prices in this engine (a model limit, stated).
- Without the programme the rule raises wealth poverty (by 3.4 points in History). With the programme its effect is near zero. Forced sales move real assets from lower-middle wealth groups to the top two.
- History checks: top 1% share matches the DFA; the bottom 50% share has the right direction but a different size; basket and wealth poverty rise where official poverty fell (does not match; reported, nothing tuned).

## In flight
- Nothing. (Simulation PR 122, the parallel session's audit wording, was still open at the end of this session: merge it once green.)

## Decisions waiting
- None.

## Next step
1. **S74 part 3** (opus, xhigh): the sweep, who gains, the stability test, the report. Start from Amendment 1 and `dev/runs/s74-pilot/tables.md`.
2. S24 (sonnet, medium) can run beside it.

## Pitfalls
- The page had a global `STAB_KEYS` (the v4.19 stabiliser list) outside the engine block. A new engine name that collides with a page-only name breaks only domtest, never the harness. Grep index.html for every new global.
- Part 1's branch `claude/s74-central-bank` was already merged, and force-pushing is off-limits, so part 2 used `claude/s74-cb-build`.
- `dev/tools/s68_pairs.js` writes over S68's files unless given `--out`.
- History's anchored SPM in `sources/history` ends in 2012.
- Release 2's main rows use 500 adults; never set one release's wealth figure beside the other's. `data/claims.csv` (research-hub) uses CRLF.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
