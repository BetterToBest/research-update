# Handoff (Nov 21, 2026): S98 done; next S97, S99-S101

## Step status
**S96 done:** compassionism-simulation PR 177 merged (`f180986`).
**S98 done (text only):** compassionism-simulation [PR 178](https://github.com/BetterToBest/compassionism-simulation/pull/178), see "In flight" for whether it has merged. S97, S99-S101 remain, in any order; S93 waits on all of them (D35).

## What shipped (S98)
- Findings page (`site/round2.js`) and its text file (`dev/reports/s64-findings-page-text.md`): every headline card carries the full-backing condition and the opt-in figure; the poverty-effects sentence is conditional on wages following prices, with the supply study's wage figure beside it; one reconciled statement of the model's own new output (mechanism 0.2-1.9%, 14-20% without its ceiling; automation study 6-17%, 3-7% opt-in; they count output differently); every below-full-backing inflation figure labelled as the size of unbacked money, not a forecast; 18-53 against 40-49 reconciled (same rows, different subsets); ratio between designs removed; the 10,000-adult check's scope; who is simulated; definitions (families in debt, robust, the 48 curves against 62 readings); the financed rows' missing tail and different income bases; the labour share as partly a denominator effect; which savings measure; shortages not in the money measures.
- CHANGELOG entry and DECISIONS entry ("S98") in compassionism-simulation. Reader-codes check: 0.
- Not on the page or text file, so unchanged: "cautious side" claims, a NEEC criterion statement. Left: a reading-by-screening-group map of the curves. The Hub's copies of these sentences belong to S101.

## In flight
- compassionism-simulation PR 178: CI (checks, guard) was running at the end of the session. If it is still open, merge it once both checks pass (`expectedHeadSha` from `git ls-remote origin refs/heads/claude/s98-findings-wording`).

## Decisions waiting
- None open.

## Next step
S97 (the other first-listed pre-release step that needs no runs; S99 and S101 are also text only and start now; S100 needs a preregistration).

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
