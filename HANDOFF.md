# Handoff (Nov 6, 2026): S47 part 4, design freeze (specs written, every job script built, dry run started)

## Step status
S47 is **partly done**. Manifest section 6 is complete (items 1-7). The engine is pinned at `ce8d030` (manifest section 1). The 2-seed dry run of every job is running on Actions.
Remaining (part 5): check each dry-run folder and load it in its consumer's script (manifest section 7); put the timings in section 3 and the cost in section 8; mark the manifest frozen; write the S47 ledger record (step 5), which names the spending-share change (Amendment 3) for Duke to read.

## What shipped
- compassionism-simulation [#76](https://github.com/BetterToBest/compassionism-simulation/pull/76) (merged, squash ce8d030, the pin; checks green): MODEL_SPEC.md section 13 (the frozen model and the C2.2 design), the eight S50 contradictions corrected in place, Appendix C (the 30 gaps); TESTBED_SPEC.md section 6; `s54_levers.py` reads gzip shards.
- compassionism-sim-results [#16](https://github.com/BetterToBest/compassionism-sim-results/pull/16) (031861a):
  - `program.js` with studies R and G-J, both designs (`c22`, `rls`) and 2% and 5% in D and D10. Every row is frozen except R's published and audit-only rows. Keys that mean nothing for a row are written as null.
  - `--frozen` in the six other jobs. Backing has 466 rows, security 12; levers gains `--sx=main` and `--gzip`.
  - `panel.js` and `series.js` (the R-panel and X jobs).
  - The workflow gzips shards when `--gzip` is given.
  - Every `--check` passes. Each job ran one seed on the session machine.
- research-update (this branch): manifest section 1 pinned, section 3's R-panel and X commands, section 6 items 5-7 done, section 7's dispatch list; PLAN.md's S47 entry.

## In flight
- 26 run-study runs on Actions, started Nov 6 about 02:07 UTC: engine `ce8d030`, job scripts at `031861a`. The list is in manifest section 7.
- Results land in compassionism-sim-results as `dry-<id>-ce8d030/`, each with run.txt, SHA256SUMS and `DONE`.
- A run that failed has no folder: its log is in the Actions tab (workflow run-study, runs 42148172842 to 42148283075).
- The levers folders hold `shard-0000.json.gz`.
- Watch `dry-a50`: 50,000 adults, which tests memory at 2 processes.

## Decisions waiting
- D14 (default A): S47 follows the default. No new decision this session. The S47 record (part 5) names the spending share's effect.

## Next step
**S47 again** (opus, high), part 5. Every manifest step is below; the order is the manifest's.
1. Each `dry-*` folder in compassionism-sim-results has `DONE`. For each, run its consumer (manifest section 7) on that folder. `pilot_studies.py` hard-codes the pilot folders and 50 seeds, so for A-J check loading with a short script, or give it folder and seed arguments.
2. Put the measured seconds per seed into section 3 (500-seed runner-hours at 2 processes) and update section 8. Shard counts: about 2 hours a shard.
3. Mark the manifest frozen (status line, section 7 result) and add a dated amendment if anything changed. Write the ledger record (step 5). The chain stops there. S48 then dispatches the manifest exactly.

## Pitfalls
- `pilot_studies.py`, `c22_pilot.py` and `lw_pilot.py` read the pilots' folder names and seed counts. The batch's row names now carry a design segment (`ENV.nN.yY.c22.cps.main`), so their loaders need a prefix change before S36.
- The C2.2 design's automatic receipt marks adults as taking part even in cells without CCO. Only `octMean` showed it, and it is now null there. Outcomes are equal on the two designs (checked).
- `panel.js` and `series.js` use the workflow's "seed range" as a shard index (I-I picks the environment, horizon and piece). Their own seed count is `--n`.
- The GitHub plugin server failed to connect again; the built-in GitHub tools worked. The PR API returned "too many files changed" for #76 (a GitHub-side error); the Actions API worked.
- A stray `/x.log` (737 bytes, a failed command's log) is in the container's root; harmless.
