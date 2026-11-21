# Handoff (Nov 21, 2026): S99 done (PR awaiting checks); next S100, S101

## Step status
**S99 done (text and labels only).** compassionism-simulation [PR 179](https://github.com/BetterToBest/compassionism-simulation/pull/179) is **open: its `checks` jobs were still running when the session ended** (`guard` passed; locally domtest 162/162, validate passes, reader-codes clean). Next session: check it once, then merge it with the head from `git ls-remote origin refs/heads/claude/s99-validation-presets-text` (75b9bd7 at the time). S100 and S101 remain; S93 waits on both (D35).

## What shipped (S99)
- PR 179 (open): the earlier engine's "Gini" renamed net-wealth Gini (page tile, chart, table, milestone, export, `harness.js validate`); MODEL_SPEC Appendix B says what `validate` compares and that the seed-42 changelog figures come from the earlier path, with a label for validation figures; Appendix C opens with the status of every gap and contradiction (nothing undescribed; the four `fx` fixes stay a release-engine question); ODD paragraph on the presets; changelog entry.
- Most of S99 was already done by earlier sessions (Appendices A and C, the four contradictions corrected in the text).

## For S101
- The Hub's "EDC-adjusted Gini 0.518 (v4.4)" is the net-wealth Gini of the validation preset, set against income-Gini targets (0.25, 0.22) and the Nordic range. Claims rows: BLEI paper (4 rows, 2 PDF-only), `research-summary.html` and `index.html` ("engine measures 0.518", 10 rows). Relabel or withdraw the comparison there; not edited in S99.

## In flight
- Nothing.

## Decisions waiting
- None open.

## Next step
S100 (needs a preregistration; opus, high) or S101 (text only; sonnet, high). S101 is the cheaper one to start; either order.

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
- compassionism-simulation's `reader_codes.py --list` prints many old report lines even when `--check` passes: trust `--check`.
- The repository's CLAUDE.md asks for `/handoff`; research-update's `/end-session` is the one to run.
- The Hub claims ledger is research-hub `data/claims.csv` (a read-only clone is enough to grep it).
