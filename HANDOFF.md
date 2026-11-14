# Handoff (Nov 14, 2026): S74 part 1 (preregistered, history data built), alongside S64's running batch

## Step status
S74 is **partly done** (part 1 of about 3). Duke chose on Nov 14 to start S74 now, during S64's round-2 batch, instead of after release 2 (ledger D24, answered). Done: the preregistration (before any engine change or run), and the 2005-2025 history paths from opened sources. Still to do: the engine build (history environment `hx`, the policy-rate rule `cb` with purchases, refinancing, asset prices, job loss and forced sales), unit tests, the 100-seed pilot, the forward sweep and the report. S64 is still **partly done** (its batch is running; see In flight).

## What shipped
- research-update [PR 105](https://github.com/BetterToBest/research-update/pull/105), **open**: its `links` check is queued behind S64's batch, which holds all 20 runners. It holds PLAN.md (D24 answered, in the Order table and S74's section), `prereg/2026-11-s74-central-bank.md`, the rebuilt indexes and this handoff.
- compassionism-simulation [PR 109](https://github.com/BetterToBest/compassionism-simulation/pull/109), **open**: `checks` and `guard` are queued behind the batch. It holds `sources/s74_history.py` and `.json` (the rebuild check passes locally), raw files with SHA-256 hashes in `sources/s74_history/raw/`, and `dev/plans/s74-build-map.md` (where each part enters the engine). No engine file changed.
- PR 104 (S64 part 1) is already merged on main (`cded01f`).

## In flight
- S64's round-2 batch: unchanged from the S64 handoff. `run-study` on GitHub Actions in compassionism-sim-results, runs 101-124, engine `104691f`, folders `r2-<part>-<env>-<years>-104691f/`, each finished when it has `DONE`. Expected to finish about 08:00-09:00 UTC on Nov 15.

## Decisions waiting
- Nothing new. D24 is answered (Duke, Nov 14: start S74 now). It had never been written to the ledger; this session adds it as answered.

## Next step
- Once the batch's runners are free: merge PR 105 and PR 109 when their checks pass.
- **S74 part 2** (opus, xhigh): build `hx` and `cb` following `dev/plans/s74-build-map.md` and the prereg's "What is built" and "Unit tests" sections. Pilots run on the session machine while Actions is busy.
- **S64 part 2** (opus, high) as soon as all 24 folders have `DONE`, ahead of S74 if both can start: its order is in PLAN.md's S64 section and the previous handoff's list (merge, check `run.txt` against Amendment 2, shard counts, `SHA256SUMS`, finite values, reruns under `-r2`, tables tool, reports, round 1's backing curve).
- S75's descriptive panel (item 2, no engine) can also run beside S74.

## Pitfalls
- bls.gov refuses this machine (HTTP 403), so R-CPI-I is not opened. Stanford's copy of Taylor (1993) fails TLS, so the Fed's page (opened in S72) is the source for the rule. FRED has no `CUSR0000SAM`; medical care is `CPIMEDSL`. FRED can return HTML instead of csv, so check the header line.
- Shiller's Yale file ends Sep 2023, and the Wu-Xia file ends Feb 2022. Both are handled in `s74_history.py` and stated in its `_meta`.
- `index.html` has very long lines (line 476 is about 1 MB). Grep with `-o` and a bounded context, or use line ranges from `dev/CODEMAP.md`.
- The GitHub MCP plugin server failed to connect again, but the `mcp__github__*` tools loaded through ToolSearch worked.
- Remote branches `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell` and older session branches in research-update still need deleting by hand.
