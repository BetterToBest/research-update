# S85: an outside reading of the preregistration, before the build (Nov 19, 2026)

**What was sent.** `audits/nvidia-2026-11-19-s85/build_packet.py` builds the packet (47,252 characters). It holds the reviewer's instructions (seven headings), the preregistration as committed (`bd7905f`), Claude's reading of the design and the sources note (compassionism-simulation `cf687db`), and MODEL_SPEC sections 6.1, 6.5, 6.7, 6.11, 6.12 and 12.1.

**Model.** The model list was read again on Nov 19 (32 models). Nemotron 3 Ultra (`nvidia/nemotron-3-ultra-550b-a55b`, temperature 0.3, max_tokens 16,000) finished with `finish_reason` "stop" and 28,895 characters of answer: `nvidia-2026-11-19-s85/nemotron/reply_content.md` (word for word), `reply_reasoning.md`, `stream.txt`.

It is a reading, not a result. Each point was checked against the preregistration, the code or an opened source before anything changed. The changes are the preregistration's Amendment 1, dated before any build.

## Triage

| # | The reading's point | Checked against | Verdict | What changes |
|---|---|---|---|---|
| 1 | The hours behind conversions (H^C) are imputed from money, not observed hours, and raise the backed share | the engine: conversions carry no hours; only project hours are hours (`PROJ`) | **Confirmed** as an assumption that favours the programme (the reviewer's "BU spent at face value" is a misreading: H^C was the participants' conversions of expired BU) | Amendment 1, item 1: main reading counts project hours only; the conversions' hours become a labelled reading, and never include ESP conversions or payroll BU |
| 2 | The forecast gain G_t applied to programme work and PTF capital is unsourced | the sources: the gains are economy-wide or one task (customer support) | **Confirmed** | Amendment 1, item 1: no gain on programme output in the main reading; a labelled reading applies it |
| 3 | Goldman Sachs' 1.5 points a year is a decade's boost, used here for 20 or 40 years | the quote as read in Acemoglu: "over a 10-year period" | **Confirmed** | Amendment 1, item 2: the high reading is a decade of 1.5 points (level 1.161) reached along the path and held; the low reading follows Penn Wharton's published levels |
| 4 | Holm within each reading lets a favourable cell be picked from many | the analysis section | **Confirmed** for the headline offsets | Amendment 1, item 3: Holm across the four outcomes and the eight displacement cells of block A in each environment and horizon; headlines come only from blocks A and F |
| 5 | Q4 has no decision rule | decision rule 5 covers only headlines at full backing | **Confirmed** | Amendment 1, item 4: three categories for each produced-backing row, and the share of work sold in shops that would be needed to reach the break-even |
| 6 | The source for `own` (and the others) is not pre-specified | "To open before the dry run" | **Confirmed** | Amendment 1, item 5: each source named now, with its fallback |
| 7 | PTF capital's yield capped at 0.32 is too low for essentials | BEA's own definition: output per dollar of capital credits capital with labour's part too | **Partly**: the direction is wrong for the main reading. Full output per dollar would count the labour the capital needs, which programme hours do not supply | Amendment 1, item 1: capital's share of output per dollar of capital (main); the full output per dollar as a reading |
| 8 | The 1.8/3.5/6.2% consistency figures use no added gain; rows run with one | the reading note: "above the usual growth", output kept | Agreed (clarify) | Amendment 1, item 6: the figures are the floor; each row reports its own |
| 9 | The IMF's "negatively affected" is not displacement | the IMF quote | Agreed | Amendment 1, item 6: the 30% anchor is loose; it covers lower pay and fewer hours as well as lost jobs |
| 10 | Pencavel's wartime munitions sample may not carry to today's service work | the paper | Agreed as a limit | Amendment 1, item 7 (limit); the design's maintained take-home reading is the counterpoint |
| 11 | No investment response to the dividend; one pass-through for every wage level; contract pay values an hour below the worker's own wage | the design | Agreed as limits, with directions | Amendment 1, item 7 |
| 12 | The dividend double-counts the gain, with no adding-up | check 4: Σ wages after B-C + Div = Σ E⁰ × G | Not confirmed: check 4 is the adding-up on the affected wage bill | Amendment 1, item 6: a reported diagnostic of the price rule's cash income with and without displacement |
| 13 | Replace cash income in the price rule with real output | MODEL_SPEC 6.12; every published figure uses cash income | Not adopted: it would change every published figure, and it is not this study's question | none (the diagnostic in item 12) |
| 14 | Essentials bought with BU should count as matched output | MODEL_SPEC 6.12: matched output is new output; BU spent on existing supply is the unmatched demand the rule prices | Not confirmed | none |
| 15 | Fix `m` to one derived value, no sweep | the design: no figure for the share of collective work sold in shops | Not adopted (no basis for one value) | Amendment 1, item 4: the share needed to reach the break-even is reported instead |
| 16 | `pw` 1 exceeds the production workers' range | Stansbury and Summers: 0.7-1 for the average and median worker | Kept as the published bound | none (a limit on pass-through by wage level, item 11) |
| 17 | `own` 1 favours the programme | `own` acts in both runs; leaving part of the dividend out lowers cash income and so raises programme inflation | Agreed in direction for inflation | Amendment 1, item 5: the main value is the sourced one; 0.5 and 1 are bounds |
