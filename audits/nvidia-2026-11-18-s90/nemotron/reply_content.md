1. **Is the diagnosis right?**  
Yes. The trace tool (`dev/tools/s90_trace.js`) isolates each price cut by switching it off in a copy of the engine. With the PTF (community) cut off, the two-year cycle persists (BU spent: $12,621, $20,987, $16,434, $19,677). With the private price off, the cycle disappears (BU spent: $23,394, $23,647, $23,287, $22,934, smooth). With both off, BU spent is flat. The same pattern holds in Adverse and Stress. The mechanism is a one-year feedback loop: the private cut is funded from last year’s premium; a large cut reduces this year’s BU spent, which shrinks the premium, which shrinks next year’s cut, producing a damped alternation. No other term is implicated.

2. **Is calling it a defect justified?**  
Yes. Duke’s design (Oct 1) states: “A privately owned ESP cuts its prices for customers paying in BU so that it stays revenue neutral. At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU.” The model’s own step decision said the same: “for BU spent at a private ESP, one BU buys as many essentials as the ESP’s conversion rate in dollars.” The code, however, paid the premium a year late and shared it by last year’s BU. The lag appears nowhere in the design text; it is a code–design mismatch (Rule 9: “the code did not do what its decision said”).

3. **Is the fix correct?**  
The algebra is sound and matches the design notes.  

- **At-sale price**: `vK = (1 − workers_share) × bizPremPerBU(p)`, where `bizPremPerBU` computes the premium per BU accepted net of conversion tax (`bizTaxRates`), face value, and ESP payroll share (`ESP.lam`), exactly as the year-end `bizNet` does. The shared function `bizTaxRates` guarantees the same formula at sale and at year-end.  
- **Budget-constrained BU spent**: `vQ` (share of BU spent at private ESPs) = `1−paW` (open access) or `1` (non-member) or `0` (PTF member). The cut `vC` solves `BU_spent = bill_remaining / (1 + vK·vQ)` when the budget covers it, else `vC = vK·vQ·fwBudget`. The code implements this as `vN = vR/(1+vG); vC = fwBudget>=vN ? vR−vN : vG·fwBudget` (where `vG = vK·vQ`, `vR = remaining bill`). Correct.  
- **Advance and repayment**: The cut is an advance (`SPS.carryV -= vC`). Next year, if `spVS && spVP ≤ 0`, the private premium `spVP` repays the advance (`SPS.carryV = spVP`); any shortfall carries. Unit tests confirm “the repayment leaves exactly the private share of the returned payroll premium (worst gap 1e-14).”  
- **Workers’ match timing**: The share at sale (`spSh[2]`) is saved in `SPS.vW` and used for the match (`spVW = spOwn * SPS.vW`), satisfying “the workers’ match is paid from that premium at the share in force at the sale.”  
- **Lagged residual**: Only the premium on payroll BU returned over workers’ caps (converted a year later, d73) is still shared by last year’s BU ($305, $73, $4 per adult in years 1–3, then zero). This is explicitly acknowledged and tested.  

No double-counting (community cut applied first, then private cut on the remainder), no lost money (advance fully repaid), no departure from the Oct 2 design note (which specifies the match comes out of the premium, leaving `1+vK` dollars per BU).

4. **Anything the fix changes not covered by the preregistration’s outcomes or checks?**  
All first-order effects are covered: primary outcomes (basket poverty, wealth poverty, BLEI, median real wealth, programme inflation), secondary outcomes (FGT2, mean real income, BU spent/expired, programme cost), and accounting identities (63 premium checks, ACCT on seeds 1–5 per environment). The preregistration also requires the lagged rows to match the published v5.9 rows bit-for-bit (check 1) and the engine commit to be clean (check 2). The only gap is that the PTF cut’s lag is not independently stress-tested beyond the trace tool’s single-run inspection; however, the trace tool already showed the PTF cut alone produces no cycle when the private price is at-sale, and the preregistration’s swing measure (Q1) is evaluated in all three environments.

5. **Are the preregistration’s decision rules sound and fixed before the run?**  
Yes. The preregistration was committed Nov 18, 2026 “before any run.” Rules are concrete and binding:  
- Checks 1–3 are gatekeepers; failure stops everything.  
- Q1 passes only if the at-sale swing measure is **below half the lagged swing in every environment**—a strict, pre-specified threshold.  
- Rule 3: “This holds whichever way the figures move” eliminates cherry-picking.  
- Rule 4 uses an objective criterion (sign change or rounding change) for findings-page statements.  
- Analysis script (`dev/tools/s90_tables.py`) is added before results are read; it prints checks first and stops on failure.  
- Paired seeds (1–500), common random numbers, fixed bootstrap seed (9001), Holm correction across five primary outcomes per cell, all intervals published unadjusted.  
- Amendments must be dated with reasons; nothing above the line changes after first run.  
No discretionary levers remain.

6. **Is the plain-words report accurate and fair?**  
Yes. It mirrors the decision record without overclaiming:  
- Quantities match (BU spent series, income series, vK values, residual payroll premium).  
- Caveats are explicit: “first look on two seeds (not a result),” “until then the swing is a stated limit,” “the preregistered rerun… will measure the change… Its results will be published whichever way they come out.”  
- It correctly explains why the at-sale price is $1.90 not Duke’s $3 (“conversion tax, payroll and the workers’ match come out of the premium too”).  
- It notes the PTF cut remains lagged by design and shows no swing once the private price is fixed.  
No statement exceeds the evidence.

7. **Three most important changes I would make**  

1. **Treat the fix as a candidate correction until the preregistered rerun passes its decision rules.**  
   The decision record reads as if the fix is already the corrected model (“If rule 2 holds, the at-sale price is the corrected model… This holds whichever way the figures move”). But Rule 2 has not yet been evaluated. The plain-words report correctly frames it as pending (“The fix (built, off until a rerun)”). I would amend the decision record to state explicitly: *This fix is a candidate; it becomes the corrected model only after the preregistered run satisfies checks 1–3 and Rule 2.*

2. **Quote the PTF design text that justifies its lagged surplus split as “a reading of the design.”**  
   The decision record says the PTF cut “is a reading of the PTFs’ design (their premium is split three ways once the year’s surplus is known)” but no PTF design text is quoted in the materials provided (only Duke’s private-ESP quote appears). Without the source text, one cannot verify that the lag is a design reading rather than a second defect. I would require the PTF design excerpt to be cited in `dev/DECISIONS.md` alongside the private-ESP quote.

3. **Add a preregistered sensitivity check for the workers’ match share transition (swYear).**  
   The share `spSh[2]` changes from 1/3 to 0.4 when community capacity is reached (`swYear`). The at-sale price saves `SPS.vW = spSh[2]` once per year during the surplus-split block. If `swYear` falls mid-year (or if the capacity threshold is crossed between the surplus-split calculation and a sale), the saved share may not match the share “in force at the sale” for every transaction. The preregistration does not test this edge case. I would add a check that the share used at sale equals the share that would apply if the surplus split were recomputed at the moment of each sale, or at least document that the annual snapshot is a modelling assumption with a bounded error.