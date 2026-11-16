# Handoff (Nov 16, 2026): S75 done (part 3, the Hub page for US policy eras)

## Step status
**S75 is done.** Parts 1 (the descriptive panel) and 2 (the engine readings) were done earlier today; part 3, the Hub page, is done and live.

## What shipped
- [research-hub PR 15](https://github.com/BetterToBest/research-hub/pull/15) (merged, 390ab06): `us-policy-eras.html`, "US Policy Eras and Stability, 1947-2025" (the name chosen as Duke asked). Short answer, four headline figures, nine charts each with a table view and a basis line, limits, Duke's note as the design's aim, sources and results folders. Data: `tools/build_s75_eras.py` reads the simulation's `sources/s75_eras.json`, `sources/s75_hx.json` and `dev/runs/s75-eras/tables.json` into `data/s75-us-eras.json` and the page. Linked from the wiki (a card beside the simulation card) and the simulation paper (section 5 notice).
- [bettertobest.github.io PR 2](https://github.com/BetterToBest/bettertobest.github.io/pull/2) (merged, d2fc502): ai-index.json, research-index.json (23 items), llms.txt and sitemap.xml list the page.
- research-update: PLAN.md (S75 part 3 note; new step S76), this handoff.

## Checks
- Every figure on the page cross-checked against `dev/reports/s75-deep-history.md` and the panel note (8/6/1 verdicts, basket poverty effects, the 111/3/6 and 115/5 tallies, tax rates, the rule's fits).
- Rendered with Playwright at 1200px (light and dark) and 390px: no console errors, no horizontal scroll, labels clear. The four-colour palette passes the colour-blindness validator in both modes (light-mode contrast relief: direct labels and table views).
- Neither repository has CI checks; both PRs merged on creation.

## In flight
- Nothing.

## Decisions waiting
- None.

## Next step
1. **S76** (opus, high): show S74 on the simulation's main page and link the new S75 page from it (Duke, Nov 16). Also correct `index.html` about line 391, which still says "there is no central bank". Attach compassionism-simulation (push).
2. S24 (sonnet, medium) can run beside it.

## Pitfalls
- The Hub's small-multiple grids must create all cells before measuring them, or the first panels are drawn at full width and shrink (fixed in the page).
- github.com page links return 403 from this machine (proxy); check that results folders exist with a blob-less clone of compassionism-sim-results instead.
- Hub rules: no model names in commits or pushed files (Co-Authored-By: Claude). Hub has no workflows, so "checks pass" is vacuous there; render the page before merging.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
