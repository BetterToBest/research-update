# Independent Review of the Compassionism Simulation Report

## 1. Does every statement in the report follow from the tables?

### Overstatements / Misquotes / Understatements

| Report sentence | Table value | Correct figure / issue |
|---|---|---|
| **Section 2, point 2**: "It offsets 80-96% of the rise in basket poverty with lost jobs and 94-100% with shorter hours, 59-93% of the rise in yearly wealth poverty, 97-100% of the rise in adult-years below 30 days of basic living, and 13-40% of the fall in median real wealth." | Section 4 table: Full coverage, lost jobs, basket poverty: 80-96% ✓; shorter hours: 94-100% ✓; yearly wealth poverty: 59-87% (not 59-93%); below 30 days: 97-102% (not 97-100%); median real wealth weighted: 14-24% (not 13-40%) | **Yearly wealth poverty max is 87%, not 93%. Below-30-days max is 102%, not 100%. Median real wealth range is 14-24% (weighted) and 13-22% (unweighted), not 13-40%.** |
| **Section 2, point 2**: "Every one of the 144 tests at 20 years is significant: 136 'offsets in part' and 8 'offsets fully'." | Section 4 category table: Full coverage Reference 20y: PPPPPF PPPPPF PPPPPF PPPPPP FPPPPF FPPPPF PPPPPP PPPPPP = 4F + 32P = 36 cells per environment. Three environments = 108 cells. But 6 outcomes × 8 cells × 3 env = 144 tests. Category table shows only Reference, Adverse, Stress for full coverage 20y. Reference: 4F+32P=36; Adverse: "PPPPPF then PPPPPP in every other cell" = 1F+7P per 8 cells? Actually "PPPPPF then PPPPPP in every other cell" is ambiguous. Stress: "PPPPPP in every cell" = 0F+8P per 8 cells? Need to count properly. | **Cannot verify 136/8 from given category table shorthand. The claim may be wrong.** |
| **Section 2, point 3**: "Of its 144 tests at 20 years, 98 offset in part, 31 do not offset and 15 worsen (at 40 years: 80, 32 and 32)." | Section 4 category table for Opt-in 20y: Reference: PPPNNP PPPPPP PNPPPP WNPPPP PPPPPP PPPPPP PPPPPP PPPPPP. Let's count: 6 outcomes × 8 cells = 48 per env. Reference: row1 (basket poverty): PPPNNP = 4P,2N; row2 (wealth poverty yearly): PPPPPP = 6P; row3 (wealth poverty last): PNPPPP = 1P,1N,4P? Wait 6 letters for 6 outcomes? Actually each row in category table = one outcome across 8 cells (4 lost jobs + 4 shorter hours). So 6 rows × 8 cells = 48 per environment. Reference opt-in: row1: P P P N N P (6 cells? but should be 8). The shorthand is compressed. | **Cannot verify counts from compressed notation. Claim may be inaccurate.** |
| **Section 2, point 4**: "programme inflation is 48-69 points a year at 20 years." | Block E tables: Ref c22 (full coverage) inflation ranges: m0.25.glow.D0 55.0 to m1.ghigh.D0 48.0. So 48-63, not 48-69. Adverse c22: 54-69. Stress c22: 53-69. Opt-in Ref rel: 36-44. **48-69 only covers full coverage across environments, not "at 20 years" generally.** | **Should say: "48-69 points in full coverage across environments; 18-50 in opt-in."** |
| **Section 2, point 4**: "the programme's own work matches 5-18% of the payout in this design" | Block E: Full coverage produced share: m0.25.glow.D0 5.9% to m1.ghigh.D0 17.1% (and vk.m1.ghigh.D0 19.3%). So 5-18% is correct for main reading (m 0.25-1), but vk reaches 19%. | **Acceptable if "main reading" implied, but vk row shows 19%.** |
| **Section 2, point 5**: "At 50% lost jobs, an adult who was in paid work at the start has on average 494 more unpaid hours a year over the run (1,032 in year 20)." | Section 9 table: "Freed hours" at 50% lost jobs = 494. Year 20 not shown in table. | **Year-20 figure 1,032 not in provided tables; cannot verify.** |
| **Section 2, point 5**: "With no programme, 76-81% of those hours fall in households below their cost of living." | Section 9 table: No programme Reference: Secure 117, Insecure 377. Insecure share = 377/494 = 76.3%. Stress: 401/494 = 81.2%. So 76-81% correct. | ✓ |
| **Section 2, point 5**: "With full coverage, 4-10% do; opt-in, 55-77%." | Section 9: Full coverage Reference: 21/494 = 4.3%; Stress: 47/494 = 9.5%. Opt-in Reference: 272/494 = 55.1%; Stress: 379/494 = 76.7%. | ✓ |
| **Section 2, point 6**: "removes displacement's cost to median wealth in the programme run (a change of $18,746 and $30,874 at 30% and 50%, Reference, full coverage)." | Section 10: "−$431 and −$649, against $18,315 and $30,225 without it". The change (offset) = cost_N - cost_P. cost_N at D0.3 = $18,315; cost_P = $431; offset = $17,884. At D0.5: cost_N = $30,225; cost_P = $649; offset = $29,576. Report says $18,746 and $30,874. | **Figures don't match. Correct offsets: ~$17,884 and ~$29,576.** |
| **Section 4**: "By year 20, basket poverty ... is 2.0, 5.6, 9.0 and 12.6 points higher at 10%, 30%, 50% and 70% lost jobs (Reference; 1.6-9.6 in Adverse and Stress)" | Block A Reference full coverage D0.1 jobs fgt0PY cost_N = 2.05; D0.3 = 5.56; D0.5 = 8.98; D0.7 = 12.64. Report rounds to 2.0, 5.6, 9.0, 12.6. Adverse D0.1=1.60, D0.7=9.60. Stress same as Adverse. | ✓ (rounding acceptable) |
| **Section 4**: "median real wealth is $7,158 to $48,326 lower" | Block A: wtMedE cost_N: D0.1=7158, D0.7=48326. | ✓ |
| **Section 4**: "At 40 years basket poverty rises 3.1 to 20.3 points in Reference." | Not in condensed tables (only 20y shown). Section 12 says "At 50% lost jobs, basket poverty rises 9.4 points with no programme (Reference), against 14.1 when it is reached by year 20." So 40y D0.5 = 9.4. D0.7 would be higher. 20.3 plausible but not verified. | **Not verifiable from provided tables.** |
| **Section 5**: "With no programme, they raise basket poverty about as much as lost jobs (Reference: 9.5 against 9.0 points at 50%)." | Block A: D0.5 hours fgt0PY cost_N = 9.52; D0.5 jobs = 8.98. | ✓ |
| **Section 5**: "The programme offsets more of it: in the full-coverage design 94-100% against 80-96%; opt-in, up to 69% against at most 17%." | Section 4 table: Full coverage shorter hours basket poverty 94-100% ✓; lost jobs 80-96% ✓. Opt-in shorter hours: -3% to 69% (max 69%) ✓; lost jobs: -23% to 17% (max 17%) ✓. | ✓ |
| **Section 5**: "Displacing adults evenly rather than the most exposed first raises the no-programme cost of 50% lost jobs from 9.0 to 10.6 points of basket poverty (Reference)" | Not in condensed tables. Block D includes ord even at D0.5 jobs and hours. Not shown. | **Not verifiable.** |
| **Section 6**: "The high gain (16% more output per hour by year 20, against 2.2%) lowers poverty in both runs, so the programme's cut in basket poverty is 1.2 points smaller at 50% lost jobs (full coverage, Reference) and 1.5 points smaller with no displacement." | Programme effects table: Ref full coverage off (D0 low gain): basket poverty -32.60; jobs.D0.5 (low gain): -41.05; jobs.D0.5 high gain? Not shown. Block B has u 1.5 (high gain) at D0.5 jobs. Not in condensed tables. | **Not verifiable from provided tables.** |
| **Section 6**: "The dividend at 50% lost jobs is 19% of wages" | Section 6 says "ohDiv" reported. Not in condensed tables. | **Not verifiable.** |
| **Section 6**: "the labour share of income falls from 99.6% with no displacement to 84%" | Section 6 says "ohLab" reported. Not in condensed tables. | **Not verifiable.** |
| **Section 6**: "The model's households receive 48% of the dividend within the run (the sourced 54%, less the last year's, which falls after the run)." | Amendment 2 item 6: "The last year's dividend falls after the run and is not paid; ohPaid reports the share paid." 54% * (19/20) ≈ 51.3%, not 48%. | **48% not explained; may be wrong.** |
| **Section 6**: "If they held all of it, the full-coverage programme's effect on median real wealth would be $902 larger." | Not in tables. | **Not verifiable.** |
| **Section 6**: "With no programme, the top 1% share of wealth rises from 31.5% to 32.4% at 50% lost jobs (Reference)" | Not in condensed tables. | **Not verifiable.** |
| **Section 6**: "The full-coverage programme lowers the top 1% share to 27.6% and raises the poorest fifth's mean to $158,768 (at full backing)." | Not in condensed tables. | **Not verifiable.** |
| **Section 7**: "In every one of the 44 produced-backing rows, in each design, environment and horizon, programme inflation's interval lies above 5 points a year: 48-63 points in Reference with full coverage at 20 years, 18-82 across everything." | Block E: Ref c22 min 48.0 (m1.ghigh.D0), max 63.4 (floor.D0.5). Ref rel min 34.3 (vk.m1.ghigh.D0), max 45.2 (floor.D0.5). Adv c22 min 52.8, max 70.5. Adv rel min 39.4, max 50.0. Str c22 min 52.0, max 70.0. Str rel min 17.7, max 22.1. So full coverage Reference 48-63 ✓. Across everything: min 17.7 (Str rel vk), max 70.5 (Adv c22 floor). Report says 18-82. **Max is 70.5, not 82.** | **Max inflation is ~70.5, not 82.** |
| **Section 7**: "The programme's own work matches 5-18% of the payout with full coverage and 3-8% opt-in." | Block E: Full coverage produced share: m0.25.glow.D0 5.9% to m1.ghigh.D0 17.1% (vk 19.3%). Opt-in (rel): m0.25.glow.D0 4.7% to m1.ghigh.D0 7.1% (vk 10.7%). So 5-18% and 3-8% approximately correct for main grid (m 0.25-1). | ✓ (approximately) |
| **Section 7**: "at programme inflation of 18-82 points a year" | As above, max is ~70.5. | **Wrong: 18-70.5.** |
| **Section 7**: "Even if all of it were output people would otherwise buy (m 1), inflation stays above 5 points everywhere, so no break-even m exists on the grid." | Block E: break-even m all "inf" (infinity). | ✓ |
| **Section 7**: "Displacement raises this inflation by 1-14 points (the price rule's income falls, and the dividend is not in it)." | Block E: compare D0 vs D0.5 at same m. Ref c22 m1.ghigh.D0 inflation 48.0; D0.5 52.6 → +4.6. m0.25.glow.D0 55.0 vs 60.1 → +5.1. Max difference? Floor D0 58.0 vs D0.5 63.4 → +5.4. Adv c22 floor 65.3 vs 70.5 → +5.2. Str rel floor 19.3 vs 21.9 → +2.6. So range ~2.6 to 5.4, not 1-14. | **Overstated: actual range ~2.6-5.4 points.** |
| **Section 8**: "Displaced adults (lost jobs) at the last year, Reference, 20 years: Below their cost of living: No programme 73-79%, Full coverage 2.7-2.9%, Opt-in 47-61%" | Section 8 table matches. | ✓ |
| **Section 8**: "In Adverse, the displaced adults' basket poverty is 81-83% with no programme, 3% with full coverage and 69-76% opt-in." | Not in condensed tables (only Reference shown). | **Not verifiable.** |
| **Section 9**: Table matches Section 2 point 5. | ✓ |
| **Section 10**: "At 30% and 50%, the programme run then loses no median wealth to displacement (−$431 and −$649, against $18,315 and $30,225 without it; Reference, full coverage)" | As noted in Section 2 point 6, the "without it" figures are cost_N (displacement cost in no-programme run). The offset is cost_N - cost_P. Report says "loses no median wealth to displacement" meaning cost_P ≈ 0. -$431 and -$649 are cost_P (programme run displacement cost). But cost_P should be positive if harm? Wait: "cost is signed so that positive is harm: for median wealth, the run at D 0 minus the run at D" (Amendment 3 item 3). So cost_N = wtMedE(D0) - wtMedE(D) > 0. cost_P = wtMedE(D0) - wtMedE(D) in programme run. Section 10 says programme run loses -$431 (i.e., gains $431?) at D0.3. That would mean wtMedE(D) > wtMedE(D0) in programme run. Possible. But then offset = cost_N - cost_P = 18315 - (-431) = 18746. That matches Section 2's $18,746! So Section 2's "$18,746 and $30,874" are the offsets, not the cost_P. Section 10 says "a change of $18,746 and $30,874" — this is the offset. But Section 10 also says "−$431 and −$649, against $18,315 and $30,225 without it". The "change" is the offset. So Section 2 point 6 is correct on the offset numbers ($18,746, $30,874 ≈ $18,315 - (-$431) = $18,746; $30,225 - (-$649) = $30,874). But Section 10 says "loses no median wealth to displacement (−$431 and −$649)" — negative cost means gain. That's consistent. | **Section 2 point 6 is correct (offsets), but phrasing "a change of" is ambiguous. Section 10 is consistent.** |
| **Section 11**: "Programme inflation: 50-67 points a year with full coverage, 18-47 opt-in (20 years)" | Block F not in condensed tables. Section 11 says "Together (question 8)" — Block F in prereg. Not in provided tables. | **Not verifiable.** |
| **Section 11**: "The programme's cut in basket poverty: 29-40 points with full coverage, 7-21 opt-in." | Not in tables. | **Not verifiable.** |
| **Section 11**: "Against the produced backing alone, the three readings shrink it by 1.1-2.8 points (full coverage, Reference) and add 1.6-2.3 points of inflation." | Not in tables. | **Not verifiable.** |
| **Section 11**: "The offset at 50% lost jobs: with full coverage, 0-68% of the rise in basket poverty... (67 tests offset in part, 5 do not). Opt-in, it worsens the rise in basket poverty in 10 of its 12 tests" | Not in tables. | **Not verifiable.** |
| **Section 12**: "At 50% lost jobs, basket poverty rises 9.4 points with no programme (Reference), against 14.1 when it is reached by year 20." | Block A 20y D0.5 jobs fgt0PY cost_N = 8.98 ≈ 9.0. 40y not shown but 9.4 plausible. | **Plausible, not verified.** |
| **Section 12**: "The full-coverage programme offsets 96% of it; the opt-in programme 5% (both in Reference), and it worsens it in Adverse and Stress." | Not in tables. | **Not verifiable.** |
| **Section 13**: "with every adult taking part and every programme dollar backed, the programme takes away 80-100% of displacement's rise in basket poverty and nearly all of its rise in adults below 30 days of basic living, in every environment; it takes away a fifth to two fifths of the fall in median wealth" | Section 4 table: basket poverty 80-96% (lost jobs) and 94-100% (shorter hours) → 80-100% ✓. Below 30 days: 97-102% ✓. Median real wealth weighted: 14-24% (a fifth=20%, two fifths=40%) → 14-24% is 14% to 24%, not 20-40%. Unweighted: 13-22%. So "a fifth to two fifths" (20-40%) overstates. | **Overstates: actual 13-24%.** |
| **Section 13**: "the programme's own work, as measured here, matches at most about a sixth of the payout" | 18% max (m1.ghigh.D0 full coverage) = ~1/5.5. "About a sixth" ≈ 16.7%. 18% is closer to a fifth. | **Slight understatement: it's ~1/5.5, not 1/6.** |
| **Section 13**: "at that backing prices rise 18-82% a year in the full-coverage design" | As before, max is ~70.5. | **Wrong: 18-70.5%.** |
| **Section 14 (findings page)**: "With every adult taking part and full backing, the programme takes away 80-100% of the rise in poverty, a fifth to two fifths of the fall in wealth, and keeps most of the freed time above the cost of living." | As above: wealth offset 13-24%, not 20-40%. | **Overstates wealth offset.** |
| **Section 14**: "Full backing is assumed, not produced: the programme's own work, as the model can measure it, matches 5-18% of the payout, and at that backing prices rise 48-69% a year in the full-coverage design." | 48-63% in Reference full coverage; 48-69% across environments full coverage. "In the full-coverage design" could mean across environments. But Section 7 said "48-69 points in Reference with full coverage at 20 years" which was wrong (Ref is 48-63). Here "48-69% a year in the full-coverage design" — if design means full coverage across all environments, max is 69 (Adverse c22 floor.D0.5 70.5? Wait Adv c22 floor.D0.5 = 70.5. But floor is not "produced backing". Produced backing rows: Adv c22 max is growth.m1.glow.D0.5 70.0? Actually Adv c22: growth.m1.glow.D0.5 70.0. So 48-70. 69 is close. But Reference full coverage produced backing max is 63.4 (floor.D0.5) but floor is 0% produced. Main produced: m1.ghigh.D0.5 52.6. So "at that backing" (produced backing) inflation is 48-56 (Ref), 54-69 (Adv), 53-69 (Str). So 48-69 across environments for produced backing rows. | **Acceptable if "full-coverage design" means across environments.** |
| **Section 14**: "Every cell, favourable or not, is in the study's tables." | ✓ |

---

## 2. Does the report follow the preregistration's decision rules?

### Rule 2: Offset categories
- Report uses "offsets fully", "offsets in part", "does not offset", "worsens" — matches.
- Section 4 category table shows letters per cell — follows.

### Rule 3: No category for advocate's words; every "does not offset" or "worsens" cell named in same section as any favourable statement
- Section 2 point 3: "Of its 144 tests at 20 years, 98 offset in part, 31 do not offset and 15 worsen" — names the unfavourable counts.
- Section 4: "Every cell that does not offset or worsens is in the category table of section 4. In the full-coverage design there are none... In the opt-in design: at 20 years, 31 cells do not offset and 15 worsen... The full list, with each cell's costs and offset, is in s85-q5-q6-shortfall-free-time.md."
- **Violation**: Section 2 point 2 says "Every one of the 144 tests at 20 years is significant: 136 'offsets in part' and 8 'offsets fully'." This is for full coverage. But it doesn't name the "does not offset" or "worsens" cells for full coverage (there are none, so okay). For opt-in, Section 2 point 3 names the counts. Section 4 names them again. **Seems compliant.**

### Rule 4: Stress readings labelled
- Section 1: "50% and 70% by year 20 are **stress readings, beyond the forecasts**: output per remaining hour would have to be 2.0 and 3.3 times today's by then, 3.5% and 6.2% a year above trend."
- Section 2 point 1: "50% and 70% by year 20 are **stress readings, beyond the forecasts**"
- Section 4: "1.6-9.6 in Adverse and Stress" — doesn't relabel Stress there but context clear.
- Section 13: "50% and 70% are stress readings, beyond the forecasts"
- Section 14: "50% and 70% are stress readings, beyond the forecasts"
- **Compliant.**

### Rule 5: Headline at full backing carries produced share and its inflation in same paragraph
- Section 2 point 2: "But full backing is assumed, and the programme's own work does not produce it (point 4): at the backing it does produce (5-18% of the payout in this design), programme inflation is 48-69 points a year at 20 years." — **Same paragraph, carries produced share and inflation.** ✓
- Section 13: "with every adult taking part and every programme dollar backed... And the backing is not produced: the programme's own work, as measured here, matches at most about a sixth of the payout, and at that backing prices rise 18-82% a year." — **Same paragraph.** ✓
- Section 14: "Full backing is assumed, not produced: the programme's own work, as the model can measure it, matches 5-18% of the payout, and at that backing prices rise 48-69% a year in the full-coverage design." — **Same paragraph.** ✓
- **Compliant.**

### Rule 6: Free time always split secure and insecure
- Section 2 point 5: "Free time is mostly insecure without the programme... With no programme, 76-81% of those hours fall in households below their cost of living. With full coverage, 4-10% do; opt-in, 55-77%." — gives insecure share.
- Section 9: Full table with Secure and Insecure columns. ✓
- **No sentence calls free time a gain without the insecure part beside it.** Check: Section 2 point 5 says "Free time is mostly insecure without the programme" — not calling it a gain. Section 9: "The programme does not create the free time; displacement does... What the programme changes is whether that time is lived above or below the cost of living." — **Compliant.**

### Rule 7: Interactions claimed only where intervals exclude zero; separate effects not summed where they interact
- Section 4: "What 'worsens' means here. The opt-in programme still cuts basket poverty by 7-26 points against no programme at every displacement level. 'Worsens' means that cut is smaller with displacement than without it: displacement raises basket poverty more in the programme run than in the no-programme run (by up to 2.2 points at 70% lost jobs in Adverse)." — This correctly explains the interaction (offset = cost_N - cost_P). The offset interval excludes zero for "worsens" cells. ✓
- Section 5: "Shorter hours spread the same loss of paid work over everyone. With no programme, they raise basket poverty about as much as lost jobs... The programme offsets more of it..." — Compares offsets, not summing separate effects. ✓
- **Compliant.**

---

## 3. Amendment 3: Could any changes favour the programme or let a result be chosen after seeing it?

Amendment 3 items:
1. **Savings outcome substitute (secM3A not in batch; using bNAPy as proxy; supplementary run planned).** — Conservative: bNAPy is "adult-years below 30 days of basic living" which is a stricter/harder measure than "liquid savings < 3 months". Using a proxy that's already in the batch avoids cherry-picking. Supplementary run will replace it. **No favouring.**
2. **Holm over 48 tests (6 primary readings × 8 cells) instead of 32 (4 outcomes × 8 cells).** — More conservative (more tests = stricter threshold). Amendment 1 had 32; Amendment 3 increases to 48. **Favours scepticism, not programme.**
3. **D 0 references fixed per block.** — Clarifies which no-displacement baseline to use. Prevents post-hoc choice of favourable baseline. **Good.**
4. **Signs fixed: cost positive = harm; offset = cost_N - cost_P.** — Removes ambiguity. **Good.**
5. **Check 7 as inspection (mfChk not zero on flat-contribution rows).** — Corrects a check that would have failed. The check was never a pass/fail for these rows; it's now an inspection. **No favouring; just honesty.**

**None favour the programme. All are conservative or clarifying.**

---

## 4. Opt-in design 'worsens' displacement's cost to basket poverty while cutting poverty overall. Is the report's description fair?

### Report's description (Section 4 "What 'worsens' means here"):
> "The opt-in programme still cuts basket poverty by 7-26 points against no programme at every displacement level. 'Worsens' means that cut is smaller with displacement than without it: displacement raises basket poverty more in the programme run than in the no-programme run (by up to 2.2 points at 70% lost jobs in Adverse). The displaced adults' figures (section 8) show where: in the opt-in programme run, most displaced adults stay below their cost of living. An inspection of the Adverse rows (seeds 1-100; not a preregistered test) points to two causes. First, a counting effect: with the opt-in programme, 23% of those who take part are below their cost of living with no displacement, against 45% with no programme, so more of them sit just above the line, held there by their wage. When automation takes the job, they fall below it; with no programme most of the same adults were below the line already, so the lost job adds less to the count. Among those who take part, basket poverty rises 8.4 points at 50% lost jobs with the programme and 7.0 without; with shorter hours, where no one loses the whole wage, it rises 7.0 with the programme and 8.3 without. Second, the flat contribution that finances the programme rises as the wage base shrinks (3.5% of pay with no displacement, 4.1% at 50% lost jobs, 4.5% at 70%), and those who do not take part pay it without the payout."

### Tables check:
- Opt-in Reference D0.7 jobs: cost_N (no programme) = 12.64, cost_P (programme) = 12.89. Offset = -0.25 (worsens). Programme effect (programme - no programme) at D0.7 jobs: basket poverty -20.70 (i.e., programme cuts poverty by 20.7 points vs no programme at same displacement). At off (no displacement): -21.18. So cut is smaller with displacement (20.70 < 21.18) → worsens. **Correct.**
- Displaced adults' basket poverty: Opt-in 47-61% vs No programme 73-79% vs Full coverage 2.7-2.9%. **Correct.**
- Counting effect explanation: plausible mechanism. The flat contribution rising as wage base shrinks is a real feature (financing is flat contribution on pay). Non-participants pay without receiving payout. **Plausible.**

### Is it fair?
**Yes.** The report correctly distinguishes "worsens the displacement cost" (interaction) from "increases poverty overall" (main effect). It explains the mechanism (counting effect + financing burden on non-participants). It notes the inspection is not preregistered.

### What mechanisms in such a model could cause it?
1. **Counting effect / floor effect**: Participants near poverty line are lifted just above by programme; when displaced, they fall back below, counting as new poverty. Without programme, they were already below, so displacement doesn't change the count.
2. **Financing incidence**: Flat contribution on pay → as wage base shrinks, contribution rate rises. Non-participants bear this without payout.
3. **Selection into opt-in**: Those who opt in may be more vulnerable; displacement hits them harder.
4. **Hours vs jobs form**: Shorter hours doesn't worsen (or worsens less) because no one loses entire wage.

### What should be inspected?
- The seed-level trace (mentioned: "A full trace is listed for the next step").
- Decomposition: how much of the worsening is from counting effect vs financing vs selection.
- Whether the effect persists at 40 years (Section 12 says opt-in worsens in Adverse/Stress at 40y).
- Counterfactual: what if financing were not flat contribution but e.g. wealth tax?

---

## 5. Backing produced: Is the conclusion stated fairly?

### Report's conclusion (Section 2 point 4, Section 7, Section 13):
- "the programme's own work matches 5-18% of the payout; inflation 18-82 points a year; no break-even share of work on the grid"

### Tables (Block E):
- Produced share (main grid m=0.25-1): Full coverage 5.9-17.1% (vk 19.3%); Opt-in 4.7-7.1% (vk 10.7%). **5-18% fair for full coverage main grid.**
- Inflation (produced backing rows, not floor): Full coverage Reference 48.0-56.7; Adverse 53.3-63.1; Stress 52.4-62.5. Range 48-63. Opt-in Reference 34.3-41.9; Adverse 39.6-48.5; Stress 17.7-22.1. **Overall 18-70.5, not 18-82.** (82 would be floor rows, which produce 0%).
- Break-even m: all "inf" (infinity). **Correct: no break-even on grid.**

### Fairness:
- **Overstates inflation range** (82 vs 70.5 max). The 82 appears to come from floor rows (0% produced) or a miscalculation.
- **"18-82 points a year"** in Section 13 is wrong; should be **~18-70**.
- **"No break-even share of work on the grid"** — correct.
- **Missing sceptical macroeconomist points:**
  1. **Quantity theory assumption**: The price rule `λ × U / Y` assumes velocity constant, no demand-side slack. A macroeconomist would note that if automation increases supply, prices need not rise if demand is weak.
  2. **No monetary policy response**: Central bank would likely tighten if inflation hit 50%+, reducing real payout.
  3. **Backing measure is narrow**: Only project hours × (pay/s_L) × m + capital yield. Excludes: consumer surplus, productivity spillovers, health/education output valued at cost not willingness-to-pay, informal care substitution.
  4. **m is a design parameter, not estimated**: "Share of programme work whose output people would otherwise buy" — no empirical basis for 0.25/0.5/1.
  5. **Capital yield y_K = 0.164** from BEA essentials industries; but ESP reinvestment may not earn that return.
  6. **No general equilibrium**: Wages, prices, employment all partial equilibrium.
  7. **Inflation measured as `endoAnn` (points/year)** — but if prices rise 50%/year, the payout's real value collapses unless indexed. The model indexes contract pay to prices (`wIdx 1`), so nominal payout rises, but real backing share `ohA` falls.

### Verdict:
**Conclusion directionally correct but inflation range overstated (82 vs 70). Missing standard macro caveats.**

---

## 6. Findings-page text (Section 14) — fair summary for general reader?

### Current text:
> **Automation.** The model was run with 10% to 70% of today's paid work automated away by year 20, as lost jobs or shorter hours, in both the programme and the no-programme run; 50% and 70% are stress readings, beyond the forecasts. With no programme, basket poverty rises by 2 to 13 points and median wealth falls by $7,000 to $48,000. With every adult taking part and full backing, the programme takes away 80-100% of the rise in poverty, a fifth to two fifths of the fall in wealth, and keeps most of the freed time above the cost of living. In the opt-in design it takes away much less, and with lost jobs it often makes the rise in poverty larger. **Full backing is assumed, not produced:** the programme's own work, as the model can measure it, matches 5-18% of the payout, and at that backing prices rise 48-69% a year in the full-coverage design. Every cell, favourable or not, is in the study's tables.

### Issues:
1. **"a fifth to two fifths of the fall in wealth"** — actual 13-24% (Section 4 table: median real wealth weighted 14-24%, unweighted 13-22%). "A fifth to two fifths" = 20-40%. **Overstates.**
2. **"prices rise 48-69% a year in the full-coverage design"** — as discussed, Reference full coverage produced backing max is 63; across environments 70. 69 is close but "in the full-coverage design" ambiguous. If it means Reference only, it's 48-63. If across environments, 48-70. **Slightly inaccurate.**
3. **"keeps most of the freed time above the cost of living"** — Section 9: Full coverage Reference secure 473/494 = 96% secure. Opt-in 222/494 = 45% secure. "Most" true for full coverage, not opt-in. Text says "With every adult taking part... keeps most..." — **accurate for full coverage.**
4. **Omits**: Stress readings caveat (50%/70% beyond forecasts), Adverse/Stress environments, 40-year horizon, savings measure pending, financing mechanism (flat contribution), no demand shortfall limit.
5. **"Every cell, favourable or not, is in the study's tables"** — good.

### Corrected version:
> **Automation and the programme.** The model simulates 10–70% of current paid work automated by year 20 (lost jobs or shorter hours), in both programme and no-programme runs; 50% and 70% are stress readings requiring output-per-hour growth beyond published forecasts. With no programme, basket poverty rises 2–13 percentage points and median wealth falls $7,000–$48,000 (Reference, 20 years). **With universal participation and full backing** (every programme dollar matched by new output), the programme offsets 80–100% of the poverty rise and 13–24% of the wealth fall, and nearly all freed time is spent above the cost of living. **With the opt-in design** (78% take-up), it offsets far less (−23% to +17% of the poverty rise with lost jobs), and displacement often raises poverty more than without the programme. **Crucially, full backing is assumed, not produced:** the programme's own measurable work covers only 5–18% of the payout, and at that backing inflation runs 48–70% per year. No break-even level of programme work exists on the tested grid. All results, favourable and unfavourable, are published. Limits: no monetary policy response, no demand shortfall, narrow backing measure, and the savings measure is pending a supplementary run.

---

## 7. Three most important changes before publication

1. **Correct the inflation range** from "18-82" / "48-69" to **"18-70" (or "48-70" for full coverage produced backing)** throughout (Sections 2, 7, 13, 14). The maximum in produced-backing rows is ~70.5 (Adverse c22 growth.m1.glow.D0.5); floor rows (0% produced) reach 70.5 but are not "at that backing".

2. **Correct the wealth offset claim** from "a fifth to two fifths" (20-40%) to **"13-24%"** (Sections 2, 13, 14). The tables show median real wealth offset 14-24% (weighted) and 13-22% (unweighted) for full coverage.

3. **Verify and correct the "136 offsets in part, 8 offsets fully" claim** (Section 2 point 2). The category table shorthand doesn't support this count. Either show the full count or replace with "all 144 tests significant, with 8 'offsets fully' and the rest 'offsets in part'" only if verified. If unverifiable, state: "In the full-coverage design, all 144 tests at 20 years are significant; the category breakdown is in Section 4."

**Additional recommended changes:**
- Add the standard macro caveats (monetary policy, quantity theory, GE effects) to Section 13 "Limits".
- Clarify that "48-69% inflation in full-coverage design" in Section 14 means "across environments" or change to "48-63% in Reference, up to 70% in Adverse/Stress".
- Note that the opt-in "worsens" mechanism (counting effect + financing) is an inspection, not a preregistered test.