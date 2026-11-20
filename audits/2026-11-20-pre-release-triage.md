# Outside readings before the release, Nov 20, 2026: Claude's triage

Written in S94. Two packets, built from public files only by `audits/2026-11-20-pre-release/build_packets.py` (the author's name replaced by a role):
- `packet-prereg.md`: the Collectives' lending reading, its sources script with output, and its preregistration.
- `packet-gaps.md`: the release step, the findings-page text (the v5.9 text file), the limits sections of the automation and supply studies, and the inventory `audits/2026-11-20-release-gaps.md`.

Readers (other makers' models; free; readings, never results): ERNIE 5.5 Flash (Baidu, OpenRouter) and Nemotron 3 Ultra (NVIDIA, OpenRouter) and Kimi K3.1 Pro (Moonshot, NVIDIA catalogue) on the gaps; Nemotron 3 Ultra (OpenRouter) and Mistral Large 4 (NVIDIA catalogue) on the preregistration. Replies word for word in the folder beside this file, one subfolder per reader (`status.txt` gives the finish reason). Every point below was checked against the files before it was accepted.

## The preregistration (Nemotron; Mistral stopped before answering)
Accepted, in Amendment 1 of `prereg/2026-11-s94-collectives-lending.md`:
- The pace should limit all new capacity, not only the fund's additions (the rate counts every new establishment): main 'total'.
- The charter share is for electricity customers; applied to gas and water it overstates. Now electricity only (55.35% of household utilities, BEA 2.4.5U, opened for this).
- The fund's outlays were counted as matched output with no source: now unmatched.
- The fund's identity charged write-offs as a second cost after the outlay (Claude's error, found through the reader's question about the identity): fixed.
- Checks added: non-vacuity of the pace limit, a hand check of the charter subsidy, the grant and loan identity.
- Robustness rule 4 now reads only the stricter readings (half the pace; all grants).
- The perpetual-loan convention and the parts of the request the model cannot represent (private start-ups, transport charters, Collective bond issuance) are stated.

Not accepted, with the reason (Amendment 1, item 9):
- "The mature failure rate is cautious": fewer failures leave more capacity and a larger effect, so the young-firm rate is the cautious side for both cost and effect.
- "The corporate rate is favourable": a higher rate returns more to the programme but charges the network more, so no direction is clearly cautious. The all-grants row bounds the case where nothing is repaid.
- Dropping the all-grants, pace × 2 and no-limit rows: they are labelled bounds and cost nothing (GitHub Actions).
- A "money rule" check: the money rule is the project's rule on paid computing, not a model quantity.
- It read 0.814 as a price; it is the utilities' full running cost. The text was unclear, so Amendment 1 item 3 states the subsidy exactly.
- Mistral (stopped after about 45,000 characters of reasoning and no answer; partial reasoning saved, not otherwise used) asked how $18,862 per adult follows from the BEA stock: the sources script now prints it ($5,088,349m over 269.8 million adults, the engine's Census count).

## The gaps before the release (ERNIE, Nemotron and Kimi)
Checked against the live page (`site/round2.js`) as well as the text file the readers saw.

| Reader's point | Checked | Goes to |
|---|---|---|
| Full backing should be in the card headings, not only the footnote | The footnote is required and present; headings are Duke's decision | D33 (readers' advice added) |
| The release must not mix engines; list the studies to rerun; a pre-publish checklist | S93 item 5 had no preregistration yet | S97 |
| Hub figures the audits flagged are still live | The ledger list is open; `drug-policy-reform.html` still shows "$847B" (a health-cost line) | S101 |
| "Poverty barely depends on backing" contradicts the supply study's wage result | The live page has a dated note after it and lists the wage result as unfavourable, but the sentence itself reads unconditional | S98 item 1 |
| The opt-in automation result is missing from the unfavourable list | **Wrong for the live page**: `site/round2.js` lists it | none |
| Opt-in beside every full-coverage card | Partly | S98 item 4 |
| Tax credits and no part-time work bias the yardstick | Ledger I15, open | S100 |
| The simulation page's Hub targets | Confirmed in `index.html` | S96 |
| Inflation figures read as forecasts | No "not a forecast" label on the main inflation figures | S98 item 3 |
| Release data lacks the BLEI visuals' series | Status unknown | S97 checklist |
| The validation "Gini" | Ledger I14 | S99 |
| "1.4 to 7.1 times" has no derivation | Found only in the v5.9 text file, in no report | S98 item 5 |
| The 10,000-adult check covers only hours and the top of wealth | True (overview, question 7) | S98 item 6 |
| Two answers for the model's own backing (0.2-1.9% and 6-17%) | True; different mechanisms and sections | S98 item 2 |
| Nemotron: "adults" in headlines should be "working-age adults" | Ledger I15 says so | S98 item 7 |
| Nemotron: undefined "families in debt"; unnamed 1.8% referent; inflation 18-53 against 40-49; 48 robust against 46 fragile; the financed rows' missing tail; the automation section's two savings measures and its trace's scope; "its ceiling" unexplained | Not checked one by one this session; each is checked on the live page in the step | S98 item 8 |
| Nemotron: charts regenerated at the release; dated notes replaced | Not in the release step | S97 checklist |
| Nemotron: the supply study's capacity costs nothing in the accounts; the Collectives' lending is what could make backing produced | The lending study funds capacity as programme cost (Amendment 1, item 5) | S94 report |
| Kimi: verify the price fix below full backing too; reproduce a sample of archived commands; call the rerun corrective, since the corrected rows were read | Agreed; S92's tables were read before any rerun preregistration | S97 item 2b |
| Kimi: shortages outside the money measures; financed bases differ; 62 readings against 48 curves; "who gains" without ranges; outside-the-labour-force poverty not in the unfavourable list; labour share as a denominator effect; negative baselines; the NEEC criterion's basis; "cautious side" claims; "robust" undefined | Not checked one by one this session | S98 item 8b |
| Kimi: the θ calibration claim has no run record | Ledger I7 open | S101 |
| Kimi: card headings conditional on full backing | Same advice as ERNIE and Nemotron | D33 |
| Acceptable as stated limits: Collectives' lending (in progress), MODEL_SPEC debt, scope, whole-population capacity, no banks, capital income, displaced outcomes by fifth, unsourced health and security effects, unopened non-headline citations, θ (if no calibration claim) | Agreed | stated limits |

Closed by this session's check: ledger I2 (the BLEI page's poverty line is not inverted: Tier 2, "Threshold 30–120 days: BLEI-defined poverty line", matches the simulation's below-30-days measure).
