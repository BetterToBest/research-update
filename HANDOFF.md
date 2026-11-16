# Handoff (Nov 16, 2026): S24 part 6 (S29 headline items)

## Step status
**S24 is partly done.** Parts 1-6 landed. **Remains** below.

## What shipped
- research-hub [PR 24](https://github.com/BetterToBest/research-hub/pull/24) (merged, e129ab6; the repository has no checks): of the 30 S29 headline items, 14 were already handled by earlier parts and S46 (A01, B001, B003, B005, B009, B016, B018, B033, B053, B061, B097, B098, B103, B127; B066 by C24). The rest are now labelled, qualified or withdrawn: B004, B026, B028, B036, B044, B048, B052/B096, B058, B062, B071, B075, B084, B093 (parameter file notes). Corrections log entry added; five PDFs rebuilt; `tools/class_claims.py` rerun (10,983 figures, 2,926 no basis; the rise is the new notes' own figures).
- Ledger written (log only).

## Remains for S24
- B022 (cco-ptf 5.4 "proves optimal": only the octave-doubling sentence at line 349 matches; check and restate) and B028 (Portugal: source Greenwald 2009 could not be opened, cato.org returned 403; try another copy, then restore the correct figures).
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
