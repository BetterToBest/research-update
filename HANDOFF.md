# Handoff (Nov 5, 2026): S47 partly done, design freeze (manifest written; engine fixes started)

## Step status
S47 is **partly done**. Step 1 is done: the run manifest and the freeze's amendments are written. Steps 2 to 5 remain: the engine and job changes in the manifest's section 6, pinning the engine commit, the 2-seed dry run, the cost estimate from the dry run's timings, and the ledger decision that ends the chain.

## What shipped
- research-update [#48](https://github.com/BetterToBest/research-update/pull/48) (merged, 3427ab1): `prereg/run-manifest.md` (draft: every job, row, consumer, folder and a first cost estimate), study programme Amendment 9 (the design freeze), and short pointer amendments in the K, L, M, N, O, P and community-layer addenda.
- compassionism-simulation, ENGINE_PR_LINE
- The freeze choices made, all in Amendment 9:
  - every row of every study runs on the frozen engine (audit corrections `au: true` plus the second implementation's fixes `fx: true`);
  - the C2.2 design is the headline, with the release design beside it in A, B, B10, C, F and G-J; D and D10 stay on the release design; at 50,000 adults, A runs the C2.2 design only;
  - the published engine runs only in a new study R (release panel and bridge, 18 rows per environment and yardstick);
  - the line stays at $49,370 (study L's rule 3);
  - the pilots' section 9 items: adopted, except dropping the 20-year rows;
  - the outcome-5 thresholds apply to the yearly inflation rate.
- First estimate: about 670 runner-hours (about 34 hours on 20 runners), all of it fitting on Actions at no cost. Runpod would be about $46 for the two largest pieces, or about $80 for everything (pod price from Oct 12; to be re-checked).

## In flight
Nothing.

## Decisions waiting
- D14 (default A, no design change): S47 follows the default.

## Next step
**S47 again** (opus, high), part 2, in this order (manifest section 6):
1. Engine: fx part `sp`. The supply path (`s3BaseS`, index.html near line 6079) comes from `priceRun`, which has no job loss, safety net or labour response. `tbStudy` computes `S` once per seed, before its rows (line ~6559), so `sp` must be decided at study level, not per row. One way: `S` from the no-programme testbed run with those modules on, and `FX` added to the cache key. Then measure `au` and each `fx` part on 50 paired seeds in all three environments, and record the result in DECISIONS and the manifest.
2. Engine reporting keys: the design-neutral BLEI share at year 20 in 40-year runs; the S53 and S52 descriptive outputs; `testbed --frozen`; the `explore_export.js` series. Re-derive the 0.593 spending share. Write MODEL_SPEC and TESTBED_SPEC for the frozen model.
3. Jobs (compassionism-sim-results): `program.js` gets studies R and G-J, both designs, 2% and 5% participation, nulls for missing keys, and `au`/`fx` on every row; the other jobs get `--frozen`, backing gets its 116 rows, and levers gets the key trim, gzip and `--sx=main`.
4. Pin the engine commit; dry-run at 2 seeds; timings; the ledger decision ("Design frozen ..."; Actions vs Runpod).
This may take 2-3 sessions.

## Pitfalls
- Row options such as `au`, `fx`, `c22` and `cl` sit on the row object (`m.fx`); study options such as `bkm`, `lv` and `sec` sit in `m.o`. The first fx unit test set `o.fx`, and nothing moved.
- `fx.pthb` and `fx.hb` move 263 of the release row's keys on seed 1 (unit test). They are real changes, so they must be measured before the freeze.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` only (no model name).
- The GitHub plugin server failed to connect again; the built-in GitHub tools worked.
