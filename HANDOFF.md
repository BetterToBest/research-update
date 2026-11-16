# Handoff (Nov 16, 2026): S11 (BLEI visuals), checked only; build waits on one basis choice

## Step status
**S11 is partly done (no code or data changed).** Done: I1's list is confirmed. The frozen-engine series (job X, result folder `x-ce8d030` in compassionism-sim-results, engine ce8d030, 500 seeds, 20 and 40 years, Reference/Adverse/Stress; SHA256SUMS verify) already holds every series I1 asks for: BLEI tier shares (all adults, participants, non-participants), median BLEI and its three parts (medians and means), relative income poverty, extreme poverty, share taking part, by year with 10th/90th percentiles. Nothing new needs exporting from `explore_export.js`.
Not done: rebuilding the visual suite (`suite.html`) from them. Reason: the series do not fit the page as it stands (see Decisions waiting). S7 is confirmed done (compassionism-simulation PR 119 merged Nov 15; manifest now at 5.9).

## What shipped
Nothing merged except this handoff.

## In flight
Nothing.

## Decisions waiting
- D30 (new): which engine and rows the rebuilt suite shows. Default proceeds: the frozen series as they are (job X, no programme / C2.2 design / release design), no new run.

## Next step
S11 again once D30 is answered or its default is taken, as the next session's first act (default needs no new run: add the three-row frozen series as a new release data folder, adapt `suite.html`'s reading selector and its panel paths, keep v5.6's files untouched, then S12 is yours). Otherwise S42 (waits on S43, blocked; ask Duke), S44.

## Pitfalls
- X's `selfCheck` says "NOT COMPARED WITH A PANEL"; S48 compared it with the merged frozen panel afterwards (`panel-frz-ce8d030`). Re-run `--panel` comparison when rebuilding.
- `suite.html` reads rows release/mid/h1 and pairs each with the release panel (v5.6, not frozen); X has rows base/c22/release on the frozen model. Mixing them would put unlike figures side by side. Use the frozen panel for the page's panel paths.
- X does not cover release 2's main row (engine 104691f); the Hub and simulation page now lead with release 2.
- Hub and other pitfalls from the earlier handoff stand: JSON-LD carries Duke's personal email (S42 fixes), clone one repository at a time, X-Cents ontology entries in the machine-readable files belong to S42; old remote branches still to delete by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`, `claude/admiring-fermi-p13aus`.
