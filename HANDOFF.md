# Handoff (Nov 15, 2026): S7 part 2, third session

## Step status
S64 is **done**. **S7 is partly done.** Part 1 merged earlier. Part 2: the Studies section (PR 113) and the first method notes and glossary (PR 114) are merged. This session wrote items 5 (inflation wording) and 8 (Holm families) in an open PR. Still to write: items 2, 3, 6, 7, 9, 10 and the S55/S56 wording. Part 3 (notes, version, checks, merge) not started. S3 runs right after S7, then S65.

## What shipped
- [compassionism-simulation PR 114](https://github.com/BetterToBest/compassionism-simulation/pull/114): merged (580abab on main at session start).
- [compassionism-simulation PR 115](https://github.com/BetterToBest/compassionism-simulation/pull/115), **open, checks (checks, guard) were still running at session end**: new `data/studies/s39-crosscheck.json` (added to `CSV_STUDIES` in `dev/tools/study_files.py`), and two notes in `site/notes.js` ("What the programme does to prices", "Which tests form a family"). Local: figure check 22/22, `study_files.py --check` 9 files match, notes render in jsdom with no NaN. Next session: merge PR 115 once its checks pass.

## Part 2: what remains
Pattern: study numbers as a file in `data/studies/` (generator `dev/tools/study_files.py`), then a function in `site/notes.js` that reads it (a note with no data file is a function with file `null`); never type a figure.
- (6) participants and non-participants: `dev/runs/s5-participation/estimates.csv` holds only bNAPy, fgt0PY, ppov_19, cost, endoAnn, jnP19; the `gPart*`/`gNon*` groups are in the shards `prog-d-ce8d030` and `prog-d10-ce8d030` (compassionism-sim-results, about 24 MB each, 4 shards for D). Needs a reader in `dev/tools/` (start from `s5_participation.py`) and a paired comparison against each group's own no-programme baseline. Do not name non-participants as the cause of the opt-in result unless the group figures show it.
- (7) levers: `dev/runs/s54-levers/` (stage1-3 effects, `stage3-settings.json`) and `dev/reports/s54-levers*.md`: front points entering confirmation, how many survived, the share, paired differences with intervals.
- (10) tax-financed C2.2 from study N: label 500 adults, 20 years.
- (2) saving and spending by income group: no data file; short session-machine run of the frozen no-programme row (free), tool in `dev/tools/`.
- (3) wealth poverty, ordinary and inflation-protected savings: release rows `sav`, `sav0` in `dev/runs/release-panel-frozen.json`; no-programme twins in studies P and N (`p-ce8d030`, `n1`-`n3x-ce8d030`, shards only).
- (9) variance reduction from paired seeds: no report found; needs a measurement.
- S55/S56 wording (PLAN.md S7 section): the open-access tables beside the members-only ones, the rule-2 sentence, the low-share check, the S56 list of sentences. The S56 "never say 0-1 is shown" item is already in the inflation note.
- The 5.4% and "updated Sept 30, 2026" are copied from the ledger and S47 report, not opened at BEA/FRED.

## In flight
- Nothing running except PR 115's checks.

## Decisions waiting
- None.

## Next step
**S7 part 2, continued** (sonnet, medium): merge PR 115, then the items above, then part 3, then **S3**, then **S65**.

## Pitfalls
- Auto-mode commit fix (Nov 15) worked: this session's commit with no URL line and a `Co-Authored-By:` line went through, push too. Not yet known whether the session ran in Auto mode; if the next Auto session is refused, the cause is something else.
- `npm install --no-audit --no-fund` in compassionism-simulation before `check_figures.js` or `domtest.js`. `node domtest.js` takes over 5 minutes; run it in the background. It loads only `site/charts.js` and `site/findings.js`.
- The `mcp__github__*` tools work; the github plugin MCP server fails to connect (400). `pull_request_read` with method `get_check_runs` shows CI; `get_status` shows nothing for Actions.
- S66's `s66_trace.js` no longer runs on `104691f`; use `s64_erosion.js`.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update need deleting by hand.
- `study_files.py` copies each study's `estimates.csv` as columns; S6 and S14 are 100-seed PILOTS and the page must label them. `s14-lw-pilot.json` has seeds null (the report says 100). `s39-crosscheck.json` is an outside engine (BeforeIT, Austria), seeds null.
