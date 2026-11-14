# Handoff (Nov 14, 2026): S63 part 1, round 2 costed and preregistered

## Step status
S63 is **partly done**. Part 1 (costing, the preregistration, the main-row decision) is done. Part 2 remains: S69's two corrections in the engine, the job script, the dry run and Amendment 1 (PLAN S63, "Part 2").

## What shipped
- research-update, branch `claude/stoic-gates-d0meuu`: `prereg/2026-11-s63-round2-freeze.md` (new), PLAN S63 part 1 recorded, the indexes, this file. Committed and merged only if the session could commit (see Pitfalls); otherwise these files sit in the working tree for the next session.
- Ledger (version 157): S63 "doing", D26 and I18 filed.

## What the costing found
- Every reading S70's rules carry fits: about 690 row-runs per environment and seed (Source rows about 320, financed rows about 365), three environments, 500 seeds, both horizons, plus the main pair at 10,000 adults. Measured on the session machine: 0.65 s per row-run at 20 years and 1.21 s at 40 years.
- About 630 core-hours, about 160 runner-hours, about 8 hours on 20 Actions runners. That is below RUNNING.md's 1,000 core-hour mark and smaller than the S48 batch. Free, and no amendment to S70's rules.
- NVIDIA (build.nvidia.com) hosts AI-model APIs, not general compute: it cannot run the engine, and nothing needs to be set up there.

## In flight
Nothing.

## Decisions waiting
- D26: the main row. Default: today's price rule, S69's two corrections on, full backing (D25), the other readings beside it.
- I18 (issue for Duke): register the freeze file on OSF after Amendment 1, before S64 dispatches.

## Next step
**S63 part 2** (opus, high), in this order: S69's corrections behind switches (earnings below $1e-9 count as zero; weighted ranks on wealth rounded to the cent), guard test, merge, pin the commit; `runner/jobs/r2.js` with `--check` and `--selftest` (reuse the setters of `runner/jobs/s70-screen.js`); the dry run at seeds 1-2 on Actions; Amendment 1 (commit, pair and bound ends, financed screened-out figures, timings) and the run-manifest amendment; S69's program on the full-backing main row.

## Pitfalls
- **Commits are blocked in Auto mode.** Switch to "Accept edits" before the first commit. This session hit it again.
- S69's two corrections were proposed in GAPS.md but never built: grep found no switch in the engine.
- The S70 job's financed block uses `gvBase 'w'` as main. The financed C2.2 main row here is on all money income (`base 'all'`, S72). Set it explicitly in `r2.js`.
- Clone the results repository sparse (`--filter=blob:none --sparse`, then `git sparse-checkout set --no-cone '/*' '!/*/' '/runner/' '/.github/'`).
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and earlier session branches in research-update still need deleting by hand.
