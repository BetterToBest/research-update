# Handoff (Nov 15, 2026): S40 part 1 done (Hub figure generator)

## Step status
**S40 is partly done.** The generator exists and one page uses it. **Remaining (part 2, also S65 part 2):** the Hub's inflation and wealth sentences on the other pages, written from the release. Most are `data/claims.csv` rows marked "remove" or "correct", so this overlaps the corrections package (S24): dual-currency-inflation, cco-ptf-integrated-framework, economic-modeling-simulation, research-summary, new-frame-and-lens, drug-policy-reform and others. These pages carry made-up Monte Carlo results (for example "$82,000 median wealth", "inflation 0.95% a year"). They need removing or relabelling, not a swap of numbers. Block `r2-inflation` is written in the script but sits on no page yet.

## What shipped
- [research-hub PR 13](https://github.com/BetterToBest/research-hub/pull/13): merged (9d663ea). `tools/build_figures.py` (`--fetch`, write, `--check`), snapshot `data/releases/v5.8.0-r2.json` (tag v5.8.0, hashes of `r2-effects` and `r2-backing`), `optimal-transfer-design.html` now generated with release labels and the full-backing statement, its PDF rebuilt, 16 claims rows marked `replaced`. The release-1 wealth passage is gone; the page says release 2 supersedes it.
- [compassionism-simulation PR 121](https://github.com/BetterToBest/compassionism-simulation/pull/121): PTF expanded correctly ("Public Trust Foundation") in `site/notes.js`. **Open: `checks` was still running at session end.** Merge it once green.
- The Nov 15 release-figures audit (`audits/2026-11-15-release-figures-audit.md`) was only on an unmerged branch; it is now in this branch.

## In flight
- Nothing running except PR 121's checks.

## Decisions waiting
- None.

## Next step
1. Merge simulation PR 121 if its checks are green.
2. **S40 part 2** (sonnet, high): use the audit's wording. Take numbers from `r2-*.json`, never from report prose. Fix the audit's five sentences too, in compassionism-simulation: "every financed result is fragile" (live on `site/round2.js` lines 183 and 192; two curves are robust) and the labour-force pointer in the "Who gains" paragraph. S74 part 2 can run beside it.

## Pitfalls
- The audit was never merged to main. Check unmerged branches when a named file is missing.
- `data/claims.csv` uses CRLF line endings; a Python rewrite changed all 6,600 lines until I restored them.
- Release 2's main rows use 500 adults per run (not 10,000); the 10,000-adult pair is a side check.
- The two releases measure wealth differently; never print one release's figure beside the other's.
- Local simulation check scripts need `npm install`; I relied on CI for PR 121.
- research-hub's `.gitattributes` prints "text/xml is not a valid attribute name"; harmless. Research-hub has no CI.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
