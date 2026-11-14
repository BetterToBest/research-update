# Handoff (Nov 14, 2026): S70 part 1, the round-2 screen preregistered and dispatched

## Step status
S70 is **partly done**. The screen is preregistered (`prereg/2026-11-s70-screen.md`, with Amendment 1) and running on Actions. The specification curve S63 will preregister is designed in that file (its own section). Part 2 remains: read the results, write the plain-words note, and put the readings S63 must carry into PLAN S63.

## What shipped
- research-update (this PR): the preregistration and Amendment 1, PLAN.md notes for S70, this file.
- compassionism-sim-results [PR 36](https://github.com/BetterToBest/compassionism-sim-results/pull/36) (merged, e115e70): `runner/jobs/s70-screen.js`. Self-test: with every reading set to its main value, it reproduces the untouched main row on all 2,880 series exactly; 3 processes give the same bytes as 1.
- compassionism-simulation [PR 106](https://github.com/BetterToBest/compassionism-simulation/pull/106): `dev/tools/s70_table.js`, the analysis (Morris μ*, noise check, interaction flags, the preregistration's decision rules).

## What the screen is
- Every swept reading of round 2 moved together (Morris, 12 trajectories) around `r2MainRow`. Engine 8b96cdd, unchanged. 500 adults, 20 years, Reference and Adverse, seeds 1-40.
- Block S: 33 readings. Rows: the no-programme run, plus both designs at full backing (`o.a` 1, the main row) and at no assumed backing (`o.a` 0).
- Block F: 41 readings (S72's financing added; it runs without the weighted tail, so the tail's 3 readings are left out). Rows: both designs paid for by a contribution.
- The backed share is not screened; S63 carries it as its own curve.
- Readings that cannot act at the main row are reported as inactive: the recession slack (no spending layer), the markdown (pass-through 0), and the policy-rate rule's coefficients (fixed rate).

## In flight
- Actions, compassionism-sim-results `run-study`:
  - [run 98](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43618138821) is study `s70-screen-s`; [run 99](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/43618141288) is study `s70-screen-f`.
  - Both use engine `8b96cdd1c6c14c0bef834ccc8a0144cf86036098`, seeds 1-40, 20 shards, `--procs=4`. About 20 minutes each.
- Results land in `s70-screen-s-8b96cdd/` and `s70-screen-f-8b96cdd/`. The study is done when each folder has a `DONE` file. A failed shard: use "Re-run failed jobs" on that run.

## Decisions waiting
- D23 (filed again Nov 14). Default: the financed rows are carried beside the main rows with rate, base, cap and deficit, and the Hub leads with none of them.

## Next step
**S70 part 2.**
1. Fetch both folders: a sparse checkout of the results repository, only the two folders.
2. Run `node dev/tools/s70_table.js <folder> dev/runs/s70-screen` once for each block.
3. Write `dev/reports/s70-screen.md`, in plain words, applying the preregistration's rules 1-7 as written.
4. Fill in PLAN S63 with the readings to carry in full, carry at one reading, or hold at main.

Then S63.

## Pitfalls
- **Commits are blocked in Auto mode.** Switch to "Accept edits" before the first commit.
- The results repository is large. Clone it sparse (`--filter=blob:none --sparse`, then `git sparse-checkout set --no-cone '/*' '!/*/' '/runner/' '/.github/'`) and add the study folders by name.
- `o.a` (backing) is a row option on the programme row, not a study option. Setting `a` in `r2MainStudy()` changes nothing.
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and earlier session branches in research-update still need deleting by hand.
