# Handoff (Nov 8, 2026): S38 done, the community-layer report from the full batch

## Step status
S38 is **done**. The report reads studies G, G10, H, I and J (the community layer) against A, B and B10 (the same rows without it, and the no-programme rows), seeds 1-500, engine `ce8d030`. It covers both designs, three environments, 500 to 10,000 adults, 20 and 40 years. The headline is at 10,000 adults.

## What shipped
- compassionism-simulation [PR 80](https://github.com/BetterToBest/compassionism-simulation/pull/80) (analysis only): `dev/tools/s38_layer.py`, the report `dev/reports/s38-community-layer.md`, every table in `dev/runs/s38-layer/tables.md`, every estimate in `estimates.csv` (about 14,000), DECISIONS.md (S38).
- research-update: PLAN.md marks S38 done, with its findings in one paragraph.

## Findings (C2.2 design unless stated)
- The layer changes no result materially anywhere: 0 of 300 layer effects. Headline (Reference, 10,000 adults, 20 years): basic living +0.01, cost of living +0.03, wealth +0.15 points; inflation −0.16 points a year; cost +$209 per adult-year (0.3%). The effects are detectable (paired seeds), but tiny.
- One programme decision moves. C2.2's small unfavourable wealth effect in Reference at year 20 (−0.19 points) becomes indistinguishable from zero.
- No synergy with the layer. PTF × SZH is at most 0.50 points on any share. 6 of 990 contrast decisions cross the materiality line, all of them overlaps already at the threshold. S36's split stands.
- The design parameters (k, f, imitation, zones needing CIP) change only the direction of these tiny effects. Rule 3 asks that the headline name them, and the report does. The PTF's starting size changes nothing (rule 4: 0). No scale effect (0 of 720).
- Likely reason (not tested): with the layer, 81% of members get the food price cut, but only 11% live where θ applies, and members are a fifth of adults.

## Checks
All pass, in tables section 0:
- row counts per study;
- G10 and J share an identical release row;
- B10 equals A at 10,000 adults;
- the 40-year rows' first 20 years equal the 20-year rows;
- rows without the CCO are identical under both designs;
- communities = adults ÷ k on every seed;
- Shapley efficiency holds per seed.

## In flight
- Nothing. PR 80's checks (guard about 3 minutes) were still running when this was written; merge it once they are green if this session could not.

## Decisions waiting
- None.

## Next step
**S5** (participation threshold; sonnet, medium): next in the Order table. It reads studies D and D10 from the batch. S39 can also start. S7 waits on S5.

## Pitfalls
- The PTF diagnostics `pfMem` and `pfCut` are written only on rows with the layer. Layer-off rows have no comparison figure.
- In this batch, "detected" means almost nothing on its own: 500 paired seeds detect effects of 0.01 points. Read the materiality flags.
- Auto-merge is not enabled on compassionism-simulation. Wait for the checks, then merge.
- The GitHub plugin failed to connect again. The built-in GitHub tools worked.
