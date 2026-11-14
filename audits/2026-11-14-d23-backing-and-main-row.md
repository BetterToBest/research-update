# What D23 is about, how the main row counts backing, and what the main row will show (Nov 14, 2026)

Written in the S69 session, at Duke's request: "I believe there is again some version drift concerning the design and my decisions. The design was set to count conversions as backed by new output, and there was a sweep to show this as a curve. That's where the low-to-no inflation came from. But maybe D23 is about how BUs are paid for." This note sets the two questions apart, says what the candidate main row does today, and says what round 2 will display. Nothing in the engine changes.

## In short
- **Two separate questions got merged.** One is *backing*: how much of the money the programme pays out is matched by new goods and services. The other is *paying for it*: whether the Source creates the money for the BU and conversions, or a tax raises it. D11 (Nov 1) was the backing question. D21 (Nov 9) and D23 (Nov 13-14) are the paying-for-it question.
- **Your second reading is right.** D23 is about how the BU are paid for. It covers one row: the C2.2 design paid for by a flat contribution on wages instead of by the Source. It is not about backing.
- **That row's "0.1 points of inflation" was not backing.** It came from a gap in the books. Between 39% and 52% of the row's cost was raised by no one and was never counted as new money, so prices never saw it. With every dollar counted (S68, S72), the row has 32-49% inflation a year, or, if the rest is borrowed, public debt larger than the whole economy by year 5.
- **The backing curve you remember exists, and it is where "no inflation" comes from.** S51 swept the backed share from 0% to 100%. At 100% ("every dollar backed"), programme inflation is zero, but zero by assumption: the model is told every dollar is matched, it does not find that it is.
- **The drift is real, on the display side.** The round-2 main row counts as backed only the output the model can see being sold. No round-2 step was set to carry the backing curve beside it. The 500-seed curve from round 1 ran on Nov 7 and no step reports it. Both are fixed below: S63 now carries the curve on the round-2 main row, and S64 reports both curves.
- **Your decision, the same day:** the design is full backing. The round-2 main row therefore takes full backing (every programme dollar matched by output), with the backing curve shown beside it. D23 is filed again in the ledger now.

## 1. Backing (D11): how much of the payout is matched by new output
- **The design's claim.** Conversions are backed by output the community chooses to fund. Your answer to D11 (Nov 1): backing is the design's requirement. The model therefore treats backing as something to measure, not something to assume, and it reports the *break-even* backed share: how much of the payout must be matched for poverty to fall without harm.
- **What S51 built (Nov 2).**
  - A mechanism in which conversion pay funds projects whose output enters supply after a lag (row option `bkm`).
  - A sweep of the backed share, from 0% to 100%, crossed with how far wages keep up with prices. This is the curve. Inflation falls as the backed share rises, and reaches zero at 100% because nothing is left unmatched.
- **What the S51 pilot found (50 seeds).**
  - C2.2 cuts basket poverty with nothing backed, because its BU rises every year with the price of basic needs.
  - The release design needs 32-75% backed before wealth poverty is no worse than without the programme.
  - Under the mechanism's main reading, the projects back about 1% of the release design's payout. With no ceiling on what they can produce, they back at most about a fifth.
- **The full curve at 500 seeds.** The frozen batch ran it on Nov 7 (study M, results folder `m-ce8d030` in compassionism-sim-results). It has not been tabulated or reported. That is one reason you are not seeing it.

## 2. Paying for it (D21, then D23): who pays for the BU and the conversions
- **The two ways.** Under the Source, the Source creates the money for the BU and the conversions; whatever is not matched by output is new money, and it raises prices. Under a contribution, a tax raises the money instead.
- **D21 (Nov 9).** It asked about one row: C2.2 paid for by a flat contribution on wages. That row came from the S54 levers pilot, at 0.1 points of inflation a year. You answered that the Hub may lead with it.
- **The Nov 13 audit's finding.** The contribution must average 84% of wages, and it hits its 90% cap by year 20 in every seed. The 39-52% of the cost it cannot raise was counted nowhere. That is where the low inflation came from.
- **D23 (filed Nov 13).** It asks what the Hub may do with that row once it is computed consistently. You answered: carry it beside the main rows; the Hub does not lead with it until S72's financing frontier is in; then you decide again. Today (10:17-10:22 UTC) you reopened D23 and added your note on backing. You then confirmed the same answer.
- **What S72 found (pilot, 100 seeds).** Reference / Adverse / Stress; poverty figures are changes from no programme, in points:

| Row | Programme inflation, % a year | Basket poverty | Wealth poverty, year 20 |
|---|---|---|---|
| C2.2, the Source (the main row's financing) | 41.9 / 49.0 / 52.4 | −29.6 / −38.1 / −37.2 | −21.7 / −22.6 / −20.8 |
| C2.2, contribution on wages, the rest as new money (D21's row, counted fully) | 32.0 / 45.0 / 41.4 | −20.0 / −24.4 / −16.6 | −16.3 / −16.2 / −14.2 |
| C2.2, contribution on wages, the rest borrowed | 0.1 / 0.2 / 0.2 | −25.5 / −34.2 / −31.6 | −19.5 / −23.0 / −19.9 |
| Release design, the Source | 36.5 / 43.4 / 18.9 | −18.4 / −22.1 / −7.9 | −14.8 / −14.3 / −7.8 |

  On the third row, programme debt passes the size of the whole economy in year 4 or 5 and keeps growing. The only C2.2 contribution that comes close is one on all money income, at 69-78% of it, with the rest borrowed. Its inflation is 0.1-0.2% a year and its debt is 12-23% of GDP at year 20, falling. But its basket poverty changes by only −11.6, −2.3 and +0.3 points. Most of C2.2's measured gain comes from money that no one in the model is asked to pay.

## 3. What the candidate main row does today
- **The row.** It is `r2MainRow`, the row S69 is checking and S63 will propose: the C2.2 design paid for by the Source, with every round-2 switch at its recommended reading and today's price rule.
- **Backing in that row.** Output counts as matching the payout only where the model sees it produced and sold: project output at market value and the PTFs' reinvestment. BU spent at face value are not matched. In the S58 money-flow table (Reference, C2.2, before S59-S73's switches), about a third of the Source's payout was matched ($19,060 of $59,180 per adult a year). The rest was new money, about 37% of cash income a year.
- **What follows.** That is why the main row's programme inflation is 42-52% a year for C2.2 and 19-43% for the release design (S72 pilot, run before S73 added the movement in and out of work, which lowers it by 0.6-3.4 points). It is also why most of its gain does not depend on backing: C2.2's BU follows the price of basic needs, and S59's asset classes keep homes and shares from melting with prices.
- **What changes with your decision.** You decided (Nov 14) that the design is full backing, so the round-2 main row takes the every-dollar-backed reading (`a` 1, the reading S51 and the frozen batch already carry). Under it the Source's payout adds no new money, so programme inflation in the main row is near zero because the design says so, not because the model finds it. Full backing is therefore labelled as a design parameter wherever the main row is shown, and the curve beside it shows what each smaller backed share gives, down to the share the model's own mechanism finds (about a third of C2.2's payout under the cautious reading).

## 4. What round 2 will display (S63 preregisters it, S64 runs it, S65 publishes it)
- **The main row**, for both designs under the Source with full backing (your decision, Nov 14; labelled as the design's statement), in all three environments, at 20 and 40 years:
  - Outcomes: basket poverty, the cost of living, wealth poverty as a yearly average, median real wealth, programme inflation.
  - Each outcome is shown on a specification curve: every preregistered reading on one chart, ordered by size, each with its seed interval. A headline sentence gives the range across readings first and the seed interval second.
- **Beside it, the backing curve (added today).** The backed share at 0, 25, 50, 75 and 100% on the round-2 main row (the 100% point is the main row itself), plus the mechanism's main reading and its no-ceiling reading, for both designs and all three environments.
  - Each point shows programme inflation and each headline outcome.
  - The curve's outputs are the break-even backed shares: the share at which inflation falls under 5% a year, and the share at which wealth poverty is no worse than without the programme.
  - The 100% point is the main row, labelled "full backing, as the design states". The point where the model's own mechanism lands is marked on the curve.
  - S64 reports round 1's 500-seed curve (study M) beside it.
- **Beside it, the financed rows (D23).**
  - C2.2 paid for by a contribution on all money income, the rest borrowed, and the same with the rest as new money.
  - The release design paid for by a flat contribution, the rest borrowed.
  - Each is printed with its rate, its base and cap, the deficit, and how the deficit is met. D21's wage-only row is shown, fully counted, as the reason the base had to widen.
  - Whether the Hub may lead with any of them is D23, which is now due again: S72's frontier is in.

## 5. Plan changes made today
- **S63:** the main row takes full backing (`a` 1; your decision, Nov 14) and carries the backing curve beside it (section 4). D23 is filed again now, with S72's figures, so you can answer it before S63.
- **S64:** reports round 1's study M at 500 seeds (`m-ce8d030`) beside round 2's curve.
- **S70:** the backed share is not part of the screen, because it moves inflation by construction and would swamp the ranking. It gets its own curve (S63) instead.
- **S69:** its packet was built on `r2MainRow` at a backed share of 0, which exercises the most of the engine (the Source's new money, the price rule, inflation's effects on wealth and debt) and is a point on the curve that round 2 carries. When S63 sets the main row to full backing, the program is rerun on it before S64 dispatches, as S69's own rule says (only the backed share differs).

## 6. How "full backing" is read
- **Full backing is read as every programme dollar matched by output**, the BU spent at face value included, because the payout reaches prices through both the BU and the conversions. This is the every-dollar-backed reading (`a` 1) that S51 and the frozen batch already carry.
- **If you meant conversions only**, the BU spent at face value would still be new money: about $18,000 of C2.2's $59,000 payout per adult a year in Reference (S58's money-flow table). Say so in the ledger's message box and S63 adds that reading as the main row instead; meanwhile the every-dollar reading stands.
- **Low inflation in earlier figures.** If you remember low inflation from an earlier engine or a Hub v1 paper, S30 traced which early figures no run produced. None of them is a target (rule 3).
