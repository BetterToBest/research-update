# Handoff (Nov 13, 2026): S60 done, bargaining power (a worker's outside option and an employer markdown)

## Step status
S60 is **done** in one session. It added no step. S7 stays held.

## What shipped
- research-update: `prereg/2026-11-s60-bargaining-power.md` (committed before the build and any run; Amendment 1 before the pilot), PLAN.md (S60 findings; notes for S62, S63, S68, S70), PLAN-done.md, a dated correction in `audits/2026-11-s39-s55-review-triage.md` (C5: the US experiment is now *QJE* 2026, 4.2 points and $1,900), the indexes, this file. Branch `claude/keen-lamport-q6fs3d`.
- compassionism-simulation [PR 98](https://github.com/BetterToBest/compassionism-simulation/pull/98): merged (8621003), checks green. Switch `BARGAIN` (row option `bg`); off identical (guard test, lineage); 7 unit tests (`bgUnitSuite`); `sources/s60_bargain.py`; report `dev/reports/s60-bargaining-power.md`; tables `dev/runs/s60-bargain/`.
- compassionism-sim-results [PR 31](https://github.com/BetterToBest/compassionism-sim-results/pull/31), merged (356eb0c): `s60-bargain-69f69f5` (seeds 1-100, three environments, plus the validation run; run.txt, SHA256SUMS, DONE).

## Findings (plain words; pilot, seeds 1-100, 500 adults; intervals unadjusted)
- **The evidence gives about zero.** Austrian benefit reforms: under a cent of wage per dollar of fallback, more than 3 cents ruled out (Nash theory predicts 24-48). The US $1,000-a-month experiment: no rise in hourly pay or in the lowest wage people would accept. Kenya's wage gains came from demand. So the main reading (pass-through 0) is identical to off.
- **At the 3-cent bound:** about $650 a worker-year in the release design ($910 in C2.2; $280 release under Stress), 5-9% of the programme's raises; poverty a further 0.1-0.6 points lower. **At 10 cents** (the US experiment's bound): 15-24%; poverty 0.4-1.9 points lower.
- **The theory readings (24, 48 cents), which the evidence rejects,** would make bargaining 28-59% of the wage gains; the Nash relation cannot even produce the measured pass-throughs with the measured markdown.
- **The programme's fallback is large** ($22,400 a worker-year, a median 33% of earnings) yet, on the evidence, moves wages little. Every reading keeps every sign.
- **No payer:** a raise comes out of owners' markdown (at 10 cents 7-23% of adults' capital income) and lowers inflation under today's price rule.
- **Validation:** 15.6 cents of earnings lost per transfer dollar per worker (study 16): passes. Nobody stops working in the engine (study −4.2 points): a limit for S70 and S63.
- **For S63, fixed before the results:** `bg` at 0 in the main row, 0.03 beside every wage, income and poverty result, 0.10 as the outer reading.

## In flight
- Nothing.

## Decisions waiting
- D21: carry the C2.2 design paid for by a contribution on every round-2 outcome (default: yes, as a labelled reading).
- S63 files the main-row price-rule decision (S67's recommendation, both views).
- Nothing new from S60.

## Next step
**S62** (PTF realism): its waits (S60, S56) are done; it is the first open row of the Order table. S68 and S70 wait on S62.

## Pitfalls
- The container restarted mid-pilot and lost every unsaved chunk: run pilots in small chunks that each save a file and skip chunks already saved (`dev/tools/s60_bargain.js --rows`).
- A reporting leak older than S60: `PDS` is reset only where the production side acts, so a no-programme row reports the previous programme run's `pdC*` and `pdMem19`. Never read them for a no-programme row; S68 resets module state per run.
- Unit tests comparing whole studies need an uncounted warm-up run and the same row structure each time (rows of a study share cached supply paths); they passed alone and failed inside the full suite until then.
- `bg` needs the labour response (testbed runs set it). Never quote a pass-through above 0.03 for a wealth or price result: no one pays the raise, and it lowers inflation mechanically.
- Commit trailers: `Co-Authored-By: Claude <noreply@anthropic.com>` (no model name).
- The remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x` and earlier session branches in research-update still need deleting by hand.
