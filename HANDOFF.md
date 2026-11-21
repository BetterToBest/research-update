# Handoff (Nov 21, 2026): S94 part 4 done (the lending study read; the main row unchanged); next S94 part 5

## Step status
**S94 parts 1-4 done.** Remaining: part 5, the study's findings-page section (sonnet, medium). S96-S101 can run in any order meanwhile; S93 waits on all of them (D35).

## What shipped
- compassionism-sim-results [PR 67](https://github.com/BetterToBest/compassionism-sim-results/pull/67), merged `fb774d2`: `s94-tables-c5682f9` (checks, tables at 20 and 40 years, decision rule 6, `s94-summary.json`, `analysis.txt`, `SHA256SUMS`).
- compassionism-simulation [PR 175](https://github.com/BetterToBest/compassionism-simulation/pull/175), merged `dfda580`: `dev/tools/s94_tables.py`, the report `dev/reports/s94-collectives-lending.md` (reader codes clean; section 10 is the findings-page text), a DECISIONS.md entry, HANDOFF.md, CODEMAP.
- research-update (this branch's PR): the preregistration's dated note on the analysis (three readings fixed in the tool before any table was read; no design change), PLAN S94 section and Order row, this file.

## What was found
- Every check passes in all six folders; the main rows and the no-programme run equal the published at-sale rows (`s90-sale-*-b8ccd8d`) in every key and seed.
- **The fund helps in no cell** (decision rule 3: 0 of 12) and worsens at least two of the six readings in every cell. In five cells the community businesses' share reaches its 49% ceiling by year 10 without it; the fund only brings growth forward, at $37-63 per adult a year. Under Stress opt-in it lifts the share at year 20 from 34% to 48%, but programme cost rises $412 a year (running-cost subsidy $291, fund net $142), the contribution $261, and all six readings worsen (basket poverty +0.07 points, median wealth -$391). No other fund reading passes anywhere.
- **Charters** at 1/3 and 2/3 improve basket poverty, yearly wealth poverty and savings in every cell and worsen nothing (2/3: all six readings); at 1/7, public power's actual share, they act only in Stress. The fund-charter interaction is negligible.
- **Decision rule 6 does not hold:** the fund is a reading beside the main row; no ledger decision.
- For S97: this study ran on `c5682f9`, so its rerun-or-label entry belongs in the release amendment's list (the S97 note says "if it lands first": it has).

## In flight
- Nothing.

## Decisions waiting
- None open.

## Next step
**S94 part 5** (sonnet, medium): the lending study's findings-page section, following the automation study's (`dev/tools/s85_page_data.py`, `s85Section()` in `site/round2.js`): a tool writing `data/studies/s94-lending.json` from compassionism-sim-results `s94-tables-c5682f9/s94-summary.json`; a section printing every figure from that file, with the report's section 10 as its text and every unfavourable cell named; reader-codes check and domtest. Then S96-S101 in any order.

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
