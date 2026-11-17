# Handoff (Nov 17, 2026): S81 done (v5.9 suite averages by weight, v5.9.9)

## Step status
**S81 done.** The rerun finished, every plain key equals the earlier series, the weighted series are in the suite files, the suite page shows them, and the report is written.

## What shipped
- compassionism-simulation PR 144 (merged `a60bd3e`): weighted keys in the suite export (earlier today).
- compassionism-sim-results `x4-a60bd3e/` (run-study run 127, engine `a60bd3e`): six shards, `run.txt`, `SHA256SUMS`, `DONE`. Plain keys of every row, year and environment equal `x2-5b62481` (zero differences in bands, deciles, lives and suite).
- compassionism-simulation PR 145 (v5.9.9; merge commit in the PR): `data/releases/r2/suite-20.json`, `suite-40.json` (31 weighted keys beside the plain ones), `index.json` (records both jobs); `dev/tools/suite_r2.py` (takes X4's folder and X2's folder, re-checks equality, `--check` covers the weighted keys); the suite page's "what the days are made of" section shows weighted medians and averages with the average beside each median; report `dev/reports/s81-suite-weighted.md`; release notes in CONTRIBUTING.md, v5.9.8 notes moved to CHANGELOG.md. Chart count stays 13.
- research-update: PLAN.md row and PLAN-done.md note for S81.

## What the weighted figures show
Only the average days from savings was wrong in kind (Year 40, Reference, opt-in design: 701,913 plain, 11,003 by weight, median 2,630). Every other share moves by about a point or less, every median by under 5%. Exceeding the spread across runs: the allowance median in 10 of 540 cells and the Crisis share of participants in 2 of 360 (by 0.06 points), all tiny quantities. The plain shares and tiers stay on the page (they equal v5.9's published unweighted figure).

## In flight
Nothing.

## Decisions waiting
- D31 (default proceeds): the engine's own share below 30 days (behind v5.9's headline basic-living effects) is unweighted too; by weight it differs by at most 0.61 points in a year. Default leaves the stored results and reports the weighted figures beside them (done in the report).
- S12 stays Duke's.

## Next step
S13, second pass (opus, high; or fable, high): outside audit of the release, run by a session that did not build round 2, given only the spec, the reports and the results, with the Nov 9 audit's eight findings as its first checklist. S7 is done, so it can start. Then S25, S42, S44.

## Pitfalls
- `set_version.py` has no `--help`; any argument is taken as the version. New version notes go in CONTRIBUTING.md; the previous version's notes move to CHANGELOG.md.
- `reader_codes.py --check` (domtest) rejects job ids, "release 1/2" and "C2.2" in reports, and the figure check rejects any typed percentage in `suite.html` text (write "one part in twenty", not "5%").
- Hub and root site were not re-scanned with the stricter patterns (earlier pitfall still stands).
