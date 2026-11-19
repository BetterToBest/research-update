Let me analyze this complex economic microsimulation review request carefully. I need to answer 7 specific questions based on the provided materials.

First, let me understand the context:
- This is the "Compassionism Simulation" - an economic microsimulation
- There's a "two-year swing" in BU (Basic Units) spent per adult
- The issue is traced to a one-year lag in private businesses' lower BU price
- A fix has been implemented behind a switch `sp.vAt: 'sale'`
- There's a preregistration for a rerun to test the fix

Let me go through each question systematically.

## 1. Is the diagnosis right? Does the evidence show that the private businesses' lagged price, and not something else, causes the two-year swing?

From the decision record (S90):
- They used `dev/tools/s90_trace.js` which runs a copy of the engine with read-only probes
- They turned off each cut one at a time:
  - With PTF (community) cut off: cycle stays (BU spent $12,621, $20,987, $16,434, $19,677)
  - With private price off: cycle goes (BU spent $23,394, $23,647, $23,287, $22,934, smooth)
  - With both off: BU spent are flat
- Same in Adverse and Stress environments

The mechanism: Private price paid from last year's premium → large cut this year → fewer BU spent this year → smaller premium → smaller cut next year → feedback with one-year lag → BU spent alternate around equilibrium level.

This seems like strong evidence. The trace tool isolates each component, and the private price being the sole cause of the cycle is demonstrated by the "off" tests. The mechanism is clearly explained and consistent with the observed damped oscillation.

## 2. Is calling it a defect (not a reading of the design) justified by the design text quoted?

Design text from Duke (Oct 1):
> "A privately owned ESP cuts its prices for customers paying in BU so that it stays revenue neutral. At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU."

The model's own earlier decision: "for BU spent at a private ESP, one BU buys as many essentials as the ESP's conversion rate in dollars"

The code paid the premium a year late (shared by last year's BU). The design says the price is set "at the sale" - meaning at the time of transaction, not a year later.

The lag is not in the design text. The design explicitly gives an example of immediate price conversion ($9 becomes $3 at 3x). The code implemented a lagged version. Rule 9: "the code did not do what its decision said."

This seems justified. The design clearly describes an at-sale price setting, not a lagged one.

## 3. Is the fix correct? Check the algebra...

Let me trace through the fix algebra carefully.

### The at-sale price formula:
From the decision record: "one BU spent at a private ESP buys 1 + vK dollars of essentials, vK = (1 - the workers' match share) x the premium per BU accepted (`bizPremPerBU`: the conversion at `FW.bizRate` under the progressive tax, less face value, less ESP payroll's share, exactly as the year end computes `bizNet` per BU)"

From the code diff:
```javascript
function bizPremPerBU(p){ 
  if(PATHWAY_OFF.conversion)return 0; 
  var t=bizTaxRates(p),
  m=(ESP?1-ESP.lam:1)*(FW.bizCap*FW.bizRate*(1-t[0])+(1-FW.bizCap)*(1-t[1])-1); 
  return LVS?Math.max(0,m):m; 
}
```

And:
```javascript
SPS.vK=Math.max(0,(1-spVw)*bizPremPerBU(p));
```

Where `spVw = spSh[2]` (the workers' share, 1/3 initially, then 0.4).

So vK = (1 - workers_share) * premium_per_BU

Premium per BU = (1 - ESP.lam) * [FW.bizCap * FW.bizRate * (1 - taxR) + (1 - FW.bizCap) * (1 - taxP) - 1]

This is the net premium after conversion tax and payroll share.

### The budget-constrained BU spent:
"BU spent = bill / (1 + vK q) when the budget covers it, the whole budget otherwise"

Where q = share of BU spent at private ESPs (1 - paW under open access; all for non-member; none for PTF member)

From code:
```javascript
var vQ=PAS?1-paW(a):(p.ptf&&a.inPTF)?0:1,
vG=SPS.vK*vQ,
vR=Math.max(0,mainLoopCostUSD*essF-spC);
if(vG>0&&vR>0){
  var vN=vR/(1+vG),
  vC=fwBudget>=vN?vR-vN:vG*fwBudget,
  ...
}
```

Let me verify: 
- vR = remaining essentials bill after community cut (spC)
- vG = vK * vQ = effective discount rate on BU spent at private ESPs
- If budget covers it: BU spent = vN = vR / (1 + vG)
- Then cut vC = vR - vN = vR - vR/(1+vG) = vR * vG/(1+vG) = vG * vN
- But vN = BU spent at private ESPs? Wait...

Actually, vN = vR/(1+vG) is the BU spent (since each BU buys 1+vG dollars of essentials, so to cover vR dollars you need vR/(1+vG) BU).
Then vC = vR - vN = the cut (BU freed).

But the code says: `vC=fwBudget>=vN?vR-vN:vG*fwBudget`

If budget >= vN (BU needed), then vC = vR - vN (the full cut)
If budget < vN, then vC = vG * fwBudget (partial cut proportional to budget)

This seems correct.

### The advance and repayment:
"The cut is paid as an advance (the private carry goes negative by it) and next year's premium repays it exactly."

From code:
```javascript
if(spVS&&spVP<=0){
  agentSet.forEach(function(a){a._spV=0;});SPS.carryV=spVP;
}
```

And:
```javascript
SPS.carryV-=vC;  // when applying the at-sale cut
```

So carryV starts at 0, goes negative by vC (the advance), then next year spVP (the private premium) repays it.

The decision record says: "What the premium leaves after the repayment is the premium on ESP payroll BU returned the next year (d73: the payroll pool an ESP cannot pay to its participating workers is converted a year later); that part cannot be known at the sale and is shared as before, by last year's BU."

From the results: "The premium left after the repayment is $305, $73 and $4 per adult in years 1-3 (payroll returned while workers' caps bind), then zero; nothing stays in the carry."

This seems consistent.

### Share of BU attributed to private businesses:
vQ = PAS ? 1-paW(a) : (p.ptf && a.inPTF) ? 0 : 1

This matches: "the share the model already uses to size the PTFs' share (1 - paW under open access; all of a non-member's BU otherwise; none of a PTF member's)"

### Potential issues to check:
1. **Double-counting**: The community cut (PTF) and private cut are separate. The private cut applies after community cut (vR = bill - spC). The code applies community cut first, then private cut on remainder. This seems correct - they're sequential discounts.

2. **Losing money**: The advance is repaid from next year's premium. The premium is calculated on BU accepted, which includes the BU spent at private ESPs. Since the cut reduces BU spent, it reduces premium, but the repayment is exactly the advance amount. The decision record says "next year's private premium repays it exactly" and tests confirm "the repayment leaves exactly the private share of the returned payroll premium (worst gap 1e-14)".

3. **Departure from design**: The design says "At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU." That's 1 BU = $3 of essentials. But the fix gives 1 BU = 1+vK dollars, where vK ≈ 0.90 initially, so 1 BU = $1.90. The report explains: "because the conversion tax, payroll and the workers' match come out of the premium too. That is the same price, on average, as the lagged rule settled to; only its timing changes."

Wait - the design says 1 BU = $3 at 3x conversion. But the model has conversion tax, payroll share, and workers' match that reduce the premium. So the actual premium per BU is less than 2 (which would give 1 BU = $3). The design might be simplified, or the model adds real-world frictions. The report acknowledges this: "a BU spent there buys about $1.90 of essentials rather than Duke's $3, because the conversion tax, payroll and the workers' match come out of the premium too."

This is a modeling decision, not necessarily a defect. The design note from Oct 2 says: "the match comes out of the premium itself: a private ESP gives its workers the same fraction of its premium that a community ESP gives its workers... and the rest becomes lower BU prices."

So the fix is consistent with the Oct 2 design note, which elaborates on Duke's Oct 1 design.

### Code diff checks:
- `bizTaxRates` function moved to shared location (used by both year-end and at-sale price) - good, ensures consistency
- `bizPremPerBU` function computes premium per BU exactly as year-end does
- `spVS = spVOn && SURP.vAt === 'sale'` - new flag for at-sale mode
- `SPS.vK` computed as `(1-spVw)*bizPremPerBU(p)` - correct
- At-sale cut applied in the spending loop with budget constraint - correct
- Advance tracked in `SPS.carryV` (goes negative)
- Next year: if `spVS && spVP <= 0`, carryV = spVP (repayment), no distribution to agents
- Else (lagged mode): distribute spVP by last year's BU weights
- Workers' match share at sale uses `SPS.vW` (saved from spSh[2] at sale time) - correct, uses share in force at sale

One subtle point: In the lagged mode, `spVW = SURP.privWk==='none'?0:spOwn*spSh[2]` (current year's share). In at-sale mode, `spVW = SURP.privWk==='none'?0:spOwn*(spVS&&SPS.vW!==undefined?SPS.vW:spSh[2])` - uses saved share from sale time. This is correct per design: "the workers' match is paid from that premium at the share in force at the sale."

The fix appears algebraically correct and consistent with the design notes.

## 4. Is anything the fix changes not covered by the preregistration's outcomes or checks?

Preregistration outcomes:
- Primary: below 30 days basic living; basket poverty; wealth poverty; median real wealth; programme inflation
- Secondary: FGT2; mean real income; BU spent/expired; programme cost; weighted versions

Checks:
1. Lagged rows = published v5.9 rows per seed
2. Every folder has 500 seeds, engine commit, clean engine, run.txt, SHA256SUMS
3. Accounting checks (ACCT) pass on at-sale rows for seeds 1-5 per environment

The fix changes the timing of the private price cut, which affects:
- BU spent per year (directly)
- Incomes (through conversion and workers' match)
- Poverty measures (through BU spent and incomes)
- Wealth (through savings)
- Prices/inflation (through money supply effects)
- Programme cost

All these seem covered by primary/secondary outcomes.

But: The preregistration says "No synergy claim is made (one change, not a factorial)." The fix only changes the private price timing. The community (PTF) price cut remains lagged. The decision record says: "Fix the PTFs' price cut too; not taken: a surplus split distributed after the year is a reading of the PTFs' design... and with the private price at the sale it shows no cycle."

So the PTF cut stays lagged. The preregistration doesn't explicitly test whether the PTF cut alone would cause a cycle (but the trace tool showed it doesn't - with private price off, cycle goes even with PTF cut on).

What about the "small part cannot be known at the sale: payroll BU that a business could not pay out and converts the next year. That part is shared a year late, as before"? This is included in the fix and tested ("the repayment leaves exactly the private share of the returned payroll premium").

The preregistration checks accounting identities including "the premium identity". So this should be covered.

One thing: The preregistration tests on seeds 1-5 for accounting checks, but the full run is 500 seeds. The accounting checks on 5 seeds might not catch rare edge cases. But the unit tests include "no accounting identity fails in the main row in three environments (63 premium checks)" - this seems more comprehensive.

Also: The preregistration says "The analysis script is added to compassionism-simulation (`dev/tools/s90_tables.py`) before the results are read; it prints checks 1-2 first and stops if one fails." So the analysis is pre-committed.

I don't see obvious gaps. The outcomes cover the main effects, and the checks cover reproducibility and accounting.

## 5. Are the preregistration's decision rules sound and fixed before the run? Anything that could let a result be chosen after seeing it?

Decision rules:
1. If checks 1,2,3 fail → stop, nothing read, defect found, redo after dated amendment
2. Q1: fix works if at-sale swing measure < half lagged swing in EVERY environment. If not, stop and report; default does not change.
3. If rule 2 holds → at-sale price is corrected model. Figures replace main rows at next release. Lagged figures stay as v5.9 record. "This holds whichever way the figures move."
4. Q3: findings-page statement changes if at-sale effect changes sign or rounding changes. List each changed statement.
5. Other published studies get dated notes; reruns are separate preregistered amendments.

Key points:
- Committed Nov 18, 2026 "before any run"
- Engine at specific commit (ENGINE_HASH, after PR)
- Run on GitHub Actions (free, public)
- Seeds 1-500 paired across all rows (common random numbers)
- Analysis script added BEFORE results read
- Holm correction across 5 primary outcomes per cell for "change is not zero"
- All intervals published unadjusted too
- "Every cell above is published... including changes against the programme and changes too small to matter."
- Amendments must be dated with reason; nothing above changes after first run.

This looks very sound. The rules are fixed, public, and binding. The "whichever way the figures move" in rule 3 is crucial - no cherry-picking. The paired design with common random numbers reduces variance. The bootstrap intervals with fixed generator seed (9001) are reproducible.

Potential concern: Rule 2 says "in EVERY environment" the swing measure must be below half. What if it passes in 2 of 3? Then "stop and report; the default does not change." This is conservative but pre-specified.

Rule 4 about findings-page statements changing sign or rounding - this is a clear, objective criterion.

The only flexibility I see: "Duke assigns the version" for the next release - but that's just version numbering, not result selection.

## 6. Is the plain-words report accurate and fair to the evidence (no overclaiming)?

Let me check the plain-words report against the decision record and preregistration.

Report claims:
- "The swing is in every programme row, and it was behind the swing in the cash share that the supply study (S82) found." - Decision record: "It reaches incomes... and every figure built on BU spent, expired BU, project hiring or programme cost by year." S82 not directly quoted but plausible.
- "A trace of one run, turning each cut off in a copy of the engine (never the engine itself), shows that the private businesses' price causes the swing. With the community cut off, the swing stays; with the private price off, it goes." - Matches decision record exactly.
- "The private price was paid from last year's premium." - Yes.
- "Average incomes swing with them ($72,358, $92,808, $81,544, $98,970 in years 1-4)" - Matches decision record.
- Design quote from Duke - matches.
- "The model's own decision for that step said the same... but the code paid the premium a year late." - Matches decision record (Rule 9).
- Fix description: "One BU spent at a private business buys 1 + vK dollars of essentials, where vK is the premium the business will earn on that BU (after the conversion tax and the share kept for business payroll) less the workers' share of it." - Matches.
- "vK is about 0.90 at first and 0.81 once community capacity is reached (0.79 and 0.71 in the Stress Test): a BU spent there buys about $1.90 of essentials rather than Duke's $3, because the conversion tax, payroll and the workers' match come out of the premium too." - Matches decision record results.
- "The cut is paid as an advance, and next year's premium repays it exactly." - Matches.
- "One small part cannot be known at the sale: payroll BU that a business could not pay out and converts the next year. That part is shared a year late, as before ($305 per adult in year 1, $73 in year 2, $4 in year 3, then nothing in the main row)." - Matches decision record.
- "With the option on, the swing is gone in all three environments: the BU spent per adult in Reference run $16,815, $16,590, $17,392, $17,592, $17,981, and stay within $16,236-18,195 after that, and incomes rise smoothly." - Matches decision record.
- "The option is off by default, so every published figure is unchanged and the registered v5.9 model can still be reproduced (the guard test is identical in every output)." - Matches.
- "Every programme row uses the private rule, so every published programme figure since v5.0 (Oct 2, 2026) is reached." - Decision record: "Every published programme figure since v5.0 (Oct 2) uses the private rule: the v5.9 main rows and readings... the central-bank and history studies, S82, and the v5.0-v5.6 panels."
- "A first look on two seeds (not a result) shows small changes, all in the programme's favour: the cut in basket poverty grows by about 0.6-0.7 points (Reference: 32.3 to 33.0 points), the deepest-poverty measure (FGT2) by about 0.1, and median real wealth by $200-1,200." - Decision record: "Reference -32.32 to -32.99 points... FGT2 about 0.1 points more; median real wealth +$856 (Reference), +$1,179 (Adverse), +$228 (Stress)." The report says "32.3 to 33.0" which is 0.7 points, and decision record says -32.32 to -32.99 which is 0.67 points. Close enough. Wealth: report says $200-1,200, decision record says $228 to $1,179. Accurate.
- "The preregistered rerun... will measure the change on 500 paired seeds in all three environments. Its results will be published whichever way they come out." - Matches preregistration rule 3.
- "Until then the swing is a stated limit of every programme row." - Accurate.
- "The community businesses' cut stays as it is: their premium is split three ways... once the year's surplus is known, which is a reading of their design. With the private price at the sale, it shows no swing." - Matches decision record alternative (c).

The report says "Written by Claude" and "A plain-words report of research-update step S90". It accurately reflects the decision record without overclaiming. It explicitly says "not a result" for the two-seed look. It says "the swing is a stated limit" until the preregistered rerun. It acknowledges the Duke design gives $3 but model gives $1.90 due to taxes/payroll/match.

One minor thing: The report says "the BU paid each month keep their value and the cost of living hardly moves." The decision record doesn't explicitly state this, but it's implied by "the BU paid per month holds its real value" in the question section. Seems consistent.

Overall, the plain-words report appears accurate and fair, with appropriate caveats.

## 7. The three most important changes you would make.

Based on my analysis:

1. **Run the preregistered rerun before declaring the fix "correct" in any final sense.** The plain-words report says "The fix (built, off until a rerun)" and "Until then the swing is a stated limit of every programme row." But the decision record presents the fix as the chosen path. The preregistration is the proper test. The fix should not be considered validated until the preregistered rerun passes its checks and decision rules. (Though the report acknowledges this, the decision record reads as if the fix is done.)

2. **Test whether the PTF (community) price cut's lag could cause issues in other scenarios.** The trace tool showed that with private price fixed, the PTF cut alone shows no cycle. But this was tested in the main row (Reference, seed 1). The preregistration only tests the at-sale fix on the v5.9 main rows. What about other configurations (different parameters, environments, horizons)? The decision record says "with the private price at the sale it shows no cycle" but this was only checked in the trace tool on main row. A more systematic check would be valuable.

3. **Clarify the relationship between Duke's design ($3 at 3x) and the model's $1.90.** The report explains it ("conversion tax, payroll and the workers' match come out of the premium too"), but this is a significant deviation from the design's illustrative example. The design note from Oct 2 says "the match comes out of the premium itself" and this was a modeling decision. But Duke's original design might have assumed no conversion tax or payroll share. This should be explicitly flagged as a modeling choice with its own justification, not just an implementation detail. The preregistration doesn't test this assumption.

Actually, let me refine these based on the materials:

1. **The preregistration should be executed and its results published before the fix is treated as the corrected model.** The decision record says "If rule 2 holds, the at-sale price is the corrected model. Its figures replace the main rows' figures at the next release... This holds whichever way the figures move." But this is contingent on the preregistered run. The plain-words report correctly frames it as pending. But the decision record reads as a done deal. I'd make the dependency explicit: the fix is a *candidate* correction until the preregistration confirms it.

2. **Add a sensitivity check on the workers' match share timing.** The fix uses the workers' share "in force at the sale" (saved in SPS.vW). But the share changes at "swYear" (when community capacity is reached, from 1/3 to 0.4). If the sale happens near that transition, which share applies? The code saves `spSh[2]` at the time of the surplus split calculation (which is at year start?). Need to verify this is consistent. The preregistration doesn't explicitly test this edge case.

3. **Document the assumption that the PTF cut's lag is "a reading of the design" more rigorously.** The decision record says the PTF surplus split is "distributed after the year is known" and this is "a reading of the PTFs' design." But the design text for PTFs isn't quoted in the materials provided. Only Duke's design for private ESPs is quoted. The Oct 2 design note says "community-owned businesses (PTFs) give from their share of the premium" but doesn't specify timing. This should be explicitly justified with design text, not just asserted.

Let me check the Oct 2 design note again: "The community businesses' cut stays as it is: their premium is split three ways (price cuts, reinvestment, workers) once the year's surplus is known, which is a reading of their design." But where is the PTF design documented? The decision record mentions "Duke's design (Oct 1, quoted in `dev/reports/v5-1-private-esp-correction.md`)" but that quote is only about private ESPs. The PTF design might be in a different document. This is a gap.

So my three changes:

1. **Treat the fix as a candidate until the preregistered rerun passes** - don't present it as the corrected model in the decision record until the preregistration's decision rules are satisfied.

2. **Provide the design text for PTF surplus split timing** to justify that its lag is a "reading of the design" rather than a defect, or fix it if it's not.

3. **Add a preregistered sensitivity test for the workers' match share transition timing** (when community capacity is reached and share changes from 1/3 to 0.4) to ensure the at-sale price uses the correct share for each transaction.

Actually, looking at the code: `SPS.vW=spVw` where `spVw=spSh[2]` is set inside the `if(spVS)` block during the surplus split calculation. The surplus split runs once per year at the start of the year (before the spending loop). So all at-sale prices that year use the same share. If the share changes mid-year (unlikely, swYear is probably a year boundary), it would use the old share for the whole year. This should be documented and tested.

Let me finalize my three changes with concrete quotes.