# Handoff (Nov 15, 2026): S64 part 2, round 2 read and reported

## Step status
S64 is **partly done**. Parts 1 (dispatch) and 2 (checks, tables, reports) are done. Part 3 remains: the erosion share of every wealth figure, the findings-page charts and text (PLAN.md, S64 section, "Part 3").

## What shipped
- compassionism-simulation [PR 110](https://github.com/BetterToBest/compassionism-simulation/pull/110): `dev/tools/s64_tables.py` (the tables tool), `dev/runs/s64-round2/` (tables, 144 curve CSVs, summary JSON, round 1's backing curve `m-ce8d030` tabulated with `s51_backing.py`), and the reports `dev/reports/s64-round2-overview.md` and `s64-round2-q1` to `q7`.
- compassionism-sim-results [PR 39](https://github.com/BetterToBest/compassionism-sim-results/pull/39), merged: `r2-tables-104691f/` (the same tables, the replay of the two mechanism points, `analysis.txt`, `SHA256SUMS`).
- research-update [PR 106](https://github.com/BetterToBest/research-update/pull/106): freeze file Amendment 3 (the checks; five points of reading), PLAN.md S64 row and section, indexes.

## What the batch shows (plain words; the overview report has the rule-1 sentences)
- All 24 runs succeeded; every check passed; no rerun.
- At the main row (full backing, a design parameter), both designs lower basic-living, basket and wealth poverty in every environment and horizon; robust across all 62 preregistered readings (48 of 48 curves). Inflation 0.0-0.2 points a year.
- The model's own backing mechanism reaches 0.2-1.9% (14-20% with no ceiling); inflation passes 5% a year below 74-90% backing. Rule 4: the findings page says so beside any inflation headline.
- Paid for by a contribution (never led with): rates 46-77%, much smaller poverty effects, the release design raises basket poverty; fragile at every curve.

## In flight
- Nothing running. (S74, a parallel session, has research-update PR 105 and compassionism-simulation PR 109 open; not this step's to merge.)

## Decisions waiting
- Nothing new.

## Next step
**S64 part 3** (opus, high): erosion share, charts, findings-page text. Then S65.

## Pitfalls
- The erosion share (S66 part B) assumes every dollar of wealth is cash: opening balance × the gap in price deflators. Round 2 holds wealth in asset classes (S59), so that term is an upper bound. Part 3 must define it on the nominal part of opening balances (deposits, bonds, the non-stock part of funds), say so, and check `s66_trace.js`'s text patches still match engine `104691f` (its `--check`).
- Part S does not store `bkA`; the mechanism's backed share came from replaying points 75-76 on the session machine (about 16 minutes per environment at 20 years and 32 at 40 years, on 2 processes).
- Rule 7 needed rule 3's materiality to avoid flagging differences of a hundredth of a point (Amendment 3, item 3).
- The GitHub MCP plugin server failed to connect again; the `mcp__github__*` tools loaded through ToolSearch worked.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
