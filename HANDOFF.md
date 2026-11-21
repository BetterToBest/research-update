# Handoff (Nov 21, 2026): S94 part 2 done (the lending fund built); next S94 part 3

## Step status
**S94 partly done.** Parts 1 and 2 are done: reading, sources, preregistration with Amendments 1 and 2, and the build. Remaining: part 3 (the job `runner/jobs/s94.js`, dry run, six folders on GitHub Actions) and part 4 (tables, report, decision rule 6). S96-S101 can run in any order meanwhile; S93 waits on all of them (D35).

## What shipped
- compassionism-simulation [PR 174](https://github.com/BetterToBest/compassionism-simulation/pull/174), merged `c5682f9`: row option `lend` (the fund and charters; `cl` is the community layer), `clUnitSuite` (8 tests, checks 2-8), DECISIONS.md section, lineage link, earlier-engine page synced.
- research-update [PR 195](https://github.com/BetterToBest/research-update/pull/195), merged `72cdadb`: preregistration Amendment 2 (the build's choices) and the engine-commit note (folders `s94-<env>-<years>-c5682f9`); PLAN S94 section.
- This file and the PLAN Order row: research-update PR for `claude/wonderful-ritchie-nwu7yz`.

## What was found
- Off = identical: guard test; the main row without `lend` matches the old engine on every key (3 environments, 20 and 40 years, both designs, 2 seeds); six release panels unchanged. unit 416, domtest 162, validate, all CI steps green.
- One-seed smoke (Stress, full coverage, no choice made from it): the PTF share at year 19 rose from 34% to 49%, cost about +$490 per adult-year. Not a result.
- In the smoke script built straight from `r2MainPair`, `ppovA` read 0: the job's rows must be checked to produce every primary key before dispatch.

## In flight
- Nothing running.

## Decisions waiting
- None open.

## Next step
**S94 part 3** (opus, high): attach compassionism-sim-results (push) and compassionism-simulation; write `runner/jobs/s94.js` on `s85.js` block A's `off` rows (`o.sec` on, `sp.vAt 'sale'`, both designs, one shared no-programme run; 15 rows x 2 + 1 per environment and horizon, as in the preregistration's Design table with Amendment 1's block A); keys `LEND_KEYS` (harness export). Dry run on a few seeds: every primary key present, row D equal to M, checks 3-8 hold. Then dispatch six folders, 20 pieces of 25 seeds, pinned to `c5682f9`.

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
