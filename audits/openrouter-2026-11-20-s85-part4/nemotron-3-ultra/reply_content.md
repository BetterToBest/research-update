**1. Trace decomposition – validity, hidden assumptions, bias risk**  
The decomposition is an arithmetic identity *given the stored keys*:  
`W = s_Part·(Δ^P_Part − Δ^N_Part) + s_Non·(Δ^P_Non − Δ^N_Non)` with `s_g = k_g/(k_Part+k_Non)` fixed per seed. Amendment 4 item 4 states “the all-adult figure is the s-weighted sum of the two groups’ figures, exactly” and the 25-seed check confirmed “the stored group figures add up to the totals exactly (largest difference 0.0)”.  

**Hidden assumptions that could bias the *shares* (W_g/W):**  
- **Latent groups fixed per seed across all runs.** Amendment 4 defines them as “those who would take part… and those who would not… the same adults in every design and in the no-programme run”. If displacement *changes* who would opt in (e.g. because the contribution rate rises), the fixed partition misattributes the displacement-induced composition change. The trace itself shows enrolment *does* change slightly (−0.2 to +0.9 pp at 20 y), so the “would take part” type is not perfectly invariant.  
- **Harm-signing convention.** Positive = harm for poverty (run at D minus run at D 0). The offset = cost_N − cost_P. The decomposition uses `W = cost_P − cost_N = −offset`. This is consistent but any sign error would flip the shares.  
- **Paired differences, same 500 seeds.** The bootstrap resamples seeds jointly (Amendment 3 item 5), so the pairing is preserved.  
- **No separation of contribution from programme inflation for the non-participants.** Amendment 4 item 5: “The stored keys do not separate the contribution from programme inflation; the report says so.” The 11–29 % share attributed to non-participants is the *combined* burden.  

The decomposition is valid *for the defined latent groups*; the shares are unbiased *for those groups*. The bias risk is that the latent groups may not match the causal groups (e.g. adults who *actually* enrol under displacement), but the report explicitly labels them “adults who would take part” and notes the limitation.

---

**2. Sentences that overstate, understate or misquote the extract**  

| Report sentence (Section 4) | Extract value | Verdict |
|---|---|---|
| “The opt-in programme still cuts basket poverty by **7–26 points** against no programme at every displacement level.” | Stress 20 y D 0.7: displaced adults below basket programme/none = **80.44 / 82.94** → cut = **2.5 pp**. Minimum cut across all 12 cells ≈ **2.5 pp** (Stress D 0.7), maximum ≈ 25 pp (Ref D 0.1). | **Overstates the minimum** (7 vs 2.5). Should read “2.5–26 points” or “3–26 points”. |
| “The two parts are each wholly above zero in all but one cell at 20 years (Stress, 10 % lost jobs, where the second part is not).” | Adverse 20 y D 0.1: `W_Non 0.01 [0.00, 0.03]`. Lower bound is 0.00 (not *strictly* >0). Stress D 0.1 shows `[-0.00, 0.02]`. | **Understates the exceptions** – Adverse D 0.1 also has a lower bound at zero. Should say “in all but one or two cells” or clarify rounding. |
| “In the opt-in design with shorter hours one cell of 12 does at 20 years (Stress, 70 %; **52 % of it on those who would take part**)…” | The provided trace extract **only covers lost jobs (Block A)**. No shorter-hours trace data are in the packet. | **Unverifiable from the packet** – the 52 % figure comes from a table not supplied. Either add the shorter-hours trace or qualify/remove the claim. |
| “Severity as a whole rises **0.4 to 9.9 points less** with the programme at 20 years.” | `W2` values (negative = severity rises less): Ref D 0.1 −1.23 … Ref D 0.7 −9.86; Adverse D 0.1 −0.90 … Adverse D 0.7 −6.79; Stress D 0.1 −0.40 … Stress D 0.7 −2.86. Range of *magnitudes* 0.40–9.86. | **Accurate** (rounding to 0.4–9.9). |
| “The stand-in offset 97–102 % with full coverage; the preregistered measure 66–94 %.” (Section 2) | Full‑coverage lost jobs, 20 y: old (bNAPy) 97–102 % ✓; new (secM3A) **66–91 %** (Stress D 0.7 66 %, Ref D 0.1 91 %). The 94 % upper bound is not in the lost‑jobs extract; it may come from shorter hours (not shown). | **Slight overstatement of the upper bound** for the cells shown. Say “66–91 % in the lost‑jobs cells shown; up to 94 % including shorter hours” or provide the missing cells. |

---

**3. “Head count, not depth” – is it the only explanation?**  
No. The trace shows `W > 0` (headcount worsens) and `W2 < 0` (severity rises less) for the take‑part group in the worsening cells. At least two other explanations fit the numbers:  

1. **Floor/ceiling effect from the programme’s own poverty reduction.** At D 0 the programme cuts basket poverty sharply (e.g. Ref 20 y: from ~32 % to ~6 % adult-years with <3 mo savings). This compresses the distribution at the bottom: fewer adults are *far* below the line, so when displacement hits, the *only* room to move is just below the line. The headcount rises but the squared gap (FGT2) cannot rise as much because the gaps are truncated.  
2. **Selection into the latent “take‑part” group.** The “would take part” adults may be systematically closer to the poverty line at baseline (e.g. lower wealth, higher automation risk). Displacement pushes them across the line, while the “would not” group is already deeper in poverty (so their severity doesn’t change much). The trace does not show baseline distances to the line.  

**Extra measurement to tell them apart:** The adult‑level *distance to the poverty line* (or the density just above/below it) in both runs at D 0 and D > 0, split by latent group. Amendment 4 item 6 notes this is not stored: “The stored values do not show the adults just above the line… listed as open follow‑ups, not built.” FGT1 (poverty gap index) would also help – if FGT1 rises proportionally to FGT0 it’s pure headcount; if it rises less, gaps are shallow.

---

**4. Savings measure switch – handled fairly?**  
- **Process:** Amendment 3 fixed the switch *before any outcome table was read*. A supplementary run (blocks A & F only) added `o.sec`; Check 10 confirmed every other key identical row‑by‑row, seed‑by‑seed. The preregistered measure `secM3A` replaces the stand‑in `bNAPy` for the headline blocks; blocks B‑E keep the stand‑in (explicitly flagged).  
- **Direction of change:** The stand‑in gave **higher** offset shares (full coverage 97–102 % → “F”/“P” categories); the preregistered measure gives **lower** shares (66–94 % → mostly “P”). Category counts confirm: full coverage 20 y “F” drops from 8 to 2; opt‑in “W” rises from 15 to 17.  
- **Could it favour the programme?** No – it *reduces* the apparent effectiveness and *increases* the “worsens” count. The account in Section 2 (“the stand-in offset 97–102 %… the preregistered measure 66–94 %”) is fair for the lost‑jobs cells shown; the 94 % upper bound likely includes shorter hours (not in the extract). The change was pre‑registered, the supplement was a clean re‑run, and the more conservative measure was adopted. No hiding of unfavourable results.

---

**5. Clarity of “worsens” for a general reader**  
The report says:  
> “**What ‘worsens’ means here**… The opt-in programme still cuts basket poverty by 7–26 points against no programme at every displacement level. ‘Worsens’ means that cut is smaller with displacement than without it: displacement raises basket poverty more in the programme run than in the no-programme run…”  

This is **clear enough** – it explicitly states the programme still reduces poverty, and defines “worsens” as a *reduction in the size of that reduction*. A minor improvement for a lay reader:  
> “‘Worsens’ does **not** mean the programme increases poverty. The programme still lowers poverty compared to no programme, but displacement *shrinks* that gain – the rise in poverty caused by displacement is larger when the programme is running than when it is not.”

---

**6. Sceptic’s flags not mentioned in the report**  

| Flag in extract | Why a sceptic would note it | Report mention |
|---|---|---|
| **Opt‑in worsening triples at 40 y** (category counts: 20 y W=17 → 40 y W=37; magnitude up to 4.2 pp vs 2.2 pp). | Long‑run deterioration is much worse; the trace shows take‑part share falls to 62 % in Stress, meaning non‑participants bear a growing burden. | Section 4 notes “and again at 40” but does not highlight the scale increase. |
| **Savings measure switch adds “worsens” cells** (opt‑in 20 y W: 15→17; 40 y W: 32→37). | The preregistered measure reveals more harm than the stand‑in. | Section 2 reports the switch but Section 4 trace does not connect it. |
| **Full‑coverage W is large and negative** (−2 to −12 pp at 20 y) while opt‑in W is small positive (0.07–2.2 pp). | The programme *strongly mitigates* displacement under full coverage but *slightly amplifies* it under opt‑in – a stark design asymmetry. | Report notes “no full‑coverage cell worsens” but does not contrast the *magnitude* of the offset. |
| **Stress 40 y enrolment change = 0.00 at all D** yet worsening grows (W 0.23→1.99). | If enrolment doesn’t fall, the “stops short” mechanism isn’t via enrolment drops in Stress long run. | Report says “Enrolment does not fall” but doesn’t flag the zero-change / worsening coexistence. |
| **Latent groups fixed per seed** – assumes “would take part” type invariant to contribution rate (which rises 0.1–3.8 pp). | If higher contributions deter participation, the fixed partition misattributes the effect. | Amendment 4 defines the groups; report does not discuss the invariance assumption. |

---

**7. Three most important changes before publication**  

1. **Correct the poverty‑cut range** in Section 4:  
   > “The opt-in programme still cuts basket poverty by **2.5–26 points** (not 7–26) against no programme at every displacement level.”  
   (Trace: Stress 20 y D 0.7 cut = 82.94 − 80.44 = **2.5 pp**.)

2. **Remove or source the shorter‑hours trace claim** (“52 % on those who would take part”). The packet contains **only the lost‑jobs trace** (Block A). Either add the shorter‑hours trace tables (`s85-trace.md` for shorter hours) or replace the sentence with “The shorter‑hours trace is not shown here; see `s85-trace.md`.”

3. **Fix the “wholly above zero” count** for `W_Non` at 20 y. The extract shows Adverse D 0.1 `W_Non [0.00, 0.03]` – lower bound at zero. Change:  
   > “The two parts are each wholly above zero in all but **one or two** cells at 20 years (Stress 10 % lost jobs, and Adverse 10 % lost jobs where the lower bound is 0.00).”  
   (Or verify whether 0.00 is rounded from >0 and state the rounding convention.)