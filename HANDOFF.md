# Handoff (Nov 15, 2026): S7 scoped

## Step status
S64 is **done** (Nov 15). **S7 has started: scoping only, no release work landed.** Duke moved S3 (OEIAS) up in the order: it now runs right after S7 (row "23 bis" in PLAN.md).

## S7 scoping (Nov 15)
- The S48 merged published panel (compassionism-sim-results `panel-merged-ce8d030`, engine ce8d030) equals the v5.6 panel (`dev/runs/release-panel.json`, engine 5bf5bcc) in all 47,466 values. So release 1 changes no published headline figure; it adds the frozen C2.2 panel (`release-panel-frozen.json`, `-40-frozen.json`) and the studies S36, S38, S5, S55, S34, S6, S14 as new data and findings-page sections.
- The findings page (`findings.html`, `site/findings.js`, `dev/tools/release_data.py`) has none of the ledger's 11 checklist items yet (saving-rate target wording, group tables, Holm families, glossary entries and so on), and `data/studies/` holds no files for S36-S55.
- Release path (`dev/ADDING-A-RELEASE.md`): "a release that changes no figure" (LATEST entry) for the headline; new studies as `data/studies/*.json` written by a `study_data.py`-style generator, as for s137 and s57.
- Proposed version labels (Duke may change): v5.7.0 for release 1, v6.0.0 for release 2 (S65).
- Proposed split: S7 part 1 data files and release entry; part 2 findings-page sections for checklist items 1-11; part 3 notes, version, checks, merge.

## In flight
- Nothing running.

## Decisions waiting
- Nothing new (version labels above default as proposed).

## Next step
**S7 part 1** (sonnet, medium), then S7 parts 2-3, then **S3**, then **S65**.

## Pitfalls
- S66's `s66_trace.js` no longer runs on `104691f` (its price-cut probe patch matches 0 times). Use `s64_erosion.js`: no text patches, a read-only hook.
- Each row makes two full-length runs per seed (the supply path); the hook keeps the last and the key check proves it is the reported one.
- The real-holdings check is not near zero in the means: it is entirely the creditor charge on shares (S71); the asset index equals the basket deflator exactly. The per-adult means are unweighted, so the weighted-tail adults dominate the top fifth.
- The auto-mode permission classifier refused several `git commit` and `commit && push` commands early in the session; separate commit and push commands went through after the stop hook asked for them.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
