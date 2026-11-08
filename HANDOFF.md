# Handoff (Nov 8, 2026): S55 part 1, open PTF access (the switch built, off by default)

## Step status
S55 is **partly done**. Part 1 (sub-steps 1 and 2) is done: every member-only rule in the engine is sorted, and the switch `PTF_ACCESS` is built. Remaining: part 2 (sub-steps 3 and 4: the growth rule, then the dated amendments and a pilot); part 3 (sub-steps 5 and 6: the runs on Actions and the report). No study has run with the switch, and nothing is a result yet.

## What shipped
- compassionism-simulation [PR 81](https://github.com/BetterToBest/compassionism-simulation/pull/81), merged `a7574cc` (checks green). Switch `PTF_ACCESS`, study row option `pa`: `'members'` (the default, the engine as it was), `'open'`, or `{fix}`. Every member-only rule sorted in `dev/DECISIONS.md` (S55). Reading in plain words: `dev/reports/s55-ptf-access-reading.md`. Also `paUnitSuite` (4 tests), TESTBED_SPEC, and an engine lineage link.
- research-update: PLAN.md marks S55 part 1 done (row 22a and its section).

## What `'open'` does
- Each zone has a PTF share s of its essential sales. A zone is a community of the layer, or the whole population without it. Every adult in the zone, member or not, buys the share s of food and utilities at PTF prices. Nobody buys more.
- The 40% and 55% tests read s, and so does PTF's damping of outside inflation.
- Each zone starts at its starting member share. `fix` holds every zone at one value (Duke's sweep, 10% to 100%). s does not grow yet: that is part 2.
- 8 customer rules are opened at share s: the price cut, the ESP price pool, its sizing, the private ESPs' mirror, θ's BLEI term, PTH's cut on utilities, cost accounting, and the plan's health cut.
- 7 rules are kept for members: joining and leaving, capacity on joining, the ESP workforce option, PTH, the layer's placement, reporting, and the conversion bonus 1.30 + θ. The Hub gives that bonus to PTF *workers* as an employment incentive. The model has no PTF workforce, so it stays with members, and open-against-members measures access alone (a stated limit).

## Checks
- Guard test identical: 25 rows × 20 seeds × 483 outputs, all three environments.
- `validate`, `unit` (253) and `domtest` (153) pass.
- Engine lineage: link 34f91a85b94a → 8bb948abed0e, with all six 12-seed release panels unchanged.
- `study_data.py --check` and `unsourced_check.py` pass. Their patterns for the damping constant were updated.
- CI green on PR 81 (checks and guard jobs).

## In flight
- Nothing.

## Decisions waiting
- None new. D16 is answered (Nov 7).

## Next step
**S5** (participation threshold; sonnet, medium) is next in the Order table. S39 and S55 part 2 can also start. S7 waits on S5 and S55.

## For S55 part 2
- Operations limit: start from the BLEI paper's section 3 cost structure, which cites Errasti et al. 2003 and Whyte and Whyte 1991. There, variable costs are 35-40% of the market price, overhead 20-25%, profit 15-20%, and PTF overhead 5-8%. Add outside retail data, opened and cited (for example Census Annual Retail Trade Survey margins for grocery stores).
- Capacity limit: c = min(1, c0 + capital per adult ÷ $18,862) (ledger d101) is counted in members today. Part 2 applies it to s.
- The growth rule goes in `paYear` (index.html), which runs before any test reads s.

## Pitfalls
- A `//` comment appended mid-line silently cut a line of the engine. Put comments at line ends only.
- `dev/tools/study_data.py` and `unsourced_check.py` read engine text with patterns. Grep `dev/tools` after editing an engine line.
- The lineage proof takes about 15 minutes on 4 cores, and domtest fails until it is committed.
- The GitHub plugin failed to connect again. The built-in GitHub tools worked.
