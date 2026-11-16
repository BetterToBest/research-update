# Handoff (Nov 16, 2026): S4 revised (X-Cents in the AI section; Findings section removed)

## Step status
**S4 is done** in the Hub. The x-cents site's own link back to the Hub (x-cents ledger S7) is not done; see Decisions waiting.

## What shipped
- research-hub [PR 32](https://github.com/BetterToBest/research-hub/pull/32) (merged, bd557d2): X-Cents glossary entry, quick-reference link, wiki search entry (the front-page article from this PR was removed again in PR 33).
- research-hub [PR 33](https://github.com/BetterToBest/research-hub/pull/33) (merged, 2d9d39d; no CI; `apply_site_shell.py --check` and `build_figures.py --check` pass), Duke's revision:
  - Front page: X-Cents article gone, X-Cents card in Tools kept. X-Cents is now a system definition in the "For AI systems" section (currency assurance system, low-tech, CIP as proposed steward, proposal not simulated). Its summary line now reads v2.4 to match the ontology version below it, which already said 2.4 (updated 2026-11-16).
  - Findings section, nav link and hero button removed (nav entry removed in `tools/apply_site_shell.py`, so all seven pages lost it). The Wiki & Documentation list's Simulation link now goes to the Simulation Findings page. `build_figures.py` now finds 5 blocks (none on the front page).

## In flight
Nothing.

## Decisions waiting
None. S43 is blocked by Duke in the ledger. Not done: `ai-index.json`, `research-index.json` and `llms.txt` (bettertobest.github.io) do not yet list X-Cents in the ontology; S42 owns that (it needs ontology v2.4 and the x-cents definition). The x-cents site's link back to the Hub is also not done (CLAUDE.md: linked, not edited).

## Next step
S11 (BLEI visuals, sonnet, medium; S7 is done). S43 is skipped (blocked). Then S42 (waits on S43 in the plan; ask Duke), S44.

## Pitfalls
- The page JSON-LD blocks still carry Duke's personal email (front page, wiki index); S42 generates them from the manifest, so change it there.
- OEIAS is not yet in the machine-readable files' front-page JSON-LD or the sitemap (S42 owns those).
- Clone research-hub one at a time (proxy cap); it is shallow.
- Pages in scope now load `assets/site.css`; do not add inline header or footer markup, run `python3 tools/apply_site_shell.py` instead. A new page needs an entry in that script's PAGES table and the three SHELL marker blocks.
- The Hub front page's figures block is owned by `tools/build_figures.py`.
- The GitHub plugin server failed to connect again; `mcp__github__*` tools worked (load them with ToolSearch).
- The Draft Act's yearly adjustment rule is not written into the Act; check the simulation's rule before stating it.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
