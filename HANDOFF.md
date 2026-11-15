# Handoff (Nov 15, 2026): S40 done (Hub figures generated from release 2); S65 part 2 done with it

## Step status
**S40 and S65 are done.** The generator, five generated blocks, and the Hub's inflation and wealth sentences on the pages named in the plan are in. What is *not* done is wider and belongs to S24 and S25: the other made-up results on the Hub (poverty, Gini, trade, IRR) that no run produced. They are marked in `data/claims.csv`.

## What shipped
- [research-hub PR 13](https://github.com/BetterToBest/research-hub/pull/13) (merged): `tools/build_figures.py` and `optimal-transfer-design.html`, generated.
- [research-hub PR 14](https://github.com/BetterToBest/research-hub/pull/14) (merged): the generator reads `data/releases/current.json`, and its blocks take the release label from the snapshot. The made-up inflation, wealth and Monte Carlo figures are withdrawn in dual-currency-inflation, cco-ptf-integrated-framework, economic-modeling-simulation (sections 5.1 and the inflation bullet; a notice over the rest), research-summary and the wiki FAQ and index. Four PDFs rebuilt. `python3 tools/build_figures.py --check` passes (5 blocks).
- [compassionism-simulation PR 121](https://github.com/BetterToBest/compassionism-simulation/pull/121) (merged): PTF is Public Trust Foundations.
- [compassionism-simulation PR 122](https://github.com/BetterToBest/compassionism-simulation/pull/122): the Nov 15 audit's wording fixes (financed results, 18-53 points at no backing, ratio 1.4-7.1, 25.9, 116 points, labour share cell, split pointer). **Merge it once its checks are green** (they take about 10 minutes; the three local checks passed).
- research-update: the audit is on main.

## In flight
- PR 122's checks.

## Decisions waiting
- None.

## Next step
1. **S24** (sonnet, medium): the corrections package is no longer held by S65 (D18). Start from the claims still marked "remove" or "correct" on economic-modeling-simulation (sections 6 to 11), cco-ptf-integrated-framework (5.4 on), public-trust-financial (IRR Monte Carlo) and basic-living-economic-index (v4.4 Gini). Then S41. S74 part 2 can run beside either.
2. Engine round 3: when it is released, run `build_figures.py --fetch <clone> --tag <tag> --label "Release 3"`, then the same pass over the Hub's inflation and wealth text; the blocks that name round 2's file columns need updating if the files differ.

## Pitfalls
- A mid-session claim check: I first wrote "the simulation does not model a traditional cash transfer" in a Hub edit with no basis and removed it. Edits that say what the simulation does not do need checking.
- `data/claims.csv` uses CRLF; keep it. Rows whose figure is still named in a withdrawal notice stay open (only 155 of the rows on the edited pages were marked `replaced`).
- Release 2's main rows use 500 adults per run. The two releases measure wealth differently; never set one's figure beside the other's.
- Local simulation checks need `npm install` first (jsdom).
- research-hub `.gitattributes` prints "text/xml is not a valid attribute name"; harmless. No CI in research-hub or the root site; the root site's index files carry none of the withdrawn figures.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
