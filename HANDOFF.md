# Handoff (Nov 21, 2026): S97 done; next S99, S100, S101

## Step status
**S97 done (text only):** the release's reruns and checks are preregistered as Amendment 2 of `prereg/2026-11-s90-private-price-at-sale.md`, before the release engine exists. S99-S101 remain, in any order; S93 waits on all of them (D35).

## What shipped (S97)
- [research-update PR 203](https://github.com/BetterToBest/research-update/pull/203), merged (`67b96a9`): Amendment 2; outside reading triage `audits/2026-11-21-s97-amendment-reading.md` (Nemotron 3 Ultra, OpenRouter; nine points taken in full or part, one needed no change); PLAN.md S97 note and S93 now points to the amendment.
- What the amendment fixes for S93: rerun on the release engine (r2 parts M, S, F, B, erosion, r2 tables; central bank; history; supply, all 231 rows; suite x2-x4, whose `series-r2.js` hard-codes the `r2-m-*-104691f` path); the automation and lending studies reproduced (seeds 1-10, every row), not rerun; a list kept as record; engine conditions (`vAt: 'lag'` reproduces the guard test); below-full-backing swing and books at a = 0, 0.5 (`s90_trace.js`/`s90_acct.js` need a backed-share option); checks D1-D5; eight archived shards plus history era e2 reproduced (drawn with seed 9797); checklist F1-F10; release text G.

## In flight
- Nothing.

## Decisions waiting
- None open.

## Next step
S99 (text only; first in the Order table of the remaining pre-release steps). S100 needs a preregistration; S101 is text only.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.


## Pitfalls
- `expectedHeadSha` in a merge call must be the exact 40-character head; take it from `git ls-remote origin refs/heads/<branch>`.
- Row option names collide: grep `c\.<name>` in `index.html` before naming a switch (`cl` was taken).
- A pushed branch name whose PR merged cannot be reused without a force-push: use a new branch name (this session: `claude/s94-lending-build`).
- After an engine change, run `python3 dev/tools/sync_earlier.py` (earlier-engine.html carries the same script) and `node dev/tools/engine_lineage.js prove "..."` (about 10 minutes); otherwise domtest fails four checks.
- The guard test's rows predate open access: for a switch on the main row, also hash every key of `r2MainPair`'s rows against the old engine (`git show HEAD:index.html` and `harness.js` into a scratch folder with `node_modules`).
- Engine globals are not harness exports unless listed in `module.exports`; use `H.STRESS_TEST`, `H.ADVERSE_REFERENCE`, `H.FULL_INTEGRATION`.
- `/end-session` cannot be started by Claude (the Skill tool refuses it); Duke types it. Land PRs as you go.
- compassionism-simulation CI takes about 12 minutes and queues behind study shards; each push runs it twice (push and pull_request).
- After adding tests: `node harness.js unit --write-counts`. domtest needs `npm install` in a fresh clone (jsdom).
- This clone's `origin/main` can be stale at session start. Run `git fetch origin main` before branching.
- compassionism-sim-results is large: clone with `--filter=blob:none --no-checkout`, then `git sparse-checkout set --no-cone` on the folders you need.
- The `oh` rows' no-programme runs are shared by both-run settings (`none.<key>` rows in `s85.js`): pair each programme row with the `none` row its `rowSpec` names.
- `mfChk` is not 0 on flat-contribution main rows: never a pass/fail check there.
- A `SHA256SUMS` made with `ls | xargs sha256sum > SHA256SUMS` lists itself: leave it out (`ls | grep -v '^SHA256SUMS$'`), then `sha256sum -c`.
- OpenRouter's free tier (ids ending `:free`, 50 requests a day, public text only) and NVIDIA: `audits/2026-11-20-openrouter-setup.md`, `audits/2026-11-17-nvidia-setup.md`. Nemotron 3 Ultra on OpenRouter answers fastest; NVIDIA's Mistral and Kimi stream reasoning very slowly. Give a reasoning model 40,000 `max_tokens`.
- BLS refuses direct requests (use the fetch tool); Census BDS and BEA download with curl. McKinsey, Goldman Sachs, OECD and Autonomy refuse automated fetches.
- The GitHub tools can fail to connect at session start or after a restart; a ToolSearch for them reconnects.
- Check `date -u` and a process's elapsed time before deciding a job is stuck.
- In a `--filter=blob:none` clone, `git ls-tree -l` downloads every blob to report sizes (it ran for minutes on compassionism-sim-results): get file sizes from the GitHub contents tool (`get_file_contents` on the folder, fields name and size).
- `ppovA` and `pmedWA` are derived by the job scripts, not reported by the engine: a script that calls `tbStudy` directly must average `ppov_1..ppov_{T-1}` itself.
- In a sparse `--filter=blob:none` clone of compassionism-sim-results, add folders with `git sparse-checkout add '/<pattern>/'`; the six study folders (about 1.6 GB) and the `s90-sale-*` folders checked out in a few minutes.
- `rev` on PLAN.md's long table rows hung the shell; use `python3 -c` to print the end of a long line.
- The interactive tiles, milestones and insight cards are drawn only on `earlier-engine.html` (`index.html` carries the same script but not the markup): check them there, after `python3 dev/tools/sync_earlier.py`.
- The NVIDIA catalogue answered "upstream request failed" within two minutes for a 25,000-character packet (Nov 21); OpenRouter's free Nemotron answered the same request.
