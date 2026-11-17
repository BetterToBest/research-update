# Handoff (Nov 17, 2026): S82 part 1, the v6 readings preregistered and built

## Step status
**S82 partly done.** Part 1 done: preregistration (with Amendment 1) and the switches built, off by default. Part 2 left: sources for the headroom values (Amendment 2), the keep-as-savings reading (`fs`), the job `runner/jobs/s82.js` in compassionism-sim-results, the 2-seed dry run, then the batch on GitHub Actions (about 108 core-hours, free). Part 3: the report and the findings-page text.

## What shipped
- research-update PR 170 (merged by this session's end): `prereg/2026-11-s82-v6-supply-indexing.md` (Amendment 1: the build, what was seen, the outside reading), PLAN.md (Duke's second Nov 17 discussion; S82's row), the outside-reading packet script `audits/nvidia-2026-11-17-s82/build_packet.py` and its reply.
- compassionism-simulation PR 151 (v5.9.16, merged `2120662`; CI green; lineage proof recorded; 389 unit tests): price options `sl` (supply limit for housing, care and food; readings full, sourced, restricted, strict; sharing rules pay, even, bu; basket poverty on what was received), `wc` (wage catch-up), `bl` (the BU's delay); `s82UnitSuite`; `dev/reports/s82-supply-reading.md` (Claude's reading of Duke's Nov 17 points); DECISIONS "S82". Guard test identical.

## How Duke's Nov 17 points were answered (plain words, in the reading note)
No ceiling at today's consumption: supply starts from the economy's headroom (idle capacity, the above-needs use better-off households give up as prices rise, capacity built over the years). The "restricted" reading is labelled as today's land-use, residency and farm policies. The "strict" bound is always shown but is never a headline alone. Three sharing rules side by side, the market's first. Monthly and quarterly cost-of-living adjustments (the design's; the Hub's surge protocol already says monthly) reported first. The Creative Collectives' lending goes to S85.

## In flight
- None (no study run).

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change).

## Next step
**S82 part 2** (opus, xhigh): open the sources named in the preregistration, section A, and convert them to shares of the no-programme needs consumption (not of sector output; Amendment 1). Then fix `SL_SRC`, build `fs` with its accounts or drop its rows, write `s82.js` (rows as the Design table; checks 1-8), and do the dry run, Amendment 2 and the dispatch. S87 may run beside it (opus, high).

## Pitfalls
- The supply limit's excess `e` is measured against the needs baskets (the engine's `essD`), so `v` and `m` must be shares of needs consumption. A sourced share of sector output must be divided by needs' share of output.
- The realised cut is within about 5% of the target, not exact (allocation is adult by adult with last year's normalisers). Report `slCutSh` beside `slR*`.
- NVIDIA's catalogue: Nemotron Ultra answered 503 (overloaded) twice. Mistral Large answered only with streaming (`"stream": true`; a plain request hit a 502 gateway timeout).
- S87: Duke's figure of about 5 oz of silver a week for the old minimum wage does not match a rough first look; recompute from opened sources.
