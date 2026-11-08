# Handoff (Nov 8, 2026): S55 done, the open-access report

## Step status
S55 is **done** (parts 1-4). Part 4 wrote the report from the nine 500-seed runs, which all finished with `DONE`. S7 now waits only on S5.

## What shipped
- compassionism-simulation [PR 83](https://github.com/BetterToBest/compassionism-simulation/pull/83) (analysis only, no engine change): report `dev/reports/s55-open-access.md`, tables `dev/runs/s55-open-access/tables.md`, every estimate `estimates.csv`, tool `dev/tools/s55_open_access.py` (17 checks pass: pilots equal seeds 1-50 of the full runs; S38's bootstrap reproduced exactly; operations never binds in the main reading; and so on), DECISIONS.md (S55 part 4), HANDOFF.md.
- Results used: compassionism-sim-results `prog-{t,u,u10,v,v10,vj,w,w10,y}-0c93593` (runs 86-94 of `run-study`, all succeeded) against `prog-{a,b,b10,g,g10,h,i,j}-ce8d030`.
- research-update PR for this session: PLAN.md (S55 done; notes for S7) and this file.

## Findings (plain words; the report has every setting)
- Headline (C2.2 design, Reference, 10,000 adults, 20 years): open access against members only moves basic living +0.03 points, the cost of living +0.14, cost +$1,398 (2.3%) and inflation -0.64 points a year. None of these is material. Wealth moves +2.42 points, which is material: the programme's wealth effect turns from -0.19 to +2.23.
- 14 of 120 effects are material: wealth under the C2.2 design (10 of 12 settings) and inflation (C2.2, 40 years, Adverse and Stress). None is material under the release design. 500 and 10,000 adults give the same decisions.
- Rule 2: the wealth result depends on the demand ceiling (a design parameter) and on the share growing. It is gone at a 25% ceiling, with outside running costs or with growth off. At 75-100% it is larger, and cost and inflation turn material too.
- Capacity binds first, then demand; operations never in the main reading. The fixed-share curve is smooth, with no step at 55% and one at 40% (wealth, C2.2, Adverse). CCO x PTF becomes a material wealth synergy. The layer still changes nothing material.

## In flight
- Nothing.

## Decisions waiting
- None new.

## Next step
**S5** (participation threshold; sonnet, medium): row 21 of the Order table; S7 waits on it. S39 can also start.

## Pitfalls
- The 2,000-adult layer comparison under open access could not be formed: the addendum preregistered no open row without the layer at 2,000 adults. The report says so; nothing was run outside the preregistration.
- The fixed-share curve is not monotone at its low end. Under C2.2 in Reference and Adverse, wealth is better at 10% than at 20-30%. This is untraced. PLAN.md's S7 section asks for a check before the findings page uses the curve.
- Paired 500-seed comparisons detect effects of a few hundredths of a point. "Stated" (interval excludes zero) is not "material"; keep the two apart in any Hub text.
- The results repository is 4.8 GB checked out (`prog-b-ce8d030` alone is 370 MB). Clone it shallow with a long timeout. The S55 script reads all 17 folders and the 5 pilots in about 70 seconds.
