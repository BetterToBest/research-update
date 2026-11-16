# Handoff (Nov 16, 2026): S24 part 5 (BLEI sensitivity, claims.csv)

## Step status
**S24 is partly done.** Landed: C23-C30, C01-C22, the four held items, the paper bodies for C23, C24, C26, C27, the BLEI sensitivity recompute and claims.csv. **Remains** below.

## What shipped
- research-hub [PR 22](https://github.com/BetterToBest/research-hub/pull/22) (merged, cfd21df): BLEI Table 2 Month 0 column recomputed from 70.7 (`tools/blei_month0_sensitivity.py`); r_a and h_AE have no Month 0 effect (AE = 0); one prose 71.3 fixed; PDF rebuilt. Month 12 column not recomputed (needs the unstated cash-saving rate).
- research-hub [PR 23](https://github.com/BetterToBest/research-hub/pull/23) (merged, 2aee8cc): `data/claims.csv` and summary regenerated: 10,928 figures, 2,873 no basis found.
- research-hub [PR 21](https://github.com/BetterToBest/research-hub/pull/21) (merged, 17c8c10; the repository has no checks):
  - Drug policy: $1.5T and $847B retired in the metadata, JSON-LD, abstract, sections 1, 4.1, 10 and the conclusions; the paper's own totals ($4,616B; $3,870B and $5,044B) are used and labelled unsourced.
  - Real estate: penetration claim replaced by the 200,000-400,000 household rollout; $70,000 labelled a 20-year projection; the 40-60 threshold labelled an assumed break-even.
  - PTH financing: $85,000, $68,000, 1.8-year and 10-year claims marked unsupported, with a correction note under section 2.3 (about 18.3 years, about $900 saved at the example's own payments). Homeowner C's years corrected to 19.3, average to 18.5 (the package said 18.4; the table's own numbers give 18.46).
  - BLEI: entry 70.7 days; month 33 qualified by the saving assumption; note that Appendix B.3's EDC 0.744 would give EPPM about 8.5x.
  - corrections.html updated; corrections link added to three papers; four PDFs rebuilt.
- Ledger written (log only).

## Remains for S24
- BLEI: Month 12 column of Table 2 and the month 60 figure.
- PTH financing's second example (section 8: $92,000, 10 years) is only labelled unverified.
- S29's items (`audits/corrections-additions.md`, 30 headline items first); S30's actions (`audits/early-figures.md`); rebuild PDFs and rerun `tools/class_claims.py` afterwards. Simulation figures wait for S65 (D18).
- The real estate pay-in $168,000 vs $70,000 reconciliation and the Draft Act section 102 items (child allowance, D8) are untouched.

## Decisions waiting
None.

## Next step
S24 again (sonnet, medium): apply the S29/S30 items.

## Pitfalls
- Clone research-hub and the root site one at a time (proxy cap); both are shallow.
- `/v1/` stays frozen.
- The GitHub plugin server failed to connect; the `mcp__github__*` tools worked.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
