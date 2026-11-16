# Handoff (Nov 16, 2026): S74 done (part 3: the central bank's report, the sweep, who gains and who pays)

## Step status
**S74 is done** (three sessions). Part 3 built the spending reading `cb.dm`, added reporting by wealth group, reran the pilot's rows at 100 seeds with it, ran the 20-seed forward sweep and wrote the report: compassionism-simulation `dev/reports/s74-central-bank.md`.

## What shipped
- [compassionism-simulation PR 124](https://github.com/BetterToBest/compassionism-simulation/pull/124) (engine a60ecd1 for the runs): `cb.dm`; who gains and who pays by fifth of starting real wealth and the top 1% (the rule's channels and the change in real wealth), P2 as a share of income, own inflation in History, yearly paths; 2 unit tests (377 in all); tools `s74_sweep.js`, `s74_sweep_table.js`, `s74_repro.js`; the report and tables (`dev/runs/s74-final/`, `dev/runs/s74-sweep/`). Off identical: guard test, round-2 main pair signatures, and all 542,000 values the pilot saved reproduce exactly.
- [compassionism-sim-results PR 42](https://github.com/BetterToBest/compassionism-sim-results/pull/42) (merged, 3cfe94a): `s74-final-a60ecd1` (100 seeds) and `s74-sweep-a60ecd1` (20 seeds, 33 settings; History 35), each with run.txt and SHA256SUMS.
- research-update: prereg Amendment 2 (Nov 16, before any part-3 run); PLAN.md S74 done.
- [compassionism-simulation PR 122](https://github.com/BetterToBest/compassionism-simulation/pull/122) (the parallel session's audit wording) merged once green, as the last handoff asked.

## Findings (plain words; the report has the intervals)
- The programme steadies households at the bottom: both designs cut the share pushed below the basket line in a recession year (C2.2 about 10% to 1%; the release design to 5-7%) and the median household's largest wealth fall. Both make the basket's price level and dollar incomes less steady. As a share of income, C2.2 steadies incomes in History and Adverse.
- The damping claim (the PTF and PTH share of essentials damps what the central bank and shocks do to the cost of basic living) is not supported for either design: the rule has no channel to essential prices (a model limit, stated).
- The rule moves wealth up: in History, without the programme, the top 1% share +0.43 points and the bottom half -0.43; gains go to the top through asset prices, deposits and buying in forced sales; the middle fifths lose through forced sales and job loss. The programme shrinks this. Forced sales move real assets from households worth $37,000-$665,000 to those worth over $1.9 million; C2.2 nearly ends them.
- The sweep changes no conclusion: the programme's effects keep their sign in every setting but one small case. The rule's own effect on wealth poverty turns on two design parameters (forced sales and the floating-debt spread).
- Own inflation by household type is close to CPI-U (2.77% a year against 2.54%, an upper bound). R-CPI-I was not opened: bls.gov refuses this machine (HTTP 403).

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
- Downloading from bls.gov with browser-like headers is refused by the session's safety rules; R-CPI-I needs another route (Duke, or a source that mirrors it).
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
