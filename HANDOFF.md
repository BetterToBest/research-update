# Handoff (Nov 23, 2026): S93 part 3 done (every release table published; next the pages)

## Step status
**S93 part 3 done.** All 60 rerun folders and the visual suite are on the release engine (`50bc51d`, v5.9.23). The checks before reading (D1-D5) pass on all of them. Every release table is published, each one made by a tool from the stored values. Record: `audits/2026-11-23-s93-part3b.md` (first session: `audits/2026-11-23-s93-part3.md`). **Next: S93 part 4, the pages.**

## What shipped
- compassionism-simulation PR 186 (merged, `ccd4cfc`): `dev/tools/s93_release_tables.py` (F1's split: published, at sale, release; it reproduces `s90-tables-b8ccd8d`'s change in all 468 estimates); `dev/tools/s93_belowfull_change.py` (C3); `--main ENGINE7` in `s85_tables.py` and `s94_tables.py` (off: the published lending tables come out byte for byte).
- compassionism-simulation PR 187 (merged, `944cfab`): `s64_erosion_table.py --engine=` (default reproduces `r2-erosion-104691f` byte for byte).
- compassionism-sim-results PR 78 (merged): `s93-release-tables-50bc51d`, `s93-c3-50bc51d`, `s100-tables-50bc51d`, `s94-tables-50bc51d`, `s82-tables-50bc51d`; tables added to `s74-final-50bc51d` and `s75-eras-50bc51d`.
- compassionism-sim-results PR 79 (merged): `r2-tables-50bc51d` (with the backing curve's replay in `replay/`), `s85-tables-50bc51d`, `r2-erosion-50bc51d`.
- research-update PR (this session): the record, PLAN note and Order-table row.
- **F1's split** (60 primary effects): no effect changes sign; 53 change at the pages' rounding; the total change is in the programme's favour in 21, against it in 25, interval includes 0 in 14. The private price at the sale moves every effect in the programme's favour (or not at all); pay by household type and the care credit shrink the opt-in design's poverty cuts and enlarge the full-coverage design's cut below 30 days of basic living, as Amendment 3 expected.

## In flight
Nothing. Run 272 (`s85-ref-20`) landed on its third finish attempt.

## Decisions waiting
- For `/end-session`, a ledger decision with a default: section C1's preregistered swing measure failed below full backing for a known reason (it counts steady growth). Amendment 5 replaced it after the failure with a growth-change measure (holds) and a detrended check (agrees). Both are unchanged on v5.9.23. Default: the below-full-backing figures are published from the release engine with both measures and the post-hoc label. Duke may instead hold them (section C4).
- D34 (version): the default, a v5.9 patch, names **v5.9.23**. Record it on D34 at `/end-session` if not yet done.

## Next step
S93 part 4 (opus, high): the pages, under Amendment 2's F and G (with Amendment 3).
1. F1's page part: extend `dev/tools/s90_page_check.py` to every release data file (each printed figure's published and release value; counts by last digit, sign, printed range); every change against the programme listed and its statement rewritten (the per-cell list is in `s93-release-tables-50bc51d/s93-release-tables.md`).
2. Regenerate the findings-page data from the `-50bc51d` tables folders with each data file's own generator (grep `dev/tools` for the generator that names `r2-tables-104691f`, `s82-tables`, `s85-tables2`, `s94-tables`, `s100-tables`, `s74-final`, `s75-eras`, `x2-`); the visual suite's data from `x2`-`x4-50bc51d`.
3. F2-F10 (swing gone, guard reference recorded, qualifiers, BLEI visuals, charts, correction notes, engine names, outside reading by two other makers, Hub corrections log and root indexes) and the release text G.
Reader-codes check before every reader-file commit.

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
- A lineage link after a by-design change (since v5.9.22) never equals the v5.6 base: `engine_lineage.js prove` records it as not reproducing, and domtest fails audits E2 and E5 until the link carries `record {version, prereg, why}`. Check first that its fingerprints equal the previous link's.
- An `acctDrawCheck` log written by a job with `--procs>1` is in append order, not point order: run `--procs=1` (or one point) to map a failing call to its point.
- The scratch-engine way to trace an accounting failure: copy `index.html`, `harness.js`, `package.json` and `data/` to the scratchpad, add an env-guarded `require('fs').appendFileSync` in the engine where the check fails, and run the job from that folder with the `s93-dry.js` wrapper (ACCT is on only under `acctDrawCheck`).
- GitHub cancels a workflow job that waits 24 hours in the queue. With 20 concurrent jobs, dispatch at most about 400 shards at once. "Re-run failed jobs" reruns only the cancelled or failed jobs and reuses the other shards' artifacts, but only until they expire (3 days).
- Large folders (the automation study, about 1.1 GB) finishing together lose the commit step's push race. Dispatch them in different hours, or rerun the finish job alone.
- The full release folder set is about 6.5 GB. The sparse download of all of them takes about 10 minutes here, and the disk allowance holds it.
- The supply study's row names carry a three-digit index (`ref.042.Achk.full.a0`); `s93-checks.js` strips it.
- A large folder's finish job can lose the push race even when rerun alone if another run finishes in the same minutes: rerun the finish job again (run 272 needed three attempts).
- The session disk allowance fills fast with the results repo: drop folders already tabled from the sparse checkout (`git sparse-checkout set` with a shorter list) before checking out more. A folder on `origin/main` but not on your branch: `git archive origin/main <folder> | tar -x -C <dir>`.
