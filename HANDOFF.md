# Handoff (Nov 16, 2026): S41, site and wiki design refresh

## Step status
**S41 is done.** One shared stylesheet, header and footer now serve the Hub front page, the papers index and the five wiki pages. The 20 paper pages still use the old `styles.css` (not in the step); `/v1/` is untouched.

## What shipped
- research-hub [PR 30](https://github.com/BetterToBest/research-hub/pull/30) (merged, ced5cdf; the repository has no checks).
  - `assets/site.css`, `assets/site.js`: light and dark (system setting plus a header button), mobile menu, focus rings, wiki header search kept and now shown on phones.
  - `tools/apply_site_shell.py` (`--check` passes) owns the header, footer and head links in the seven pages; edit its template, never the blocks.
  - Front page order: what Compassionism is, findings (the generated `r2-inflation` block; `build_figures.py --check` passes), papers, key concepts, tools (Simulation, CIP portal, X-Cents, NEEC), documentation, authors, how to help.
  - axe-core (WCAG A/AA plus best practice), seven pages, light and dark, 1280 and 390 wide: no serious or critical findings, no horizontal scroll.
  - Screenshots (light, dark, mobile) in `docs/s41-screenshots/`.
- Prose changes, all navigation or link blurbs: front page heading "About The Research Initiative" is now "What Compassionism Is"; one intro line above the findings block; card blurbs copied from the portal, X-Cents and NEEC pages' own descriptions; emoji dropped from the two wiki guide titles.

## In flight
Nothing.

## Decisions waiting
None.

## Next step
S4 (X-cents folded into the CCO architecture, sonnet, medium; first in the Order table), then S43 (links and publications, sonnet, medium; D3 was answered Nov 1). The front page already links the portal, X-Cents, NEEC and the Simulation; S43 adds the publications page and the wiki links. Then S42, S44 (S44 also needs S65, done).

## Pitfalls
- Clone research-hub one at a time (proxy cap); it is shallow.
- Pages in scope now load `assets/site.css`; do not add inline header or footer markup, run `python3 tools/apply_site_shell.py` instead. A new page needs an entry in that script's PAGES table and the three SHELL marker blocks.
- The Hub front page's figures block is owned by `tools/build_figures.py`.
- The GitHub plugin server failed to connect again; `mcp__github__*` tools worked (load them with ToolSearch).
- The Draft Act's yearly adjustment rule is not written into the Act; check the simulation's rule before stating it.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
