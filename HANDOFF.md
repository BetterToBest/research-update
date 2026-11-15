# Handoff (Nov 15, 2026): S7 part 1 built, PR open

## Step status
S64 is done. **S7 part 1 is built; its pull request is open, checks running when the session ended (not merged).** S3 (OEIAS) runs right after S7.

## What shipped
- compassionism-simulation [PR 112](https://github.com/BetterToBest/compassionism-simulation/pull/112), branch `claude/s7-part1-study-data`, commit 394f0c5: `dev/tools/study_files.py` (`--check`) writes `data/studies/` files for S34, S36, S38, S5, S55, S6, S14 (each study's own estimates copied, not recomputed); frozen C2.2 panels in `dev/runs/`; release entry v5.7 (no headline figure changes, `figuresFrom` 5.6; Duke confirmed v5.7). `check_figures.js`: 22 of 22 pass locally. `validate`, `unit` and `domtest` are left to CI.
- No change in compassionism-sim-results (the data files point at the existing folders).

## In flight
- PR 112 checks (`checks`, `guard`). This session subscribed to the PR; a new session must check them first, then merge it (CLAUDE.md, Landing work). If they fail and cannot be fixed, leave it open and say so here.

## Decisions waiting
- None. Release 2 stays v6.0.0 unless Duke says otherwise.

## Next step
**Merge PR 112, then S7 part 2** (sonnet, medium): findings-page sections for ledger checklist items 1-11 (`findings.html`, `site/findings.js`, `dev/tools/release_data.py`), printing study figures from `data/studies/` and labelling S6 and S14 as pilots; then part 3 (notes in CONTRIBUTING.md and CHANGELOG.md, `set_version.py 5.7`, replication timeline panel, the three checks, merge); then **S3**, then **S65**.

## Pitfalls
- S66's `s66_trace.js` no longer runs on `104691f` (its price-cut probe patch matches 0 times). Use `s64_erosion.js`: no text patches, a read-only hook.
- Each row makes two full-length runs per seed (the supply path); the hook keeps the last and the key check proves it is the reported one.
- The real-holdings check is not near zero in the means: it is entirely the creditor charge on shares (S71); the asset index equals the basket deflator exactly. The per-adult means are unweighted, so the weighted-tail adults dominate the top fifth.
- The auto-mode permission classifier refused several `git commit` and `commit && push` commands early in the session; separate commit and push commands went through after the stop hook asked for them.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
- Start S7 sessions in Accept edits, not Auto: Auto's classifier refused `git commit` four times on Nov 15 (also noted early in S64). Commits and pushes worked at once in Accept edits.
- The github plugin MCP server failed to connect (400, authorization header); the built-in `mcp__github__*` tools worked.
- Nov 15 (part 1): Auto mode refused `git add && commit && push` and a plain `git commit`; after Duke said go, a plain `git commit` and a separate `git push` went through. The `mcp__github__*` tools are loaded with ToolSearch.
- study_files.py copies each study's `estimates.csv` (dev/runs/<study>/) as columns; S6 (`pilot-k-395dd5b`) and S14 (`pilot-l-f66dc67`) are 100-seed PILOTS and the findings page must label them so. `s14-lw-pilot.json` has seeds null (the report says 100).
