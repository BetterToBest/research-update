# Handoff (Nov 17, 2026): S79 (release 2's other BLEI-paper measures) done

## Step status
**S79 done.** Release 2's view of the suite page now draws its own EDC, EPPM, FBS, CSI and IPBI cards and the measures study (who gains, how people move, wealth net of drain), from job X3. No card says "release 1 only" any more; without the X3 files the page falls back to the old wording.

## What shipped
- Job X3 results: compassionism-sim-results `x3-6d095a1/` (run-study run 126, Nov 17, engine `6d095a1`, 6 shards, seeds 1-500). Verified this session: every `SHA256SUMS` line matches; in every shard each engine key of every row and seed equals release 2's stored part M (2,931 row-keys, 1,465,500 values) and the accounting check has no failures.
- compassionism-simulation PR 139 (v5.9.4): `data/releases/r2/study-20.json`, `study-40.json` and `index.json` (`studyFiles`, `studyFrom`); `suite_r2.py` points at X3, and `--check` ties each row's share below the cost of living to release 2's published basket poverty (exact in 18 of 18 cells); `suite.html` (EDC with its paired change and 95% interval; IPBI said to have no interval); figure check reads the X3 files for the release 2 view (5,076 numbers, 12 views); a new domtest check (160 checks); report `dev/reports/s79-r2-measures.md`; `dev/DECISIONS.md` S79 part 3; v5.9.4 notes in CONTRIBUTING.md; v5.9.2's notes moved to CHANGELOG.md, plus short v5.9.3 notes (it shipped without any).
- research-update: PLAN.md S79 section and Order row; this handoff.

## What the results say (full tables in the report)
Both designs lower the drain to rent and interest (EDC) and every poverty line in every environment and horizon, each interval excluding zero (C2.2: EDC −17 to −23 points). The release design is weak under Stress (EDC −5.3 points against C2.2's −18.3 at 20 years; half of adults with no monthly surplus). The wealth Gini is about 0.985 in every row, with or without the programme: a null result, published as such. Cells with no one to count (non-participants under C2.2, where everyone takes part) are shown as missing, not zero.

## In flight
Nothing.

## Decisions waiting
S12 (which visuals go on which page) stays Duke's. Nothing new.

## Next step
S13 (outside audits, second round): next in the Order table. It must run in a session that did not build round 2 and is given only the spec, reports and results (Nov 9 audit, finding 8).

## Pitfalls
- The engine branch `claude/s79-suite-measures` had been cut before PR 138 merged. Re-applying its commits on main and pushing was refused (no force-push), so the old remote branch was merged in (a shallow clone needs `git fetch --depth=20 origin +refs/heads/<branch>:refs/remotes/origin/<branch>` first, or git calls the histories unrelated).
- The engine's `cost` is the gross programme cost per adult-year in year-0 dollars ($68,000 to $84,000 under C2.2); the report says it is gross. Check its definition before quoting it anywhere as a net cost.
- Release 1's own `explore_export.js --study` (no `--r2`) still fails its "equity" accounting check on today's engine; it matters only if release 1's study is re-run.
- Earlier pitfalls still stand: the engine's `dev/CODEMAP.md` is stale; old remote branches to delete by hand; JSON-LD carries Duke's personal email (S42 fixes).
