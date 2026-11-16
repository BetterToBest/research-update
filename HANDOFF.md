# Handoff (Nov 16, 2026): S24 part 2 (corrections C01-C22 landed)

## Step status
**S24 is partly done.** Landed: C23-C30 (part 1) and now C01-C22 except four held items. **Remains** below.

## What shipped
- research-hub [PR 19](https://github.com/BetterToBest/research-hub/pull/19) (merged, dc5f60e): C01-C07, C10, C12, C14-C22 on `index.html`, `research-summary.html`, `research-summary.md`; log entries in `corrections.html`; ontology version 2.4 (2026-11-16) on both pages.
- bettertobest.github.io [PR 4](https://github.com/BetterToBest/bettertobest.github.io/pull/4) (merged, 778396b): the same items in `ai-index.json`, `ai-manifest.json`, `research-index.json`, `llms.txt`; simulation version fields set to 5.9.1, changelogs replaced by links. All JSON and JSON-LD parse.
- `audits/corrections-package.md`: the package (D29 answered). Its script and `corrections/` files were not supplied; I applied its before/after table with a throwaway script (every "Now" text matched exactly once).
- Neither repository has checks.

## Remains for S24
- Held: C08 (θ gate), C09 (γ ramp), C11 (EDC profile, 0.625), C13 ($2.75 per food BU). They describe the engine at v4.21; check each against the current engine (v5.9.x, `dev/CODEMAP.md`) and land the true wording. Also the C17 `features` list in the AI files (still v3.x wording).
- C17's version fields use 5.9.1, not the package's 4.21.
- Paper bodies: C23, C26, C24, C27, BLEI worked examples; S29's items (`audits/corrections-additions.md`); S30's actions; regenerate `data/claims.csv` (`tools/class_claims.py`).
- The package's ledger CSVs (claims ledger) were offered by Duke; not needed yet.
- Papers' PDFs were not rebuilt this part (no paper changed).

## Decisions waiting
- New: the four held items (default: check against the current engine, then land). Queued in `ledger-sync/2026-11-16-S24b.json`; the ledger was not written this session.

## Next step
S24 again (sonnet, medium): the remains above.

## Pitfalls
- Clone research-hub and the root site one at a time (proxy cap); both are shallow.
- `/v1/` stays frozen.
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
