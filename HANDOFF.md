# Handoff (Nov 16, 2026): S11 (BLEI visuals), checked and re-planned; no build yet

## Step status
**S11 partly done; nothing in the engine, results or suite changed.** Checked what exists: job X (`x-ce8d030`, engine ce8d030) has every series I1 asks for but is not release 2. Release 2's stored shards (`r2-*-104691f`, parts b, f, m, s, three environments, 20 and 40 years, 500 seeds) hold yearly poverty and median wealth, but BLEI poverty only as end totals: no tier shares, no median BLEI or its three parts, no share taking part by year. `explore_export.js` has no mode for release 2's main row (`r2FreezePair`).
Duke chose a **new run of release 2's main row on GitHub Actions (free)** to get the full series on the current engine (D30). The plan's S11 section now lists the four sub-steps; they need about two sessions, so S11 moved to opus, high.

## What shipped
This handoff and the PLAN.md edit (PR in this repository). No other repository changed.

## In flight
Nothing running. Shallow clones of compassionism-simulation and a sparse compassionism-sim-results sit in the session machine only.

## Decisions waiting
- D30: answered by Duke (new run, release 2 main row, Actions). Nothing else waiting.

## Next step
S11 again: sub-steps 1-3 (an `--r2` mode in `dev/tools/explore_export.js`, a short prereg addendum, a runner job and a workflow run on the pinned commit; folder `x2-<commit 7>`). Start the run, record where it lands, end. A later session does sub-step 4 (rebuild `suite.html` as a new release data folder; v5.6's files stay untouched). S12 stays Duke's.

## Pitfalls
- Do not mix engines on one page: job X (ce8d030) and release 2 (104691f or the new commit) are different models. Label each panel with its engine.
- explore_export's self-checks compare with a merged panel; for release 2 use the r2 results (`r2-tables-104691f`) as the panel, and say which.
- Clone one repository at a time; fetch a pinned commit with `git fetch --depth=1 origin <sha>`.
- JSON-LD carries Duke's personal email (S42 fixes); X-Cents ontology entries in the machine-readable files belong to S42; old remote branches to delete by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
