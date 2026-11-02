# Handoff (Nov 1, 2026): S50 done, the second independent implementation of the release row

## Step status
S50 is **done**. Part 1 (the packet) was done earlier today. In part 2, a session that had never read the engine wrote a Python program from the packet alone, and it reproduces the published release row and its no-programme run.

## What shipped
- compassionism-simulation [#61](https://github.com/BetterToBest/compassionism-simulation/pull/61), merged `60170ef`. No engine change.
  - `dev/reports/s50-independent-implementation/`: the program `s50_release.py`, `GAPS.md`, `REPORT.md` (plain words, for Duke), and `results/` (per-seed outputs for seeds 1-500 in all three environments, both phases; `COMPARISON.md`, `COMPARISON-phase2.md`, `run.txt`, `SHA256SUMS`).
  - Phase 1 (commit 50a6ffd, pushed before the engine was opened): in all six runs and in the programme's effect, 630 of 631 keys are exact on every seed, and all 631 pass the 2-SE test. The exception, `snAbN`, counts rounding remainders of about 1e-16 of a month.
  - Phase 2: Python's and Node's maths libraries differ in the last binary digit of log, exp, pow, cos and tan. The `--js-math` switch (Node's Math, not the engine) shows that this is the only source of difference: with it, every key of every seed in all six runs is identical to the engine's in every binary digit (1,893,000 values).
- research-update (this PR): this handoff; PLAN.md's S50 section (part 2 done) and S47 step 2 (the S50 findings to fix and measure).

## Findings for the design freeze (S47; GAPS.md, phase-2 table)
- **PTH's books are opened before households are formed.** About 28% of PTH members have no books (their equity grows by the old 3-5% rule and they never leave the network), and about 25 homes a seed have books but no member.
- **The supply path's price-only run lacks job loss, the safety net and the labour response** (stale since September). As a result the no-programme price level moves 0.5% in Reference.
- **PTH home prices are set at the BLEI daily cost** (about half the basket's housing cost), against the engine's own comment.
- `snAbN` counts rounding remainders.
- **MODEL_SPEC.md needs four corrections:** the flat contribution's need; the octave cost base (the BLEI cost, deliberately); recessions can start in the last year; zone induction is for participants only. It also needs its 30 gaps closed.

## In flight
Nothing.

## Decisions waiting
None new. The findings above are model and code questions (delegated), to be fixed and measured in S47 as dated amendments.

## Next step
**S51** (added Nov 1 in the planning chat, with S52 and S53): backing as a mechanism and the break-even backing share. Then S52 (supply-shock environment), S53 (security outcomes), then **S47**, the design freeze, which now also waits on S51-S53. Ledger decision D11 (backing) is open; its default proceeds.

## Pitfalls
- The release row's programme inflation is about 51% a year in Reference (prices about 2,500 times higher after 20 years). Both programs compute it, so it is the model's rule, not a code slip: it is the S13 audit's E6 question, for S47.
- `s50_release.py` reads the packet zip. After any engine change it reproduces the old engine until a new packet is built.
- Python's math and Node's Math differ in the last digit of log, exp, pow, cos and tan (3-10% of calls). Use `--js-math` for a bit-for-bit comparison.
- The `gh` CLI has no valid token here; the GitHub MCP tools work for pull requests.
