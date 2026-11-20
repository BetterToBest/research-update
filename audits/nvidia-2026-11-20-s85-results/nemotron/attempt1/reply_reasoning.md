Let me carefully analyze this complex query. I need to review the report against the tables and preregistration, answering 7 specific questions. Let me start by understanding all the materials.

First, the preregistration with three amendments:
- Original preregistration committed Nov 19, 2026
- Amendment 1: Nov 19, after outside reading, before build
- Amendment 2: Nov 19, after build, before dry run
- Amendment 3: Nov 20, after batch finished, before any table read

The checks file shows all checks passed.

The condensed results tables show Block A (headline cells) for 20 years across Reference, Adverse, Stress environments, both full coverage and opt-in designs, and Block E (backing produced) for 20 years.

The report is a plain-words report with 15 sections.

I need to answer 7 questions concretely, quoting text.

Let me go through each question systematically.

## Question 1: Does every statement in the report follow from the tables? Quote any sentence that overstates, understates or misquotes a figure, and give the correct figure.

I need to check the report against the tables. Let me go section by section.

### Section 2: "The answer in short"

1. "By year 20, basket poverty (adult-years below one's own cost of living) is 2.0, 5.6, 9.0 and 12.6 points higher at 10%, 30%, 50% and 70% lost jobs (Reference; 1.6-9.6 in Adverse and Stress), and median real wealth is $7,158 to $48,326 lower."

Check tables: Reference, full coverage, D 0.1 jobs fgt0PY cost_N = 2.05 (table says 2.05, report says 2.0 - close but rounded). D 0.3 jobs: 5.56 (report 5.6). D 0.5 jobs: 8.98 (report 9.0). D 0.7 jobs: 12.64 (report 12.6). These are rounded but essentially correct.

Median real wealth: Reference full coverage D 0.1 jobs wtMedE cost_N = 7158 (report $7,158). D 0.7 jobs: 48326 (report $48,326). Correct.

Adverse and Stress: Adverse D 0.1 jobs fgt0PY cost_N = 1.60, D 0.7 jobs = 9.60. Stress same. Report says "1.6-9.6" - correct.

2. "At 40 years basket poverty rises 3.1 to 20.3 points in Reference." - I don't have 40-year tables in the condensed extract, but the report says 40-year tables exist. I'll note this can't be verified from given tables.

3. "It offsets 80-96% of the rise in basket poverty with lost jobs and 94-100% with shorter hours, 59-93% of the rise in yearly wealth poverty, 97-100% of the rise in adult-years below 30 days of basic living, and 13-40% of the fall in median real wealth."

Check Reference full coverage 20 years:
- Basket poverty lost jobs: D0.1 0.96, D0.3 0.95, D0.5 0.94, D0.7 0.94 → 94-96% (report says 80-96% - wait, 80% is lower than any of these. Let me check other environments. Adverse: D0.1 0.93, D0.3 0.92, D0.5 0.92, D0.7 0.92. Stress: D0.1 0.83, D0.3 0.81, D0.5 0.80, D0.7 0.80. Ah, across all environments: 80-96% correct.
- Shorter hours: Reference D0.1 1.00, D0.3 1.00, D0.5 1.00, D0.7 0.98 → 98-100%. Adverse: D0.1 1.00, D0.3 0.99, D0.5 0.99, D0.7 0.97. Stress: D0.1 1.00, D0.3 0.99, D0.5 0.98, D0.7 0.94. So 94-100% correct.
- Yearly wealth poverty (ppovA): Reference lost jobs: D0.1 0.87, D0.3 0.82, D0.5 0.80, D0.7 0.79 → 79-87%. Adverse: D0.1 0.81, D0.3 0.76, D0.5 0.73, D0.7 0.73. Stress: D0.1 0.72, D0.3 0.65, D0.5 0.61, D0.7 0.59. So 59-87%? Report says 59-93%. Let me check shorter hours: Reference D0.1 0.93, D0.3 0.92, D0.5 0.92, D0.7 0.91. Adverse: D0.1 0.92, D0.3 0.91, D0.5 0.91, D0.7 0.89. Stress: D0.1 0.89, D0.3 0.88, D0.5 0.87, D0.7 0.85. So across all: 59-93% seems right (Stress lost jobs D0.7 0.59, Reference shorter hours D0.1 0.93).
- Below 30 days (bNAPy): Reference lost jobs: D0.1 1.02, D0.3 1.01, D0.5 1.00, D0.7 1.00. Shorter hours: all 1.00. Adverse lost jobs: D0.1 1.00, D0.3 0.99, D0.5 0.98, D0.7 0.98. Shorter hours: all 0.99. Stress lost jobs: D0.1 0.99, D0.3 0.98, D0.5 0.97, D0.7 0.97. Shorter hours: all 0.99. So 97-102%? Report says 97-100%. The 1.02 is slightly above 100% (offsets fully category). But 102% > 100%. Report says 97-100% - this understates the upper bound. Should be 97-102% or "up to 102%".
- Median real wealth (wtMedE): Reference lost jobs: D0.1 0.22, D0.3 0.20, D0.5 0.16, D0.7 0.15 → 15-22%. Shorter hours: D0.1 0.18, D0.3 0.21, D0.5 0.26, D0.7 0.26 → 18-26%. Adverse lost jobs: D0.1 0.20, D0.3 0.19, D0.5 0.16, D0.7 0.14. Shorter hours: D0.1 0.32, D0.3 0.34, D0.5 0.37, D0.7 0.31. Stress lost jobs: D0.1 0.20, D0.3 0.24, D0.5 0.21, D0.7 0.19. Shorter hours: D0.1 0.38, D0.3 0.38, D0.5 0.40, D0.7 0.35. So range 13-40%? Report says 13-40%. Lowest is Adverse D0.7 lost jobs 0.14 (14%), Stress D0.1 lost jobs 0.20. Wait, Reference D0.7 lost jobs 0.15. Adverse D0.7 lost jobs 0.14. But report says 13%. Let me check unweighted: Reference lost jobs D0.7 0.14. Adverse lost jobs D0.7 0.13. Stress lost jobs D0.7 0.17. So 13-40% correct (Adverse D0.7 lost jobs unweighted 0.13).

4. "Every one of the 144 tests at 20 years is significant: 136 'offsets in part' and 8 'offsets fully'."

144 tests = 6 outcomes × 8 cells × 3 environments? 6×8×3=144. Yes.

Category table for full coverage 20 years:
Reference: PPPPPF PPPPPF PPPPPF PPPPPP FPPPPF FPPPPF PPPPPP PPPPPP
Count: P=?, F=?
Let me count: Each row has 8 cells × 6 outcomes = 48 per environment.
Reference: First row (lost jobs): PPPPPF (5P,1F) ×4 = 20P,4F? Wait, "PPPPPF PPPPPF PPPPPF PPPPPP" that's 4 groups of 6 = 24 entries? No, 8 cells × 6 outcomes = 48. The notation: "PPPPPF" is 6 letters for 6 outcomes at one cell. So 8 cells = 8 groups of 6.

Reference full coverage 20 years: "PPPPPF PPPPPF PPPPPF PPPPPP FPPPPF FPPPPF PPPPPP PPPPPP"
That's 8 groups: 
1. PPPPPF (5P,1F)
2. PPPPPF (5P,1F)
3. PPPPPF (5P,1F)
4. PPPPPP (6P)
5. FPPPPF (1F,4P,1F? Wait FPPPPF = F,P,P,P,P,F = 2F,4P)
6. FPPPPF (2F,4P)
7. PPPPPP (6P)
8. PPPPPP (6P)

Total P: 5+5+5+6+4+4+6+6 = 41
Total F: 1+1+1+0+2+2+0+0 = 7
Total: 48. But 41+7=48. No N or W.

Adverse full coverage 20 years: "PPPPPF then PPPPPP in every other cell" - so first cell PPPPPF (5P,1F), other 7 cells PPPPPP (6P each) = 5+42=47P, 1F = 48.

Stress full coverage 20 years: "PPPPPP in every cell" = 8×6=48P.

Total full coverage 20 years: Reference 41P+7F, Adverse 47P+1F, Stress 48P = 136P + 8F = 144. Correct! "136 'offsets in part' and 8 'offsets fully'" - matches.

5. "But full backing is assumed, and the programme's own work does not produce it (point 4): at the backing it does produce (5-18% of the payout in this design), programme inflation is 48-69 points a year at 20 years."

Check Block E: Reference full coverage (ref c22): programme inflation ranges from 48.0 (m1.ghigh.D0) to 63.4 (floor.D0.5). But the produced backing rows (not floor) at m1: 48.0 to 52.6. At m0.5: 51.8 to 56.7. At m0.25: 53.6 to 61.3. So 48-63 for produced backing rows. Report says 48-69. 69 appears in Adverse (growth.m1.ghigh.D0.5 68.3, floor.D0.5 70.5). Stress: up to 70.0. So across environments 48-70. Report says 48-69 - close, maybe rounding.

Produced share: ref c22 m1.ghigh.D0 17.1%, m0.5 9.6%, m0.25 5.9%. So 5-18% correct (17.1% rounds to 17%, but 18% is close).

6. "The opt-in design offsets far less, and with lost jobs it often makes displacement's cost larger. It offsets up to 69% of the rise in basket poverty with shorter hours (and in one cell it worsens it), and with lost jobs between −23% and +17%: in 9 of the 12 lost-jobs cells the rise in basket poverty is larger with the programme than without it."

Check opt-in Reference 20 years basket poverty lost jobs:
D0.1: offset share 0.17 (17%)
D0.3: 0.08 (8%)
D0.5: 0.02 (2%)
D0.7: -0.02 (-2%)
Adverse lost jobs:
D0.1: -0.07 (-7%)
D0.3: -0.14 (-14%)
D0.5: -0.19 (-19%)
D0.7: -0.23 (-23%)
Stress lost jobs:
D0.1: -0.04 (-4%)
D0.3: -0.08 (-8%)
D0.5: -0.10 (-10%)
D0.7: -0.11 (-11%)

So range -23% to +17% correct. "In 9 of the 12 lost-jobs cells the rise in basket poverty is larger with the programme than without it" - larger means negative offset share. Count negative: Adverse 4, Stress 4, Reference 1 (D0.7) = 9. Yes, 9 of 12.

Shorter hours opt-in Reference: D0.1 0.69, D0.3 0.66, D0.5 0.57, D0.7 0.35. Adverse: D0.1 0.31, D0.3 0.24, D0.5 0.13, D0.7 0.01. Stress: D0.1 0.11, D0.3 0.07, D0.5 0.02, D0.7 -0.03. So up to 69% (Reference D0.1), and one cell worsens (Stress D0.7 -0.03). Correct.

"Of its 144 tests at 20 years, 98 offset in part, 31 do not offset and 15 worsen (at 40 years: 80, 32 and 32)."

Opt-in 20 years category table:
Reference: PPPNNP PPPPPP PNPPPP WNPPPP PPPPPP PPPPPP PPPPPP PPPPPP
Let me count: 8 cells × 6 outcomes = 48.
Reference: 
Cell1: PPPNNP = 4P,2N
Cell2: PPPPPP = 6P
Cell3: PNPPPP = 5P,1N? Wait PNPPPP = P,N,P,P,P,P = 5P,1N
Cell4: WNPPPP = 1W,5P
Cell5: PPPPPP = 6P
Cell6: PPPPPP = 6P
Cell7: PPPPPP = 6P
Cell8: PPPPPP = 6P
Total Reference: P=4+6+5+5+6+6+6+6=44, N=2+0+1+0=3, W=1. 44+3+1=48.

Adverse: WNPNNP WNNNPP WNNNNP WWWNNP PPPPPP PPPPPP PPPPPP PPPPPP
Cell1: WNPNNP = 1W,1N,1P,1N,1N,1P = 2P,3N,1W
Cell2: WNNNPP = 1W,3N,2P
Cell3: WNNNNP = 1W,4N,1P
Cell4: WWWNNP = 3W,1N,1N,1P = 1P,1N,3W? Wait WWWNNP = W,W,W,N,N,P = 1P,2N,3W
Cell5-8: each PPPPPP = 6P ×4 = 24P
Total Adverse: P=2+2+1+1+24=30, N=3+3+4+2=12, W=1+1+1+3=6. 30+12+6=48.

Stress: WNNNNP WNNNNP WWNNNP WWWNNP PPPPNP PPPPPP PPPPPP WPNPPP
Cell1: WNNNNP = 1W,4N,1P
Cell2: WNNNNP = 1W,4N,1P
Cell3: WWNNNP = 2W,2N,1N,1P = 1P,3N,2W? WWNNNP = W,W,N,N,N,P = 1P,3N,2W
Cell4: WWWNNP = 3W,2N,1P
Cell5: PPPPNP = 5P,1N
Cell6: PPPPPP = 6P
Cell7: PPPPPP = 6P
Cell8: WPNPPP = 1W,1P,1N,3P = 4P,1N,1W
Total Stress: P=1+1+1+1+5+6+6+4=25, N=4+4+3+2+1+0+0+1=15, W=1+1+2+3+0+0+0+1=8. 25+15+8=48.

Grand total opt-in 20 years: P=44+30+25=99, N=3+12+15=30, W=1+6+8=15. Total 144.
Report says 98 offset in part, 31 do not offset, 15 worsen. Close: 99 vs 98, 30 vs 31. Probably rounding or I miscounted one. Essentially correct.

40 years: report says 80, 32, 32. I don't have 40-year category tables, but plausible.

7. "Displaced adults' basket poverty in their last year is 47-61% with the opt-in programme (Reference), against 73-79% with none and 3% with full coverage."

Check section 8 table: Displaced adults (lost jobs) at last year, Reference, 20 years:
No programme: 73-79%
Full coverage: 2.7-2.9%
Opt-in: 47-61%
Matches exactly.

8. "The backing produced is far from enough. In every one of the 44 produced-backing rows, in each design, environment and horizon, programme inflation's interval lies above 5 points a year: 48-63 points in Reference with full coverage at 20 years, 18-82 across everything."

Block E shows for ref c22: all rows "does not back enough" with inflation 48.0 to 63.4. ref rel: 34.3 to 45.2. adv c22: 52.8 to 70.5. adv rel: 39.6 to 50.0. str c22: 52.0 to 70.0. str rel: 17.7 to 22.1. So across all: 17.7 to 70.5. Report says 18-82. 82 not seen in 20-year tables. Maybe 40-year? Or Stress full coverage 40-year? The report says "across everything" including 40 years. 82 might be from 40-year tables not shown. But in given 20-year tables, max is 70.5. However, the report section 2 says "48-63 points in Reference with full coverage at 20 years, 18-82 across everything." The 18-82 likely includes 40-year and all environments. Since I don't have 40-year Block E, I'll note the 20-year range is 17.7-70.5, so 18-82 is plausible for full set.

"The programme's own work matches 5-18% of the payout with full coverage and 3-8% opt-in."

Full coverage ref c22: produced share 5.9% (m0.25) to 19.3% (vk.m1). But main reading m0.25 to m1: 5.9% to 17.1%. Report says 5-18%. Close.
Opt-in ref rel: m0.25 4.7%, m0.5 5.5%, m1 7.0-7.1%, vk 10.7-10.8%. So 3-8%? Lowest is m0.25.glow.D0.7 4.7%? Wait ref rel m0.25.glow.D0 4.7%, m0.25.glow.D0.7 4.7%. But adv rel m0.25.glow.D0.7 4.8%. str rel m0.25.glow.D0 2.6%. Ah, Stress opt-in (str rel) m0.25.glow.D0 2.6%. So 2.6% to 10.8%. Report says 3-8% - understates range (2.6% to 10.8%), but 3-8% covers most main readings.

"Even if all of it were output people would otherwise buy (m 1), inflation stays above 5 points everywhere, so no break-even m exists on the grid."

Block E: break-even m all "inf" (infinity). Correct.

"Displacement raises this inflation by 1-14 points (the price rule's income falls, and the dividend is not in it)."

Check: ref c22 m1.ghigh.D0 48.0, D0.5 52.6 → +4.6. m0.5 D0 51.8, D0.5 56.7 → +4.9. m0.25 D0 53.6, D0.5 58.7 → +5.1. Adverse larger. Stress similar. 1-14 seems plausible.

9. "Free time is mostly insecure without the programme. At 50% lost jobs, an adult who was in paid work at the start has on average 494 more unpaid hours a year over the run (1,032 in year 20). With no programme, 76-81% of those hours fall in households below their cost of living. With full coverage, 4-10% do; opt-in, 55-77%."

Section 9 table: No programme Reference: 494 freed hours, 117 secure, 377 insecure. Insecure share = 377/494 = 76.3%. Adverse: 494, 93 secure, 401 insecure? Wait table shows No programme Stress: 494, 93 secure, 401 insecure → 81.2%. Reference 76.3%, Stress 81.2%. Report says 76-81%. Correct.

Full coverage Reference: 473 secure, 21 insecure → 4.3%. Stress: 447 secure, 47 insecure → 9.5%. So 4-10% correct.

Opt-in Reference: 222 secure, 272 insecure → 55.1%. Stress: 116 secure, 379 insecure → 76.6%. So 55-77% correct.

"With shorter hours the hours are the same and more of them are secure (no programme: 191 of 494 in Reference)." Table doesn't show shorter hours free time split, but report says "the hours are the same" - for shorter hours form, the freed hours should be the same total (since mean cut = D_t), but distribution differs. The table only shows lost jobs. Report says "no programme: 191 of 494 in Reference" for shorter hours - 191/494=38.7% secure. Not in table but plausible.

10. "The design's maintained take-home, with shorter hours and the automated hours' output paid to the workers whose hours fell, removes displacement's cost to median wealth in the programme run (a change of $18,746 and $30,874 at 30% and 50%, Reference, full coverage)."

Section 10: "At 30% and 50%, the programme run then loses no median wealth to displacement (−$431 and −$649, against $18,315 and $30,225 without it; Reference, full coverage)". So the change is $18,315 - (-$431) = $18,746 and $30,225 - (-$649) = $30,874. Correct.

11. "Together with the supply limit, wages that follow prices at three quarters made up a year later, and the BU a month behind, at the produced backing, programme inflation is 50-67 points a year with full coverage (20 years), the programme still cuts basket poverty by 29-40 points, and it offsets 0-68% of the rise in basket poverty at 50% lost jobs. Opt-in, it worsens that rise in 10 of its 12 tests."

Section 11: "Programme inflation: 50-67 points a year with full coverage, 18-47 opt-in (20 years)". Matches.

"The programme's cut in basket poverty: 29-40 points with full coverage, 7-21 opt-in." Matches.

"Offset at 50% lost jobs: with full coverage, 0-68% of the rise in basket poverty... Opt-in, it worsens the rise in basket poverty in 10 of its 12 tests." Section 11 says "Opt-in, it worsens that rise in 10 of its 12 tests." Matches.

12. Section 12: "Displacement reached by year 40 instead of 20 costs less over a 40-year run... At 50% lost jobs, basket poverty rises 9.4 points with no programme (Reference), against 14.1 when it is reached by year 20." I don't have 40-year Block A tables, but plausible.

13. Section 13: "with every adult taking part and every programme dollar backed, the programme takes away 80-100% of displacement's rise in basket poverty and nearly all of its rise in adults below 30 days of basic living, in every environment; it takes away a fifth to two fifths of the fall in median wealth; and the free time displacement brings is mostly secure."

80-100%: full coverage across environments: Reference 80-100%, Adverse 81-100% (Stress D0.7 lost jobs 80%, shorter hours 94%), so 80-100% correct.

"nearly all of its rise in adults below 30 days": 97-102% across environments. Correct.

"a fifth to two fifths of the fall in median wealth": 13-40% → 13% is less than a fifth (20%), 40% is two fifths. Report says "a fifth to two fifths" but 13% is below a fifth. Should be "about an eighth to two fifths" or "13-40%". This understates the lower bound.

"With the opt-in design, it takes away much less, and with lost jobs it often makes the rise in poverty larger." Correct.

"And the backing is not produced: the programme's own work, as measured here, matches at most about a sixth of the payout, and at that backing prices rise 18-82% a year."

"at most about a sixth" = 16.7%. Full coverage max 17.1% (m1.ghigh.D0), opt-in max 10.8% (vk). So "about a sixth" correct for full coverage.

"prices rise 18-82% a year" - Block E shows 17.7 to 70.5 in 20-year tables. 82% might be 40-year. Report says 18-82 in section 2, 48-69 in section 2 for full coverage 20 years, 18-82 across everything. In section 13 says "18-82% a year" without qualification. Could be misleading if 82% is only at 40 years Stress. But "across everything" includes 40 years.

14. Section 14 (findings page text): "With no programme, basket poverty rises by 2 to 13 points and median wealth falls by $7,000 to $48,000." Reference: 2.05 to 12.64 → 2-13. Adverse: 1.60 to 9.60. Stress: 1.60 to 10.85. So 2-13 covers Reference, but Adverse/Stress go to 9.6/10.85. "2 to 13 points" is Reference range. But says "with no programme" generally. Could be interpreted as across all, but max is 12.64. Okay.

"With every adult taking part and full backing, the programme takes away 80-100% of the rise in poverty, a fifth to two fifths of the fall in wealth, and keeps most of the freed time above the cost of living." As above, 80-100% correct, "a fifth to two fifths" - 13-40%, 13% < 20%. "keeps most of the freed time above cost of living" - full coverage: 90-96% secure (4-10% insecure). Yes, most.

"In the opt-in design it takes away much less, and with lost jobs it often makes the rise in poverty larger." Correct.

"Full backing is assumed, not produced: the programme's own work, as the model can measure it, matches 5-18% of the payout, and at that backing prices rise 48-69% a year in the full-coverage design." Section 2 said 48-69 for full coverage 20 years. Block E ref c22: 48.0 to 63.4. 69 is higher. Adverse goes to 70.5. But "in the full-coverage design" at 20 years Reference is 48-63. 48-69 overstates for Reference full coverage 20 years. Should be 48-63.

Now, let me check for any other discrepancies.

Section 4 table: "Basket poverty | 80-96% (81-97%) | 94-100% (90-101%) | −23% to 17% (−32% to 15%) | −3% to 69% (−19% to 73%)"

Check 40-year ranges in parentheses. I don't have 40-year data, but the 20-year ranges match what I calculated.

"Wealth poverty, yearly average | 59-87% (75-95%) | 85-93% (88-98%) | −7% to 18% (−9% to 21%) | 4-47% (−1% to 56%)"

20-year: full coverage lost jobs: Reference 79-87%, Adverse 73-81%, Stress 59-72% → 59-87% correct.
Full coverage shorter hours: Reference 91-93%, Adverse 89-92%, Stress 85-89% → 85-93%? Wait Reference D0.1 0.93, D0.7 0.91. Adverse D0.1 0.92, D0.7 0.89. Stress D0.1 0.89, D0.7 0.85. So 85-93% correct.
Opt-in lost jobs: Reference -7% to 18%? Reference D0.1 17%, D0.3 8%, D0.5 2%, D0.7 -2%. Adverse D0.1 -7%, D0.3 -14%, D0.5 -19%, D0.7 -23%. Stress D0.1 -4%, D0.3 -8%, D0.5 -10%, D0.7 -11%. So -23% to 18%. Report says -7% to 18% for 20 years? Wait table says "−7% to 18% (−9% to 21%)" for opt-in lost jobs yearly wealth poverty. But I see -23% in Adverse D0.7. Let me check Adverse opt-in D0.7 jobs ppovA: cost_N 1.78, cost_P 1.90, offset -0.12, offset share -0.07. That's -7%. D0.5: -0.06/-0.04. D0.3: -0.00. D0.1: 0.03/0.10. So Adverse opt-in lost jobs yearly wealth poverty offset shares: 10%, 0%, -4%, -7%. Stress: D0.1 2%, D0.3 -3%, D0.5 -4%, D0.7 -5%. Reference: 17%, 8%, 2%, -2%. So range -7% to 17%. Report says -7% to 18%. Close (17% vs 18%). But Adverse D0.7 is -7%, not -23%. The -23% was for basket poverty. For yearly wealth poverty, it's -7%. Okay, correct.

"Wealth poverty, last year | 72-94% (82-97%) | 88-97% (90-100%) | −5% to 20% (−14% to 25%) | 2-54% (−5% to 62%)"

Check: full coverage lost jobs last year (pov): Reference D0.1 0.94, D0.3 0.91, D0.5 0.89, D0.7 0.89. Adverse D0.1 0.89, D0.3 0.86, D0.5 0.84, D0.7 0.84. Stress D0.1 0.79, D0.3 0.74, D0.5 0.72, D0.7 0.72. So 72-94% correct.

Full coverage shorter hours: Reference D0.1 0.97, D0.3 0.97, D0.5 0.97, D0.7 0.95. Adverse D0.1 0.97, D0.3 0.96, D0.5 0.95, D0.7 0.94. Stress D0.1 0.94, D0.3 0.93, D0.5 0.92, D0.7 0.88. So 88-97% correct.

Opt-in lost jobs last year: Reference D0.1 0.20, D0.3 0.10, D0.5 0.07, D0.7 0.06. Adverse D0.1 0.13, D0.3 0.00, D0.5 -0.02, D0.7 -0.05. Stress D0.1 0.05, D0.3 -0.02, D0.5 -0.03, D0.7 -0.05. So -5% to 20% correct.

Opt-in shorter hours: Reference D0.1 0.54, D0.3 0.51, D0.5 0.47, D0.7 0.36. Adverse D0.1 0.27, D0.3 0.25, D0.5 0.20, D0.7 0.13. Stress D0.1 0.11, D0.3 0.08, D0.5 0.05, D0.7 0.02. So 2-54% correct.

"Median real wealth, weighted | 14-24% (7-33%) | 18-40% (7-44%) | 1-8% (−5% to 18%) | 6-21% (1-19%)"

Full coverage lost jobs wtMedE: Reference 15-22%, Adverse 14-20%, Stress 19-24%? Wait Stress D0.1 0.20, D0.3 0.24, D0.5 0.21, D0.7 0.19. So 14-24% correct.
Full coverage shorter hours: Reference 18-26%, Adverse 31-37%, Stress 35-40%. So 18-40% correct.
Opt-in lost jobs: Reference 4-8%, Adverse 2-8% (D0.1 0.07, D0.3 0.08, D0.5 0.05, D0.7 0.02), Stress 2-3% (D0.1 0.02, D0.3 0.03, D0.5 0.03, D0.7 0.01). So 1-8% correct.
Opt-in shorter hours: Reference 11-20%, Adverse 18-21%, Stress 8-15%. So 6-21% correct.

"Median real wealth, unweighted | 13-22% (8-31%) | 18-38% (6-42%) | −3% to 10% (−4% to 16%) | 6-20% (0-19%)"

Similar, correct.

"Below 30 days of basic living (in place of the savings measure) | 97-102% (98-100%) | 99-100% (99-100%) | 4-38% (−2% to 42%) | 9-61% (2-67%)"

Full coverage lost jobs bNAPy: Reference 100-102%, Adverse 98-100%, Stress 97-99%. So 97-102% correct.
Full coverage shorter hours: all 99-100%. Correct.
Opt-in lost jobs: Reference 38-61%? Wait Reference D0.1 0.38, D0.3 0.33, D0.5 0.30, D0.7 0.29. Adverse D0.1 0.28, D0.3 0.19, D0.5 0.14, D0.7 0.10. Stress D0.1 0.11, D0.3 0.07, D0.5 0.05, D0.7 0.04. So 4-38% correct (Stress D0.7 4%, Reference D0.1 38%).
Opt-in shorter hours: Reference 59-61%, Adverse 33-39%, Stress 9-30%. So 9-61% correct.

Category tables match my earlier count.

Section 5: "Shorter hours spread the same loss of paid work over everyone. With no programme, they raise basket poverty about as much as lost jobs (Reference: 9.5 against 9.0 points at 50%)."

Reference D0.5 jobs fgt0PY cost_N 8.98, hours 9.52. Report says 9.5 vs 9.0. Correct.

"The programme offsets more of it: in the full-coverage design 94-100% against 80-96%; opt-in, up to 69% against at most 17%."

Full coverage shorter hours basket poverty offset share: Reference 1.00,1.00,1.00,0.98; Adverse 1.00,0.99,0.99,0.97; Stress 1.00,0.99,0.98,0.94 → 94-100%. Lost jobs: 80-96%. Correct.
Opt-in shorter hours: Reference up to 0.69, Adverse up to 0.31, Stress up to 0.11 → up to 69%. Lost jobs: up to 17% (Reference D0.1). Correct.

"The order. Displacing adults evenly rather than the most exposed first raises the no-programme cost of 50% lost jobs from 9.0 to 10.6 points of basket poverty (Reference), and the full-coverage programme's cut grows by 1.5 points."

I don't have even-order tables in the condensed extract. Block D includes ord even at D0.5 jobs and hours. But not in condensed tables. Report states this as fact. Since it's from Block D which is in the full results, and the report says "the tables by fifth are in s85-q2-q3-q7-readings.md", this is likely correct but I can't verify from given data.

Section 6: "The high gain (16% more output per hour by year 20, against 2.2%) lowers poverty in both runs, so the programme's cut in basket poverty is 1.2 points smaller at 50% lost jobs (full coverage, Reference) and 1.5 points smaller with no displacement."

Programme effects: off (D0 low gain) basket poverty -32.95; jobs.D0.5 (high gain) -41.05. Difference 8.1 points? Wait, "programme's cut in basket poverty" means the programme effect (programme minus no programme). At D0 low gain: -32.60. At D0.5 high gain: -41.05. The cut is larger (more negative) with high gain. But report says "programme's cut in basket poverty is 1.2 points smaller at 50% lost jobs". Smaller cut means less reduction? Let's see: displacement's cost at D0.5 high gain no programme: 8.98. With programme: 0.53. Offset 8.45. At low gain D0.5: cost_N? Not directly given. Block B has D0.5 jobs at u 0.1 (low) and u 1.5 (high). The programme effect at low gain D0.5: from programme effects list, "jobs.D0.5" is at high gain (since Block A uses high gain). The low gain row would be separate. The report says "1.2 points smaller at 50% lost jobs (full coverage, Reference)". Probably comparing offset shares or programme effects between low and high gain. Without the low gain D0.5 programme effect, hard to verify. But the report references Block B which is in full results.

"The pass-through to pay (none or all of the gain instead of seven tenths) changes the programme's effects by 0.3 points or less." Plausible.

"The dividend at 50% lost jobs is 19% of wages; the labour share of income falls from 99.6% with no displacement to 84%, and the programme barely changes it."

From section 6: "The dividend at 50% lost jobs is 19% of wages; the labour share of income falls from 99.6% with no displacement to 84%, and the programme barely changes it." This is from Q3 tables (ohDiv, ohLab). Not in condensed extract but likely correct.

"The model's households receive 48% of the dividend within the run (the sourced 54%, less the last year's, which falls after the run)." Amendment 2 item 6: "The last year's dividend falls after the run and is not paid; ohPaid reports the share paid." 54% * (19/20) ≈ 51.3%, but with weighting and timing, 48% plausible.

"If they held all of it, the full-coverage programme's effect on median real wealth would be $902 larger." Plausible calculation.

"Who gains. Displacement moves wealth toward the top. With no programme, the top 1% share of wealth rises from 31.5% to 32.4% at 50% lost jobs (Reference) and the poorest fifth's mean real wealth falls from $32,103 to $23,166. The full-coverage programme lowers the top 1% share to 27.6% and raises the poorest fifth's mean to $158,768 (at full backing)."

These specific numbers (31.5%, 32.4%, 32103, 23166, 27.6%, 158768) are from Q3 tables (wtT1E, fifths). Not in condensed extract but likely correct.

Section 7: Backing produced table matches Block E.

"m names the share of programme work whose output people or businesses would otherwise buy... At m 1, all programme work counts. Even then inflation stays at 48-56 points a year (Reference, full coverage, 20 years)."

Ref c22 m1.ghigh.D0 48.0, D0.3 50.7, D0.5 52.6, D0.7 55.0. m1.glow.D0 49.2, D0.3 52.0, D0.5 53.8, D0.7 56.3. So 48-56 correct.

"With nothing produced (the floor), inflation is 58-63 points a year; at m 1 it is 48-56. The produced output takes off 1 to 10 points, depending on m; reaching 5 points a year would take 53 to 58 off the floor's rate."

Floor.D0 58.0, D0.5 63.4. m1.D0 48.0, D0.5 52.6. Difference: 10.0 and 10.8. So 10 points. At m0.25: 53.6 vs 58.0 = 4.4. m0.5: 51.8 vs 58.0 = 6.2. So 4-10 points. Report says 1-10. Close.

"Stricter accounting, in which only each year's added output absorbs new money, leaves a produced share near 1% and inflation 56-63 points."

Growth rows: ref c22 growth.m1.ghigh.D0 55.9, share 1.0; D0.5 61.4, share 0.9. Inflation 56-61. Report says 56-63. Close.

"The fuller valuation of capital (all value added per dollar, capped at 0.32) raises the share to 19% and lowers inflation by about 1 point."

vk.m1.ghigh.D0 46.9 vs m1.ghigh.D0 48.0 → -1.1. Share 19.3% vs 17.1%. Correct.

"The high gain on programme output and participants' own conversions add almost nothing (the conversions are none in these rows)."

Convgain vs gain: ref c22 convgain.m0.5.ghigh.D0 51.4 vs gain.m0.5.ghigh.D0 51.4. Same. Conv vs main: conv.m0.5.ghigh.D0 51.8 vs m0.5.ghigh.D0 51.8. Same. Correct.

"Displacement raises inflation at every m, by 2 to 9 points at 50% lost jobs: the price rule's income falls with wages, and the dividend is not counted in it."

Ref c22 m1.D0 48.0, D0.5 52.6 → +4.6. m0.5.D0 51.8, D0.5 56.7 → +4.9. m0.25.D0 53.6, D0.5 58.7 → +5.1. Adverse larger. 2-9 plausible.

Section 8: Displaced adults table matches.

"Every cell that does not offset or worsens is in the category table of section 4. In the full-coverage design there are none, in any environment or horizon."

Full coverage category tables: Reference has F and P only. Adverse all P. Stress all P. 40-year Reference has F and P. Adverse all P. Stress all P. So no N or W. Correct.

"In the opt-in design: at 20 years, 31 cells do not offset and 15 worsen, nearly all with lost jobs, and most in Adverse and Stress. Basket poverty worsens at every lost-jobs level in Adverse and Stress, and at 70% in Reference."

My count: opt-in 20 years N=30, W=15. Report says 31 and 15. Close (30 vs 31).

Basket poverty worsens (W) in opt-in lost jobs: Reference D0.7 (W), Adverse D0.1,D0.3,D0.5,D0.7 (all W), Stress D0.1,D0.3,D0.5,D0.7 (all W). So every lost-jobs level in Adverse and Stress, and 70% in Reference. Correct.

"At 40 years: 32 and 32." Plausible.

Section 9: Free time table matches.

"With shorter hours the hours are the same and more of them are secure (no programme: 191 of 494 in Reference)." Not in table but plausible.

Section 10: Matches.

Section 11: Matches.

Section 12: 40-year, not verified.

Section 13: "a fifth to two fifths of the fall in median wealth" - as noted, 13-40%, 13% < 20%. Understates lower bound.

"prices rise 18-82% a year" - 20-year max 70.5, 40-year might reach 82. But unqualified.

Section 14: "prices rise 48-69% a year in the full-coverage design" - Ref full coverage 20 years 48-63. 69 is higher (Adverse 70.5). But "in the full-coverage design" without environment/horizon qualification. Could be misleading.

Now, let me compile the answer for Question 1.

Key issues found:
1. Section 2: "97-100% of the rise in adult-years below 30 days of basic living" - actual 97-102% (Reference D0.1 lost jobs 102%).
2. Section 13: "a fifth to two fifths of the fall in median wealth" - actual 13-40%, 13% < 20% (a fifth).
3. Section 13: "prices rise 18-82% a year" - unqualified, 20-year max ~70.5, 82% likely 40-year Stress.
4. Section 14: "prices rise 48-69% a year in the full-coverage design" - Reference 20-year 48-63, 69 overstates for Reference.
5. Section 2: "Every one of the 144 tests at 20 years is significant: 136 'offsets in part' and 8 'offsets fully'." - This is for full coverage only. The sentence structure implies all 144 tests (which are full coverage 3 env × 48 = 144). But it says "Every one of the 144 tests at 20 years is significant" right after describing full coverage results. Actually reading: "With full coverage at full backing... Every one of the 144 tests at 20 years is significant: 136 'offsets in part' and 8 'offsets fully'." The 144 tests = 3 environments × 48 tests (6 outcomes × 8 cells). Yes, full coverage 20 years has 144 tests (48 per env × 3). And all are significant (no N or W). Correct.

Wait, but the report says "Every one of the 144 tests at 20 years is significant" in the full coverage paragraph. That's correct for full coverage.

But then "Of its 144 tests at 20 years, 98 offset in part, 31 do not offset and 15 worsen" for opt-in. That's separate.

Okay, so the main misquotes are the four I identified.

Let me also check: Section 2: "median real wealth is $7,158 to $48,326 lower" - tables show wtMedE cost_N: D0.1 7158, D0.7 48326. But medWealthReal: D0.1 7148, D0.7 48329. Report says "median real wealth" and gives wtMedE numbers. wtMedE is "median real wealth, weighted". The outcome list says "median real wealth, weighted (wtMedE) and unweighted (medWealthReal)". So using weighted is fine.

Section 4 table: "Below 30 days of basic living (in place of the savings measure) | 97-102% (98-100%)" - the 102% is from Reference D0.1 lost jobs offset share 1.02. But offset share = 1 - cost_P/cost_N. cost_N=0.40, cost_P=-0.01, offset=0.41, share=1.025. So 102.5%. Report says 102%. Correct.

But in Section 2 summary: "97-100%" - this drops the 102%. Understates.

Section 7: "reaching 5 points a year would take 53 to 58 off the floor's rate." Floor rate ~58-63. 58-5=53, 63-5=58. Correct.

Section 7: "the produced share near 1%" - growth rows show 0.9-1.0%. Correct.

Now, Question 2: Does the report follow the preregistration's decision rules?

Rule 2: Offset categories per primary outcome, D, form, environment, horizon; after Holm: offsets fully, offsets in part, does not offset, worsens. Report uses these categories in Section 4 category table. Good.

Rule 3: No category for Duke's words. "Prevents much of the distress" not a category. Report gives offset share with interval, and names every cell in "does not offset" or "worsens" (Q5) in same section as any favourable statement.

Check: Section 4 has category table with all cells. Section 8 (Q5) says "Every cell that does not offset or worsens is in the category table of section 4." And lists opt-in cells. Section 4 category table includes all. Rule 3 says "every 'does not offset' or 'worsens' cell named in the same section as any favourable statement". Section 4 has the category table showing all. Section 8 describes the unfavourable cells. Section 2 mentions "15 worsen". So favourable and unfavourable in same sections. Seems followed.

Rule 4: Stress readings D 0.5 and 0.7 at T 20 need output per hour to grow faster than forecasts (3.5% and 6.2% a year above trend). Wherever shown, labelled "stress readings, beyond the forecasts". No headline rests on them alone.

Report Section 1: "50% and 70% by year 20 are stress readings, beyond the forecasts: output per remaining hour would have to be 2.0 and 3.3 times today's by then, 3.5% and 6.2% a year above trend." Good.

Section 2: "At 40 years basket poverty rises 3.1 to 20.3 points in Reference." - includes stress? But 40-year stress not highlighted.

Section 4 tables include Stress D0.5 and D0.7. They are labelled in the environment name "Stress". The category tables have "Stress" column. The report doesn't explicitly label each Stress cell as "stress reading" in the tables, but the environment is named Stress. Section 1 defines them. Rule 4: "Wherever they are shown, they are labelled 'stress readings, beyond the forecasts'." In Section 4 tables, the column header is "Stress" not "Stress (stress readings, beyond forecasts)". But Section 1 defines it. The preregistration says "Wherever they are shown, they are labelled...". The report shows them in tables under "Stress" header. Is that sufficient? The preregistration example: "Stress readings: D 0.5 and 0.7 at T 20 need output per hour to grow faster than any forecast opened (3.5% and 6.2% a year above trend). Wherever they are shown, they are labelled 'stress readings, beyond the forecasts'." The report in Section 1 gives the label. In subsequent tables, they appear under "Stress". Might be considered labelled by context. But strictly, each table showing Stress D0.5/D0.7 should have the label. The condensed tables here just say "Stress". The report's Section 4 tables have "Stress" column. I'd say it's borderline but probably acceptable since Section 1 defines it clearly.

"No headline rests on them alone." Section 2 says "At 40 years basket poverty rises 3.1 to 20.3 points in Reference." - Reference, not Stress. Section 13: "in every environment" includes Stress, but the headline findings are for full coverage across environments. The "80-100% in every environment" includes Stress. But Stress is one of three environments. The headline "in every environment" includes Stress, but doesn't rest on Stress alone. Okay.

Rule 5: The backing produced: if programme inflation at produced share exceeds 5 points a year, any headline at full backing carries, in same paragraph, the produced share and that inflation.

Report Section 2: "But full backing is assumed, and the programme's own work does not produce it (point 4): at the backing it does produce (5-18% of the payout in this design), programme inflation is 48-69 points a year at 20 years." This is in the same paragraph as the full backing results. Good.

Section 13: "And the backing is not produced: the programme's own work, as measured here, matches at most about a sixth of the payout, and at that backing prices rise 18-82% a year." In same paragraph as full backing results. Good.

Section 14 (findings page): "Full backing is assumed, not produced: the programme's own work, as the model can measure it, matches 5-18% of the payout, and at that backing prices rise 48-69% a year in the full-coverage design." In same paragraph. Good.

Rule 6: Free time always split secure and insecure. No sentence calls free time a gain without the insecure part beside it.

Section 9: Table shows secure and insecure. Text: "Free time is mostly insecure without the programme... With no programme, 76-81% of those hours fall in households below their cost of living. With full coverage, 4-10% do; opt-in, 55-77%." Always gives both. Good.

Section 2: "and the free time displacement brings is mostly secure." For full coverage. But doesn't give insecure % in that sentence. However, it's in Section 2 summary, and Section 9 has the split. Rule 6: "No sentence calls free time a gain without the insecure part beside it." The sentence "the free time displacement brings is mostly secure" calls it a gain (mostly secure) without giving insecure part in that sentence. But it's a summary sentence. The rule says "Free time is always reported split. No sentence calls free time a gain without the insecure part beside it." This sentence in Section 2 says "mostly secure" implying a gain, but doesn't give the insecure % beside it. However, it's in the "answer in short" summary. The detailed split is in Section 9. Might violate strict reading. But "beside it" could mean in the same section/report. I'd flag it.

Rule 7: Interactions claimed only where intervals exclude zero; separate effects not summed where they interact.

Report Section 4: "The offset share, by form and design... Each cell's full figures, its costs in both runs and its category are in..." The offset is the interaction (cost_N - cost_P). Report gives offset shares with categories based on Holm-adjusted significance. Good.

Section 5: "The order. Displacing adults evenly rather than the most exposed first raises the no-programme cost... and the full-coverage programme's cut grows by 1.5 points." This is a separate effect (order), not summing interactions. Good.

Section 11: "Against the produced backing alone, the three readings shrink it by 1.1-2.8 points... and add 1.6-2.3 points of inflation." This describes the effect of adding the three readings (supply limit, wage indexing, BU delay) on top of produced backing. Not summing separate effects incorrectly. Good.

Rule 8: No tuning. Amendment 3 fixed choices after batch but before reading tables. Report mentions amendments. Good.

Now, specific violations:

Rule 6: Section 2 sentence "and the free time displacement brings is mostly secure" - calls free time a gain (mostly secure) without insecure part beside it. The insecure part for full coverage is 4-10%, but not stated in that sentence.

Rule 4: Stress readings in tables not explicitly labelled "stress readings, beyond the forecasts" in each table, only in Section 1 and column header "Stress". Preregistration says "Wherever they are shown, they are labelled...". The tables in Section 4 show Stress column without the full label. The condensed tables provided to me also just say "Stress". The report's own tables (s85-q1-displacement.md) might have the label. But based on what's in the report text, Section 4 tables are described as "across the three environments" with "Stress" column. Not explicitly labelled in the table. Could be a violation.

Rule 3: "every 'does not offset' or 'worsens' cell named in the same section as any favourable statement". Section 4 has category table showing all. Section 8 describes unfavourable cells. Section 2 mentions "15 worsen". So favourable (offsets in part/fully) and unfavourable (does not offset/worsens) are in same sections. Good.

Rule 5: Checked, seems followed.

Rule 2: Categories used correctly.

Rule 7: Seems followed.

Rule 8: Amendment 3 after batch but before reading tables - allowed as dated amendment with reason and full rerun (supplementary run for savings). The report says "A supplementary run... is under way". Amendment 3 says "Supplementary run: blocks A and F... rerun with o.sec on... same engine commit, seeds 1-500". The report says it's under way, not yet read. That's fine.

Now Question 3: Amendment 3 fixed several choices after batch finished. Could any favour the programme or let a result be chosen after seeing it?

Amendment 3 items:
1. Savings outcome substitute and supplementary run. The batch didn't have the preregistered savings measure (secM3A). Amendment 3 says: use bNAPy as substitute until supplementary run completes. Supplementary run will rerun blocks A and F (headline blocks) with o.sec on. This is a pre-specified fix before reading tables. The substitute bNAPy is "the batch's nearest stored measure". This seems cautious (bNAPy is "adult-years below 30 days of basic living" - a more severe measure). The preregistered measure is "share of adults with at least three months of cost of living in liquid savings" (security measure). bNAPy is different. But Amendment 3 says "Every statement says which of the two it uses." This is transparent. Could it favour the programme? The offset shares for bNAPy in full coverage are 97-102% (very high). If the real savings measure shows less offset, using bNAPy overstates. But the report says it's a substitute and the real measure is coming. The supplementary run is pre-specified (blocks A and F only). This seems proper.

2. Holm over 48 tests (6 primary readings × 8 cells) instead of 32 (4 outcomes × 8 cells). Amendment 1 had 32 (4 outcomes). Amendment 3 changes to 48 (6 readings: wealth poverty yearly and last year; median wealth weighted and unweighted; plus basket poverty and bNAPy). This is more conservative (more tests, harder to survive Holm). The preregistration said "Holm across the four primary outcomes within each question, environment, horizon and reading". But primary outcomes are 4: basket poverty, wealth poverty (yearly avg and last year? Wait: "wealth poverty, the yearly average over years 1-19 (ppovA), and at the last year (pov)" - that's two measures for one outcome? The outcomes list: "1. basket poverty (fgt0PY); 2. wealth poverty, the yearly average over years 1-19 (ppovA), and at the last year (pov); 3. median real wealth, weighted (wtMedE) and unweighted (medWealthReal); 4. savings...". So wealth poverty has two measures, median wealth has two measures. That's 6 measures for 4 outcomes. Amendment 1 said "Holm across the four primary outcomes... (32 tests)". Amendment 3 corrects to 48 tests (6 measures × 8 cells). This is more stringent, not favouring the programme. Good.

3. D 0 references: fixed which D0 row to use for each block. Pre-specified before reading tables. Good.

4. Signs: fixed sign convention (positive = harm). Pre-specified. Good.

5. Check 7 as inspection: money accounts residual not zero by construction (flat contribution financing), so printed not tested. This is a check change, not a result choice. Good.

None seem to favour the programme or allow cherry-picking. All fixed before reading tables.

Question 4: Opt-in design 'worsens' displacement's cost to basket poverty in many lost-jobs cells while still cutting poverty overall. Is the report's description fair? Mechanisms