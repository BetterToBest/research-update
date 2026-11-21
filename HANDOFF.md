# Handoff (Nov 21, 2026): S93 part 1 done (the release engine)

## Step status
**S93 part 1 done:** the release engine v5.9.22 is built and proved; its PR merges once checks pass (see "In flight"). Duke adopted pay by household type and the care credit (D36), so the release main row carries both. Next: S93 part 2, the dry runs and the dispatch of every rerun.

## What shipped
- research-update PR 211: Amendment 3 of `prereg/2026-11-s90-private-price-at-sale.md` (D36 adopted; version v5.9.22 by D34's default; the automation and lending studies rerun in full; D2/D3 against the yardstick study's `both` rows; F1 split) and Amendment 4 (a defect found by proof A3, its fix and reach), both committed before the engine change; PLAN notes; S103 added.
- compassionism-simulation PR 182 (branch `claude/s93-release-engine`): `SURP_DEFAULTS.vAt 'sale'` (other values refused); `r2FreezePair` adds `eh {}` and `sn.cdc true` in both runs (`r2FreezePair(P, d, true)` = the v5.9 row); `rowKeyS93` keys the stored no-programme supply path on the settings it missed; guard reference rewritten by design (previous kept in `dev/runs/guard/v5.9.21/`, `guard_test.js --lag --ref=...` reproduces it); `dev/tools/s93_release_proof.js` (A2, A3); a lineage link marked as keeping the v5.6 panels as the record (domtest prints it); one unit test (424); release notes; dated notes on the yardstick report and findings section.
- compassionism-sim-results PR 70 (branch `claude/s93-release-jobs`): `s100.js` builds its rows from the v5.9 row, for its rerun.
- **Found:** the engine's stored no-programme supply path ignored pay by household type, the price rule's settings, bargaining, the government account and PTF running costs. The yardstick study's `eh` and `both` readings took the path of the rows before them (its decision-rule rows did not, so D36 stands); the study is rerun. Record studies: audit in S103.

## In flight
- compassionism-simulation PR 182: CI (about 12 minutes) was running at the session's end. If green, merge it (expectedHeadSha from `git ls-remote`); the merge commit is **the release engine** (its full hash goes in every rerun's dispatch and in Amendment 3's terms). If red, fix on the branch.
- compassionism-sim-results PR 70: merge once checks pass (no study runs from it).

## Decisions waiting
- None open. D34 (version): v5.9.22 by default (Duke held the release on Nov 19 without naming a number; renaming is one `set_version.py` call if he prefers another). D36: adopted.

## Next step
S93 part 2 (opus, high): dry runs on the release engine (seeds 1-2, every row and cell, `acctDrawCheck` and each job's own checks, the two readings beside every switch), then dispatch every rerun (list and shard counts in PLAN's S93 part 2 note), record the run numbers, end. Do not read any figure before checks D1-D5.

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
