# Handoff (Nov 15, 2026): S7 part 2 finished in one go; part 3 (version and tag) remains

## Step status
S64 **done**. **S7 part 2 done** (all nine checklist items now have a note on the findings page). **Part 3 not done:** the version number and the tag. Duke assigns versions (compassionism-simulation CHANGELOG, "Unreleased"); a tag cannot be moved, so I did not pick one. Default if Duke does not answer (D28): **v5.7.0**, set with `python3 dev/tools/set_version.py 5.7.0`, then `node dev/tools/check_versions.js`; `release.yml` tags on merge. Then **S3**, then **S65**.

## S74 (central bank), part 1 of about 3: done
Duke chose on Nov 14 to start S74 now, not after release 2 (ledger D24, answered and in the ledger). Done: the preregistration `prereg/2026-11-s74-central-bank.md` (before any engine change or run), PLAN.md's Order table and S74 section updated, indexes rebuilt, and the 2005-2025 history paths from opened sources. Still to do: the engine build (history environment `hx`, policy-rate rule `cb` with purchases, refinancing, asset prices, job loss and forced sales), unit tests, the 100-seed pilot, the forward sweep and the report. Every part sits behind a switch that is off by default.
- research-update [PR 105](https://github.com/BetterToBest/research-update/pull/105): merged.
- compassionism-simulation [PR 109](https://github.com/BetterToBest/compassionism-simulation/pull/109), merged: `sources/s74_history.py` and `.json` (rebuild check passes), raw files with SHA-256 hashes in `sources/s74_history/raw/`, and `dev/plans/s74-build-map.md` (where each part enters the engine). No engine file changed.
- **S74 part 2** (opus, xhigh): build `hx` and `cb` following `dev/plans/s74-build-map.md` and the prereg's "What is built" and "Unit tests" sections. S75's descriptive panel (item 2, no engine) can also run beside S74.

## What shipped
- compassionism-simulation [PR 117](https://github.com/BetterToBest/compassionism-simulation/pull/117) (participants and non-participants): merged (e66ddee) after its checks passed.
- [PR 118](https://github.com/BetterToBest/compassionism-simulation/pull/118), **open** (checks were queued at session end; local: `check_figures` 22/22, `study_files --check` 14 files, glossary ok, `check_versions` ok, notes render with no NaN; `domtest.js` was still running locally): items 2, 3, 9 and the S55/S56 note. Readers `dev/tools/s7_spend_groups.js/.py`, `s7_savings.py`, `s7_pairing.py`; data `data/studies/s7-spend-groups.json`, `s7-savings.json`, `s7-pairing.json`; file browser lists them; CHANGELOG "Unreleased" entry.
- Results: saving rate by income fifth runs from strongly negative (lowest) to about a quarter of income (highest), all adults at the target by construction; wealth poverty with ordinary savings rises, with savings that keep their value it falls (all three environments); pairing removes from about a tenth of the variance (median wealth, 90% take-up) to over eight tenths (basket measure, Stress, 30% take-up).

## In flight
- PR 118's checks. Merge it once green (CLAUDE.md); Duke may merge it earlier.

## Decisions waiting
- D28: version for the release (default v5.7.0). Part 3 of S7 waits on it only to tag; the default proceeds.

## Next step
**S7 part 3** (sonnet, medium): merge PR 118; `set_version.py` with the D28 answer (default 5.7.0), changelog "Release Notes" section listing each preregistered study with links to its results folder, checks, merge; confirm `release.yml` tagged it. Then **S3**, **S65**.

## Pitfalls
- The 5.4% and "updated Sept 30, 2026" are copied from the ledger and S47 report, not opened at BEA/FRED. The pairing and savings notes cover study D and the frozen release panel only; the studies P and N twins were not needed (the panel holds the controls). In the panel, Stress shares Adverse's no-programme control; the note says so.
- `compassionism-sim-results` clones through the proxy: `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse`, then `git sparse-checkout set <folder>`.
- `no_figure_change.py compare` reports added words in notes.js and studies.js as moved numbers; CI does not run it.
- The github MCP tools work; the github plugin server fails (400). `npm install --no-audit --no-fund` before `check_figures.js` or `domtest.js`; domtest takes over 10 minutes (run in the background).
- Old remote session branches in research-update need deleting by hand: `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`.
