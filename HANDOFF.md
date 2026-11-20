# Handoff (Nov 20, 2026): S94 part 1 done; pre-release steps added; next S94 part 2

## Step status
**S94 partly done.** Part 1 is done: Claude's reading, sources, preregistration, and Amendment 1 from outside readings, all before any build. Remaining: part 2 (build switch `cl`), part 3 (job, dry run, dispatch), part 4 (tables, report, decision rule 6). Also this session, at Duke's request: a gap audit before the release, with six new pre-release steps (S96-S101). S93 waits on them (D35, confirmed).

## What shipped
- compassionism-simulation [PR 173](https://github.com/BetterToBest/compassionism-simulation/pull/173), merged `821b139`: `dev/reports/s94-collectives-lending-reading.md`, `sources/s94_lending.py` and `sources/s94_lending/` (Census BDS, BEA 3.1ESI and 2.4.5U, Fed credit survey, Reinvestment Fund, APPA, EPA, SIFMA). No engine change.
- research-update [PR 193](https://github.com/BetterToBest/research-update/pull/193), merged `f7841f8`: `prereg/2026-11-s94-collectives-lending.md` (31 rows per environment and horizon; Amendment 1), `audits/2026-11-20-release-gaps.md` (22 items), `audits/2026-11-20-pre-release/` (packets, `ask.py` for NVIDIA or OpenRouter, the replies), `audits/2026-11-20-pre-release-triage.md`, PLAN sections S94 and S96-S101.
- This file and PLAN.md (D33 and D35 answered): research-update PR for `claude/s94-handoff`.

## What was found
- In the main row the PTF share of sales is capped by owned capital: binding in 21-32% of adult-years in Reference and Adverse, and in every year under Stress in the opt-in design. The fund acts there.
- Readers: Nemotron (OpenRouter) answered both packets in minutes; ERNIE (OpenRouter) and Kimi (NVIDIA) answered the gap packet; Mistral (NVIDIA) was stopped with no answer. Amendment 1 took six of Nemotron's points (pace on all new capacity, charters on electricity only, outlays unmatched, no double count of write-offs, new checks, robustness rule on the strict side) and states why the rest were rejected.
- Ledger I2 closed: the BLEI page's poverty line is not inverted.

## In flight
- Nothing running.

## Decisions waiting
- None open. D35 confirmed (the release waits for S94 and S96-S101). D33 answered by Duke Nov 20: the full-backing condition goes on the headline cards (S98 item 9).

## Next step
**S94 part 2** (opus, high): build switch `cl` per the preregistration with Amendment 1. Code anchors are in PLAN.md's S94 section: `paYear`, `ptfsCut`/`poPtfsCut`, `tbAccount`, the premium charge ~6344, row wiring ~8090. Get the outlay into programme cost and unmatched money exactly once. Then `clUnitSuite`, the guard test, and an amendment naming the engine commit. Attach compassionism-simulation (push). S96-S101 can run in any order after it, or between its parts. S96, S98, S99 and S101 are sonnet steps.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.


## Pitfalls
- `expectedHeadSha` in a merge call must be the exact 40-character head; take it from `git ls-remote origin refs/heads/<branch>`, never guess the tail.
- BLS refuses direct requests and its API key's daily quota is shared: fetch BLS files through the fetch tool (it saves binaries in `tool-results/`), then parse them with `openpyxl`.
- The `oh` rows' no-programme runs are shared by both-run settings (`none.<key>` rows in `s85.js`): pair each programme row with the `none` row its `rowSpec` names, not with `none.off`.
- `/end-session` cannot be started by Claude (the Skill tool refuses it); Duke types it. Land PRs as you go so little is left for it.
- McKinsey, Goldman Sachs, OECD and Autonomy refuse automated fetches; open a paper's own PDF or a paper that quotes it, and label a quoted figure as context only. PDFs the fetch tool saves can be read with `pdftotext`.
- The GitHub tools failed to connect at session start; a ToolSearch for them reconnected.
- The Hub is cloned read-only at `/home/user/bettertobest/research-hub` for reading its papers (S95 needs it attached with push).
- compassionism-simulation has auto-merge off, and its CI queues behind running study shards. Don't wait: leave the PR open and say so here.
- After adding tests: `node harness.js unit --write-counts`. domtest needs `npm install` in a fresh clone (jsdom).
- This clone's `origin/main` can be stale at session start. Run `git fetch origin main` before branching.
- compassionism-sim-results is large: clone with `--filter=blob:none --no-checkout`, then `git sparse-checkout set --no-cone` on the folders you need.
- An NVIDIA reasoning model can spend its whole `max_tokens` on reasoning and return no answer: give it 40,000 for a long packet.
- `s85_tables.py` takes about 25 minutes for six folders: run it in the background.
- `mfChk` is not 0 on flat-contribution main rows: never a pass/fail check there.
- Each push to a PR branch queues new CI runs; cancel the stale ones (runners are shared with study shards).
- OpenRouter's free tier (`openrouter.ai`, ids ending `:free` only; 50 free-model requests a day; free providers may keep prompts, so send only public text, with the author's name turned into a role) is a second route for outside readings: `audits/2026-11-20-openrouter-setup.md`. Google's Gemma was rate-limited upstream (429, a shared pool) on every try; Nemotron on OpenRouter answers. `audits/openrouter-2026-11-20-s85-part4/ask.py` sends a packet and saves the reply.
- A `SHA256SUMS` made with `ls | xargs sha256sum > SHA256SUMS` lists itself and cannot match: leave it out (`ls | grep -v '^SHA256SUMS$'`), then `sha256sum -c`.
- The page's figures are read from `data/studies/*.json` by `site/round2.js` (`show`, `find`, `snum`; no figure typed there); the supply study's tool `dev/tools/s82_page_data.py` is the pattern. The report's backing ranges (5-18%, 3-8%, 18-71 points a year) are over every non-floor backing row (main readings and variants); the 72 main-reading rows alone give 6-17%.
- The results clone's sparse checkout needs `s90-sale-*-b8ccd8d` (check 1) as well as `s85-*` and `s85sec-*`; the tables tool took about 12 minutes for six folders this time, the trace tool about 2.
- `node dev/tools/check_round2.js` (every printed number on the v5.9 findings section is tied to a row of its file) is not run by CI: run it by hand after editing `site/round2.js`. A share printed as a percent must be stored as a percent in the data file, or the check fails.
- PR 172 was merged after PR 171 landed, on checks that ran before it; wording only, so accepted.
- The GitHub tools disconnect after a worker restart; a ToolSearch for them reconnects.

- NVIDIA's Mistral Large 4 and Kimi K3.1 Pro stream reasoning very slowly: Kimi took most of an hour, and Mistral gave no answer after about 45,000 characters. Nemotron 3 Ultra on OpenRouter (`:free`) answers a 30,000-character packet in a few minutes: send to it first.
- Hiding in-flight files from git (`git update-index --assume-unchanged`) is refused, rightly. Commit a reader's files when it finishes, or stop it.
- The outside readers saw the v5.9 findings text file (`dev/reports/s64-findings-page-text.md`), not the live page (`site/round2.js`). Check every claim on the live page first: several are already fixed there.
- Census BDS CSVs (www2.census.gov) and BEA XLSX tables (apps.bea.gov) download with curl. The Census API needs a key. BLS still refuses curl (the fetch tool reads its .txt tables).
- Check `date -u` and the process's elapsed time before deciding a job is stuck. This session misjudged elapsed time twice.
