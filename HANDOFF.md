# Handoff (Nov 16, 2026): S75 part 1 done (the descriptive panel of US policy eras)

## Step status
**S75 is partly done.** Part 1 (preregistration, then the descriptive panel from published data, no engine) is done. Still to do: part 2, the engine readings (prereg Part B), and part 3, a separate Hub page for the findings. Duke's instruction (Nov 16): Claude names the page, and it is linked from the simulation and wiki pages once complete.

## What shipped
- research-update: `prereg/2026-11-s75-deep-history.md` (committed before any figure), with Amendment 1 (after the downloads, before any figure: Holm over all 14 measures, series coverage and splices, the sources that did not open); PLAN.md S75 part 1 note.
- [compassionism-simulation PR 128](https://github.com/BetterToBest/compassionism-simulation/pull/128) (c5759be): `sources/s75_eras.py` -> `sources/s75_eras.json` and `dev/runs/s75-panel/tables.md`; raw files in `sources/s75_eras/raw/` (SHA-256 in `_meta`; `check` mode rebuilds identically); note `dev/reports/s75-panel.md`. No engine change.
- [compassionism-sim-results PR 44](https://github.com/BetterToBest/compassionism-sim-results/pull/44): `s75-panel-c5759be` (JSON, tables, run.txt, SHA256SUMS).

## Findings (plain words; the note has every cell)
- Duke's view that 2005-2025 was less stable than the decades before it: supported on 0 of 14 measures, against it on 5 (mostly because 1973-1983 was worse), mixed on 9. Unemployment swings (2.0 points, against 1.1 in 1947-1972 and 1.0 in 1984-2007), home-price swings (against 1947-1972) and food-price swings (against 1984-2007) lean his way, but they do not pass Holm's correction.
- 1973-1983 was the unstable era: higher inflation, essentials prices and unemployment than the eras on either side.
- Top shares fell in 1947-1972 and rose from 1984 (top 1% of income 11.0% in 1972, 19.1% in 2019). Tax rates actually paid were far more progressive in the 1950s (PSZ: top 0.1% 57.3%, top 1% 45.5%, bottom half about 20%). The planning figures (42% and 50.6% for the 1950s; 36.4% and 39.8% in 2014) do not match the file; the file's are used.
- The fitted rate rule: phi 0.45-0.65 before 1984 (below one for one), 1.3 in 1984-2007, about 0 in 2008-2025 (the floor, then a late rise).

## In flight
- Nothing running. PR 128's checks (checks, guard) were running when the session ended; merge both PRs once green.

## Decisions waiting
- New (default proceeds): Duke to supply hospital ownership counts by year (Health, United States 2017 Table 82, or AHA Hospital Statistics, or the Historical Statistics' "Hospitals and beds, by ownership" table). cdc.gov and ssa.gov refuse this machine. Default: the gap stays stated, and nothing is estimated in its place.

## Next step
1. **S75 part 2** (opus, high): the engine readings. Extend `hx` with era paths (`hx.era` e1-e4: 26, 11, 24, 18 years). HX is a 21-year array copied into `index.html` by `dev/tools/s74_hx_copy.py`; `hxT` caps years at HX.n. Add the era's fitted rule to `cb` (B5 fits in `s75_eras.json`), plus tax setting T (PSZ group rates, revenue-neutral by default) and health setting H (the basket's medical line grows at the era's medical minus CPI). Write Amendment 2 with the mechanics and the substitute series before any engine run; then unit tests and 100 seeds; then the full report.
2. S75 part 3: the Hub page (attach research-hub and bettertobest.github.io). S24 (sonnet, medium) can run beside it.

## Pitfalls
- FRED's CSV endpoint fails intermittently (HTTP/2 stream errors, empty replies). Retrying without a user agent works.
- PSZ's 2022 appendix ends in 2019. The CPI file is missing October 2025 (the shutdown), so 2025's unemployment mean uses 11 months and the rule's fit ends in 2025Q3.
- The 2008-2025 fitted rule has phi of about 0, so a = -1.05 in S74's terms. Part 2 must state that the engine has no expectations channel wherever arm R is read.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
