# Handoff (Nov 17, 2026): S82 part 2a (sources, the job), beside S87 part 1

## Step status
**S82 partly done.** Done: part 1 (preregistration, switches built); part 2a (sources opened, Amendment 2, v5.9.17, the job `s82.js` with checks 1-8 passing). Part 2b is left: section D's reporting keys, the screen in Stress and with the tail (question 7), the full outside reading, the dry run, the timings and dispatch lines in Amendment 2, and the batch on GitHub Actions. Part 3: the report and the findings-page text.
**S87 partly done** (another session). Items 1-3 and the case for and against metal backing are done; items 4-8 are left (the page's "Still being checked" section lists them).

## What shipped
- compassionism-simulation PR 152 (v5.9.17, merged `7a5408c`; CI green): `SL_SRC` from opened sources (`sources/s82_supply.py`); `fx.eb` (the PTH equity base from the basket); `WT_CUTS.p95`; `acctDrawCheck`; `fs` not built. Guard test identical; lineage proof recorded; 390 unit tests.
- compassionism-sim-results PR 52 (merged `2ffeb79`): `runner/jobs/s82.js` (137 rows a folder; `--check`, `--selftest` = checks 1-8, `--dry`).
- research-update: Amendment 2 in `prereg/2026-11-s82-v6-supply-indexing.md`; PLAN.md (S82 row and section; Duke's S85 note on automation).
- Earlier the same day (S87): research-hub PR 35 (`us-money-history.html`), bettertobest.github.io PR 7, `audits/2026-11-17-s87-reading.md`.

## What the sources say (Amendment 2, plain words)
In 2025 no sector has idle capacity beyond normal use: vacancy below its long-run mean, food manufacturing above its mean, hospitals 75% full against 64% in 2009-2019. Housing has large headroom: households consume about 1.8 times the needs baskets' housing; elasticity 0.70; 20% of a lasting gap built each year. Medical care and food have none on household spending, so new capacity alone answers them (design-parameter speed 0.25). The sourced reading is therefore close to the strict bound for those two. This was stated before any run.

## Duke's S85 note (Nov 17)
AI and automation raise output per hour but cut hours, and may displace workers in the near term; the programme can prevent much distress if well run. It is recorded in PLAN.md S85 with Claude's plan: output per hour and hours as separate inputs; displacement on both sides of each pair, from sourced ranges. Whether the programme prevents the distress is measured, not assumed.

## In flight
- None (no study run).

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change).

## Next step
**S82 part 2b** (opus, xhigh). Do in this order:
1. Build study option `s82` (reporting only): the real BU and real wage at year 20; the no-programme run's unmet need by fifth; the weighted share below 30 days; wages over factor income; wealth poverty at half the same seed's no-programme median, for both runs (the programme row needs the no-programme median, for example from the supply-path run); the weights comment near `index.html` 4237. Add `s82: true` to the job's study options.
2. Give `s70-screen.js` an `str` environment and a tail flag for its financed block, with a dated note in the preregistration on the two bases not read with the tail.
3. Get the full outside reading (Mistral with streaming).
4. Run the dry run (`s82.js --dry --seeds=1-2 --procs=4`) and record its timings and dispatch lines in Amendment 2.
5. Dispatch six runs of `run-study` (study `s82-v6-<env>-<years>`, job `s82.js`) and the screen.

**S87 part 2** (opus, high) can run beside it.

## Pitfalls
- `fx.pe` is already a frozen-model fix (the PTH estate); the new option is `fx.eb`.
- `domtest.js` takes over 15 minutes locally. Its first run, beside other heavy jobs, reported 2 of 162 checks failed; the rerun on the same tree passed all 162. CI's guard job takes about 2 minutes.
- FRED's first request timed out once; a retry worked. NVIDIA: Mistral Large answers only with streaming; Nemotron Ultra returned 503 twice.
- The outside reading's extra sources (Census construction surveys, NASS, AHA) were not opened; Amendment 2 says so.
