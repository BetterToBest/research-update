# Handoff (Nov 15, 2026): S3 done; S7 done (release v5.7.0)

## Step status
**S7 is done:** compassionism-simulation PR 119 is merged, tag `v5.7.0` exists and its release (with the v5.7.0 notes and the reproduce zip) was published by the workflow. **S3 is done.** Next: **S65** (release 2), which waits on S64's results; check the Order table. S4 (X-cents) was not part of this session.

## What shipped
- [compassionism-simulation PR 119](https://github.com/BetterToBest/compassionism-simulation/pull/119): merged (a3f687b), checks and guard green, tag `v5.7.0`.
- [research-hub PR 12](https://github.com/BetterToBest/research-hub/pull/12): OEIAS glossary entry (term card, quick-reference link, JSON-LD DefinedTerm). Merged (7a3e84d). No checks are configured there.
- [bettertobest.github.io PR 1](https://github.com/BetterToBest/bettertobest.github.io/pull/1): OEIAS in ai-index.json and llms.txt. Merged (19d8ea9).
- S3 is a name only: it defines OEIAS as the umbrella for CCO, PTF, PTH, SZH and CIP with X-cents and says it adds no mechanism or result. I did not gloss the words of the name, because the text is silent on them.

## In flight
- Nothing.

## Decisions waiting
- None open. D68 (OEIAS scored as a 24th entry on Hub v2) was already confirmed.

## Next step
1. **S65** (release 2 and findings page; sonnet, medium) once S64's results are in. 2. **S74 part 2** (opus, xhigh, engine build) can run beside it. S4 (X-cents) and S40 follow.

## Pitfalls
- Old remote branches still need deleting by hand: research-update `claude/s66-low-share-trace`, `claude/jolly-davinci-dbcv2x`, `claude/stoic-hypatia-99pell`; compassionism-simulation `claude/s7-part2-saving-groups` if it still exists.
- research-hub's `.gitattributes` prints "text/xml is not a valid attribute name" on every git command; harmless.
- The research-hub and root-site repositories have no CI, so a merge there is not checked by anything; read the diff.
- The release workflow reads notes from CONTRIBUTING.md's exact heading `## v<version> Release Notes`; no date in the heading.
- Commits with no URL line and a `Co-Authored-By:` line go through.
- `index.html` in compassionism-simulation has very long lines; use `dev/CODEMAP.md` line ranges.
- `compassionism-sim-results` clones with `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse`, then `git sparse-checkout set <folder>`.
- S74 sources: bls.gov refuses this machine (HTTP 403); FRED can return HTML instead of csv.
