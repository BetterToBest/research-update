# Handoff (Nov 18, 2026): S82 part 2b (the strict-bound sweep, the reporting keys, the batch dispatched)

## Step status
**S82 partly done.** Part 2b is done and the batch is running. Part 3 is left: once all nine result folders show `DONE`, the analysis as preregistered, the plain-words report and the findings-page text.
**S87 done** (Nov 18, another session: research-hub PR 37, root site PR 8).
**S88 done** (Nov 18, unplanned, Duke's edits): research-hub [PR 38](https://github.com/BetterToBest/research-hub/pull/38) (merged `a7603ad`: money-history page wording, "media", average house price, 2026 metals note, clarity pass); compassionism-simulation [PR 155](https://github.com/BetterToBest/compassionism-simulation/pull/155) (the central-bank aim note off the findings page; text only; checks were queued, merge it once they pass). House tile checked: 2023 median 58,952 hours is right; Duke's book figure of about 8,000 hours for a 1970s house cannot be reproduced (Census gives 14,600 to 24,800). **S89 is Duke's:** find his old Reddit posts on gold and crypto.

## What shipped
- compassionism-simulation [PR 154](https://github.com/BetterToBest/compassionism-simulation/pull/154) (v5.9.18, merged `eb0969c`; CI green): `sl.lam` (the building speed by sector) and study option `s82` (section D's keys). After the outside reading, the real BU now divides by the needs' price. Also: the weights comment corrected, `earlier-engine.html` resynced. Guard test identical, lineage links recorded, 393 unit tests.
- compassionism-sim-results [PR 53](https://github.com/BetterToBest/compassionism-sim-results/pull/53) (merged `4881a84`): `s82.js` (231 rows, checks 1-10 pass); `s70-screen.js` (Stress, `--env=all`, block FT: the financed rows with the tail, the base held at wages).
- research-update: Amendments 3 and 4, and the dry run and dispatch section, in `prereg/2026-11-s82-v6-supply-indexing.md`; `audits/2026-11-18-s82-prereg-reading-nemotron.md` (the reply word for word, with its triage) and `audits/nvidia-2026-11-18-s82/`; research rule 9 in CLAUDE.md; PLAN.md.

## Duke's requests this session (Nov 18)
- "A sweep on the strictest bound": Amendment 3.
  - For medical care and food, the sourced reading differs from the strict bound only by an unsourced building speed (0.25). It is swept at 0, 0.1, 0.5 and 1; at 0, those two sectors are at the strict bound.
  - The strict bound also runs on backed shares 0.125-0.875.
  - Every "holds under the sourced limit" statement must name the slowest building speed at which it still holds.
- His rule of thumb for engine additions ("source, measure, sweep test, inspect, verify, if correct validate, if not modify and repeat; the sweep is key") is research rule 9, recorded with how it maps onto the guardrails. Modify means fixing a defect, or an amendment and a rerun; never tuning toward a figure.
- From the outside reading, Amendment 4 sweeps the unsourced essentials price response θ at half and double.

## In flight (GitHub Actions, run-study runs 128-136, dispatched 01:45 UTC Nov 18)
- Engine `eb0969cc56615d3c268c7a9dd17951be0b8d3d37`. Results land in compassionism-sim-results `main`:
  - `s82-v6-{ref,adv,str}-{20,40}-eb0969c/` (seeds 1-500, 20 shards each);
  - `s82-screen-s-str-eb0969c/`, `s82-screen-ft-eb0969c/`, `s82-screen-f-str-eb0969c/` (seeds 1-40).
- Done when each folder has `DONE` beside `run.txt` and `SHA256SUMS`. Expected within about 4-5 hours: 180 jobs at 20 at a time.
- If a run failed, rerun only that study id. A folder that is already `DONE` cannot be overwritten.

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change).

## Next step
**S82 part 3** (opus, xhigh), once the nine folders show `DONE`. Analysis exactly as in the preregistration's Analysis section and Amendments 3-4:
- paired effects with bootstrap intervals; break-even shares, the strict bound also on its 9-point grid;
- the slowest building speed; the θ check; Holm adjustment;
- the Q4 factorial; Q5 by fifth (`s82Uq`, `s82Xq`); Q7 by S70's screen method.

Then the report (`dev/reports/s82-supply-indexing.md`) and the findings-page text (decision rule 5). If the folders are not done, S85's preregistration can start (it needs S82's limit only for its readings).

## Pitfalls
- A container restart cut both outside-reading streams. Nemotron Ultra answers in about 6 minutes (32,000 tokens, streaming). Mistral Large was too slow for a 228,000-character packet.
- `earlier-engine.html` must be resynced after any engine edit (`python3 dev/tools/sync_earlier.py`), or domtest's source-parity and earlier-engine checks fail.
- The packet builder's code slice started at the first S82 comment in `index.html` (line 5568), not at the supply limit. Harmless, but it makes the packet large.
- The job runs one row at a time, so a programme row cannot see the no-programme row. The half-median wealth line reads the supply-path run (`fx.sp`) instead.
