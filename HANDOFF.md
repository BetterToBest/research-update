# Handoff (Nov 14, 2026): S69 part 2, the independent program (S69 done)

## Step status
S69 is **done**. A Python program written from the S69 packet alone reproduces the candidate main row of round 2 and its no-programme run (Reference, Adverse, Stress; seeds 1-500) to rounding. The rerun on the full-backing main row (D25) is left to S63 to schedule, before S64 dispatches.

## What shipped
- compassionism-simulation [PR 105](https://github.com/BetterToBest/compassionism-simulation/pull/105) (merged, 8b96cdd): `dev/reports/s69-independent-implementation/` with the program, REPORT.md (plain words, for Duke), GAPS.md, results/ (per-seed results gzipped, comparison tables, run.txt, SHA256SUMS), and one DECISIONS.md entry (the acceptance rule).
- research-update (this PR): PLAN.md notes for S69 and S63, this file.

## What the check found
- 948 of 958 no-programme keys, and 677-694 of 990 programme keys, are exact (relative 1e-9) in every seed. Every key and every programme effect is within two standard errors: 0 failures in 5,844 key tests and 2,874 effect tests.
- Every non-exact value has a rounding cause in the last binary digit. V8's `Math.pow(1.02, 12)` is one digit off the correctly rounded value, which Python gives. The two causes:
  - (a) Under `lf.pm`, a worker whose whole earnings go to the income effect earns ±1e-10, not 0. That decides "worked" and next year's EITC test. It moves dollar figures in 1-3 seeds of 500, by under 1e-5.
  - (b) Households sit within 1e-11 of the borrowing limit, which reorders the weighted fifths and low percentiles.
- GAPS.md:
  - 3 contradictions. The one that matters: with `lf.fl` and no ages, the year-0 draw uses `CFG.LF_SHARES`, not the fitted stock that MODEL_SPEC 14.15 states.
  - 18 gaps: the CPS wage reading is not described; RT_*, WT_CUTS and GV_US are missing from the config; Stress's config lacks the two supply-path captures; the reporting keys are defined only by code.
  - Two reporting corrections are proposed to S63, behind switches.

## In flight
- Nothing running.

## Decisions waiting
- D23 (filed again Nov 14). Default: the financed rows are carried beside the main rows with rate, base, cap and deficit, and the Hub leads with none of them.

## Next step
**S70** (screen every swept parameter together, then design the specification curve), then S63. S63 also decides the two reporting switches. Before S64, it schedules S69's rerun on the full-backing row: a packet built on that row with `make_s69_reference.js`, then `s69_main.py` and `s69_compare.py`, about 25 minutes for the six runs (PLAN.md, S63).

## Pitfalls
- **Commits are blocked in Auto mode** ("Destructive or Unwanted Actions"), in both parts of S69. Switch the mode dropdown to "Accept edits" before the session's first commit; each command then asks for approval.
- The S69 packet's main row is the backed share 0 (the backing curve's low end), not the full-backing row Duke chose (D25). Its figures are not the headline.
- The engine clone was sparse (only the packet and the report folder) to keep phase 1 honest. Add paths with `.git/info/sparse-checkout` before reading anything else.
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and earlier session branches in research-update still need deleting by hand.
