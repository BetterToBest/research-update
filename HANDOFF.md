# Handoff (Nov 6, 2026): S47 partly done, design freeze (part 3: reporting keys, frozen modes, the spending share re-derived)

## Step status
S47 is **partly done**.
- Done: step 1 (manifest), Duke's route choice (Actions), and manifest section 6 items 1-4: the four `fx` parts; the reporting keys; `testbed --frozen` and `explore_export.js --frozen`; the 0.593 spending share re-derived.
- Remaining: item 5 (MODEL_SPEC.md and TESTBED_SPEC.md for the frozen model), items 6-7 (the job scripts in compassionism-sim-results), pinning the engine commit, the 2-seed dry run on Actions with timings in manifest section 3, and the closing ledger record.

## What shipped
- compassionism-simulation [#75](https://github.com/BetterToBest/compassionism-simulation/pull/75) (see "In flight" for its merge state):
  - reporting keys, all reporting only: `bNAy20`/`bOAy20`; under `sec`, `secF25*` (money-income falls by cause) and `secU25b*`; under `sx`, the payer breakdown `sxE*`/`sxK*`, the Source's payout by year `sxQ*_t`, and `sxVd`.
  - harness `FROZEN`, `SPEND_FROZEN`, `frozenRow`, `c22Design`; `testbed ... release ... --frozen` (C2.2 row `c22`); `explore_export.js --frozen` (its self-check passes against a 2-seed frozen panel).
  - checks: guard test identical, unit 249/249, validate, domtest 153/153, lineage link recorded.
- **The spending share, re-derived** (audit E17; Simulation `dev/reports/s47-spend.md`; tools `dev/tools/s47_spend.js` and `s47_spend_effect.js`; data `dev/runs/s47-spend/`):
  - At 0.593 the frozen no-programme run saves 19.5% of disposable income; the method's target is 5.4%. Re-derived: 0.877, or 0.862 on the method's own formula over wages.
  - The original derivation also counted the supply-path run and a repeated year 0 (counting faults, now fixed in the tool).
  - Measured on 50 paired seeds: basket poverty and inflation do not move. Savings halve. The programmes' wealth-poverty effect rises sharply: at 0.877 the C2.2 design no longer cuts wealth poverty in Reference (+0.5 points) and raises it in Adverse (+30) and Stress (+42).
  - Recorded as a dated amendment (manifest Amendment 3, study programme Amendment 10). Study R gets 3 rows at 0.593 beside the frozen ones. The published engine keeps 0.593.
- research-update (this branch): manifest section 1, sections 3-4 (R is 21 rows), section 6 items 2-4 marked done, Amendment 3; study programme Amendment 10; PLAN.md's S47 entry.

## In flight
Nothing running. #75 merges once its checks pass; if this file still says "open" for it, merge it next session first.

## Decisions waiting
- D14 (default A, no design change): S47 follows the default.
- No new decision. The share is a calibration re-derived by its own method; under CLAUDE.md that is Claude's call, recorded as an amendment. It changes the headline wealth result a great deal, so the S47 ledger record (step 5) should name it for Duke to read.

## Next step
**S47 again** (opus, high), part 4:
1. Item 5: MODEL_SPEC.md and TESTBED_SPEC.md for the frozen model: every switch `frozenRow` and the rows turn on, including the share; correct the S50 contradictions; close its 30 gaps (Simulation `dev/reports/s50-independent-implementation/GAPS.md`).
2. Items 6-7 in compassionism-sim-results `runner/jobs/`, all through `H.frozenRow` and `H.c22Design`:
   - `program.js`: R (21 rows: published, au-only, frozen, and frozen at 0.593), G-J, both designs in A, B, B10, C and F; D and D10 at 2% and 5%; nulls for missing keys.
   - `--frozen` in `c22.js`, `lw.js`, `backing.js`, `shock.js`, `security.js` and `levers.js`.
   - backing's 116 rows; levers' trim, gzip and `--sx=main`.
   - add the new keys to KEYS where the consumers read them (`bNAy20`, `secF25*`, `sxE*`).
3. Pin the engine; dry-run every job at 2 seeds on Actions; put the timings in manifest section 3; write the ledger record.

## Pitfalls
- `frozenRow` sets the row's `sc` to 0.877. A job that sets `sc` after calling it replaces the frozen share (the measurement tools do this on purpose). Under `fx.sp` the study-level `sc` does not matter; the row's does.
- Ledger-based measurements double-count: each cold seed also writes its supply-path run and tbRun's one-year rate pass into `LEDGER`. Warm the cache first, or read flows with the reporting hook and ACCT, as `s47_spend.js` does.
- Run `engine_lineage.js prove` on a clean tree; it takes about 10 minutes on 4 cores. Don't run other studies beside it.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` only (no model name).
- The GitHub plugin server failed to connect again; the built-in GitHub tools worked.
