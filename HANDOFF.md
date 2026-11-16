# Handoff (Nov 16, 2026): S24 part 8 (B028 closed)

## Step status
**S24 is partly done.** Parts 1-8 landed. **Remains** below.

## What shipped
- research-hub [PR 24](https://github.com/BetterToBest/research-hub/pull/24) (merged, e129ab6; the repository has no checks): of the 30 S29 headline items, 14 were already handled by earlier parts and S46 (A01, B001, B003, B005, B009, B016, B018, B033, B053, B061, B097, B098, B103, B127; B066 by C24). The rest are now labelled, qualified or withdrawn: B004, B026, B028, B036, B044, B048, B052/B096, B058, B062, B071, B075, B084, B093 (parameter file notes). Corrections log entry added; five PDFs rebuilt; `tools/class_claims.py` rerun (10,983 figures, 2,926 no basis; the rise is the new notes' own figures).
- Ledger written (log only).

## Part 7 (this session)
- research-hub [PR 25](https://github.com/BetterToBest/research-hub/pull/25) (merged, b83f0c2; no checks): B022 restated (cco-ptf 5.4 is now design choices); B028: Portugal table and timeline marked unverified. Greenwald (2009) still could not be opened (Cato bot block, web.archive.org blocked by the proxy, SSRN/ResearchGate 403), so no figures restored. Two PDFs rebuilt, class_claims rerun (11,003 figures, 2,932 no basis), corrections log entry added.

- Part 8: research-hub [PR 26](https://github.com/BetterToBest/research-hub/pull/26) (merged). Duke supplied Greenwald (2009); it contains none of the page's Portugal figures (nor the audit's 131 to 20). The page now states only the source's: opiate deaths -53% (281 to 133, 2000-06), all drug deaths -27%, HIV notifications -17%, substitution treatment +147%, youth lifetime use 27.6% to 21.6%. B028 closed. Still unsourced: appendix A's Portugal rates (2.6 and 1.2 per 100,000) and timeline entries from 2015.

## Remains for S24
- The 23 derivation and table items in `audits/corrections-additions.md` (A04, A06, B002, B007 ... B108) are untouched; S46 may have covered A04, A06, B013, B019, B035, B067, B070 (check the pages first).
- S30's actions (`audits/early-figures.md`), the BLEI Month 12 column and month 60, PTH financing section 8, real estate $168,000 vs $70,000, Draft Act section 102 (D8).
- After any edit rebuild the PDFs and rerun `tools/class_claims.py`. Simulation figures wait for S65 (D18).

## Decisions waiting
None.

## Next step
S24 again (sonnet, medium): the derivation items, then S30's actions.

## Pitfalls
- Clone research-hub one at a time (proxy cap); it is shallow.
- `/v1/` stays frozen.
- The GitHub plugin server failed to connect; the `mcp__github__*` tools worked.
- Many S29 "live" rows were stale (fixed by earlier parts); grep the page before editing.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
