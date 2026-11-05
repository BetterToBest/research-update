# Handoff (Nov 5, 2026): S54 partly done, policy levers (pilot stages 1-2 reported, stage 3 running)

## Step status
S54 is **partly done**. Done: the analysis script (written before the results were read), the analysis of stages 1-2, stage 3's rows in a dated amendment, stage 3 dispatched, and the pilot report for stages 1-2. Remaining: analyse stage 3 when it lands and add its section to the report. Then S54 is done.

## What shipped
- compassionism-simulation [#70](https://github.com/BetterToBest/compassionism-simulation/pull/70) (squash f0bf959): `dev/tools/s54_levers.py`, pushed as 5b22d9f before any result was read. DECISIONS (S54) records the readings where the addendum is silent.
- compassionism-simulation [#71](https://github.com/BetterToBest/compassionism-simulation/pull/71): pilot report `dev/reports/s54-levers.md`, tables `dev/reports/s54-levers-tables.md`, every cell in `dev/runs/s54-levers/`, its HANDOFF.
- research-update [#45](https://github.com/BetterToBest/research-update/pull/45) (merge eee8856): addendum Amendment 1, which lists stage 3's 246 settings before they run.
- compassionism-sim-results [#15](https://github.com/BetterToBest/compassionism-sim-results/pull/15) (squash 6dd6627): `levers.js --stage=3` and `runner/jobs/levers-stage3.json`. Stages 1-2 build byte-identical rows; a seed-1 stage-3 run reproduced 4,634 values exactly.
- Results read: `s54-levers1-e6da050/`, `s54-levers2-e6da050/` (checksums verified, `--check` PASS).

## Pilot outcome (labelled pilot, 50 seeds)
- No setting tested meets D13, in either design or at either wage. Inflation is the barrier: the BU's face value is new money, and every lever inside the design leaves 21% a year or more in some environment.
- The conversion tax has no break-even within 0-40%: it never makes the Source self-funding, basket poverty is lowest at 0%, and participation hardly moves.
- Only outside finance gets under 5%. The closest setting is C2.2 with a flat wage contribution. It fails only on big income falls (+1.4 to +5.2 per 100 adult-years).

## In flight
- Study `s54-levers3` (stage 3, seeds 51-100, 250 rows per environment): run [42112585864](https://github.com/BetterToBest/compassionism-sim-results/actions/runs/42112585864), 25 shards, engine e6da050, `levers.js --stage=3 --env=all --procs=4`. It is done when `s54-levers3-e6da050/DONE` exists in compassionism-sim-results. A failed shard: "Re-run failed jobs".
- Then run `python3 dev/tools/s54_levers.py --s3 ../compassionism-sim-results/s54-levers3-e6da050 --list dev/runs/s54-levers/stage3-settings.json` (run `--s3 ... --check` first). Replace the report's "Stage 3 (running)" section, then the S54 step is done.

## Decisions waiting
- D14 (new): should the design change before the freeze? The C2.2 design paid by a flat wage contribution or a land-value tax is the only route under 5% inflation. Default: no change; S47 carries study N as preregistered.

## Next step
**S54** (continued, short: stage 3's analysis and report section). Then S47, the design freeze. D14 has a default, so it blocks nothing.

## Pitfalls
- A commit trailer named the model (branch commit 5b22d9f, before the squash). Commit trailers must read `Co-Authored-By: Claude <noreply@anthropic.com>` only.
- A sparse, blob-less clone of compassionism-sim-results: `git ls-tree -l` fetches every blob, one at a time. Use `--name-only`.
- The three issuance caps give identical rows: each removes the whole premium, since the BU's face value alone exceeds the cap.
- Recycling expired BU is inert in combination: smaller BU leave nothing unspent.
- Under C2.2, "non-participants" (the X group) receive the BU too. The group is the model's fixed set of adults who would not choose to join.
