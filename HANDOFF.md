# Handoff (Nov 15, 2026): S7 part 3, release v5.7.0 (one merge left); S74 part 1 done

## Step status
S64 is **done**. **S7 is done except one merge:** part 2 is finished and merged (PR 117, PR 118), and part 3 (version 5.7.0, release notes, checks) is in open PR 119. Merging PR 119 creates the tag `v5.7.0` (`release.yml`, tag once, never moved). Then **S3**, then **S65**.

## What shipped
- compassionism-simulation PR 117 (participants and non-participants note): merged.
- compassionism-simulation PR 118 (saving and spending by group, savings readings, paired seeds, open-access note, file browser, changelog): merged.
- **[compassionism-simulation PR 119](https://github.com/BetterToBest/compassionism-simulation/pull/119), open, checks queued at session end**: version 5.7.0 set with `set_version.py`; v5.7.0 notes in CONTRIBUTING.md (the release workflow reads them there), v5.6.0 notes moved to CHANGELOG.md. No engine line changed. Local: 17 regressions and 360 unit tests pass, `check_figures.js` 22/22, `study_files.py --check` 14 files, glossary ok, `check_versions.js` ok. A local `domtest.js` was started but not read; the CI `checks` job runs it.
- S74 part 1 (earlier, unchanged): research-update PR 105, compassionism-simulation PR 109, both merged.

## In flight
- PR 119's checks (checks, guard). To merge: confirm both pass (`get_check_runs`; if `checks` fails, `get_job_logs` first), then squash-merge; then confirm the `release` workflow created tag `v5.7.0` and its release notes show the v5.7.0 section.

## Decisions waiting
- None open. D28 (the version number) was confirmed by Duke as v5.7.0 (Nov 15); tags cannot be moved.

## Next step
1. Merge PR 119 (above). 2. **S3** (sonnet, medium): OEIAS as the umbrella name. 3. **S65** (release 2). **S74 part 2** (opus, xhigh, engine build) can run beside them.

## Pitfalls
- A session that started from an old HANDOFF built item 2 again (a duplicate of PR 118; deleted unmerged). Check open PRs (`list_pull_requests`) before building a handoff item.
- The release workflow reads the notes from CONTRIBUTING.md's exact heading `## v<version> Release Notes`; no date in the heading.
- Commits with no URL line and a `Co-Authored-By:` line go through.
- `npm install --no-audit --no-fund` in compassionism-simulation before `check_figures.js` or `domtest.js`; `node domtest.js` takes over 5 minutes, run it in the background.
- `compassionism-sim-results` clones through the proxy with `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse`, then `git sparse-checkout set <folder>`.
- S66's `s66_trace.js` no longer runs on `104691f`; use `s64_erosion.js`. Old remote session branches in research-update (`claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`) need deleting by hand; so does compassionism-simulation's `claude/s7-part2-saving-groups` if it still exists.
- S74 sources: bls.gov refuses this machine (HTTP 403); FRED can return HTML instead of csv, so check the header line; see `sources/s74_history.py`.
- `index.html` has very long lines (line 476 is about 1 MB). Grep with `-o` and bounded context, or use line ranges from `dev/CODEMAP.md`.
