# Handoff (Nov 21, 2026): S100 part 1 done; part 2 reads the batch

## Step status
**S100 partly done.** Part 1 (reading, sources, preregistration, switch, runs started) is done. Part 2 remains: read the batch, have outside readers check it, then the main-row decision. S93 waits on S100 (D35).

## What shipped
- compassionism-simulation [PR 180](https://github.com/BetterToBest/compassionism-simulation/pull/180), merged `e50a3b3`. Row option `eh` gives pay by household type (CPS ASEC 2026; partners correlated 0.22; no draw). `sn.cdc` is the child and dependent care credit (tax year 2025, Publication 503; paid only to the CPS share of families who pay for care; claimed before the CTC). `sn.rep` adds reporting keys. Also: reading `dev/reports/s100-part-time-reading.md`, `sources/s100_earnings_by_household.py`, 7 unit tests, `dev/tools/s100_tables.py` (written before any result). Guard identical; main pair identical on 5,862 series; unit 423/423, validate, domtest 162/162, lineage proved.
- compassionism-sim-results [PR 68](https://github.com/BetterToBest/compassionism-sim-results/pull/68): `runner/jobs/s100.js` (22 rows; `--check` passes).
- research-update [PR 208](https://github.com/BetterToBest/research-update/pull/208): `prereg/2026-11-s100-part-time-dcc.md` (engine recorded before the run); PLAN note.
- Finding: the old EITC gap (11.9% against 15.3%) was mostly a measurement mismatch. The US figure counted other tax units in the poverty unit and assumed full take-up. Like for like: 10.9% against 11.8%.

## In flight
- Six runs on compassionism-sim-results `run-study.yml` (runs 173-178, started Nov 21 13:35 UTC), engine `e50a3b3`. Folders `s100-{ref,adv,str}-{20,40}-e50a3b3`; a folder is done when it has `DONE`.

## Decisions waiting
- The main-row change. Duke, Nov 21: decide after the study completes and outside audit reviews verify the findings. Part 2 runs the tables, gets the outside readings (NVIDIA / OpenRouter free tier, public text only), then writes the ledger decision. Default meanwhile: the release keeps today's main row.

## Next step
S100 part 2 (opus, high). Run `python3 dev/tools/s100_tables.py <results> <out> --engine e50a3b3` and publish the tables folder. Read Q1-Q4 under the decision rules. Write the report and the findings-page text. Send it for outside reading. Add the ledger decision. Then S93.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.

## Pitfalls
- `expectedHeadSha` in a merge call must be the exact 40-character head; take it from `git ls-remote origin refs/heads/<branch>`.
- A pushed branch name whose PR merged cannot be reused without a force-push: use a new branch name (this session: `claude/s94-lending-build`).
- After an engine change, run `python3 dev/tools/sync_earlier.py` (earlier-engine.html carries the same script) and `node dev/tools/engine_lineage.js prove "..."` (about 10 minutes); otherwise domtest fails four checks.
- The guard test's rows predate open access: for a switch on the main row, also hash every key of `r2MainPair`'s rows against the old engine (`git show HEAD:index.html` and `harness.js` into a scratch folder with `node_modules`).
- `/end-session` cannot be started by Claude (the Skill tool refuses it); Duke types it. Land PRs as you go.
- compassionism-simulation CI takes about 12 minutes and queues behind study shards; each push runs it twice (push and pull_request).
- After adding tests: `node harness.js unit --write-counts`. domtest needs `npm install` in a fresh clone (jsdom).
- This clone's `origin/main` can be stale at session start. Run `git fetch origin main` before branching.
- compassionism-sim-results is large: clone with `--filter=blob:none --no-checkout`, then `git sparse-checkout set --no-cone` on the folders you need.
- The `oh` rows' no-programme runs are shared by both-run settings (`none.<key>` rows in `s85.js`): pair each programme row with the `none` row its `rowSpec` names.
- OpenRouter's free tier (ids ending `:free`, 50 requests a day, public text only) and NVIDIA: `audits/2026-11-20-openrouter-setup.md`, `audits/2026-11-17-nvidia-setup.md`. Nemotron 3 Ultra on OpenRouter answers fastest; NVIDIA's Mistral and Kimi stream reasoning very slowly. Give a reasoning model 40,000 `max_tokens`.
- BLS refuses direct requests (use the fetch tool); Census BDS and BEA download with curl. McKinsey, Goldman Sachs, OECD and Autonomy refuse automated fetches.
- The GitHub tools can fail to connect at session start or after a restart; a ToolSearch for them reconnects.
- `ppovA` and `pmedWA` are derived by the job scripts, not reported by the engine: a script that calls `tbStudy` directly must average `ppov_1..ppov_{T-1}` itself.
- The interactive tiles, milestones and insight cards are drawn only on `earlier-engine.html` (`index.html` carries the same script but not the markup): check them there, after `python3 dev/tools/sync_earlier.py`.
- Row option names collide: grep `c\.<name>` in `index.html` before naming a switch (`cl` was taken).
- Engine globals are not harness exports unless listed in `module.exports`; use `H.STRESS_TEST`, `H.ADVERSE_REFERENCE`, `H.FULL_INTEGRATION`.
- `mfChk` is not 0 on flat-contribution main rows: never a pass/fail check there.
- A `SHA256SUMS` made with `ls | xargs sha256sum > SHA256SUMS` lists itself: leave it out (`ls | grep -v '^SHA256SUMS$'`), then `sha256sum -c`.
- The Hub has no CI: run `reader_codes.py --preset hub` and `--preset root` (from compassionism-simulation) before merging. Do not rerun `tools/class_claims.py` as a side effect: it rewrites `data/claims.csv` wholesale (about 20,000 rows against 11,173).
- `add_repo` clones must run one at a time (proxy cap). The Hub's pattern for a withdrawn figure: keep the sentence, add an italic dated note, add a `corrections.html` entry, rebuild the PDF (`node tools/build_pdf.js <page>`).
- The run's report hook fires twice per row (the supply reference run too): a test hook must replace, not append.
- The US "EITC reach" in the CPS is the SPM unit's and the Census tax model's (full take-up): compare with own tax unit and `sn.taxTake 1`.
