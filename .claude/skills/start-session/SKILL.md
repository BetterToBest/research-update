---
name: start-session
description: Start one step of the Research Update plan (Simulation, Research Hub v2, NEEC) by ledger ID, for example /start-session S29 or /start-session N-S70. Use only when invoked by name.
disable-model-invocation: true
argument-hint: S<ledger step, e.g. S29> or N-S<NEEC step, e.g. N-S70>
---

# Start a Research Update session

The argument is: $ARGUMENTS

1. **Find the step.** "S29", "s29", "29" and "H-S29" all mean step S29 of the Hub & Simulation plan. "N-S70" means NEEC step S70. If the argument is missing, or `PLAN.md` has no `### <ID>` section and it is not an N step, print PLAN.md's Order table and stop.
2. **Read only what the step needs:** `CLAUDE.md` (this repository), `HANDOFF.md`, and the `### <ID>` section of `PLAN.md` (grep for the heading, then read that range). If `ledger-sync/` holds files, note them: `/end-session` applies them.
3. **Check it can start.** If HANDOFF.md or the Order table says the step is done, or it waits on an unanswered decision or an unfinished step, say so, name the next step that can start, and stop. A decision with a default ("default proceeds") does not block.
4. **Attach repositories.** For each repository the step lists, call add_repo (access "push"), clone it shallow beside this one (`../<name>`; use a full clone when the step needs history), and read that repository's CLAUDE.md before editing it. Engine changes follow compassionism-simulation's guardrails. For an N step: attach NormativeEvaluation, read its CLAUDE.md and the top of STATE.md, and take the step text from the ledger document `neec` (ToolSearch "ArtifactData"); if the ledger cannot be read, use the newest NEEC_Project_Handoff file.
5. **Plan briefly, then work.** Put the step's sub-steps in the task list. Proceed without waiting for approval (Duke has delegated); stop only where the step or CLAUDE.md says a decision is Duke's, and record it for `/end-session`.
6. **Land as you go.** Commit and push after each finished sub-step; open the PR early; merge it yourself once checks pass (CLAUDE.md, Landing work). Long jobs: start them, confirm they started, record them, move on.
7. **Finish** with `/end-session` (its file: `.claude/skills/end-session/SKILL.md`). Do not end the session without it.
