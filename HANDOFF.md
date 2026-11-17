# Handoff (Nov 17, 2026): S82 part 1 (v6 readings preregistered and built) and S87 part 1 (money and metals page), run side by side

## Step status
**S82 partly done** (another session). Part 1 done: the preregistration (with Amendment 1), and the switches built and off by default. Part 2 is left: sources for the headroom values (Amendment 2), the keep-as-savings reading (`fs`), `runner/jobs/s82.js` in compassionism-sim-results, the 2-seed dry run, then the batch on GitHub Actions (about 108 core-hours, free). Part 3: the report and the findings-page text.
**S87 partly done.** Done: items 1-3 of the step and the case for and against metal backing. Left: items 4-8 (crypto; offshore money and corporate tax; tuition and student debt against bankruptcy and buyouts; media ownership; the table of other changes). The page's "Still being checked" section lists them.

## What shipped
- research-update PR 170 (S82): `prereg/2026-11-s82-v6-supply-indexing.md`, PLAN.md, `audits/nvidia-2026-11-17-s82/`.
- compassionism-simulation PR 151 (S82; v5.9.16, merged `2120662`): price options `sl`, `wc` and `bl`, `s82UnitSuite`, `dev/reports/s82-supply-reading.md`.
- research-hub PR 35 (S87, merged `4701da9`): the new page `us-money-history.html`. It has gold and silver since 1791 with 11 laws marked (each checked against the statute or order); a house, college, the minimum wage, the CPI basket, food, shelter and medical prices in dollars, 2025 dollars, gold, silver or minimum-wage hours; the minimum wage in silver since 1938, in coin to 1964 and at market; and the case for and against metal backing, with Duke's position stated. Also `tools/fetch_s87_sources.sh`, `tools/build_s87_money.py`, `data/s87/` (SOURCES.md with checksums; CSVs) and `data/s87-money-history.json`. Linked from `us-policy-eras.html` and the wiki.
- bettertobest.github.io PR 7 (S87, merged `36fda47`): the page added to ai-index.json, research-index.json, llms.txt and sitemap.xml.
- research-update (S87): `audits/2026-11-17-s87-reading.md` (the outside reading and what was done with it), `audits/s87-reading/` (packet, request, reply, script), and PLAN.md's S87 row.

## S87 findings worth knowing
- Duke's "about 5 oz of silver a week" matches neither measure for the old wage. From 1938 to 1964 a minimum-wage week held 8.0 to 36.2 oz in coin and bought 20.0 to 44.9 oz at market. Today's $290 week buys 7.2 oz at 2025's average price, and 5 oz if silver is near $58. The page says this neutrally.
- The 1938 week ($11 = 25¢ × 44 h) held 7.96 oz in coin (7.87 at the dealers' 0.715) and bought 25.3 oz at market.

## In flight
- None.

## Decisions waiting
- D33 (do the headline cards' headings name the full-backing condition? default: no change).

## Next step
**S82 part 2** (opus, xhigh): open the sources named in the preregistration, section A, and convert them to shares of the no-programme needs consumption, not of sector output (Amendment 1). Then fix `SL_SRC`, build `fs` with its accounts or drop its rows, write `s82.js`, run the dry run, write Amendment 2 and dispatch the batch. **S87 part 2** (opus, high) can run beside it: items 4-8, one opened source per claim, a new outside reading before publishing, and the page's "Still being checked" section replaced.

## Pitfalls
- S82: the supply limit's excess is measured against the needs baskets, so `v` and `m` must be shares of needs consumption. The realised cut is within about 5% of the target; report `slCutSh` beside `slR*`.
- Several sites refuse scripted downloads: BLS, DOL, the US Mint, EPI, SEC and loc.gov. Do not get round them with a browser user-agent (auto mode refuses it, rightly). Use WebFetch for a page's text, govinfo.gov for statutes (`/content/pkg/STATUTE-<vol>/pdf/STATUTE-<vol>-Pg<page>.pdf`), MeasuringWorth for the CPI, and the American Presidency Project for executive orders. FRED timed out.
- NVIDIA's catalogue: Nemotron Ultra answered S87's reading in about 200 s (a first attempt came back empty), and returned 503 twice for S82. Node's `fetch` ignores the proxy, so send with curl (`audits/s87-reading/read_s87.js` writes `request.json`).
- The outside reading flagged one figure that was right (the 2023 silver price); check each point against the source before acting.
- In the Hub repository, commit trailers carry no model name (its CLAUDE.md).
