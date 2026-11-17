# Handoff (Nov 17, 2026): S79 (release 2's other BLEI-paper measures), sub-steps 1-2 done, run X3 in flight

## Step status
**S79 partly done.** (1) The check: every one of the five measures (EDC, EPPM, FBS, CSI, IPBI) and the measures study can be reported for release 2 without changing the engine, so nothing keeps "release 1 only". (2) Job X3 is preregistered, its tool is merged, and it is running on GitHub Actions (free). (3) The suite page work is written and tested on 2-seed files, on a branch without a PR. It is waiting for X3's results.

## What shipped
- compassionism-simulation PR 138, merged as engine commit `6d095a1`: `dev/tools/explore_export.js --r2 --study` (tool only; harness.js and index.html unchanged; old modes byte-identical). It adds two reporting switches (measured EDC `em`; FBS50 tally `fb {dist 'lambda', scale 1}`, the rule unchanged). Each seed's three rows run in turn. The check compares every one of the 2,931 engine keys of every row and seed with release 2's part M and allows only the switches' own new keys. Note: `dev/reports/s79-r2-measures-check.md`; `dev/DECISIONS.md` S79.
- compassionism-sim-results PR 51, merged as `e88585d`: `runner/jobs/series-r2.js --study`.
- research-update: `prereg/2026-11-x3-measures-addendum.md`, committed before the run (`3521671`); PLAN.md S79 note and Order row; this handoff.

## In flight
- run-study **run 126** (compassionism-sim-results, dispatched Nov 17 00:02 UTC): study `x3`, engine `6d095a1eefe71abbb025b82e8942cd80cfe9a34a`, job `series-r2.js --env=all --years=20,40 --n=500 --study`, seeds 1-6, 6 shards (one per environment and horizon). Results land in `x3-6d095a1/`; done when `x3-6d095a1/DONE` exists. X2 took 37 minutes; X3 should take about 1-2 hours (3.3 s a seed at 20 years and 6.5 at 40, locally).
- compassionism-simulation branch `claude/s79-suite-measures` (2 commits, **no PR yet**, because it needs X3's data): `suite_r2.py --study RESULTS/x3-6d095a1` writes `data/releases/r2/study-20.json` and `study-40.json` and lists them in `index.json` as `studyFiles`/`studyFrom`. `--check` also ties each row's share below the cost of living to release 2's published basket poverty (verified exact on release 2's own shards). `suite.html` fills the five cards and the measures study from them, with EDC's paired change and its 95% interval, and keeps the old wording without them. domtest 159/159 on the branch.

## To finish S79 (next session)
1. Check run 126: `run.txt`, `SHA256SUMS`, and each shard's `_meta.selfCheck` (must say "every engine key of every row equals release 2's part M") and `_meta.study.acct.failures` (empty).
2. In `suite_r2.py`, set `STUDY_RERUN = '6d095a1eefe71abbb025b82e8942cd80cfe9a34a'` and `STUDY_RUN` (e.g. "run-study run 126, Nov 17, 2026 (GitHub Actions)"). Run `--study` on the folder, then `--check`.
3. Extend `dev/tools/check_figures.js` (suite views) and domtest Phase 15 to cover the release 2 cards and the measures study. Write the report `dev/reports/s79-r2-measures.md`, with every outcome, nulls and Adverse/Stress included. Bump the version (`set_version.py 5.9.4`, CHANGELOG). Open the PR and merge it once checks pass.

## Decisions waiting
S12 (which visuals go on which page) stays Duke's. Nothing new.

## Next step
S79 again (sub-step 3), once `x3-6d095a1/DONE` exists; it is next in the Order table. If the run failed a check, follow the prereg's decision rules (amendment, new id `x3b`). S13 comes after.

## Pitfalls
- The previous session's S78/S79 commits were on an unmerged branch (`claude/affectionate-maxwell-tetjkz`); they are merged into this session's branch.
- `index.json` already uses `study` for the job id ("x2"), so the measures files are listed as `studyFiles`.
- Under C2.2 everyone takes part, so non-participant cells and "starts in Crisis" transitions are null ("–"). The page shows them as missing, not zero; the report should say why.
- Release 1's own `explore_export.js --study` (no `--r2`) fails its accounting check ("equity" identity) on today's engine, before and after this change. It is not used now; it matters if release 1's study is ever re-run.
- Earlier pitfalls still stand: the engine's `dev/CODEMAP.md` is stale; old remote branches to delete by hand (see git history of this file); JSON-LD carries Duke's personal email (S42 fixes).
