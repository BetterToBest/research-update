# Handoff (Nov 18, 2026): S87 part 2 (money history: crypto to other changes)

## Step status
**S87 done.** Part 2 added items 4-8 to the Hub page `us-money-history.html`, replacing its "Still being checked" section.
**S82 partly done** (unchanged since Nov 17): part 2b and part 3 are left (see Next step).

## What shipped
- research-hub PR 37 (merged `4082912`): five sections (Bitcoin and other crypto; offshore money and corporate tax; college costs and student debt; who owns the news; other changes), with 2 charts and 5 tables. New `tools/build_s87_part2.py`, `tools/fetch_s87_part2.sh`, `data/s87-part2.json`, `data/s87/part2-*.csv`; `data/s87/SOURCES.md` part 2 (54 files with checksums, plus the sources not opened). Wiki card and policy-eras link updated. Part 1's build and data unchanged.
- bettertobest.github.io PR 8 (merged `3f4ae67`): ai-index.json, research-index.json, llms.txt, sitemap.
- research-update: `audits/2026-11-18-s87-part2-reading.md` and `audits/s87-part2-reading/` (packet, request, reply, script); PLAN.md S87 row and section.

## What the page says (plain words)
Bitcoin's swings, 2015-2025: 59% a year against gold 11%, shares 15% and the dollar 4%. Corporate income tax was 27.6% of federal receipts in the 1950s and 8.2% in 2018-2025; against profits it went from about 40% to about 11%. Student loans have been dischargeable only on "undue hardship" since 1998 (federal) and 2005 (qualifying private loans). Every claim comes from an opened source; where a source refused (the Justice Department, EPI, the full Medill report, the Ayash and Rastad paper), the page uses an opened report and names it, or leaves the claim out (Bagdikian's media counts; small firms' actual tax rate).

## Outside reading
Nemotron Ultra (NVIDIA catalogue) found no factual errors. Of its five presentation points, four led to changes: the July 1 minimum-wage rule stated; volatility defined as log changes; the monthly and daily falls labelled; the fixed $7.25 column labelled. The IC3 figures it could not confirm were already from the opened report. With a 6,000-token limit it returned no text (all spent on reasoning); 20,000 worked.

## In flight
- None.

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change).

## Next step
**S82 part 2b** (opus, xhigh). Do in this order:
1. Build study option `s82` (reporting only): the real BU and real wage at year 20; the no-programme run's unmet need by fifth; the weighted share below 30 days; wages over factor income; wealth poverty at half the same seed's no-programme median, for both runs (the programme row needs the no-programme median, for example from the supply-path run); the weights comment near `index.html` 4237. Add `s82: true` to the job's study options.
2. Give `s70-screen.js` an `str` environment and a tail flag for its financed block, with a dated note in the preregistration on the two bases not read with the tail.
3. Get the full outside reading (Mistral with streaming).
4. Run the dry run (`s82.js --dry --seeds=1-2 --procs=4`) and record its timings and dispatch lines in Amendment 2.
5. Dispatch six runs of `run-study` (study `s82-v6-<env>-<years>`, job `s82.js`) and the screen.

## Pitfalls
- Sites that refuse scripted reads: justice.gov, epi.org, bls.gov, sec.gov, fcc.gov, congress.gov (WebFetch reads BLS; not DOJ or EPI). Do not route around a refusal through an archive copy; use another opened source and say so.
- FRED's `fredgraph.csv` returns only the last year of SP500 (licensing) and TDSP from 2005; add `&cosd=...` for long series. Sending a browser user-agent to FRED timed out; the plain request worked.
- openpyxl's read-only mode returned no rows for the OMB tables; open them normally.
- `domtest.js` takes over 15 minutes locally (S82 note); CI's guard job takes about 2 minutes.
