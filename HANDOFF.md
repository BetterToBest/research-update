# Handoff (Nov 16, 2026): S4 X-cents folded into the CCO architecture

## Step status
**S4 is done** in the Hub. The x-cents site's own link back to the Hub (x-cents ledger S7) is not done; see Decisions waiting.

## What shipped
- research-hub [PR 32](https://github.com/BetterToBest/research-hub/pull/32) (merged, bd557d2; the repository has no checks; `apply_site_shell.py --check` and `build_figures.py --check` pass).
  - Front page, Key Concepts: a new X-Cents article after CCO. It says what Duke asked: X-Cents was designed as a currency assurance system for places where the monetary system has failed and the government will not introduce CCO or a similar reform; it is low-tech (cash and coins) and can be supported by high-tech systems such as CIP. Checked against the x-cents page (the #portal section's caveat is kept: CIP integrations are proposals, still to be specified and piloted).
  - Glossary entry and quick-reference link; wiki search entry.
  - Labelled a proposal; the Simulation does not model it, so no figure is claimed (basis class: none needed).

## In flight
Nothing.

## Decisions waiting
None. Small follow-up, no decision needed: x-cents is "linked, not edited" in CLAUDE.md, so I did not edit it. A one-line link from its page to `research-hub/wiki/glossary.html#x-cents` (x-cents ledger S7) needs Duke's go-ahead or a plan line that names the x-cents repository.

## Next step
S43 (links and publications, sonnet, medium; D3 answered Nov 1): the publications page and wiki links. Then S42 (add the new glossary entry to the manifest), S44.

## Pitfalls
- The page JSON-LD blocks still carry Duke's personal email (front page, wiki index); S42 generates them from the manifest, so change it there.
- OEIAS is not yet in the machine-readable files' front-page JSON-LD or the sitemap (S42 owns those).
- Clone research-hub one at a time (proxy cap); it is shallow.
- Pages in scope now load `assets/site.css`; do not add inline header or footer markup, run `python3 tools/apply_site_shell.py` instead. A new page needs an entry in that script's PAGES table and the three SHELL marker blocks.
- The Hub front page's figures block is owned by `tools/build_figures.py`.
- The GitHub plugin server failed to connect again; `mcp__github__*` tools worked (load them with ToolSearch).
- The Draft Act's yearly adjustment rule is not written into the Act; check the simulation's rule before stating it.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
