# Handoff (Nov 16, 2026): S75 part 2 done (the engine readings of US policy eras)

## Step status
**S75 is partly done.** Parts 1 (the descriptive panel) and 2 (the engine readings) are done. Still to do: part 3, a separate Hub page for the findings (Duke's instruction, Nov 16: Claude names the page; it is linked from the simulation and wiki pages once complete).

## What shipped
- research-update: prereg `prereg/2026-11-s75-deep-history.md` Amendment 4 (the build's mechanics, committed before any study run); PLAN.md S75 part 2 note.
- [compassionism-simulation PR 129](https://github.com/BetterToBest/compassionism-simulation/pull/129) (merged, 87e9769; commits 77a85d6, 71e1ee9, 3d0051c; the study ran at 77a85d6): options `hx.era` (four eras' yearly paths, `HXE`, from `sources/s75_hx.py`), `hx.T` (the era's PSZ tax schedule on earnings and Social Security, revenue-neutral), `hx.H` (the era's real medical price growth); the era's fitted rule passed to `cb`. Off identical (guard, lineage proved); unit 384 of 384 (7 new). Report `dev/reports/s75-deep-history.md` (both parts); tables `dev/runs/s75-eras/tables.md`.
- [compassionism-sim-results PR 46](https://github.com/BetterToBest/compassionism-sim-results/pull/46) (merged, 8a625d1): `s75-eras-77a85d6` (100 seeds, four eras, seven arms, both designs; run.txt, SHA256SUMS).

## Findings (plain words; the report has every cell)
- Without the programme, today's households are not steadier in every way under an earlier era's settings. Under each era's own path, against 2008-2025: the earlier eras give smaller falls in real wealth and smaller yearly income swings, but larger swings in the basket's price (1947-1972, 1973-1983), slower recovery from income shocks (1947-1972, 1984-2007) and more people pushed below the basket line in recession years (1973-1983, 1984-2007). 8 of 15 cells steadier, 6 less steady, 1 no clear difference: mixed.
- Basket poverty without the programme is higher under every earlier era's path (47-58% of person-years against 44% in 2008-2025): a property of the model's paths, not a measure of life then.
- Inside the model: the central bank's rule moves the largest wealth falls most; the era's tax schedule barely moves stability and lowers basket poverty 0.1-0.4 points; the era's health cost growth raises it 0.1-1.1 points; nothing moves the basket's price swings (no channel).
- Today's rule put into 1947 tightens 28 points against the pegged rates, which the engine's stance slopes turn into a $261,000 larger wealth fall: reported as a limit of the model.
- The programme's effect keeps S74's direction in 226 of 240 cells (both designs, every era and arm); 8 cells show no measurable difference; the 6 reversals (C2.2's price swings in 2008-2025) are favourable. Both designs cut basket poverty in every era (C2.2 by 41-52 points, the release design 23-32).

## In flight
- Nothing.

## Decisions waiting
- None.

## Next step
1. **S75 part 3** (opus, high): the Hub page. Attach research-hub and bettertobest.github.io (ai-index.json, research-index.json, llms.txt kept in step). Sources: `dev/reports/s75-deep-history.md`, `dev/reports/s75-panel.md`, the two tables files. Carry the limits (arm T taxes work and pensions only; the stance slopes' reach; no war, military spending or corruption in the model) and Duke's note as the design's aim, in his words (PLAN.md S75). Link it from the simulation and wiki pages. S24 (sonnet, medium) can run beside it.

## Pitfalls
- Arm T first charged the capital income wealth pays: unweighted, the weighted tail's 18 adults set a mean charge near $350,000 per adult-year. It now charges earnings and Social Security only (Amendment 4, item 4); say so wherever arm T is read.
- Era runs shorter than 20 years write 0 for keys past the run, so r2PairCheck's own-effects test says "the share fell" spuriously; check with the 27-year era.
- The unit test counting reads of `a._ret` must be raised when a new read is added (now 45).
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
