# Handoff (Nov 5, 2026): S54 done, policy levers (pilot stages 1-3 reported)

## Step status
S54 is **done**. Stage 3 (the confirmation on fresh seeds 51-100) is analysed as preregistered, and the pilot report is complete.

## What shipped
- compassionism-simulation [#72](https://github.com/BetterToBest/compassionism-simulation/pull/72): the stage 3 section of `dev/reports/s54-levers.md`, and tables for all three stages in `dev/reports/s54-levers-tables.md` (stages 1-2 regenerate byte-identical). Every stage 3 cell is in `dev/runs/s54-levers/stage3-effects.csv.gz`. `s54_levers.py --csv` now writes stage 3 too; this changes output only (DECISIONS S54). HANDOFF updated.
- Results read: compassionism-sim-results `s54-levers3-e6da050/` (run 42112585864, 25 shards). Checksums pass and `--check` passes (750 rows, 33 keys). The settings file's SHA-256 matches addendum Amendment 1.
- Earlier today: #70 and #71 (script, stages 1-2 report), research-update #45 (Amendment 1), compassionism-sim-results #15 (stage 3 job).

## Pilot outcome (labelled pilot; chosen on seeds 1-50, confirmed on 51-100)
- No setting meets D13 (Duke's rule). Rule 4 chose none, so stage 3 could not confirm a best setting.
- Three points of the C2.2 trade-off front pass the poverty and no-harm tests on fresh seeds, all at 29-82% inflation a year:
  - the Source keeping half of project sales (wages 100%);
  - the capped protected account (wages 100% and 90%).
  They are confirmed points of the front, not findings of a best setting.
- These three failed rule 4's strict no-harm test on the choosing seeds and pass rule 5's half-point margin. Both rules were preregistered.
- No release-row point passes. Most fail four no-harm tests at once (non-participants' wealth poverty, months of cover, big income falls, wealth poverty overall).
- The flat wage contribution (C2.2) is again the only point under 5% inflation. It fails again on big income falls, by the same amount (+1.4 to +5.2 per 100 adult-years).
- Fresh-seed estimates differ from the choosing seeds' by a median of 0.1-0.4 points.

## In flight
Nothing.

## Decisions waiting
- D14: should the design change before the freeze? Stage 3 changes nothing in it: the outside-finance C2.2 rows are still the only route under 5% inflation. Default: no change; S47 carries study N as preregistered.

## Next step
**S47**, the design freeze (Order table row 17). D14 has a default, so nothing blocks it. S47 carries from S54 (report section "What S47 carries"):
- stages 1-3 at 500 seeds;
- the full study's stage-3 confirmed points on S52's shock path;
- stage 3 at about 59 processor-hours for a front of this size (142 seconds per seed per environment on one process).

## Pitfalls
- Under the flat wage contribution, the 90% and 100% wage rows are byte-identical. Wages follow the general price level, which only new money moves, and a fully taxed payout makes none.
- The release-row points nearest to passing have the uncapped protected account (runaway inflation of 1,100-1,400% a year). Never present them as near-misses without that figure.
- A sparse, blob-less clone of compassionism-sim-results: `git sparse-checkout set <folders>` fetches just those blobs (stages 1-3 total 134 MB). `git ls-tree -l` fetches every blob, so use `--name-only`.
- Commit trailers must read `Co-Authored-By: Claude <noreply@anthropic.com>` only.
- The GitHub plugin server failed to connect this session; the built-in GitHub tools worked.
