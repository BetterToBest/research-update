# Handoff (Nov 28, 2026): S106 part 1 done; the recovered draft is verified and waits for Duke to publish

## Step status
**S106 (the results home), parts 1-2 done; the publish click is Duke's.** The Zenodo draft 24615619 (58 files) was downloaded and checked: every archive equals its listed SHA-256 and Zenodo's MD5, and every results folder inside passes its own `SHA256SUMS`. It holds 55 results folders (47 of the 60 release-engine rerun folders) **and `runner.tar.gz`: the job scripts were recovered after all** (the Nov 27 note saying they were not was wrong). Claude set the draft's metadata (CC BY 4.0, creator Duke Johnson, links to the repositories) and uploaded `README.md` and `results-manifest.json`. **Publishing was refused by the permission classifier, so Duke presses Publish** on the draft at zenodo.org (Upload, the draft, "Publish"; the DOI is already reserved: 10.5281/zenodo.24615619). Inventory, the 13 missing release folders and the sessions to reopen: `audits/2026-11-28-s106-inventory.md`.
Tool and manifest: compassionism-simulation PR 191 (`dev/tools/deposit.py`, `data/results-manifest.json`, a CI check that every cited folder is deposited or listed as not deposited). OSF read access checked (account answers); the OSF copy waits for the publish. Kaggle: a read request answered 200 (empty list), write untested.

## Decisions (ledger H)
- **Answered Nov 27:** D39, Zenodo plus an OSF copy; D41, GitLab group `BetterToBest-group` (ID 148851118).
- **Open:** D40, where big studies run (ledger I22, candidates in the Nov 27 record; Kaggle added as a candidate). S107 waits.
- **New ask (Duke):** press Publish on Zenodo draft 24615619 (it is permanent; the files are verified). Then say so, and S106 part 3 (OSF copy, manifest status, DOI in the reports) runs.
- Carried: the D34 record (v5.9.23) and the below-full-backing swing measure (S93 part 3), as before.

## Next step
- **S108** (opus, high): the job scripts are back (`runner.tar.gz` in the record; unpack beside the engine). Check each on seeds 1-5 against the published tables and fix what no longer runs, instead of rebuilding. Free; the session machine.
- **S106 part 3** after the publish: OSF copy, status in the manifest, then S110 (links to DOIs).
- **S102** (sonnet, medium) can run any time. **S109** (GitLab mirrors) can start. **S107** waits for D40. **S105** (Duke): send the ticket.

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
- `s93_page_check.js` pairs printed figures by file, row label and column, not by position: lists that print a row only when it meets a rule, and files that hold such rows (the lending study's cost per point), differ between the published and the release data.
- A scratch Node script outside the repo needs `NODE_PATH=<repo>/node_modules` to find jsdom.
- A new results folder in the sparse clone must be added to the sparse set (`git sparse-checkout add <folder>`) before `git add`.
- The Hub's simulation figures are generated blocks (`<!-- FIG:name -->`, written by `research-hub/tools/build_figures.py` from a snapshot of a release's data files); never edit them by hand. Tag `v5.9.23` is the engine commit, which holds the *published* data: fetch the snapshot from PR 188's merge commit with `--release v5.9.23`, and create or move no tag.
- In the release tables a negative change to a poverty effect is a larger cut. Both outside readers misread it (they read "−0.26" on an effect of −20.9 as a worsening): say so at the top of any packet that holds those tables.
- `s93_page_check.js` pairs only figures printed in both renders; a cell the published page did not print (the wage reading at 40 years) appears in its section 7, not in the sign-change list.
- After merging a results PR, the local `origin/main` of the shallow results clone is stale: `git fetch --depth=1 origin main` before branching from it.
- A remote branch delete through the proxy can fail ("remote end hung up"); the stray branch `claude/s93-part4-continued` in research-update is this session's and points at a merged commit.
- compassionism-sim-results was disabled by GitHub on or before Nov 26 (a terms-of-service matter; no archive copy). Do not try to reach it, and do not wait for it: rebuild what a step needs (S108) and deposit results (S106). The pitfalls above about the `run-study` workflow, shards on Actions and the sparse results clone are history: **never run a study on GitHub Actions again** (CLAUDE.md).
- A public repository can be cloned anonymously through the git proxy without attaching it (`add_repo` with access "read" says so; `GIT_LFS_SKIP_SMUDGE=1`). Pushing still needs access "push".
- An old engine in a scratch folder (`git archive COMMIT index.html harness.js package.json data dev/tools`) runs its own job scripts, but `runManifest()` has no commit there. Table tools that print it fail; `audits/s103/setcommit.py SHA FILES` writes it in.
- The S103 patches (`audits/s103/patch.py`, `patch_esp.py`, `patch_reset.py`) are reporting-only switches; with every switch off the engine reproduced the price-rule study's tables byte for byte. Apply them to a scratch copy, never to a checkout.
- Before `df9cfbe` (Nov 14) the mechanisms' per-run state carried over between runs in one process. A row's year-0 reads (PTF's capacity test reads `PDS`) can depend on the run before it, even with the store key fixed. Use `S103_RESET=1` when comparing.
- A shell wait loop `while pgrep -f 'PATTERN'` inside `bash -c "...PATTERN..."` matches itself and never ends. Wait on a pid (`kill -0 PID`) instead.
- The government study's published `tables.md` includes the frontier without the weighted tail, which only the current `dev/tools/s72_table.js` prints (the engines' own copies do not). The bargaining study's published tables renamed twelve row labels after its engine.
