---
name: end-session
description: End a Research Update session - land the work, rewrite HANDOFF.md, sync the ledger, and print the next session's start lines with model and effort. Use when invoked by name or at the end of a /start-session step.
disable-model-invocation: true
---

# End the session

Do these in order, then stop. Start no new work.

1. **Land the work.** Every repository changed this session has its PR merged (checks green), or HANDOFF.md says why it is open.

2. **Rewrite `HANDOFF.md`** in this repository, under 45 lines, plain words:
   - Title line: date and the step.
   - **Step status:** done / partly done (what remains) / blocked (by what).
   - **What shipped:** one line per PR (link, merged commit) or result folder.
   - **In flight:** long jobs: where they run, pinned commit, where results land, how to tell they are done (`DONE` file).
   - **Decisions waiting:** ledger decision IDs and one line each.
   - **Next step:** its ID and why it is next (the Order table in PLAN.md, skipping blocked steps).
   - **Pitfalls:** what went wrong or nearly did.
   If the step changed the plan, edit PLAN.md too (its section and the Order table). Commit and merge.

3. **Sync the ledger** (artifact https://claude.ai/artifact/F1hceP6XEfPQ1pf6Sw1Ki8). Load the ArtifactData tool (ToolSearch "ArtifactData").
   - First apply any files in `ledger-sync/` (oldest first), then delete them in the HANDOFF commit.
   - Read collection `projects`, document `hub` (or `neec` for an N step). Then ONE `update`, pinned with `if_version`, changing only:
     - `steps`: the step's `s` to "done" (or "doing"/"blocked") and `doneAt` like "Oct 29"; new steps as {id, t, d, s: "todo", phase}, ids from `seq.S`, then raise `seq.S`.
     - `decisions`: new ones as {id, q, opts, def, sel: def, conf: false, why}; ids from `seq.D`, then raise `seq.D`. `why` says what the default does if Duke does not answer.
     - `issues`: new ones as {id, title, items: [{d: false, t}], conf: false, gh: ""}; ids from `seq.I`.
     - `next`: the next five step IDs from the Order table; `left`: one paragraph on where things stand; `log`: prepend {t: <epoch ms>, m: "<ID> done: <one line>"}, keep 15; `updated`: like "Oct 29".
   - If the tool is missing or the write fails twice, write the same change as JSON to `ledger-sync/<YYYY-MM-DD>-<ID>.json` ({doc, set: {...}, add_steps: [...], add_decisions: [...], add_issues: [...], log}) and commit it; the next Chat or session applies it.

4. **Print, as the last thing in the reply,** exactly this block, filled in:

```
LEDGER NOTE
Done: <one line>
Evidence: <checks run, PR links>
Decide: <decision IDs for Duke, or "nothing">
Ledger: <synced | written to ledger-sync/<file>>

NEXT SESSION (start a new session on research-update, then paste these three lines in order)
/model <model from PLAN.md's Order table>
/effort <effort from the table>
/start-session <next step ID>
```

5. **Chain the next session** (only when `AUTOCHAIN.md` says `status: on`). Skip it, and say why under the block, if any stop condition in AUTOCHAIN.md holds. Otherwise load the scheduling tool (ToolSearch "create_trigger") and create one one-shot scheduled task:
   - `run_once_at`: now plus `delay_minutes`; `name`: "Research update <next ID>"; `initiation`: "human_schedule"; leave `permission_mode` unset; no local device.
   - `prompt`, exactly these lines:
     ```
     /model <model>
     /effort <effort>
     /start-session <next ID>
     This is a chained session started by the previous step's /end-session (research-update AUTOCHAIN.md). First record in HANDOFF.md which model this session is actually running on.
     ```
   Append one line to AUTOCHAIN.md's log (date and time UTC, from, to, model, effort) and commit it. In the reply, add "Chained: <next ID> at <time>" under the block, and say whether the scheduled task's runs ask for approval (if they do, Duke can switch it to "Automatically approve" in the task's settings). If the tool is missing, write "Chain: not available here" and leave the three lines for Duke.

Take model and effort from the Order table row of the next step. If the table says "(or fable, high)", write `/model fable` and `/effort high` only when fable uses no usage credits on this account; otherwise use the first model and effort. When nothing can start until Duke decides, replace the three lines with "Waiting on <decision IDs>".
