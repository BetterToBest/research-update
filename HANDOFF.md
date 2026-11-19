# Handoff (Nov 19, 2026): S85 part 1 done (output per hour and automation: reading, sources, preregistration)

## Step status
**S85 partly done.** Part 1 is done: Claude's reading of the design, the sources opened, the preregistration with Amendment 1, and an outside reading, all before any build or run. **Part 2 is next:** open the sources Amendment 1 item 5 names and record them in Amendment 2, build row option `oh` behind its switch (off = identical), dry run, job, dispatch on Actions. Part 3: checks, tables, report, findings-page text.

## What shipped
- compassionism-simulation [PR 166](https://github.com/BetterToBest/compassionism-simulation/pull/166) (**open**: its CI was still running at session end; auto-merge is off). It holds `dev/reports/s85-output-reading.md`, `sources/s85_output.md`, `sources/s85_hours.py` with `sources/s85_owid/us_hours.csv`, and the engine HANDOFF. No engine change. **Merge it once green** (merge commit).
- research-update [PR 185](https://github.com/BetterToBest/research-update/pull/185) (this PR): `prereg/2026-11-s85-output-per-hour.md` (committed `bd7905f` before any build; Amendment 1 items 1-8), `audits/2026-11-19-s85-prereg-reading-nemotron.md` with the packet and reply in `audits/nvidia-2026-11-19-s85/`, PLAN.md (S85 notes; new steps S94 and S95), this handoff.
- Earlier this session: compassionism-simulation PR 165 (S92's notes), merged `353662e`.

## What was found
- Pencavel (2015), which the Hub's corporate transformation paper cites for falling output per hour at 35-40 hours, finds output proportional to hours below 49 a week. So shorter weeks alone bring no gain per hour. The Hub correction note is S95.
- Since 1950, US hours per worker fell 0.17% a year while output per hour grew about 2.2%: about 8% of the gain was taken as shorter hours.
- Duke's 50% and 70% displacement at 20 years need output per remaining hour to grow 3.5% and 6.2% a year above trend. That is beyond every forecast opened (0.1 points a year from Acemoglu and Penn Wharton; 1.5 for a decade from Goldman Sachs, as Acemoglu quotes it), so they are labelled stress readings.
- The outside reading found three choices that favoured the programme without a source (hours behind conversions, the gain on programme work, and a decade's forecast run for 20-40 years). All three were fixed in Amendment 1 before any build.
- Duke asked "what about services?": m counts goods and services alike, plus work that replaces a purchase (Amendment 1 item 8).

## Sources Duke offered to collect (pages that refused automated fetches; paste the passages into the part 2 session)
- McKinsey 2023, generative AI: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier (the share of work activities automatable, the midpoint year, the 60-70% technical potential, the productivity ranges).
- McKinsey 2017, jobs lost and gained: https://www.mckinsey.com/featured-insights/future-of-work/jobs-lost-jobs-gained-what-the-future-of-work-will-mean-for-jobs-skills-and-wages (share of hours automatable by 2030; US figures).
- Goldman Sachs 2023: https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent (the productivity boost and its years; occupations exposed).
- UK four-day week pilot: https://autonomy.work/portfolio/uk4dwpilotresults/ (companies, hours cut, revenue, how many kept it).
- Rosenthal and Burke 2020: https://www.taxpolicycenter.org/publications/whos-left-tax-us-taxation-corporations-and-their-shareholders (the share of US corporate equity US households hold). The session tries this one, the Fed's L.223, BLS and BEA itself first.

## In flight
Nothing.

## Decisions waiting
- D33 (the headline cards' headings and the full-backing condition; default: no change).
- D34 (the version of the release that makes the price at the sale the default; default: a v5.9.x patch at the next engine session). S93 waits on it.

## Next step
**S85 part 2** (opus, xhigh). First merge compassionism-simulation PR 166 if it is green.

## Standing rules (permanent: copy this section word for word on every rewrite)
**Reader text carries no internal labels. Write it right the first time; don't wait for the reader-codes check to catch it.** Fixing each failure afterwards has slowed every step that touches a report.
- Reader text: the pages (HTML outside `<code>`/`<pre>`, plus title/alt/aria-label), prose in `site/*.js`, the JSON text fields the pages show, and Markdown outside code. In compassionism-simulation that includes README, CHANGELOG, REPRODUCE, ODD, ECONOMIST-REVIEW and **every `dev/reports/*.md`**, so a new report is checked like a page. The Hub and the root site are checked too.
- Never in reader text: step and ledger codes (S90, D33, N-S72, H-S29, pairs like S47/S7), "session 12", "part M", job ids (X3), "round 2", "release 1/2", "C2.2" (write "the full-coverage design" and name NEEC's criterion once), and row ids, key or option names in plain prose.
- Name things by subject: "the report on the private price at the sale", not "the S90 report"; "the preregistered rerun", not "S92". A file path, option or command goes in backticks or `<code>`, which is where a reader looks something up, so it is allowed there. Step codes belong in DECISIONS.md, PLAN.md, prereg/, audits/ and commit messages, which readers don't open.
- Before committing an edit to any reader file, run the check on it: `python3 dev/tools/reader_codes.py --list` (compassionism-simulation), or `--root ../research-hub --preset hub` / `--root ../bettertobest.github.io --preset root`. Then `--check`, which is what CI (domtest Phase 17) runs.
- `dev/tools/reader_codes_allow.txt` is only for labels that are not ours (a formula symbol such as D0, a report's own numbering), each with a reason. Never use it to let a step code through.

## Pitfalls
- `/end-session` cannot be started by Claude (the Skill tool refuses it); Duke types it. Land PRs as you go so little is left for it.
- McKinsey, Goldman Sachs, OECD and Autonomy refuse automated fetches; open a paper's own PDF or a paper that quotes it, and label a quoted figure as context only. PDFs the fetch tool saves can be read with `pdftotext`.
- The GitHub tools failed to connect at session start; a ToolSearch for them reconnected.
- The Hub is cloned read-only at `/home/user/bettertobest/research-hub` for reading its papers (S95 needs it attached with push).
- compassionism-simulation has auto-merge off, and its CI queues behind running study shards. Don't wait: leave the PR open and say so here.
- After adding tests: `node harness.js unit --write-counts`. domtest needs `npm install` in a fresh clone (jsdom).
- This clone's `origin/main` can be stale at session start. Run `git fetch origin main` before branching.
- compassionism-sim-results is large: clone with `--filter=blob:none --no-checkout`, then `git sparse-checkout set --no-cone` on the folders you need.
