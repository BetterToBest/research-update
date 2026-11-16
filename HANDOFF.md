# Handoff (Nov 16, 2026): S77 done (S74 and S75 readings rerun with the release's settings; sticky-bar fixes, v5.9.1)

## Step status
**S77 is done.** It also fixed the two page bugs Duke reported at its start (v5.9.1).

## What shipped
- compassionism-simulation [PR 132](https://github.com/BetterToBest/compassionism-simulation/pull/132) (merged; v5.9.1). On both simulation pages, release 1's controls float under the section links and show only over release 1's sections. Section links now land on the clicked section: sections stop below the bar's measured height, and the target is held for 2 s while the charts above it draw. Links to sections that an earlier release lacks are hidden. Code: `site/stickynav.js`.
- compassionism-simulation [PR 133](https://github.com/BetterToBest/compassionism-simulation/pull/133): the S74 report is corrected throughout, and the S75 report has a dated correction. It also adds the tables (`dev/runs/s77-sweep`, `s77-fd`, `s77-s75`) and the checks (`dev/tools/s77_check_off.py`, `s77_check_start.js`, `s77_sweep_summary.py`).
- compassionism-sim-results [PR 48](https://github.com/BetterToBest/compassionism-sim-results/pull/48) (`s74-sweep-d94b73c`, `s74-fd-e5649ef`) and [PR 49](https://github.com/BetterToBest/compassionism-sim-results/pull/49) (`s75-eras-e5649ef`): both merged.
- research-hub [PR 17](https://github.com/BetterToBest/research-hub/pull/17): `us-policy-eras.html` corrected, its "correction pending" notice replaced by a dated note, and the wiki card updated.
- research-update: S75 preregistration Amendment 5 (committed before the rerun), PLAN.md (S77 done), this handoff.

## Findings that changed (all are in the reports' dated notes)
- **S74:** no primary verdict and no decision-rule verdict changed. S76's note said every interaction verdict held, but that is true only for P1. Two others changed:
  - History P3: the interaction is now null for both designs.
  - Stress, release design, P5: the interaction now excludes zero (+0.07).
- **S74, secondary readings:**
  - P2 as a share of income: C2.2 is now less steady in Stress and Reference.
  - C2.2's top 1% share in Adverse and Stress now falls, though not distinguishably from zero.
- **S75:** C2.2 now lengthens recovery from an income shock in 1973-1983, by 0.07-0.17 years. Its reversals are now 6 favourable and 6 unfavourable, so C2.2 keeps its direction in 107 of 120 cells. The release design keeps its direction in 120 of 120. The 8·6·1 tally is unchanged.
- **Hub tiles now read** 227 of 240 kept, and 40-51 points (release design 22-30).

## Checks
- In each S74 rerun, the no-central-bank arm equals release 2 per seed (720 values). The discount readings equal the sweep's cells exactly (410,880 values).
- With the S75 tool's start, the main pair reproduces release 2 in Reference.
- All sweep figures in the report are read by `s77_sweep_summary.py`, which reproduces the first publication from the first run's tables.
- Pages: validate, unit, domtest (153), check_versions and guard all pass. Every nav link was clicked at 1050x480 and 390x844 on both pages. The Hub page was rendered at 390 and 1200 px with no errors.

## In flight
- PR 133 and Hub PR 17: merge them once PR 133's checks pass. If they are still open, the checks failed or had not finished; the PR says which.

## Decisions waiting
- None.

## Next step
S24 (sonnet, medium): the corrections package on the Hub, then PDFs rebuilt.

## Pitfalls
- **Every study tool must call `H.applyNR6(); H.tbSetG(H.TB_PROFILE_G);`.** S77 found no other tool that lacks them, but check a new tool's "off" arm with `dev/tools/s77_check_off.py` (for sweep-format files) before trusting it.
- A sweep file stores values to 6 significant digits, so compare at a relative 1e-5, not exactly.
- The results repository is a sparse clone: run `git sparse-checkout add <folder>` before `git add`, or the files are silently skipped.
- Eight jobs on 4 cores roughly doubles each run's time. S75 alone takes about 45 min on 4 cores.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
