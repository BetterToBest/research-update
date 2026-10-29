# Handoff (Oct 29, 2026): S28 wiring

## Step status
S28 done once the three open pull requests below show merged (see "What shipped"). Next: **S2**.

## What shipped
- research-hub [pull request 5](https://github.com/BetterToBest/research-hub/pull/5): short CLAUDE.md (merged, no checks run in that repo).
- compassionism-simulation [pull request 47](https://github.com/BetterToBest/compassionism-simulation/pull/47): landing rule replaces "Duke merges"; guardrails untouched; `/handoff` points at ledger F1hceP6XEfPQ1pf6Sw1Ki8, document `hub`, and prefers this repository's `/end-session`.
- NormativeEvaluation [pull request 53](https://github.com/BetterToBest/NormativeEvaluation/pull/53): same landing rule; NEEC stays paused.
- This repository: `.github/workflows/links.yml` (relative-link check), this file.

## Checks of the old items
- S9: nothing to merge. The compare-page restyle and study-page history removal shipped in pull requests 40-46 (merged Oct 16); no draft pull request is open. Close S9.
- S17: mostly shipped. Confirmed: shared glossary on front and findings pages; "same-rules reading" on both; CONTRIBUTING.md open-items table and dev/PROGRESS.md marked historical. **Missing, small follow-up:** British spellings remain on live pages (index.html: labour, behaviour, neighbourhood, Labour, including inside the release data strings; compare.html: favour, labour); one "design-neutral reading" remains in an index.html code comment (line ~2372). Not found by grep, check by eye on the live pages: the damping row wording for PTF/PTH and the v5.5 entry in the release list (the v5.5.0 notes exist in CHANGELOG.md).
- S18: `dev/packets/` holds three zips: s118 (is S10), s119 (is S15), s148 (is S13), with builders and a README. Nothing else remains; close S18.
- Corrections package (C1-C30) and claims-ledger draft: not in any of the five repositories (only mentions in PLAN.md and a one-line item in compassionism-simulation `dev/background/ledger-export.md`). Decision for Duke: bring them over from the other account (ledger sync file below).
- Workflow file: GitHub accepted `.github/workflows/links.yml` pushed from this session with `git push`. S33 can rely on that.
- Chaining test: see the end-of-session reply.

## Decisions waiting
- Bring the corrections package and claims-ledger draft over from the other account (default: S23/S24 start from the Hub as it is today).

## Next step
S2 (tag Hub v1 and the cited Simulation release; build /v1/ archive), sonnet, medium. D1 default proceeds.

## Pitfalls
- The GitHub connector's pull-request tools worked this time (create, read checks, merge); the 403 in the earlier handoff did not recur. `gh` here fails to log in; use the connector.
- compassionism-simulation's checks include a ~3 minute `guard` job; do not wait on it in a loop.
- research-hub has no CI, so its pull requests merge at once; review your own diff first.
