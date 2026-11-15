# Handoff (Nov 15, 2026): S65 part 1 done (release v5.8.0)

## Step status
**S65 is partly done.** Release 2 is published as v5.8.0 (tag, release notes, reproduce zip); the findings page has its Release 2 section beside release 1. **Remaining (part 2):** the Hub's inflation and wealth sentences, to what round 2 shows. They sit in about ten Hub pages (new-frame-and-lens, economic-modeling-simulation, research-summary, cco-ptf-integrated-framework, dual-currency-inflation and others). They overlap S24 (corrections) and S40 (generated figures), so part 2 is best done as the first move of S40, which needs `data/studies/r2-effects.json` and the manifest's `round2` entry. S40's generator does not exist yet in research-hub.

## What shipped
- [compassionism-simulation PR 120](https://github.com/BetterToBest/compassionism-simulation/pull/120): merged, checks and guard green, tag `v5.8.0`. New: `site/round2.js`, six `data/studies/r2-*.json` files with `dev/tools/r2_study_files.py --check`, 24 charts in `data/studies/r2-charts/`, `dev/tools/check_round2.js` (every printed number tied to its file row; run it after any change to the section).
- Engine and release 1's figures unchanged (guard green). Version 5.8.0 changes only labels in `index.html`.

## In flight
- Nothing.

## Decisions waiting
- None open.

## Next step
1. **S40** (sonnet, high): research-hub's `tools/build_figures.py` reading `r2-effects` by tag v5.8.0; do S65 part 2's Hub sentences with it. 2. **S74 part 2** (opus, xhigh, engine build) can run beside it. S4 (X-cents) follows.

## Pitfalls
- **Read `audits/2026-11-15-release-figures-audit.md` before S40.** Release 2's numbers reproduce from the raw results, but five sentences in the S64 reports and on the findings page overstate the data ("every financed result is fragile": two financed curves are robust; "15 to 53 points a year without backing": 18.2 to 53.3 at no backing). Take Hub numbers from the `r2-*.json` files, not the report prose.
- S64's page text said inflation at the model's own mechanism is "15 to 53 points a year"; the data's range is 14.9 to 53.3 over both mechanism readings (with and without the ceiling). The page prints the data's figures.
- `check_figures.js` now lets a superseded "latest" release take the figures of a "current" one; if a later release adds its own figures, re-read that rule.
- The data file's erosion share is already in percent; the mechanism's backed share was in percent in the summary and is a fraction in `r2-backing`.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`; compassionism-simulation `claude/s7-part2-saving-groups` if it still exists.
- research-hub's `.gitattributes` prints "text/xml is not a valid attribute name" on every git command; harmless. Research-hub and the root site have no CI.
