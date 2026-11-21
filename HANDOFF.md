# Handoff (Nov 21, 2026): S94 part 3 done (the job, dry run, six folders dispatched); next S94 part 4

## Step status
**S94 partly done.** Parts 1-3 are done: reading, sources, preregistration with Amendments 1 and 2, the build, and now the job, its dry run and the six study runs dispatched. Remaining: part 4 (confirm the folders, tables, report, decision rule 6). S96-S101 can run in any order meanwhile; S93 waits on all of them (D35).

## What shipped
- compassionism-sim-results [PR 66](https://github.com/BetterToBest/compassionism-sim-results/pull/66), merged `35c8401`: `runner/jobs/s94.js` (31 rows per environment and horizon: M, the fund's 9 readings, charters 1/7, 1/3, 2/3, fund and charters together, D, in both designs, plus one shared no-programme run; every key at full precision plus derived `ppovA`, `pmedWA`, and `ppov20`, `pmedW20` at 40 years).
- research-update (this branch's PR): the preregistration's dated note on the job and dry run (no design change), the PLAN S94 section and Order row, this file.

## What was found
- The `ppovA` = 0 from part 2's smoke script came from the script, not the engine: `ppovA` is not an engine key. Earlier jobs (`r2.js`, `s82.js`) average `ppov_1..ppov_{T-1}`, and `s94.js` now does the same.
- Dry run (seeds 1-2, Stress 20 years, Adverse 40 years; only rows and keys checked, no outcome used for any choice): `--check` passes; every primary key is present with no nulls; D equals M on every shared key in both designs; the no-programme run is identical with `lend` set on it (all three environments); `clChk` is about 1e-16; `clUnitSuite` passes 8 of 8 on `c5682f9`.
- Cost: about 1 CPU-second per row and seed at 20 years and 2 at 40. A 25-seed shard is about 19 MB uncompressed (the output-per-hour study's savings folders were stored the same way).

## In flight
- run-study runs 167-172 in compassionism-sim-results, dispatched Nov 21 00:57 UTC: ref 20, adv 20, str 20, ref 40, adv 40, str 40 (study ids `s94-<env>-<years>`; 20 shards of 25 seeds; `--procs=4`; engine `c5682f93fe25ea8f926e12141ea1831a16fa2bd2`). Each run commits its folder `s94-<env>-<years>-c5682f9/` to main when it finishes. The 40-year runs need roughly twice as long as the 20-year ones.

## Decisions waiting
- None open.

## Next step
**S94 part 4** (opus, high): check that the six folders are on main, each with DONE, run.txt and SHA256SUMS, and that `sha256sum -c` passes (check 9). If a run failed, read its log and rerun that folder as frozen. Then the tables: paired seed differences row − M per design; 10,000-replicate paired bootstrap; Holm across the six primary measures; Q5's interaction (C − M) − (A main − M) − (B 1/7 − M). Then the report (`dev/reports/`, reader-codes check), the findings record, and decision rule 6 (rule 4 reads the pace × 0.5 and all-grants rows, per Amendment 1 item 8). If the fund passes, add a ledger decision (default: the fund joins the main row at the release, with charters off).

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
