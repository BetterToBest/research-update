# Handoff (Nov 15, 2026): S7 part 2, fourth session

## Step status
S64 is **done**. **S7 is partly done.** Part 1 merged earlier. Part 2: Studies section (PR 113), first notes and glossary (PR 114), inflation and Holm notes (PR 115) are merged. Items 7 (levers) and 10 (tax-financed C2.2, labelled 500 adults, 20 years) are written in an open PR (below). Still to write: items 2, 3, 6, 9 and the S55/S56 wording. Part 3 (notes, version, checks, merge) not started. S3 runs right after S7, then S65.

## What shipped
- [compassionism-simulation PR 115](https://github.com/BetterToBest/compassionism-simulation/pull/115): merged by Duke.
- Glossary fix, in PR 115 before its merge: `site/glossary.json` now holds all 20 entries (PR 114 had added 8 to `findings.html` by hand, so `glossary.py --check` failed). The front page now shows those 8 too, because the glossary is shared.
- [compassionism-simulation PR 116](https://github.com/BetterToBest/compassionism-simulation/pull/116), **open, checks (checks, guard) were still queued at session end**: new `data/studies/s54-levers.json` (made by `study_files.py` from `dev/runs/s54-levers/stage3-*`), and a levers note in `site/notes.js`. It shows points entering stage 3 (162, 74, 5, 5), how many passed (0, 0, 2, 1), the three confirmed points with intervals, and the flat wage contribution (the tax-financed C2.2) beside them. Counts and figures match `dev/reports/s54-levers.md`. Local: figure check 22/22, `study_files.py --check` 10 files, notes render in jsdom with no NaN. Next session: merge PR 116 once its checks pass; if `checks` fails, read the log (`get_job_logs`) first.

## Part 2: what remains
Pattern: study numbers as a file in `data/studies/` (generator `dev/tools/study_files.py`), then a function in `site/notes.js` that reads it; never type a figure.
- (6) participants and non-participants: `gPart*`/`gNon*` groups are in shards `prog-d-ce8d030` and `prog-d10-ce8d030` (compassionism-sim-results, about 24 MB each). Needs a reader in `dev/tools/` (start from `s5_participation.py`, which uses `batch_load.py`), paired against each group's own no-programme baseline. Do not name non-participants as the cause of the opt-in result unless the group figures show it.
- (2) saving and spending by income group: no data file; short session-machine run of the frozen no-programme row (free), tool in `dev/tools/`.
- (3) wealth poverty, ordinary and inflation-protected savings: release rows `sav`, `sav0` in `dev/runs/release-panel-frozen.json`; no-programme twins in studies P and N (`p-ce8d030`, `n1`-`n3x-ce8d030`, shards only).
- (9) variance reduction from paired seeds: no report found; needs a measurement.
- S55/S56 wording (PLAN.md S7 section): open-access tables beside the members-only ones, the rule-2 sentence, the low-share check, the S56 list of sentences.
- The 5.4% and "updated Sept 30, 2026" are copied from the ledger and S47 report, not opened at BEA/FRED.

## In flight
- Only PR 116's checks.

## Decisions waiting
- None. (Whether to adopt a tax-financed design stays a design decision for Duke; the note says it is undecided.)

## Next step
**S7 part 2, continued** (sonnet, medium): merge PR 116, then the items above, then part 3, then **S3**, then **S65**.

## Pitfalls
- `compassionism-sim-results` clones through the proxy with `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse`, then `git sparse-checkout set <folder>`. It is cloned at `/home/user/bettertobest/compassionism-sim-results` (read only; `n1-ce8d030`, `n2-ce8d030` are checked out).
- Study N's folders `n1`-`n3x` are the S54 lever runs (`levers.js`, 500 seeds); the report and my data file use seeds 1-50 (choose) and 51-100 (confirm), labelled pilot.
- The github MCP tools work; the github plugin server fails to connect (400). `get_check_runs` shows CI; `get_job_logs` shows why a job failed.
- Commits with no URL line and a `Co-Authored-By:` line went through again this session.
- `npm install --no-audit --no-fund` in compassionism-simulation before `check_figures.js` or `domtest.js`; `node domtest.js` takes over 5 minutes, run it in the background.
- S66's `s66_trace.js` no longer runs on `104691f`; use `s64_erosion.js`. Old remote session branches in research-update (`claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`) need deleting by hand.
- `study_files.py` copies each study's `estimates.csv` as columns; S6 and S14 are 100-seed PILOTS the page must label. `s39-crosscheck.json` is an outside engine (BeforeIT, Austria), seeds null.
