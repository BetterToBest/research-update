# Handoff (Nov 16, 2026): S74 done (part 3, plus Amendment 3: R-CPI-I and the forced-sale discount from Duke's sources)

## Step status
**S74 is done** (three sessions). Part 3 built the spending reading `cb.dm`, added reporting by wealth group, reran the pilot's rows at 100 seeds with it, ran the 20-seed forward sweep and wrote the report: compassionism-simulation `dev/reports/s74-central-bank.md`.

## What shipped
- **Amendment 3 (after the report, Nov 16):** Duke supplied R-CPI-I and Campbell, Giglio and Pathak 2011. [compassionism-simulation PR 127](https://github.com/BetterToBest/compassionism-simulation/pull/127): the R-CPI-I check (`dev/tools/s74_rcpi.py`) and two source-based forced-sale discount readings (0.034, 0.062); report updated. [compassionism-sim-results PR 43](https://github.com/BetterToBest/compassionism-sim-results/pull/43): `s74-fd-a60ecd1`, `s74-rcpi-a60ecd1`. research-update: prereg Amendment 3.
- [compassionism-simulation PR 124](https://github.com/BetterToBest/compassionism-simulation/pull/124) (merged, 918bf44; engine a60ecd1 for the runs; checks and guard green): `cb.dm`; who gains and who pays by fifth of starting real wealth and the top 1% (the rule's channels and the change in real wealth), P2 as a share of income, own inflation in History, yearly paths; 2 unit tests (377 in all); tools `s74_sweep.js`, `s74_sweep_table.js`, `s74_repro.js`; the report and tables (`dev/runs/s74-final/`, `dev/runs/s74-sweep/`). Off identical: guard test, round-2 main pair signatures, and all 542,000 values the pilot saved reproduce exactly.
- [compassionism-sim-results PR 42](https://github.com/BetterToBest/compassionism-sim-results/pull/42) (merged, 3cfe94a): `s74-final-a60ecd1` (100 seeds) and `s74-sweep-a60ecd1` (20 seeds, 33 settings; History 35), each with run.txt and SHA256SUMS.
- research-update: prereg Amendment 2 (Nov 16, before any part-3 run); PLAN.md S74 done.
- [compassionism-simulation PR 122](https://github.com/BetterToBest/compassionism-simulation/pull/122) (the parallel session's audit wording) merged once green, as the last handoff asked.

## Findings (plain words; the report has the intervals)
- The programme steadies households at the bottom: both designs cut the share pushed below the basket line in a recession year (C2.2 about 10% to 1%; the release design to 5-7%) and the median household's largest wealth fall. Both make the basket's price level and dollar incomes less steady. As a share of income, C2.2 steadies incomes in History and Adverse.
- The damping claim (the PTF and PTH share of essentials damps what the central bank and shocks do to the cost of basic living) is not supported for either design: the rule has no channel to essential prices (a model limit, stated).
- The rule moves wealth up: in History, without the programme, the top 1% share +0.43 points and the bottom half -0.43; gains go to the top through asset prices, deposits and buying in forced sales; the middle fifths lose through forced sales and job loss. The programme shrinks this. Forced sales move real assets from households worth $37,000-$665,000 to those worth over $1.9 million; C2.2 nearly ends them.
- The sweep changes no conclusion: the programme's effects keep their sign in every setting but one small case. The rule's own effect on wealth poverty turns on two design parameters (forced sales and the floating-debt spread).
- Own inflation: BLS's R-CPI-I (Dec 2005-Dec 2025) rose 2.69% a year for the lowest-income fifth and 2.43% for the highest (CPI-U 2.52%). The engine's measure cannot see that gap, even given BLS's own shares (0.01 points), and its 2.77% is confirmed as an upper bound.
- Forced-sale discount, now from its source: 3.4-6.2% for a house (bankruptcy-related), with 27% (foreclosure) as an upper bound. The main reading stays 0. In History the rule's effect on wealth poverty without the programme is 3.5 / 3.7 / 3.9 points at discounts of 0 / 0.034 / 0.062. No conclusion changes.

## In flight
- Nothing.

## Decisions waiting
- None.

## Next step
1. **S75** (opus, high; may take 2 sessions): deep history from 1947, on S74's history environment and rule. Read S74's report first.
2. S24 (sonnet, medium) can run beside it.

## Pitfalls
- `dev/tools/s74_table.js` with no folder writes over the committed `dev/runs/s74-pilot/tables.md` with an empty table (the pilot JSONs live in compassionism-sim-results). Always pass the folder.
- Forced sales exist only with the rule on, and the rule charges a 3-point floating-debt spread the no-central-bank reading does not: "rule minus off" carries both (the sweep's readings size them).
- bls.gov refuses this machine; BLS files come from Duke (R-CPI-I is now in compassionism-simulation `sources/s74_history/raw/`).
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
