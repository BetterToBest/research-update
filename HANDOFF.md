# Handoff (Oct 29, 2026): S10 second, independent implementation of the yearly loop

## Step status
S10 **done**. A Python program written from the s118 packet reproduces the engine's validation presets: statistically from the packet alone, and **exactly on all 2,500 runs** (5 presets × seeds 1-500) once the three functions the packet lacked were added. The validation presets run the engine's older path, not the release row, so the figures the Hub and NEEC cite are not yet covered. New step **S50** does that, before the freeze. Duke asked to pause auto-chaining: `AUTOCHAIN.md` is `status: off`.

## What shipped
- compassionism-simulation #48 `claude/s10-independent-loop` (open, checks running), `dev/reports/s118-independent-implementation/`:
  - `s118_loop.py`: the program, Python standard library only.
  - `REPORT.md`: plain words, for Duke.
  - `GAPS.md`: 31 gaps in the written description, 8 of them contradictions.
  - `results/`, with `run.txt` and `SHA256SUMS`.
  - Two entries in `dev/DECISIONS.md`.
- How it ran. Phase 1, the packet alone, was committed (6ba43e0) before any engine code was read. Phase 2 read only the engine's `gamma`, `beta`, `lognormal` and `calcMetrics`, behind `--engine-fills`. Fresh seeds 501-1500 showed the phase-1 differences outside the Gini were chance.
- Main findings:
  - The description is of the release model; the packet's reference results come from the validation path. In that path nobody spends their surplus, wages are not indexed, and the octave wage raise, PTF/PTH price damping and the PTH appreciation double count are all still on.
  - The validation presets' "Gini" is of wealth less one year of EDC × wage. The description says wealth Gini. (Issue I14.)
  - Today's engine (main 6f4c6e7) gives identical validation outputs to the Oct 15 engine (seeds 1-30, all presets).
- research-update (this branch): AUTOCHAIN paused; PLAN.md adds S50 (row 16a, before S47) and marks S10 done.

## In flight
Nothing.

## Decisions waiting
- D2 (chat exports for S31): still waiting; S31 is skipped.

## Next step
**S34** (the no-programme baseline against outside data), opus, high: next in the Order table, waits on nothing. The chain is paused, so Duke starts it by hand.

## Pitfalls
- **The s118 brief's acceptance rule is too strict.** It uses only the engine's standard error. A program drawing different adults fails it on about one figure in six even when it is a perfect copy. Report the two-sample test beside it (S50 should preregister that).
- **Reading engine code spoils independence.** Commit the independent result before reading any engine code; S50 needs a session that has not read the engine (this one has).
- `python3 -I` does not put the script's folder on `sys.path`; scratch scripts that import `s118_loop` must add it.
- Commit trailers: CLAUDE.md forbids model names. Use `Co-Authored-By: Claude <noreply@anthropic.com>` even when the session's own attribution line names a model.
- **A step can run twice** (S46). Before starting by hand, check the scheduled tasks list; none were pending this session.
- Left for S24: dual-currency-inflation 4.3, A.2 and A.3 (from S46).
