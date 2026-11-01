# Handoff (Nov 1, 2026): S50 second independent implementation, part 1 (the packet) done

## Step status
S50 is **partly done**. Part 1 is done: the spec now describes the published release row, and the packet for the second program is built and checked. Part 2 (the program itself) remains, for a fresh session that has not read the engine. This session read the engine, so it could not write an independent program.

## What shipped
- compassionism-simulation [#60](https://github.com/BetterToBest/compassionism-simulation/pull/60), merged `MERGE_SHA`. No engine change (`index.html` and `harness.js` unchanged since 168d287).
  - `MODEL_SPEC.md` describes the v5.6 release row. Section 12 covers job loss and re-employment, PTH's books, PTF by sector, today's safety net with SNAP's work rule, and the flat contribution (audit finding E2). Section 4.1 gives the samplers exactly as drawn. Appendix A closes the 31 gaps S10 found; Appendix B describes the validation path.
  - `dev/packets/s50-release-row.zip` (6.6 MB) holds the spec, every switch in effect as data, the code the six runs execute (V8 coverage: folded and whole, about 3,600 lines), and the engine's per-seed outputs for seeds 1-500 (631 keys) in Reference, Adverse and Stress. It is built by `make_s50_reference.js` and `build_s50_packet.py`; the brief is `dev/packets/s50-brief.md`.
- research-update: this handoff and PLAN.md's S50 section (the part-2 rules).

## Checks
- The 500-seed reference equals the published v5.6 panel (`data/releases/v5.6.json`) to its rounding on every headline key, for both runs in all three environments.
- A second Stress run gave identical outputs. The PR's CI is green.

## In flight
Nothing.

## Decisions waiting
None new.

## Next step
**S50, part 2** (opus, xhigh). Start it in a fresh session. It attaches compassionism-simulation, unzips the packet outside the repository and follows `00-START-HERE.md`. It must not open `index.html`, `harness.js`, `earlier-engine.html`, `dev/` (other than the packet and `dev/reports/s50-independent-implementation/`) or the results repository until its phase-1 program and results are pushed. Phase 2 (explaining the differences) may follow in the same session or the next. Then S47.

## Pitfalls
- In the packet, the "dirty" flag on Stress means a doc file was being edited while it ran; the engine hashes are asserted equal across all files. Run reference jobs from a tree you are not editing.
- Two quirks of the packet:
  - In `release-config.json`, the entries `S3_CACHE`, `HL_GOVREF`, `HHS` and `TB_BLEI_NET` are run state, not settings.
  - Keys `_20` to `_39` are 0 in 20-year runs.
- The release row's Stress no-programme run is the same economy as Adverse's (identical figures); that is by design, not a bug.
- `check_stale_claims.js` and domtest need `npm install` first (jsdom).
- `gh` has no valid token here; the GitHub tools work for pull requests.
