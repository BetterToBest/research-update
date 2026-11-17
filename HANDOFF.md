# Handoff (Nov 17, 2026): S13 second pass, part 1 (release audit, v5.9.9)

## Step status
**S13 partly done.** Part 1 is done: the in-house pass and the outside prompt. Parts 2 and 3 wait on Duke pasting the Grok and ChatGPT or Gemini replies into a fresh S13 session. The NVIDIA reading is done (Duke's key is saved on the Default environment for integrate.api.nvidia.com): `audits/2026-11-17-release-review-nemotron.md`, untriaged. Duke also pasted a general Grok audit (not from the prompt): `audits/2026-11-17-grok-general-audit.md`, untriaged.

## What shipped
- research-update (PR 162 merged `fe6d481`, PR 163 merged `3dc08d1`; then a third PR, branch `claude/eloquent-clarke-zhszqj`):
  - `audits/2026-11-17-release-audit-s13.md`: the in-house audit, done in a fresh session from the spec, reports and results.
  - `audits/2026-11-17-release-audit-prompt.md`: the outside prompt. It has a role line to swap per system: Grok is a sceptical macroeconomist; ChatGPT or Gemini is a methods reviewer.
  - `audits/2026-11-17-nvidia-setup.md`: the NVIDIA steps.
  - `audits/2026-11-17-release-review-nemotron.md` and `audits/nvidia-2026-11-17/build_packet.py`: the NVIDIA reading.
  - `audits/2026-11-17-grok-general-audit.md`: Grok's general audit, word for word.
  - PLAN.md: the S13 note and its Order-table row.
- No engine change. The Simulation and results repositories were read at `1d50b19` and `c732c7f`.

## What the in-house pass found
- Nov 9 findings: 1, 2, 4 and 6 are closed; 3, 5 and 8 are partly closed; 7 (clarity: the README) is still open.
- **B (A before Duke's reply):** the model has no limit on the economy's total supply (the no-programme run has the same structure). At full backing this matches the design's reading. Below full backing, poverty still falls with no new output, so "poverty effects barely depend on backing" needs a note saying why.
- **C (B before Duke's reply):** full backing has no inputs; the design's intent is more output per hour, which the model assumes and does not model.
- **B:** S69 was given the engine's code excerpts and its results, so its exact agreement checks the translation, not the model.
- **C:** ECONOMIST-REVIEW.md still describes v5.6.
- Duke replied the same day (amendment at the end of the note): finding 1 narrowed to readings below full backing (B), finding 2 is a model limit (C), finding 3 is wording only. The prompt was revised before sending to state the design's reading (part B, items 3-4). No wording or engine change yet.
- Nemotron's reply recommends replacing the full-backing main row with a range of backing. That is a design question (D23, D26 are Duke's); the triage weighs it, and does not change the main row on its own.

## In flight
Nothing.

## Decisions waiting
- D32 answered by Duke (Nov 17): the main row's headlines stay as they are; a dated note goes only on the sentences and figures below full backing.
- D31 (the default goes ahead) and S12 (Duke's) are unchanged.

## Next step
S13 parts 2-3, when Duke brings the replies. The S13 section of PLAN.md lists what to do: save each reply word for word, triage them with the Nemotron reply and Grok's general audit into `audits/2026-11-release-review-triage.md`, add dated wording notes in a Simulation PR, and add new steps. Until then, S25, S42 and S44 can start.

## Pitfalls
- A shallow clone of compassionism-simulation came out at `a60bd3e`, not main's `1d50b19`. Run `git fetch --depth 1 origin main` and check out `FETCH_HEAD`, and check the version in CONTRIBUTING.md.
- `register_repo_root` failed once for compassionism-simulation ("internal error reading session"). Its CLAUDE.md was read directly.
- The NVIDIA models cannot browse, so a reading there needs a packet of the files' text (see the setup note).
- Earlier pitfalls still apply: `set_version.py` treats any argument as the version; `reader_codes.py --check` rejects step codes in reports; the Hub and root site have not been re-scanned with the stricter patterns.
