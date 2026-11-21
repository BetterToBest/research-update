# Handoff (Nov 21, 2026): S93 part 2 done in part (dry run, dispatch, section C, reproductions)

## Step status
**S93 part 2 done in part.** The dry run on the release engine passed for every rerun job except r2 part F and the supply study, which fail the BU stock identity in runaway runs (the engine before fails the same). 570 shards are dispatched; part F and the supply study are held. Next: S93 part 2b (the BU identity; then part F, the supply study and the visual suite). Full record: `audits/2026-11-21-s93-dispatch.md`.

## What shipped
- compassionism-sim-results PR 71 (`runner/jobs/s93-dry.js`, the dry-run job: `acctDrawCheck` around every `tbStudy` call through `NODE_OPTIONS=--require`; `series-r2.js --panel=ENGINE7`), PR 72 (`runner/compare-shards.js`), PRs 73-74 (`s93-belowfull-69e8953`, section C), PR 75 (`s74-final-69e8953`, `s75-eras-69e8953`, `s93e-s75-eras-e2-e5649ef`). The workflow also committed `s93dry-69e8953` and seven `s93e-*` reproduction folders.
- compassionism-simulation PR 183 (merged `244b249`; tools only): `s90_trace.js --a=X --lag`, `s90_swing.js --a=X --s92=FILE`, `s90_acct.js --a=X`, `s90_swing_growth.js`.
- research-update (this PR): Amendment 5 of `prereg/2026-11-s90-private-price-at-sale.md` (section C1 failed on its measure; the growth-change measure, committed before computing; changes from the outside reading), `audits/2026-11-21-s93-amendment5-reading.md`, `audits/2026-11-21-s93-dispatch.md`, PLAN notes.
- **Found:** (1) the BU stock identity (`acctYearEnd`, index.html about line 3643) fails by 0.5-1.7% of its scale in runs where the BU price level explodes: r2 part F's least-favourable bound points (points 116, 120, 123-125) and supply rows 47-48 at 40 years; present on `a33c59d` too, so the published part F and supply folders carry it. (2) Below full backing the preregistered swing measure counts the price level's steady growth as swing; the at-sale fix still removes the swing (growth-change measure 0.05-0.11 of lagged; detrended measure agrees).

## In flight
- **Workflow runs 188-229** (compassionism-sim-results `run-study.yml`, runner `fcf9029`, engine `69e89533d0aed26f9c3e3ccc5523e0df72192786`): r2 parts M (1 shard per cell), S (6/11), B (2/4); `s100.js` (10/20); `s85.js`, `s85.js --sec`, `s94.js` (20 each); six cells each; folders `<id>-69e8953`. GitHub's free concurrency is 20 jobs, so expect about a day.
- **Workflow run 181:** the section E reproduction of `r2-s-ref-40-104691f` shard 0000 (folder `s93e-r2-s-ref-40-104691f`); compare with `node runner/compare-shards.js r2-s-ref-40-104691f/shard-0000.json.gz s93e-r2-s-ref-40-104691f/shard-0000.json.gz`.

## Decisions waiting
- For `/end-session`, a ledger decision with a default: section C1's preregistered swing measure failed below full backing for a reason found (it counts steady growth); Amendment 5 replaced it after the failure with a growth-change measure (holds) and a detrended check (agrees). Default: the below-full-backing figures are published from the release engine with both measures and the post-hoc label. Duke may instead hold them (section C4).
- D34 (version): v5.9.22 by default, as before.

## Next step
S93 part 2b (opus, high): (1) read the part S reproduction (run 181); (2) find the BU identity's missing flow in runaway runs (one point: `s93-dry.js --seeds=13-13` is part F Reference 20 years; or run the one bound point with `acctDrawCheck`); a defect is fixed by Amendment 6 (its reach: published part F bound rows, supply rows, any exploding run) under the engine guardrails; then dry-run and dispatch part F (7/14 shards) and the supply study's both batches (20; 10 for `--rows=134-136`, ids `s82-v6-…` and `s82-v6-age-…`); (3) once part M lands, the visual suite (`series-r2.js --panel=69e8953`: x2 `--env=all --years=20,40 --n=500`, x3 with `--study`, x4 as x2; seeds 1-6, 6 shards). Do not read any figure before checks D1-D5 (part 3).

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.

## Pitfalls
- The engine's stored no-programme supply path (`tbBaseS`, `s3BaseS`) is keyed by hand: a new row option that acts on a no-programme run must be added to `rowKeyS93`, or rows run after others in one process take the wrong path. Test: a no-programme row has programme inflation exactly 0 on its own path.
- A unit test that sets engine state by hand and then calls `tbStudy` must clear that state first (`PTFS`, `PTF_OPS`, `POS`, `PAS`, `PA`, `PFS`, `CMS`, `PRICE`, `LEND`, `LDS`).
- The release baseline check (every study job's start) reads `data/baseline.json`, the v5.9 no-programme run, so since v5.9.22 it runs the v5.9 row. When the rerun part M lands: `dev/tools/make_baseline.js` from it, with `release: 'v5.9.22'` in the file, and the check runs the release row (S93 part 3).
- Since v5.9.22 the guard reference hashes the v5.9.21 output list (483 keys): rewrite it with `--write --keys-from=dev/runs/guard/v5.9.21`, or unchanged rows get new hashes.
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
- OpenRouter's free Gemma is often refused upstream (429, Google's shared pool). NVIDIA's catalogue serves the same model (`google/gemma-4-31b-it`), but stream it (`"stream": true`, `curl -N`): unstreamed, the gateway returns 502 after about 160 seconds.
- `dev/tools/check_round2.js` is not in CI; run it after any change to `site/round2.js`. It needs at least 400 number spans and checks each against its file.
- Report tables: generate them from the summary file; do not type figures (a typed inflation column was wrong here and was caught before commit).
- The dry-run job `runner/jobs/s93-dry.js` (results repo): seed I is a unit (1-54 job x cell, in the order of its header; 55 the `--check`s; 56-57 the selftests); run it locally in an engine checkout with `--seeds=I-I --out=FILE` for one unit. A shard exits 0 whatever its checks find: read `_meta.pass` in each `shard-*.json`, not the job's colour.
- The run-study workflow's checkout of the results repository takes about 20 minutes for the plan job and about 5 per shard; a dispatch shows "queued" for a long time before shards start.
- To reproduce an archived shard on its own runner commit, push a branch at that commit (`git fetch --depth=1 origin SHA; git push origin SHA:refs/heads/claude/<name>`) and dispatch with that ref and a new study id (the old id's folder is DONE).
- `git ls-tree -l` in the partial (blob:none) results clone fetches every blob: never ask it for sizes.
- Since v5.9.22 `s90_trace.js` without a flag runs the sale (the default): name the lagged rule with `--lag`.
