# Handoff (Nov 16, 2026): S41 follow-ups after Duke's review of the front page and wiki

## Step status
**S41 is done.** One shared stylesheet, header and footer now serve the Hub front page, the papers index and the five wiki pages. The 20 paper pages still use the old `styles.css` (not in the step); `/v1/` is untouched.
Duke's review notes (below) are done in research-hub PR 31 and compassionism-simulation PR 134.

## What shipped
- research-hub [PR 30](https://github.com/BetterToBest/research-hub/pull/30) (merged, ced5cdf; the repository has no checks).
  - `assets/site.css`, `assets/site.js`: light and dark (system setting plus a header button), mobile menu, focus rings, wiki header search kept and now shown on phones.
  - `tools/apply_site_shell.py` (`--check` passes) owns the header, footer and head links in the seven pages; edit its template, never the blocks.
  - Front page order: what Compassionism is, findings (the generated `r2-inflation` block; `build_figures.py --check` passes), papers, key concepts, tools (Simulation, CIP portal, X-Cents, NEEC), documentation, authors, how to help.
  - axe-core (WCAG A/AA plus best practice), seven pages, light and dark, 1280 and 390 wide: no serious or critical findings, no horizontal scroll.
  - Screenshots (light, dark, mobile) in `docs/s41-screenshots/`.
- Prose changes, all navigation or link blurbs: front page heading "About The Research Initiative" is now "What Compassionism Is"; one intro line above the findings block; card blurbs copied from the portal, X-Cents and NEEC pages' own descriptions; emoji dropped from the two wiki guide titles.

- Follow-ups, research-hub [PR 31](https://github.com/BetterToBest/research-hub/pull/31) (merged, 0b9f5a1):
  - The Economic System Comparison section is gone (NEEC has its Tools card; the Medium article link went with it).
  - Each of the five architecture cards jumps to its own concept. Findings now follows Key Concepts; nav, hero buttons and page order agree (Papers, Findings, Tools, Wiki, Get involved). Duke was unsure it belonged: kept, one block, easy to drop.
  - Findings block read from v5.9.1 (Release 2's data files are byte-identical to v5.8.0's, same SHA-256), so the label changed and no figure did. The four papers carrying the block have rebuilt PDFs.
  - Space beneath each front-page section is about half (124 px to about 60 px).
  - OEIAS added: front page, Architectural Index, wiki index and FAQ, glossary usage note. It supplements Compassionism and CCO-PTF-PTH-CIP-SZH (NEEC: old label for the earlier simulation, OEIAS for the latest).
  - Wiki banner: November 2026, Simulation Apache 2.0. The shared footer (all seven pages) says the same and now gives BetterToBestResearch@gmail.com instead of Duke's address.
- compassionism-simulation [PR 134](https://github.com/BetterToBest/compassionism-simulation/pull/134): OEIAS in the simulation, findings and replication glossaries (pages only; no version bump). Open: checks (including the 3-minute guard test) were still running; I will merge it when they pass. If it is still open, merge it once checks are green.

## In flight
Nothing.

## Decisions waiting
None.

## Next step
S4 (X-cents folded into the CCO architecture, sonnet, medium; first in the Order table), then S43 (links and publications, sonnet, medium; D3 was answered Nov 1). The front page already links the portal, X-Cents, NEEC and the Simulation; S43 adds the publications page and the wiki links. Then S42, S44 (S44 also needs S65, done).

## Pitfalls
- The page JSON-LD blocks still carry Duke's personal email (front page, wiki index); S42 generates them from the manifest, so change it there.
- OEIAS is not yet in the machine-readable files' front-page JSON-LD or the sitemap (S42 owns those).
- Clone research-hub one at a time (proxy cap); it is shallow.
- Pages in scope now load `assets/site.css`; do not add inline header or footer markup, run `python3 tools/apply_site_shell.py` instead. A new page needs an entry in that script's PAGES table and the three SHELL marker blocks.
- The Hub front page's figures block is owned by `tools/build_figures.py`.
- The GitHub plugin server failed to connect again; `mcp__github__*` tools worked (load them with ToolSearch).
- The Draft Act's yearly adjustment rule is not written into the Act; check the simulation's rule before stating it.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
