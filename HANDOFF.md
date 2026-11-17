# Handoff (Nov 17, 2026): S13 second pass, part 1 (release audit, v5.9.9)

## Step status
**S13 partly done.** Part 1 is done: the in-house pass and the outside prompt. Parts 2 and 3 wait on Duke pasting the Grok and ChatGPT or Gemini replies into a fresh S13 session (and, if he wants, an NVIDIA API key for a third reading).

## What shipped
- research-update (this PR, branch `claude/eloquent-clarke-zhszqj`):
  - `audits/2026-11-17-release-audit-s13.md`: the in-house audit, done in a fresh session from the spec, reports and results.
  - `audits/2026-11-17-release-audit-prompt.md`: the outside prompt. It has a role line to swap per system: Grok is a sceptical macroeconomist; ChatGPT or Gemini is a methods reviewer.
  - `audits/2026-11-17-nvidia-setup.md`: the NVIDIA steps.
  - PLAN.md: the S13 note and its Order-table row.
- No engine change. The Simulation and results repositories were read at `1d50b19` and `c732c7f`.

## What the in-house pass found
- Nov 9 findings: 1, 2, 4 and 6 are closed; 3, 5 and 8 are partly closed; 7 (clarity: the README) is still open.
- **A:** the model has no limit on real goods. Wages, the BU and the basket all follow prices, essentials prices rise with demand but demand is always met, and food has no price response at all. So with no backing at all the programme still lowers basket poverty by 31 points and raises median wealth by $86,800. "Poverty effects barely depend on backing" comes from how the model is built; it says nothing about the design.
- **B:** full backing has no inputs: the matching output needs no work, capital or time, while participation falls.
- **B:** S69 was given the engine's code excerpts and its results, so its exact agreement checks the translation, not the model.
- **C:** ECONOMIST-REVIEW.md still describes v5.6.
- No wording or engine change yet: the outside reviews are asked these questions first (prompt, part B, items 3 and 4).

## In flight
Nothing.

## Decisions waiting
- D32 (new; the default goes ahead): should the Hub's poverty headlines say they hold "in a model with no limit on real goods" until an engine step adds a limit? Default: yes, from S40 on, once the triage confirms it.
- D31 (the default goes ahead) and S12 (Duke's) are unchanged.

## Next step
S13 parts 2-3, when Duke brings the replies. The S13 section of PLAN.md lists what to do: save each reply word for word, run the NVIDIA reading if there is a key, triage everything into `audits/2026-11-release-review-triage.md`, add dated wording notes in a Simulation PR, and add new steps. Until then, S25, S42 and S44 can start.

## Pitfalls
- A shallow clone of compassionism-simulation came out at `a60bd3e`, not main's `1d50b19`. Run `git fetch --depth 1 origin main` and check out `FETCH_HEAD`, and check the version in CONTRIBUTING.md.
- `register_repo_root` failed once for compassionism-simulation ("internal error reading session"). Its CLAUDE.md was read directly.
- The NVIDIA models cannot browse, so a reading there needs a packet of the files' text (see the setup note).
- Earlier pitfalls still apply: `set_version.py` treats any argument as the version; `reader_codes.py --check` rejects step codes in reports; the Hub and root site have not been re-scanned with the stricter patterns.
