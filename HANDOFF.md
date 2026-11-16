# Handoff (Nov 16, 2026): S24 partly done (corrections part 1 landed on the Hub)

## Step status
**S24 is partly done.** Landed: the summary and front page corrections C23-C30, the corrections log, two paper-body fixes, the root site's AI files, and all 18 PDFs rebuilt. **Remains** (below). The main package C01-C22 is not in any repository (D29 asks Duke to bring it; default: carry on without it).

## What shipped
- research-hub [PR 18](https://github.com/BetterToBest/research-hub/pull/18) (merged, 612f6ad): C23-C30 on `research-summary.html` and `index.html`; development paper's $1,847 corrected to the $2,046 its formula gives (illustrative); dual-currency "14% of GDP" corrected to about 11%; new `corrections.html`, linked from the seven corrected pages and `v1/README.md`; all 18 PDFs rebuilt (`tools/build_pdf.js`).
- bettertobest.github.io [PR 3](https://github.com/BetterToBest/bettertobest.github.io/pull/3) (merged, 6e3ab78): 33-month horizon labelled illustrative in the three JSON files (C28); S75 wording now "release design 120 of 120 cells, C2.2 107 of 120".
- Neither repository has checks, so both merged at once.

## Remains for S24 (a second session)
- Paper bodies: C23 (drug policy abstract, §1, §10, §9.1) and C26 (financing §2.2-2.3, 9.2), C24 and C27 in their papers, the BLEI worked examples.
- S29's other valid items: `audits/corrections-additions.md` (about 50 items; most need a decision on wording, a few need a source opened, e.g. Greenwald 2009 for B028).
- S30's provenance actions (`audits/early-figures.md`): not started.
- Regenerate `data/claims.csv` after the paper edits (`tools/class_claims.py`); not done.
- `v1/index.html` and its pages are frozen and not linked to the log; only `v1/README.md` is.
- Add every landed item to `corrections.html` (it lists C23-C30, the NPV, GDP share, S75 and S46 so far).

## In flight
- None. Every S77 PR is merged (compassionism-simulation 132 and 133, compassionism-sim-results 48 and 49, research-hub 17, research-update 133).

## Decisions waiting
- D29: the corrections package C01-C22 (and its handoff) is not in the repositories; please place `corrections-package.md` in `audits/`. Default: S24 goes on without it.

## Next step
S24 again (sonnet, medium): the remaining items above.

## Pitfalls
- The Hub clone is shallow; fetch before branching if PR 17 has merged.
- `/v1/` pages stay frozen; link the log only from its README.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
