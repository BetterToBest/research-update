# The findings page: the v5.9 section


## v5.9: the newer model #
 
v5.9 is the newer model. Its main results come from the release engine (v5.9.23, engine 50bc51d), rerun under a preregistration; the model it carries forward was preregistered and frozen before it ran (registered on OSF, engine 104691f, without a central bank, first published as v5.8), and the v5.9 figures before this release stay published as the record. v5.9 added the central-bank switch, whose study was preregistered separately. Its main row takes the design’s statement that every dollar paid is matched by new output (full backing); the model’s own backing mechanism is shown beside it, and the financed rows are shown but never led with. Every result, the unfavourable ones included, is here and in the study files. v5.6, the earlier panel, is further down. Every number is read from a data file when the page loads.

## v5.9: the answer in ten seconds
With Compassionism (the full-coverage design), against no programme, Reference, 20 years, main row. The people simulated are working-age adults and their families; “adults” and “adult-years” below mean them. Each card carries its condition, full backing, and the opt-in design’s figure beside the full-coverage design’s. Each figure is a mean over 500 paired runs; its 95% seed interval is in the table under “How sure we are”, below:

At full backing: every programme dollar matched by new output (a design statement; not shown by the model)
Below 30 days of basic living (adult-years)
1.0%
against 20.3% with no programme (−19.3 points)
Opt-in design (adults choose to join): 8.0% against the same 20.3% (−12.3 points)
Counted per simulated adult (unweighted).

At full backing: every programme dollar matched by new output (a design statement; not shown by the model)
Below the cost of living (the basket of essentials, adult-years)
3.5%
against 36.4% with no programme (−32.8 points)
Opt-in design (adults choose to join): 16.0% against the same 36.4% (−20.3 points)
Counted per simulated adult (unweighted).

At full backing: every programme dollar matched by new output (a design statement; not shown by the model)
Too little wealth, yearly average (adults)
6.2%
against 25.1% with no programme (−18.9 points)
Opt-in design (adults choose to join): 14.3% against the same 25.1% (−10.8 points)
Counted per simulated adult (unweighted).

At full backing: every programme dollar matched by new output (a design statement; not shown by the model)
Median real wealth at year 20
$434,102
against $224,185 with no programme (+$209,918). Rests on full backing (corrected Nov 17, 2026: it said today’s price rule, which full backing barely tests); 1.0% of the gain is the erosion of opening balances, in the programme’s favour
Opt-in design (adults choose to join): $323,882 against the same $224,185 (+$99,697)
Counted by population weight (weighted).
This release (v5.9.23, engine 50bc51d). The figures in this section come from the preregistered reruns on the release engine. The main row changed in three ways: the private businesses’ lower BU price is now set at the sale, as the design states (Duke’s design, Oct 1, 2026), instead of a year late out of the previous year’s premium; pay differs by household type, as in the survey; and the child and dependent care credit is included (the last two adopted by Duke on Nov 21, 2026, after the yardstick study’s preregistered rule held). No main-row effect changed sign. The price at the sale moved every main-row poverty and wealth effect in the programme’s favour, and raised the full-coverage design’s programme inflation in Adverse and Stress by less than 0.0001 points a year; the two additions made the opt-in design’s poverty cuts smaller and the full-coverage design’s cut below 30 days of basic living larger. Below full backing, the reading that changed most is wages that follow programme inflation only in part: with no backing the programme is now worse than no programme in 2 of the six cells (Reference at 40 years, Stress at 40 years), better in the other 4 on basket poverty (the supply study, above), and the change comes from the price at the sale. The model registered on OSF (v5.8, engine 104691f) and the v5.9 figures stay published as the record, reproducible from their engine commits. Tables of every main-row effect, published against release, with the change split into its two steps: s93-release-tables-50bc51d in compassionism-sim-results.
Main row: every dollar the programme pays is matched by new output, as the design states (a design parameter, not a model estimate). The model’s own production mechanism reaches 0.2% to 1.8% of it across the designs, environments and horizons (about 0.8% in the full-coverage design in Reference at 20 years), and the automation study’s more generous count 6% to 17% (full coverage) and 3% to 7% (opt-in design) at 20 years. The two differ in what they count as new output; see “How much new output does the model itself produce?”, below.
One sentence. Across the 62 preregistered readings, both designs lower all three poverty measures and raise median real wealth, in every environment and at both horizons (the table “How sure we are” gives the count for each). These results hold when every dollar paid is matched by new output, which is the design’s statement and not something the model shows; with the model’s own backing mechanism (with or without its ceiling), prices rise 15.5 to 50.3 points a year across the environments and designs at 20 and 40 years. That is the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices. Both designs’ main-row figures are in the cards above.

## How sure we are: the range across readings
Each preregistered reading changes one setting the design leaves open (how much of their spare cash adults spend, how wealth is held, the price rule’s settings, and others). For each outcome, the curve below shows every reading’s effect. The table gives the range, the main row with its seed interval, and whether every reading keeps its sign. The seed interval covers the model’s randomness only, not the choice of reading; the spread across readings shows that. The wealth figures rest on full backing (corrected Nov 17, 2026: this sentence also said they rest on today’s price rule, but at full backing almost no unmatched money reaches prices, so the price rule is barely tested there; below full backing they rest on it), and only a small part of any of them is the erosion of the balances adults held at the start (in the programme’s favour; if all wealth were cash, against it).
“Robust” means that at every preregistered reading the effect keeps its sign and its seed interval excludes zero. It is a statement about the readings the study swept inside this model’s structure, not about other structures (see “What no figure here covers”). A curve is one outcome, in one environment, at one horizon, for one design: four outcomes (cost of living, basic living, wealth poverty, median real wealth), three environments, two horizons and two designs make 48 curves, and each plots all of the preregistered readings (the table gives the count for each). All 48 main-row curves are robust. The financed rows (below) are the same 48 curves with the programme paid by a contribution, drawn with the same readings and the financed readings added; nearly all of them are fragile.

v5.9, 20 years: the effect at each preregistered reading (lowest to highest), the main row with its seed interval, and whether every reading keeps its sign
| Design | Environment | Outcome | Across the readings | Main row (95% seed interval) | Readings keeping the sign | Class | 
| Full-coverage design | Reference | cost of living (unweighted) | −33.6 to −26.4 | −32.8 (−33.0 to −32.7) | 62 of 62 | robust | 
| Full-coverage design | Reference | basic living (unweighted) | −20.2 to −17.1 | −19.3 (−19.5 to −19.2) | 62 of 62 | robust | 
| Full-coverage design | Reference | wealth poverty, yearly average (unweighted) | −20.0 to −16.0 | −18.9 (−19.0 to −18.8) | 62 of 62 | robust | 
| Full-coverage design | Reference | median real wealth (weighted) | $188,924 to $661,614 | +$209,918 ($208,559 to $211,241) | 62 of 62 | robust | 
| Full-coverage design | Adverse | cost of living (unweighted) | −41.7 to −34.4 | −40.6 (−40.8 to −40.4) | 62 of 62 | robust | 
| Full-coverage design | Adverse | basic living (unweighted) | −22.9 to −18.2 | −20.4 (−20.5 to −20.2) | 62 of 62 | robust | 
| Full-coverage design | Adverse | wealth poverty, yearly average (unweighted) | −21.7 to −17.1 | −19.9 (−20.0 to −19.7) | 62 of 62 | robust | 
| Full-coverage design | Adverse | median real wealth (weighted) | $167,416 to $635,667 | +$199,004 ($197,729 to $200,352) | 62 of 62 | robust | 
| Full-coverage design | Stress | cost of living (unweighted) | −41.2 to −33.4 | −40.1 (−40.3 to −39.9) | 62 of 62 | robust | 
| Full-coverage design | Stress | basic living (unweighted) | −22.8 to −18.2 | −20.4 (−20.5 to −20.2) | 62 of 62 | robust | 
| Full-coverage design | Stress | wealth poverty, yearly average (unweighted) | −21.2 to −16.6 | −19.3 (−19.4 to −19.2) | 62 of 62 | robust | 
| Full-coverage design | Stress | median real wealth (weighted) | $142,644 to $533,757 | +$171,216 ($169,937 to $172,477) | 62 of 62 | robust | 
| Opt-in design | Reference | cost of living (unweighted) | −21.8 to −15.8 | −20.3 (−20.5 to −20.2) | 62 of 62 | robust | 
| Opt-in design | Reference | basic living (unweighted) | −12.9 to −10.8 | −12.3 (−12.4 to −12.2) | 62 of 62 | robust | 
| Opt-in design | Reference | wealth poverty, yearly average (unweighted) | −12.6 to −9.0 | −10.8 (−10.9 to −10.7) | 62 of 62 | robust | 
| Opt-in design | Reference | median real wealth (weighted) | $85,335 to $281,126 | +$99,697 ($98,442 to $100,951) | 62 of 62 | robust | 
| Opt-in design | Adverse | cost of living (unweighted) | −19.7 to −14.9 | −18.2 (−18.3 to −18.0) | 62 of 62 | robust | 
| Opt-in design | Adverse | basic living (unweighted) | −11.7 to −9.1 | −10.5 (−10.6 to −10.4) | 62 of 62 | robust | 
| Opt-in design | Adverse | wealth poverty, yearly average (unweighted) | −11.5 to −8.1 | −9.4 (−9.6 to −9.3) | 62 of 62 | robust | 
| Opt-in design | Adverse | median real wealth (weighted) | $58,724 to $193,254 | +$72,077 ($71,001 to $73,175) | 62 of 62 | robust | 
| Opt-in design | Stress | cost of living (unweighted) | −8.1 to −6.2 | −7.4 (−7.5 to −7.3) | 62 of 62 | robust | 
| Opt-in design | Stress | basic living (unweighted) | −4.7 to −3.7 | −4.3 (−4.3 to −4.2) | 62 of 62 | robust | 
| Opt-in design | Stress | wealth poverty, yearly average (unweighted) | −4.7 to −3.3 | −3.8 (−3.9 to −3.7) | 62 of 62 | robust | 
| Opt-in design | Stress | median real wealth (weighted) | $24,389 to $75,109 | +$28,958 ($28,117 to $29,793) | 62 of 62 | robust | 
The same at 40 years

v5.9, 40 years: the effect at each preregistered reading (lowest to highest), the main row with its seed interval, and whether every reading keeps its sign
| Design | Environment | Outcome | Across the readings | Main row (95% seed interval) | Readings keeping the sign | Class | 
| Full-coverage design | Reference | cost of living (unweighted) | −32.1 to −24.4 | −31.2 (−31.4 to −31.1) | 62 of 62 | robust | 
| Full-coverage design | Reference | basic living (unweighted) | −20.5 to −17.3 | −19.7 (−19.8 to −19.6) | 62 of 62 | robust | 
| Full-coverage design | Reference | wealth poverty, yearly average (unweighted) | −21.5 to −17.7 | −20.5 (−20.7 to −20.4) | 62 of 62 | robust | 
| Full-coverage design | Reference | median real wealth (weighted) | $401,312 to $1,645,529 | +$441,410 ($438,882 to $444,011) | 62 of 62 | robust | 
| Full-coverage design | Adverse | cost of living (unweighted) | −47.2 to −39.6 | −45.8 (−46.0 to −45.6) | 62 of 62 | robust | 
| Full-coverage design | Adverse | basic living (unweighted) | −27.8 to −20.9 | −23.4 (−23.6 to −23.3) | 62 of 62 | robust | 
| Full-coverage design | Adverse | wealth poverty, yearly average (unweighted) | −28.0 to −21.1 | −24.0 (−24.1 to −23.9) | 62 of 62 | robust | 
| Full-coverage design | Adverse | median real wealth (weighted) | $306,562 to $1,516,985 | +$390,293 ($387,991 to $392,537) | 62 of 62 | robust | 
| Full-coverage design | Stress | cost of living (unweighted) | −46.4 to −38.1 | −45.0 (−45.2 to −44.8) | 62 of 62 | robust | 
| Full-coverage design | Stress | basic living (unweighted) | −27.7 to −20.8 | −23.4 (−23.5 to −23.3) | 62 of 62 | robust | 
| Full-coverage design | Stress | wealth poverty, yearly average (unweighted) | −26.9 to −20.3 | −23.4 (−23.5 to −23.3) | 62 of 62 | robust | 
| Full-coverage design | Stress | median real wealth (weighted) | $260,192 to $1,257,990 | +$332,781 ($330,610 to $334,895) | 62 of 62 | robust | 
| Opt-in design | Reference | cost of living (unweighted) | −20.8 to −14.9 | −19.5 (−19.6 to −19.4) | 62 of 62 | robust | 
| Opt-in design | Reference | basic living (unweighted) | −14.1 to −12.0 | −13.5 (−13.6 to −13.4) | 62 of 62 | robust | 
| Opt-in design | Reference | wealth poverty, yearly average (unweighted) | −13.6 to −10.5 | −12.7 (−12.8 to −12.6) | 62 of 62 | robust | 
| Opt-in design | Reference | median real wealth (weighted) | $183,385 to $714,711 | +$210,810 ($208,474 to $213,012) | 62 of 62 | robust | 
| Opt-in design | Adverse | cost of living (unweighted) | −17.5 to −13.6 | −16.0 (−16.1 to −15.8) | 62 of 62 | robust | 
| Opt-in design | Adverse | basic living (unweighted) | −12.5 to −9.4 | −10.9 (−11.0 to −10.8) | 62 of 62 | robust | 
| Opt-in design | Adverse | wealth poverty, yearly average (unweighted) | −12.2 to −8.9 | −10.4 (−10.5 to −10.3) | 62 of 62 | robust | 
| Opt-in design | Adverse | median real wealth (weighted) | $85,733 to $360,004 | +$113,228 ($111,480 to $114,949) | 62 of 62 | robust | 
| Opt-in design | Stress | cost of living (unweighted) | −7.2 to −5.6 | −6.5 (−6.5 to −6.4) | 62 of 62 | robust | 
| Opt-in design | Stress | basic living (unweighted) | −5.1 to −3.8 | −4.4 (−4.5 to −4.4) | 62 of 62 | robust | 
| Opt-in design | Stress | wealth poverty, yearly average (unweighted) | −5.0 to −3.7 | −4.2 (−4.3 to −4.1) | 62 of 62 | robust | 
| Opt-in design | Stress | median real wealth (weighted) | $34,572 to $134,951 | +$45,897 ($44,631 to $47,164) | 62 of 62 | robust | 
Each dot in a chart is one preregistered reading, sorted by its effect, with its 95% seed interval. The seed interval covers the model’s randomness only, not the choice of reading; the spread of the dots shows that.
The curves, one chart per outcome (the full-coverage design, then the opt-in design; the financed rows beside each)[chart: Cost of living (basket poverty), full-coverage design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Cost of living (basket poverty), full-coverage design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Cost of living (basket poverty), opt-in design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Cost of living (basket poverty), opt-in design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Basic living, full-coverage design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Basic living, full-coverage design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Basic living, opt-in design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Basic living, opt-in design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Wealth poverty, yearly average, full-coverage design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Wealth poverty, yearly average, full-coverage design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Wealth poverty, yearly average, opt-in design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Wealth poverty, yearly average, opt-in design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Median real wealth, full-coverage design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Median real wealth, full-coverage design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Median real wealth, opt-in design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Median real wealth, opt-in design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Programme inflation, full-coverage design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Programme inflation, full-coverage design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Programme inflation, opt-in design, 20 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.][chart: Programme inflation, opt-in design, 40 years: effect at each preregistered reading, three environments, with the financed rows beside. The numbers are in the table above and in the file r2-curves.]

## Prices, and how much new output backs the payout
At the main row, programme inflation is 0.16 points a year above no programme in Reference at 20 years in the full-coverage design (0.12 in the opt-in design): no material change. The main row assumes that every dollar the programme pays is matched by new output, as the design states (a design parameter). Every inflation figure below full backing on this page is the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices: all unmatched new money reaches prices (the model’s placeholder price rule), no central bank responds and no expectations adjust.
How much new output does the model itself produce? Two studies measure it, and they count differently, so one model gives two answers. The production mechanism sends a share of the payout into projects that add output after a lag. It counts only output that is new (output that already exists absorbed earlier money and cannot absorb more), and it holds project output to a ceiling of 8% of earned income. It reaches 0.2% to 1.8% of the payout across both designs, the three environments and both horizons, and 14% to 20% with the ceiling removed. The automation study counts all the output of the programme’s own work, valued at its pay over the labour share and scaled by the share of that work whose output people would otherwise buy (a design parameter, swept from 0.25 to 1), plus the yield of the providers’ reinvested capital. It reaches 6% to 17% of the payout in the full-coverage design at 20 years and 3% to 7% in the opt-in design. Counted the mechanism’s stricter way, the automation study’s own figure is near 1%. So the model’s own answer runs from the mechanism’s figure to about a fifth of the payout, depending on what counts as new output, and never reaches the whole; full backing is the design’s assumption.
Do the poverty effects depend on backing? It depends on wages. Where wages follow prices in full (the main row’s assumption), the poverty effects barely depend on backing; inflation and median wealth do. Where wages follow programme inflation only in part, they depend on it strongly: if wages follow half of it and the rest is never made up, then with no backing the programme’s effect on basket poverty is −8.5 points in Reference (−12.7 in Adverse, −1.2 in Stress) at 20 years and +11.3 (−2.0 in Adverse, +12.1 in Stress) at 40 years against no programme (full-coverage design): worse than no programme in 2 of the six cells (Reference at 40 years, Stress at 40 years), better in the other 4 (the supply study, below). No source says how wages follow an inflation the programme itself makes. Replaced Nov 18, 2026: the dated note of Nov 17 said the poverty effects held because the model had no limit on what the economy can supply; a limit on supply barely moves the curve, but wages that follow programme inflation only in part do.
With no backing and no limit on supply, programme inflation is 39 to 46 points a year in the full-coverage design at 20 years across the three environments, and 35 to 50 at 20 and 40 years together; the opt-in design’s is 19 to 47. All of these rows together (two designs, three environments, two horizons) run 19 to 50 points a year; the narrower ranges are parts of that set, not a different measurement. These are the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices.

Full-coverage design, Reference, 20 years: effects against no programme at each backed share (change in points, change in $, programme inflation in points a year: the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast)
| Reading | Backed share | Cost of living (points) | Median real wealth | Programme inflation | 
| Backed share | 0% | −31.9 | +$94,056 | +38.80 | 
| Backed share | 25% | −32.1 | +$110,466 | +29.52 | 
| Backed share | 50% | −32.3 | +$135,823 | +19.98 | 
| Backed share | 75% | −32.6 | +$175,992 | +9.97 | 
| Full backing (the main row, as the design states) | 100% | −32.8 | +$209,918 | +0.16 | 
| The model’s own mechanism (where it reaches) | 0.8% | −31.9 | +$94,120 | +38.50 | 
| The model’s own mechanism, no ceiling (where it reaches) | 19.5% | −32.0 | +$105,458 | +31.60 | 
| Break-even: programme inflation 5% a year | 88% | | | | 
The opt-in design, and the backing charts

Opt-in design, Reference, 20 years: effects against no programme at each backed share (change in points, change in $, programme inflation in points a year: the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast)
| Reading | Backed share | Cost of living (points) | Median real wealth | Programme inflation | 
| Backed share | 0% | −19.7 | +$62,274 | +36.50 | 
| Backed share | 25% | −19.9 | +$72,496 | +27.95 | 
| Backed share | 50% | −20.1 | +$87,573 | +19.01 | 
| Backed share | 75% | −20.6 | +$107,564 | +9.72 | 
| Full backing (the main row, as the design states) | 100% | −20.3 | +$99,697 | +0.12 | 
| The model’s own mechanism (where it reaches) | 1.0% | −19.7 | +$62,460 | +36.11 | 
| The model’s own mechanism, no ceiling (where it reaches) | 19.5% | −19.8 | +$69,448 | +29.82 | 
| Break-even: programme inflation 5% a year | 87% | | | | [chart: Programme inflation by backed share (the size of the unbacked money, not a forecast), with the break-even share and the mechanism’s own points marked (backing-c22-20); the numbers are in the table above and in the file r2-backing.][chart: Programme inflation by backed share (the size of the unbacked money, not a forecast), with the break-even share and the mechanism’s own points marked (backing-c22-40); the numbers are in the table above and in the file r2-backing.][chart: Programme inflation by backed share (the size of the unbacked money, not a forecast), with the break-even share and the mechanism’s own points marked (backing-rel-20); the numbers are in the table above and in the file r2-backing.][chart: Programme inflation by backed share (the size of the unbacked money, not a forecast), with the break-even share and the mechanism’s own points marked (backing-rel-40); the numbers are in the table above and in the file r2-backing.]

## Below full backing: limits on supply, wages and the BU’s adjustment (v6 readings, added Nov 18, 2026)
The v5.9 engine had no limit on what the economy can supply, and wages, the BU and the cost-of-living basket followed prices in full and at once. A preregistered study adds each of these as a reading, behind its own switch, and runs it at every backed share on 500 paired seeds. Full backing is the main row, and no reading changes it. In order of what moves the curve least to most:
- A limit on supply of housing, medical care and food, from the economy’s headroom in opened sources, shared by the market’s rule, evenly, or the design’s rule. It costs little. With no backing in Reference, the programme’s effect on basket poverty is −31.5 points under the sourced limit with the market’s rule and −29.9 in the strictest case, against −31.9 with no limit. But the limit as built moves only basket poverty: the money a cut leaves unspent goes to other goods, and the cut moves no price, so wealth, basic living and inflation are the same with and without it. A shortage therefore never shows in the basic-living, wealth-poverty, median-wealth or inflation figures anywhere on this page, which are measured as if the goods could always be bought. Basket poverty’s effect keeps its sign, with an interval that excludes zero, under the sourced limit at every share, in every environment and with every rule; for the other outcomes that test says nothing.
- The BU’s adjustment to prices. The design’s monthly and quarterly adjustments cost little; a yearly or two-year delay costs much more (table).
- Wages that follow programme inflation only in part. This is what makes the results depend on backing. If wages follow half of it and the rest is never made up, the programme with no backing changes basket poverty by −8.5 points in Reference (−12.7 in Adverse, −1.2 in Stress) at 20 years and +11.3 (−2.0 in Adverse, +12.1 in Stress) at 40 years against no programme: worse than no programme in 2 of the six cells (Reference at 40 years, Stress at 40 years), better in the other 4. In the figures published before this release, all three 20-year figures were worse than no programme as well. The change comes from the private businesses’ BU price, now set at the sale: with that price a year late, the release engine gives the published figures again, and pay by household type and the care credit move them by half a point at most (a check on 20 paired runs in each environment and horizon, results s93-wage-dec-50bc51d). Median real wealth then breaks even at a backed share of none on the grid at 20 years and 0.73 at 40 (Reference). If the rest is made up a year later, the cost is small. No source says how wages follow an inflation the programme itself makes: the readings never made up are the pessimistic end of the range swept.

Full-coverage design, Reference, 20 years: the change in basket poverty against no programme at each backed share (points), and the break-even backed share (where the effect is no better than no programme; Reference / Adverse / Stress)
| Reading | No backing | Half backed | Full backing (the main row) | Break-even share, 20 years | Break-even share, 40 years | 
| No limit on supply (the v5.9 engine) | −31.9 | −32.3 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| Supply limit, sourced; the market's rule (those least able to pay go short first) | −31.5 | −32.2 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| Supply limit, sourced; the design's rule (basics bought with the BU served first) | −31.7 | −32.2 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| Supply limit, restricted (a policy reading: every sourced value halved, for today's land-use, residency and farm policies); the market's rule | −31.0 | −31.9 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| The strictest case: no essentials beyond today's needs consumption; not the economy and not the design; the market's rule | −29.9 | −31.4 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| The BU follows the needs' price a month behind (the design's monthly adjustment) | −31.3 | −32.0 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| The BU a quarter behind | −30.6 | −31.7 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| The BU a year behind (as Social Security's adjustment) | −25.1 | −28.8 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| The BU two years behind (a bound) | −19.4 | −24.7 | −32.7 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| Wages follow half of programme inflation, the rest made up a year later | −31.3 | −32.0 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| Wages follow three quarters of programme inflation, never made up | −27.8 | −31.1 | −32.8 | none on the grid / none on the grid / none on the grid | none on the grid / none on the grid / none on the grid | 
| Wages follow half of programme inflation, never made up | −8.5 | −28.7 | −32.8 | none on the grid / none on the grid / none on the grid | 0.12 / none on the grid / 0.28 | 
Effects are programme minus no programme, mean over paired seeds; 95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model's randomness only. The wage and BU readings are design parameters, as are the building speed of medical care and food and the essentials’ price response; each is swept in the study, and every result above holds at the slowest building speed and at half and double the price response. Programme inflation is unchanged by the supply limit (inflation stays under 5 points a year only above about 0.88 backing in Reference). One reading of the study (adults who age and are replaced, at no backing) measures a defect and is not shown; it is rerun once fixed. Every figure, with the 40-year horizon, who goes short by fifth of income, and the smaller readings: the report dev/reports/s82-supply-indexing.md, the files data/studies/s82-supply.json and s82-breakeven.json (python3 dev/tools/s82_page_data.py s82-tables-50bc51d/s82-summary.json), engine 50bc51d, results s82-tables-50bc51d in BetterToBest/compassionism-sim-results; preregistration prereg/2026-11-s82-v6-supply-indexing.md (research-update; Amendments 1-6).

## Automation: displacement in both runs, and the backing the programme’s own work produces (added Nov 20, 2026)
A preregistered study runs automation in both runs of every pair, so the no-programme run faces the same displacement: 10%, 30%, 50% or 70% of today’s paid work gone by year 20, net of new work, as lost jobs (the most exposed adults leave paid work first) or as shorter hours for everyone. 50% and 70% are stress readings, beyond every forecast the study opened. The automated work is still done: output per hour grows by a sourced forecast, part of the gain reaches pay, and the rest goes to owners by their holdings. Two designs, 500 paired seeds, three environments; figures are for 20 years unless named.
- With no programme, displacement raises basket poverty (adult-years below one’s own cost of living) by 2.0 to 12.2 points with lost jobs in Reference (1.6 to 9.5 in Adverse and Stress), and median real wealth (weighted) falls by $7,244 to $50,015 (Reference).
- With every adult taking part and full backing (the full-coverage design), the programme takes away 80% to 100% of the rise in basket poverty (lost jobs and shorter hours, three environments), 56% to 91% of the rise in wealth poverty, 64% to 92% of the rise in the share of adult-years with under three months of savings, and 13% to 40% of the fall in median real wealth (weighted and unweighted). Of its 144 tests, 1 offset fully, 143 offset in part, every one significant. At 50% lost jobs, 5% to 10% of the hours no longer paid fall in households below their cost of living, against 76% to 81% with no programme.
- In the opt-in design it takes away much less: −20% to 16% of the rise in basket poverty with lost jobs, and −2% to 66% with shorter hours. With lost jobs it often makes the rise in poverty larger: in 7 of its 12 lost-jobs cells the rise in basket poverty is larger with the programme than without it. The cells where it is larger: Reference at 70%; Adverse at 30%, 50%, 70%; Stress at 30%, 50%, 70% (lost jobs); Stress at 70% (shorter hours). Where the rise in the share with under three months of savings is larger with the programme: none. With full coverage no test worsens, for any reading, in any cell, at either horizon. Of its 144 tests, 84 offset in part, 50 do not offset, 10 worsen (40 years: 144 tests, 74 offset in part, 39 do not offset, 31 worsen). At 50% lost jobs, 56% to 77% of the freed hours fall below the cost of living. The opt-in programme still cuts basket poverty against no programme at every level; “larger” means that cut shrinks as displacement grows. A trace of these cells finds that the adults who would take part carry most of the extra rise, as more of them sit just below the line rather than far below it, and that enrolment does not fall (the report gives the figures).
- Full backing is assumed, not produced. Every figure above assumes that each programme dollar is matched by new output (a design parameter). Counting only what the programme’s own work produces (project hours valued at their pay over the labour share, times m, the share of that work whose output people would otherwise buy, a design parameter; plus the yield of the providers’ reinvested capital), it matches 6% to 17% of the payout in the full-coverage design at 20 years (5% to 18% at 40) and 3% to 7% opt-in (4% to 8% at 40). At that backing programme inflation is 48 to 69 points a year with full coverage across the three environments (Reference: 48 to 62) and 18 to 50 opt-in, at 20 years (the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices). In 528 of the block’s 528 rows (every reading, design, environment and horizon, m 1 included) the interval of programme inflation lies above 5 points a year: no row backs enough.

The share of displacement’s rise in basket poverty that the programme takes away, 20 years, at full backing (95% interval; category after the multiple-testing correction). Negative: the rise is larger with the programme.
| Design, form, share of paid work displaced by year 20 | Reference | Adverse | Stress | 
| Full coverage, lost jobs, 10% | 96% (95 to 96), offsets in part | 94% (93 to 94), offsets in part | 84% (83 to 85), offsets in part | 
| Full coverage, lost jobs, 30% | 94% (94 to 95), offsets in part | 92% (92 to 92), offsets in part | 81% (80 to 81), offsets in part | 
| Full coverage, lost jobs, 50% | 94% (94 to 94), offsets in part | 91% (91 to 92), offsets in part | 80% (79 to 80), offsets in part | 
| Full coverage, lost jobs, 70% | 94% (94 to 94), offsets in part | 91% (91 to 92), offsets in part | 80% (80 to 80), offsets in part | 
| Full coverage, shorter hours, 10% | 100% (100 to 100), offsets fully | 99% (99 to 99), offsets in part | 99% (99 to 99), offsets in part | 
| Full coverage, shorter hours, 30% | 100% (100 to 100), offsets in part | 99% (99 to 99), offsets in part | 98% (98 to 98), offsets in part | 
| Full coverage, shorter hours, 50% | 99% (99 to 99), offsets in part | 98% (98 to 98), offsets in part | 97% (97 to 97), offsets in part | 
| Full coverage, shorter hours, 70% | 98% (98 to 98), offsets in part | 97% (97 to 97), offsets in part | 93% (93 to 93), offsets in part | 
| Opt-in, lost jobs, 10% | 16% (14 to 18), offsets in part | −4% (−6 to −1), does not offset | −2% (−4 to −1), does not offset | 
| Opt-in, lost jobs, 30% | 7% (5 to 8), offsets in part | −10% (−12 to −9), worsens | −6% (−7 to −5), worsens | 
| Opt-in, lost jobs, 50% | 1% (0 to 2), does not offset | −15% (−16 to −14), worsens | −8% (−9 to −7), worsens | 
| Opt-in, lost jobs, 70% | −2% (−3 to −2), worsens | −20% (−21 to −19), worsens | −10% (−10 to −9), worsens | 
| Opt-in, shorter hours, 10% | 66% (65 to 67), offsets in part | 30% (28 to 31), offsets in part | 10% (8 to 11), offsets in part | 
| Opt-in, shorter hours, 30% | 63% (62 to 63), offsets in part | 23% (22 to 24), offsets in part | 7% (6 to 7), offsets in part | 
| Opt-in, shorter hours, 50% | 55% (54 to 55), offsets in part | 14% (13 to 15), offsets in part | 2% (1 to 3), offsets in part | 
| Opt-in, shorter hours, 70% | 34% (33 to 34), offsets in part | 3% (2 to 3), offsets in part | −2% (−3 to −2), worsens | 
The same for savings, wealth poverty and median real wealth, and at 40 years

Savings under three months of need: the share of displacement’s rise the programme takes away, 20 years, at full backing
| Design, form, share of paid work displaced by year 20 | Reference | Adverse | Stress | 
| Full coverage, lost jobs, 10% | 90% (88 to 92), offsets in part | 83% (80 to 85), offsets in part | 76% (73 to 79), offsets in part | 
| Full coverage, lost jobs, 30% | 84% (83 to 86), offsets in part | 79% (77 to 81), offsets in part | 71% (68 to 73), offsets in part | 
| Full coverage, lost jobs, 50% | 81% (80 to 82), offsets in part | 76% (75 to 77), offsets in part | 66% (64 to 68), offsets in part | 
| Full coverage, lost jobs, 70% | 80% (79 to 81), offsets in part | 75% (73 to 76), offsets in part | 64% (62 to 66), offsets in part | 
| Full coverage, shorter hours, 10% | 92% (91 to 93), offsets in part | 92% (91 to 92), offsets in part | 89% (88 to 90), offsets in part | 
| Full coverage, shorter hours, 30% | 92% (92 to 92), offsets in part | 91% (90 to 91), offsets in part | 89% (88 to 89), offsets in part | 
| Full coverage, shorter hours, 50% | 92% (91 to 92), offsets in part | 90% (90 to 91), offsets in part | 87% (87 to 88), offsets in part | 
| Full coverage, shorter hours, 70% | 90% (90 to 91), offsets in part | 89% (88 to 89), offsets in part | 85% (85 to 86), offsets in part | 
| Opt-in, lost jobs, 10% | 18% (12 to 24), offsets in part | 12% (4 to 19), does not offset | 0% (−6 to 6), does not offset | 
| Opt-in, lost jobs, 30% | 11% (7 to 15), offsets in part | 7% (2 to 12), does not offset | 1% (−3 to 4), does not offset | 
| Opt-in, lost jobs, 50% | 5% (2 to 8), offsets in part | 3% (−0 to 7), does not offset | −1% (−4 to 2), does not offset | 
| Opt-in, lost jobs, 70% | 3% (0 to 6), does not offset | −1% (−4 to 3), does not offset | −3% (−5 to −0), does not offset | 
| Opt-in, shorter hours, 10% | 44% (42 to 47), offsets in part | 27% (23 to 30), offsets in part | 11% (7 to 15), offsets in part | 
| Opt-in, shorter hours, 30% | 44% (42 to 46), offsets in part | 25% (22 to 28), offsets in part | 7% (5 to 10), offsets in part | 
| Opt-in, shorter hours, 50% | 43% (42 to 45), offsets in part | 21% (19 to 23), offsets in part | 5% (3 to 7), offsets in part | 
| Opt-in, shorter hours, 70% | 37% (36 to 39), offsets in part | 17% (15 to 19), offsets in part | 4% (2 to 5), offsets in part | 

Wealth poverty, yearly average: the share of displacement’s rise the programme takes away, 20 years, at full backing
| Design, form, share of paid work displaced by year 20 | Reference | Adverse | Stress | 
| Full coverage, lost jobs, 10% | 88% (86 to 89), offsets in part | 81% (79 to 84), offsets in part | 72% (68 to 75), offsets in part | 
| Full coverage, lost jobs, 30% | 81% (80 to 82), offsets in part | 75% (73 to 76), offsets in part | 63% (61 to 66), offsets in part | 
| Full coverage, lost jobs, 50% | 78% (77 to 79), offsets in part | 71% (70 to 73), offsets in part | 58% (56 to 60), offsets in part | 
| Full coverage, lost jobs, 70% | 77% (76 to 78), offsets in part | 70% (69 to 72), offsets in part | 56% (54 to 58), offsets in part | 
| Full coverage, shorter hours, 10% | 91% (91 to 92), offsets in part | 91% (91 to 92), offsets in part | 88% (87 to 88), offsets in part | 
| Full coverage, shorter hours, 30% | 91% (91 to 92), offsets in part | 90% (90 to 91), offsets in part | 87% (87 to 88), offsets in part | 
| Full coverage, shorter hours, 50% | 91% (90 to 91), offsets in part | 90% (89 to 90), offsets in part | 86% (85 to 87), offsets in part | 
| Full coverage, shorter hours, 70% | 89% (89 to 90), offsets in part | 88% (88 to 88), offsets in part | 83% (82 to 84), offsets in part | 
| Opt-in, lost jobs, 10% | 18% (12 to 23), offsets in part | 11% (4 to 17), does not offset | 0% (−5 to 6), does not offset | 
| Opt-in, lost jobs, 30% | 6% (2 to 10), offsets in part | 2% (−3 to 6), does not offset | −1% (−5 to 2), does not offset | 
| Opt-in, lost jobs, 50% | 1% (−2 to 4), does not offset | −3% (−7 to 0), does not offset | −3% (−6 to −1), does not offset | 
| Opt-in, lost jobs, 70% | −1% (−4 to 1), does not offset | −6% (−10 to −3), worsens | −4% (−7 to −2), worsens | 
| Opt-in, shorter hours, 10% | 45% (42 to 48), offsets in part | 29% (26 to 32), offsets in part | 7% (3 to 10), offsets in part | 
| Opt-in, shorter hours, 30% | 45% (43 to 46), offsets in part | 26% (23 to 28), offsets in part | 8% (6 to 10), offsets in part | 
| Opt-in, shorter hours, 50% | 43% (41 to 45), offsets in part | 23% (21 to 25), offsets in part | 6% (5 to 8), offsets in part | 
| Opt-in, shorter hours, 70% | 37% (35 to 38), offsets in part | 18% (16 to 20), offsets in part | 5% (3 to 6), offsets in part | 

Median real wealth (weighted): the share of displacement’s fall the programme takes away, 20 years, at full backing; today’s price rule, barely tested at full backing
| Design, form, share of paid work displaced by year 20 | Reference | Adverse | Stress | 
| Full coverage, lost jobs, 10% | 21% (12 to 30), offsets in part | 15% (4 to 25), offsets in part | 21% (10 to 31), offsets in part | 
| Full coverage, lost jobs, 30% | 16% (11 to 20), offsets in part | 13% (7 to 19), offsets in part | 17% (12 to 23), offsets in part | 
| Full coverage, lost jobs, 50% | 16% (13 to 19), offsets in part | 14% (10 to 19), offsets in part | 18% (14 to 22), offsets in part | 
| Full coverage, lost jobs, 70% | 16% (13 to 18), offsets in part | 14% (11 to 17), offsets in part | 18% (15 to 21), offsets in part | 
| Full coverage, shorter hours, 10% | 18% (13 to 24), offsets in part | 34% (29 to 39), offsets in part | 39% (33 to 43), offsets in part | 
| Full coverage, shorter hours, 30% | 22% (19 to 26), offsets in part | 36% (33 to 39), offsets in part | 39% (36 to 42), offsets in part | 
| Full coverage, shorter hours, 50% | 27% (25 to 30), offsets in part | 37% (34 to 39), offsets in part | 40% (38 to 42), offsets in part | 
| Full coverage, shorter hours, 70% | 25% (23 to 27), offsets in part | 31% (29 to 33), offsets in part | 35% (32 to 37), offsets in part | 
| Opt-in, lost jobs, 10% | 2% (−9 to 11), does not offset | 12% (−0 to 22), does not offset | 13% (3 to 22), does not offset | 
| Opt-in, lost jobs, 30% | 4% (−2 to 9), does not offset | 7% (1 to 12), does not offset | 5% (−0 to 11), does not offset | 
| Opt-in, lost jobs, 50% | 6% (3 to 9), offsets in part | 4% (−0 to 9), does not offset | 2% (−2 to 6), does not offset | 
| Opt-in, lost jobs, 70% | 6% (4 to 9), offsets in part | 1% (−2 to 5), does not offset | −1% (−4 to 2), does not offset | 
| Opt-in, shorter hours, 10% | 11% (5 to 17), offsets in part | 23% (17 to 29), offsets in part | 14% (9 to 20), offsets in part | 
| Opt-in, shorter hours, 30% | 16% (13 to 19), offsets in part | 23% (20 to 27), offsets in part | 11% (8 to 14), offsets in part | 
| Opt-in, shorter hours, 50% | 22% (20 to 24), offsets in part | 21% (19 to 24), offsets in part | 9% (6 to 11), offsets in part | 
| Opt-in, shorter hours, 70% | 18% (16 to 20), offsets in part | 16% (13 to 18), offsets in part | 5% (3 to 7), offsets in part | 

Basket poverty: the share of displacement’s rise the programme takes away, 40 years, at full backing
| Design, form, share of paid work displaced by year 20 | Reference | Adverse | Stress | 
| Full coverage, lost jobs, 10% | 97% (96 to 97), offsets in part | 95% (94 to 95), offsets in part | 83% (83 to 84), offsets in part | 
| Full coverage, lost jobs, 30% | 96% (96 to 96), offsets in part | 94% (93 to 94), offsets in part | 81% (81 to 82), offsets in part | 
| Full coverage, lost jobs, 50% | 96% (96 to 96), offsets in part | 94% (93 to 94), offsets in part | 81% (81 to 82), offsets in part | 
| Full coverage, lost jobs, 70% | 96% (96 to 96), offsets in part | 94% (94 to 94), offsets in part | 82% (82 to 82), offsets in part | 
| Full coverage, shorter hours, 10% | 100% (100 to 101), offsets fully | 100% (99 to 100), offsets in part | 99% (99 to 99), offsets in part | 
| Full coverage, shorter hours, 30% | 100% (100 to 100), offsets fully | 99% (99 to 99), offsets in part | 98% (98 to 99), offsets in part | 
| Full coverage, shorter hours, 50% | 100% (100 to 100), offsets in part | 99% (98 to 99), offsets in part | 96% (96 to 97), offsets in part | 
| Full coverage, shorter hours, 70% | 98% (98 to 98), offsets in part | 96% (96 to 97), offsets in part | 89% (89 to 90), offsets in part | 
| Opt-in, lost jobs, 10% | 13% (12 to 15), offsets in part | −13% (−15 to −11), worsens | −9% (−10 to −8), worsens | 
| Opt-in, lost jobs, 30% | 4% (3 to 5), offsets in part | −19% (−21 to −18), worsens | −11% (−12 to −10), worsens | 
| Opt-in, lost jobs, 50% | −0% (−1 to 1), does not offset | −24% (−25 to −23), worsens | −13% (−13 to −12), worsens | 
| Opt-in, lost jobs, 70% | −3% (−4 to −2), worsens | −29% (−29 to −28), worsens | −14% (−14 to −13), worsens | 
| Opt-in, shorter hours, 10% | 69% (68 to 70), offsets in part | 15% (14 to 17), offsets in part | 3% (2 to 4), offsets in part | 
| Opt-in, shorter hours, 30% | 64% (64 to 65), offsets in part | 7% (6 to 8), offsets in part | −2% (−2 to −1), worsens | 
| Opt-in, shorter hours, 50% | 52% (52 to 53), offsets in part | −5% (−6 to −4), worsens | −6% (−7 to −6), worsens | 
| Opt-in, shorter hours, 70% | 19% (18 to 19), offsets in part | −16% (−17 to −15), worsens | −10% (−10 to −9), worsens | 

The backing the programme’s own work produces (nothing assumed backed; displacement as lost jobs at 0-70%): the main reading’s rows (m 0.25 to 1, low or high automation gain)
| Design, environment | Produced share of the payout, 20 years | Programme inflation, points a year, 20 years | With nothing produced, 20 years | Produced share, 40 years | Programme inflation, 40 years | Rows that do not back enough (every reading, both horizons) | 
| Full coverage, Reference | 6% to 17% | 48 to 62 | 58 to 63 | 6% to 18% | 45 to 67 | 88 of 88 | 
| Full coverage, Adverse | 6% to 17% | 54 to 69 | 65 to 70 | 5% to 17% | 58 to 81 | 88 of 88 | 
| Full coverage, Stress | 6% to 17% | 53 to 69 | 64 to 70 | 6% to 17% | 57 to 82 | 88 of 88 | 
| Opt-in, Reference | 5% to 7% | 35 to 44 | 39 to 43 | 4% to 7% | 33 to 48 | 88 of 88 | 
| Opt-in, Adverse | 5% to 7% | 41 to 50 | 45 to 50 | 4% to 7% | 45 to 62 | 88 of 88 | 
| Opt-in, Stress | 3% | 18 to 23 | 19 to 22 | 7% to 8% | 19 to 27 | 88 of 88 | 
Which savings measure. The savings figures here (adult-years with under three months of savings) are the preregistered measure, run for the headline rows. The report’s tables for the other rows (lost jobs against shorter hours, who gets the output gain, the slower path) use a stand-in, adult-years below 30 days of basic living, and say so; it moves differently, so no figure on this page mixes the two. The trace of the opt-in cells splits adults into those who would take part and those who would not; it decomposes a difference and does not test a cause.
Cost: a run at a displacement level minus the same run with none, positive is harm. Offset share: the cost with no programme minus the cost with it, over the cost with no programme. 95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model's randomness only; each category holds after a Holm correction over the 48 tests of its environment, horizon and design. Wealth figures are real wealth at year-0 prices under the engine’s price rule; in the headline block that rule is barely tested, because at full backing almost no unmatched money reaches prices. Inflation figures are at the produced backing, under the model’s placeholder price rule (all unmatched new money reaches prices), with no central bank response, no expectations and no general equilibrium: they measure the size of the unbacked money, not a forecast of prices. Not modelled: a fall in owners’ spending, investment out of the dividend, pay that differs by wage level in the pass-through, adults under 25 or over 64. Every figure, with the 40-year tables, displaced adults’ own outcomes, the design’s maintained take-home and the readings together: the report dev/reports/s85-output-per-hour.md, the files data/studies/s85-automation.json, s85-backing.json and s85-free-time.json (python3 dev/tools/s85_page_data.py s85-tables-50bc51d/s85-summary.json), engine 50bc51d, results s85-tables-50bc51d and s85-trace-50bc51d in BetterToBest/compassionism-sim-results; preregistration prereg/2026-11-s85-output-per-hour.md (research-update; Amendments 1-4).

## The Creative Collectives’ lending, and charters of public utilities (added Nov 21, 2026)
The proposal: the Creative Collectives lend to community businesses that sell essentials, for premises, equipment and set-up costs, where banks will not, and public utilities move to Collective charters. These are Duke’s statements; the Hub’s papers give the Collectives no lending role, so the study adds them to the design and models them as stated. A preregistered study adds a fund for the community businesses (grocers, counter-service restaurants, utilities), paced at the rate new establishments open in these sectors, with young firms’ failure rates, 14% of it in grants (the share Pennsylvania’s fresh-food financing gave), and charters under which public power’s customers pay the community-business price for electricity. Public power serves one customer in seven (APPA), so a third and two thirds are design parameters, swept. Both run in the full-coverage and the opt-in designs, in the three environments, at 20 and 40 years, on 500 paired seeds. The model has no private firms, so the fund finances community-business capacity only. Each figure is a row minus the main row of the same design; the main row is unchanged.
- The fund helps in no cell. Under the preregistered rule (it helps where it lowers basket poverty or yearly wealth poverty and worsens none of the six readings), it helps in 0 of 12 cells (three environments, two designs, 20 and 40 years), and it worsens at least two of the six readings in 12 of them. Of the eight other readings of the fund (half and double the pace, no pace limit, and others), 0 of 96 cells and readings pass. No reading changes the verdict.
- Where the share would reach its ceiling anyway, the fund only brings the gain forward. In five of the six cells at 20 years (everywhere but Stress with the opt-in design) the community businesses’ share of essential sales reaches the 49% ceiling by year 10 without the fund. The fund raises the share at year 5 and costs $37 to $63 per adult a year; yearly wealth poverty rises by 0.006 to 0.023 points in these cells.
- Where capital holds the share back (Stress, opt-in), the fund lifts the share at year 20 from 34% to 48%, but it makes every reading worse. Changes at 20 years, in dollars per adult a year: programme cost +$412 (running-cost subsidy on the extra sales +$291, the fund’s net outlay $142), the contribution that finances it +$261. Basket poverty changes by +0.066 points and weighted median wealth by −$416.
- The changes are small beside the programme’s own effect (for example, −32.8 points of basket poverty against no programme in Reference with full coverage), but they are on the unfavourable side.
- Charters of public utilities improve basket poverty, yearly wealth poverty and savings wherever they act, and worsen no reading: at one customer in seven (the share public power serves today) only in 2 of the six cells at 20 years (Stress, full coverage; Stress, opt-in), because elsewhere every zone already has more than that share; at two in three, basket poverty changes by −0.062 to −0.023 points at an added cost of $54 to $96 per adult a year (20 years, six cells). Charter rows that worsen a reading: 0 at 20 years and 0 at 40.
- The fund and charters together give the fund’s result: the interaction’s interval excludes zero for at least one reading in 12 of the 12 cells and for the programme’s cost in 12, but it is negligible: at most 0.002 points of any share and $7 of median wealth. Of the 52 readings whose interval excludes zero, 44 are on the unfavourable side, 8 on the favourable side and 0 too small to show at six decimals. No headline joins the two.

The fund, main reading, 20 years: change against the main row of the same design (95% seed interval; bold: worsens after the multiple-testing correction). Share in points at year 5; cost in dollars per adult a year; poverty and savings in points; median wealth in year-0 dollars.
| Environment, design | Share of essential sales, year 5 | Programme cost | Basket poverty | Wealth poverty, yearly average | Median wealth, weighted | Savings shortfall | 
| Reference, full coverage | +0.4 | +$45 ($42 to $49) | +0.001 (−0.001 to 0.002) | +0.008 (0.005 to 0.010) | −$35 (−$83 to $18) | +0.005 (0.003 to 0.007) | 
| Reference, opt-in | +2.6 | +$40 ($40 to $41) | +0.005 (0.001 to 0.009) | +0.017 (0.014 to 0.019) | −$72 (−$91 to −$52) | +0.015 (0.012 to 0.018) | 
| Adverse, full coverage | +0.5 | +$44 ($41 to $48) | −0.001 (−0.003 to 0.002) | +0.006 (0.004 to 0.008) | −$13 (−$42 to $18) | +0.004 (0.002 to 0.006) | 
| Adverse, opt-in | +2.9 | +$37 ($37 to $38) | +0.009 (0.005 to 0.013) | +0.014 (0.011 to 0.016) | −$44 (−$68 to −$20) | +0.012 (0.008 to 0.015) | 
| Stress, full coverage | +4.6 | +$63 ($60 to $65) | −0.007 (−0.011 to −0.004) | +0.023 (0.020 to 0.026) | +$19 (−$17 to $55) | +0.014 (0.012 to 0.017) | 
| Stress, opt-in | +7.5 | +$412 ($407 to $418) | +0.066 (0.058 to 0.075) | +0.025 (0.020 to 0.030) | −$416 (−$518 to −$315) | +0.011 (0.005 to 0.018) | 
The fund at 40 years, its other readings, and charters

The fund, main reading, 40 years: change against the main row of the same design (95% seed interval; bold: worsens after the multiple-testing correction). Share in points at year 5; cost in dollars per adult a year; poverty and savings in points; median wealth in year-0 dollars.
| Environment, design | Share of essential sales, year 5 | Programme cost | Basket poverty | Wealth poverty, yearly average | Median wealth, weighted | Savings shortfall | 
| Reference, full coverage | +0.4 | +$20 ($19 to $22) | +0.000 (−0.001 to 0.001) | +0.003 (0.002 to 0.004) | −$58 (−$95 to −$19) | +0.002 (0.001 to 0.003) | 
| Reference, opt-in | +2.6 | +$19 ($19 to $19) | +0.003 (0.001 to 0.005) | +0.009 (0.007 to 0.011) | −$96 (−$126 to −$66) | +0.009 (0.007 to 0.011) | 
| Adverse, full coverage | +0.5 | +$20 ($18 to $22) | −0.000 (−0.002 to 0.001) | +0.002 (0.001 to 0.003) | −$32 (−$60 to −$2) | +0.001 (0.000 to 0.003) | 
| Adverse, opt-in | +2.9 | +$18 ($18 to $18) | +0.006 (0.004 to 0.008) | +0.009 (0.007 to 0.011) | −$55 (−$73 to −$37) | +0.007 (0.005 to 0.010) | 
| Stress, full coverage | +4.6 | +$29 ($28 to $31) | −0.003 (−0.005 to −0.001) | +0.008 (0.006 to 0.010) | −$50 (−$77 to −$24) | +0.004 (0.003 to 0.006) | 
| Stress, opt-in | +7.5 | +$270 ($262 to $279) | +0.058 (0.052 to 0.063) | +0.024 (0.019 to 0.029) | −$573 (−$688 to −$455) | +0.009 (0.003 to 0.014) | 

The other readings of the fund, 20 years, six cells (three environments, two designs): the added cost, the number of its 36 readings that improve or worsen after the correction, and the cells where the preregistered rule counts it as helping
| Reading of the fund | Added programme cost, $ per adult a year (lowest to highest cell) | Readings that improve | Readings that worsen | Cells where it helps | 
| half the pace | 19 to 87 | 1 of 36 | 17 of 36 | 0 of 6 | 
| double the pace | 85 to 860 | 3 of 36 | 25 of 36 | 0 of 6 | 
| no pace limit | 371 to 1,233 | 4 of 36 | 32 of 36 | 0 of 6 | 
| the pace limits the fund's additions only | 106 to 736 | 2 of 36 | 27 of 36 | 0 of 6 | 
| mature firms' failure rate | 36 to 468 | 3 of 36 | 27 of 36 | 0 of 6 | 
| no failures | 30 to 495 | 3 of 36 | 29 of 36 | 0 of 6 | 
| all loans | 36 to 408 | 2 of 36 | 23 of 36 | 0 of 6 | 
| all grants | 45 to 436 | 5 of 36 | 14 of 36 | 0 of 6 | 

Charters of public utilities (no fund), 20 years: the range of the change against the main row over the six cells (three environments, two designs). Subsidy and cost in dollars per adult a year; poverty and savings in points; median wealth in year-0 dollars.
| Charters | Subsidy | Programme cost | Basket poverty | Wealth poverty, yearly average | Median wealth, weighted | Savings shortfall | 
| charters at 1/7 (public power today) | 0 to 4 | 0 to 3 | −0.002 to 0.000 | −0.002 to 0.000 | −0 to 7 | −0.003 to 0.000 | 
| charters at 1/3 | 6 to 35 | 5 to 25 | −0.018 to −0.003 | −0.015 to −0.003 | 4 to 50 | −0.023 to −0.004 | 
| charters at 2/3 | 67 to 113 | 54 to 96 | −0.062 to −0.023 | −0.041 to −0.022 | 68 to 218 | −0.071 to −0.026 | 

Charters of public utilities (no fund), 40 years: the range of the change against the main row over the six cells (three environments, two designs). Subsidy and cost in dollars per adult a year; poverty and savings in points; median wealth in year-0 dollars.
| Charters | Subsidy | Programme cost | Basket poverty | Wealth poverty, yearly average | Median wealth, weighted | Savings shortfall | 
| charters at 1/7 (public power today) | 0 to 2 | 0 to 1 | −0.001 to 0.000 | −0.001 to 0.000 | −0 to 2 | −0.002 to 0.000 | 
| charters at 1/3 | 3 to 18 | 3 to 13 | −0.009 to −0.002 | −0.011 to −0.002 | 3 to 42 | −0.016 to −0.002 | 
| charters at 2/3 | 59 to 82 | 44 to 90 | −0.046 to −0.015 | −0.039 to −0.015 | 132 to 478 | −0.058 to −0.018 | 
Limits, stated in advance: the model has no private firms, so lending to private start-ups that are not community businesses cannot be represented; transport, health care and child care have no community-business price, so charters of roads, transit, airports and ports change nothing in it; capacity is for the whole population, not by zone; the pace limit is a whole-economy rate, generous to one network; no concessional rate and no recovery on failures were opened as sources, and the loan’s principal is never repaid; charters act on electricity only; the fund’s money is new programme money, matched by full backing as every programme dollar is, and under a limit on supply it would compete for real resources, which is not in this design; and the trace of the cost reads stored totals and does not test a cause by switching each part off. 95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model's randomness only. Categories after the multiple-testing correction across the six readings of each row. Dollars are year-0 dollars; poverty and savings are unweighted, median wealth as labelled.

## The yardstick: pay by household type and the child and dependent care credit
Adopted in the release. The preregistered rule held, and Duke decided on Nov 21, 2026 to adopt both: the release’s main row includes pay by household type and the care credit, so every figure above already carries them. This section compares them with the v5.9 main row without them (the private businesses’ price set late, as published), which stays published as the record. Its figures come from the study’s rerun on the release engine (v5.9.23, engine 50bc51d). The first runs had a defect, fixed in that engine: the runs with pay by household type reused the stored no-programme supply path of a run without it. The comparison with US data at full take-up, which the rule reads, was not affected, and the rule reads the same on the rerun.
Every effect here is the programme against a run with no programme, so that run should look like the US. A preregistered study gave each household type its own pay from the Current Population Survey: single parents are paid less and couples with children more, as in the survey, and the overall pay distribution still matches the survey’s closely. It also added the child and dependent care credit. Both sit behind options, and the v5.9 main row is unchanged when they are off.
- The no-programme run is closer to the US. In Reference at 20 years, with full take-up, the EITC reaches 11.3% of adults (US 11.8%, on the same basis: each adult’s own tax unit, full take-up): single parents 51.4% (US 49.8%; the v5.9 main row 38.0%), couples with children 16.8% (US 16.5%). The four household types’ gaps sum to 5.1 points against 19.0 today. By the preregistered rule, Claude recommends this reading for the main row. Duke adopted both on Nov 21, 2026, so the results above carry them.
- Two gaps remain, reported and not tuned: the care credit reaches 18.3% of families with a child under 13 (tax data 21.4%) and pays $835 per receiving family (tax data $606). The model’s paying families all pay the full price of care.
- Opt-in design: in every environment and horizon, the programme cuts basket poverty by 0.33 to 0.94 points less, against cuts of 6.8 to 21.2 points, and the share below 30 days of basic living by 0.13 to 0.39 points less. These changes are unfavourable to the programme.
- Full-coverage design: the programme cuts the share below 30 days of basic living by 0.42 to 0.75 points more in every cell, and basket poverty changes by −0.21 to 0.68 points (less cut in five cells, more in one).
- Median wealth and inflation barely move: median wealth changes measurably in 0 of 12 cells, and programme inflation by at most 0.0069 points a year.
- Pay by household type does almost all of it. The credit alone changes no poverty effect by more than 0.02 points. The two additions’ interaction excludes zero in 15 of 60 tests, but is never larger than 0.005 points of basket poverty, which is negligible.
- With partners’ pay drawn independently rather than correlated as in the survey, the changes are larger (basket poverty 0.37 to 1.68 points), and the full-coverage change in the share below 30 days of basic living reverses: the programme then cuts it by 0.00 to 0.26 points less. The correlation is the survey’s, so this is a bound.

Change in the programme’s effect with both additions, against the v5.9 main row, 20 years (95% seed interval; bold: the interval excludes zero after correcting for five outcomes). A positive change on a poverty measure means the programme cuts it less. Poverty in points, median wealth in year-0 dollars, inflation in points a year.
| Design, environment | Below 30 days of basic living | Basket poverty | Too little wealth, yearly average | Median wealth, weighted | Programme inflation | 
| Full coverage, Reference | −0.55 (−0.60 to −0.49) | +0.11 (0.04 to 0.17) | −0.00 (−0.06 to 0.05) | +$891 (−$322 to $2,123) | +0.0069 (0.0066 to 0.0072) | 
| Full coverage, Adverse | −0.45 (−0.50 to −0.40) | +0.59 (0.52 to 0.66) | +0.10 (0.04 to 0.16) | +$444 (−$719 to $1,607) | +0.0044 (0.0041 to 0.0047) | 
| Full coverage, Stress | −0.44 (−0.50 to −0.39) | +0.62 (0.55 to 0.69) | +0.13 (0.07 to 0.19) | +$865 (−$294 to $1,999) | +0.0044 (0.0041 to 0.0047) | 
| Opt-in, Reference | +0.21 (0.15 to 0.27) | +0.84 (0.78 to 0.91) | +0.31 (0.25 to 0.37) | −$228 (−$1,403 to $976) | +0.0034 (0.0032 to 0.0037) | 
| Opt-in, Adverse | +0.28 (0.22 to 0.34) | +0.94 (0.87 to 1.01) | +0.35 (0.28 to 0.41) | −$420 (−$1,540 to $681) | −0.0014 (−0.0017 to −0.0010) | 
| Opt-in, Stress | +0.13 (0.09 to 0.17) | +0.39 (0.33 to 0.44) | +0.19 (0.14 to 0.24) | −$90 (−$1,046 to $857) | −0.0013 (−0.0016 to −0.0010) | 
The same at 40 years, the yardstick table, and the bounds

Change in the programme’s effect with both additions, against the v5.9 main row, 40 years (95% seed interval; bold: the interval excludes zero after correcting for five outcomes). A positive change on a poverty measure means the programme cuts it less. Poverty in points, median wealth in year-0 dollars, inflation in points a year.
| Design, environment | Below 30 days of basic living | Basket poverty | Too little wealth, yearly average | Median wealth, weighted | Programme inflation | 
| Full coverage, Reference | −0.75 (−0.80 to −0.69) | −0.21 (−0.26 to −0.16) | −0.34 (−0.40 to −0.29) | −$1,725 (−$3,958 to $408) | +0.0035 (0.0033 to 0.0036) | 
| Full coverage, Adverse | −0.43 (−0.48 to −0.38) | +0.61 (0.55 to 0.67) | −0.04 (−0.10 to 0.02) | −$58 (−$2,042 to $1,858) | +0.0022 (0.0021 to 0.0024) | 
| Full coverage, Stress | −0.42 (−0.47 to −0.37) | +0.68 (0.62 to 0.74) | +0.04 (−0.02 to 0.10) | +$810 (−$1,116 to $2,619) | +0.0022 (0.0020 to 0.0023) | 
| Opt-in, Reference | +0.14 (0.08 to 0.20) | +0.60 (0.55 to 0.65) | +0.32 (0.26 to 0.38) | −$1,942 (−$4,090 to $112) | +0.0021 (0.0020 to 0.0022) | 
| Opt-in, Adverse | +0.39 (0.33 to 0.45) | +0.79 (0.73 to 0.85) | +0.42 (0.36 to 0.49) | −$334 (−$2,095 to $1,399) | −0.0008 (−0.0009 to −0.0006) | 
| Opt-in, Stress | +0.17 (0.12 to 0.21) | +0.33 (0.29 to 0.37) | +0.19 (0.14 to 0.24) | −$565 (−$2,020 to $955) | −0.0000 (−0.0000 to 0.0000) | 

The no-programme run against US data, Reference, 20 years (full take-up, except the care credit). US: the Current Population Survey (own tax unit, full take-up) and IRS Statistics of Income (the care credit).
| Measure | US | Today’s main row | Both additions | 
| EITC reach, all adults | 11.77% | 10.90% | 11.32% | 
| EITC reach, single adults | 8.62% | 6.30% | 9.29% | 
| EITC reach, single parents | 49.77% | 37.99% | 51.37% | 
| EITC reach, couples without children | 4.55% | 2.66% | 1.88% | 
| EITC reach, couples with children | 16.54% | 19.60% | 16.76% | 
| refundable child tax credit reach, single parents | 45.31% | 36.69% | 49.79% | 
| refundable child tax credit reach, couples with children | 19.00% | 21.27% | 18.64% | 
| care credit reach, families with a child under 13 (take-up as measured) | 21.37% | none | 18.29% | 
| care credit per receiving family | $606 | none | $835 | 

The bounds: change in the programme’s effect on basket poverty (points) under each reading, 20 years (95% seed interval; bold: excludes zero after the correction).
| Design, environment | Both | Partners’ pay independent | The credit for every family | The credit in the no-programme run only | 
| Full coverage, Reference | +0.11 (0.04 to 0.17) | +1.10 (1.03 to 1.17) | +0.14 (0.07 to 0.20) | +0.11 (0.05 to 0.18) | 
| Full coverage, Adverse | +0.59 (0.52 to 0.66) | +1.63 (1.56 to 1.70) | +0.62 (0.55 to 0.69) | +0.60 (0.53 to 0.67) | 
| Full coverage, Stress | +0.62 (0.55 to 0.69) | +1.66 (1.59 to 1.73) | +0.63 (0.57 to 0.71) | +0.62 (0.56 to 0.70) | 
| Opt-in, Reference | +0.84 (0.78 to 0.91) | +1.52 (1.45 to 1.59) | +0.84 (0.77 to 0.90) | +0.86 (0.79 to 0.92) | 
| Opt-in, Adverse | +0.94 (0.87 to 1.01) | +1.31 (1.23 to 1.38) | +0.92 (0.85 to 0.99) | +0.97 (0.90 to 1.04) | 
| Opt-in, Stress | +0.39 (0.33 to 0.44) | +0.50 (0.44 to 0.55) | +0.39 (0.34 to 0.44) | +0.40 (0.35 to 0.45) | 

The bounds: change in the programme’s effect on basket poverty (points) under each reading, 40 years (95% seed interval; bold: excludes zero after the correction).
| Design, environment | Both | Partners’ pay independent | The credit for every family | The credit in the no-programme run only | 
| Full coverage, Reference | −0.21 (−0.26 to −0.16) | +0.73 (0.68 to 0.78) | −0.19 (−0.24 to −0.14) | −0.21 (−0.26 to −0.16) | 
| Full coverage, Adverse | +0.61 (0.55 to 0.67) | +1.60 (1.54 to 1.65) | +0.64 (0.58 to 0.70) | +0.62 (0.56 to 0.68) | 
| Full coverage, Stress | +0.68 (0.62 to 0.74) | +1.68 (1.62 to 1.73) | +0.70 (0.64 to 0.76) | +0.69 (0.63 to 0.75) | 
| Opt-in, Reference | +0.60 (0.55 to 0.65) | +1.28 (1.23 to 1.33) | +0.60 (0.55 to 0.65) | +0.62 (0.57 to 0.67) | 
| Opt-in, Adverse | +0.79 (0.73 to 0.85) | +0.98 (0.93 to 1.05) | +0.78 (0.72 to 0.83) | +0.82 (0.76 to 0.87) | 
| Opt-in, Stress | +0.33 (0.29 to 0.37) | +0.37 (0.33 to 0.41) | +0.33 (0.29 to 0.37) | +0.35 (0.31 to 0.39) | 
Limits: pay by household type sets who has low yearly pay, not a choice of hours, so hours that respond to the programme or to taxes enter only through the labour response on yearly pay; hours are not modelled separately (part-time and part-year work are inside the yearly pay the model reads); household types are fixed for the run; each type’s pay is a lognormal curve fitted to its quartiles, so the bottom tenth of pay is somewhat too high, as before. The seed intervals cover the model’s randomness only. Report: dev/reports/s100-part-time-dcc.md; preregistration: prereg/2026-11-s100-part-time-dcc.md (research-update); engine 50bc51d, seeds 1-500, tables s100-tables-50bc51d.

## Paid for by a contribution instead (shown, never led with)
If the programme is paid for by a contribution, with the rest borrowed, the contribution needed is far larger and the poverty effects are much smaller, and in some cells they reverse. Nearly every financed result is fragile: 45 of the 48 poverty and wealth curves change sign or lose significance at some reading, depending on how the contribution is set up. The 3 that hold are the full-coverage design’s wealth-poverty effect in Reference at 40 years; and the opt-in design’s basic-living effect in Reference, at both horizons. The contribution is measured against different incomes by design: the full-coverage design’s is a share of all money income (capped at 90%), the opt-in design’s a flat share of wages, so the two designs’ rates are not comparable. These rows were run without the weighted top tail (the 18 adults who carry population weights and stand for the very wealthy), so the top of the wealth distribution is less extreme than on the main rows and the figures that count by population weight (median real wealth, shares of wealth) are the ones that can differ from the main rows’; the size of that difference is not reported. The poverty measures count every simulated adult once.

Paid for by a contribution instead, 20 years (shown, never led with; run without the weighted top tail): the contribution needed, the effects, and debt at the end
| Design | Environment | Mean contribution | Cost of living (points) | Median real wealth | Government debt (% of GDP) | 
| Full-coverage design | Reference | 69% | −13.6 | −$3,761 | 4% | 
| Full-coverage design | Adverse | 78% | −3.7 | −$1,909 | 14% | 
| Full-coverage design | Stress | 76% | −0.6 | −$4,818 | 9% | 
| Opt-in design | Reference | 69% | +6.6 | −$31,083 | 14% | 
| Opt-in design | Adverse | 58% | +8.0 | −$20,373 | 2% | 
| Opt-in design | Stress | 18% | +0.4 | −$2,133 | 0% | 

## Who gains
The programme lowers the top 1%’s share of wealth, raises the bottom half’s, and sharply reduces the share of families in debt (a family is a household where the model has households, otherwise an adult, whose net worth, its adults’ wealth together, is below zero at the end of the run); the opt-in design moves them about half as far. These measures are reported for the main row only, with seed intervals, and were not swept across the preregistered readings, so no range across readings is given for them. Below the top fifth of starting wealth, slightly higher prices lower what adults owe (a small gain); at the top, where money is lent, they are a loss. Adults outside the labour force (disability, early retirement, care, school) stay far more often below the cost of living than adults in the labour force under the same design; the dollar gains are quoted as dollars, not percentages, because the lowest tenth of adults start from negative wealth; the Question 6 report and the erosion tables (r2-erosion-50bc51d/tables.md in the results repository) give the split.

Who gains: Reference, 20 years, main row. Wealth in year-0 dollars; changes with 95% seed intervals
| Measure | Design | No programme | Programme | Change | 
| top 1% share of wealth (%) | Full-coverage design | 31.6% | 27.0% | −4.6 (−4.7 to −4.5) | 
| top 1% share of wealth (%) | Opt-in design | 31.6% | 29.3% | −2.3 (−2.3 to −2.3) | 
| bottom 50% share of wealth (%) | Full-coverage design | 2.8% | 9.1% | +6.3 (6.2 to 6.4) | 
| bottom 50% share of wealth (%) | Opt-in design | 2.8% | 5.7% | +2.9 (2.8 to 2.9) | 
| families in debt (%) | Full-coverage design | 24.1% | 0.9% | −23.3 (−23.4 to −23.1) | 
| families in debt (%) | Opt-in design | 24.1% | 9.1% | −15.0 (−15.2 to −14.9) | 
| stayed in the lowest wealth fifth (%) | Full-coverage design | 66.4% | 70.2% | +3.8 (3.5 to 4.2) | 
| stayed in the lowest wealth fifth (%) | Opt-in design | 66.4% | 72.3% | +5.9 (5.5 to 6.3) | 
| wealth P10 ($) | Full-coverage design | −$2,498 | $120,206 | +$122,704 ($121,874 to $123,528) | 
| wealth P10 ($) | Opt-in design | −$2,498 | $20,981 | +$23,480 ($22,755 to $24,248) | 
| wealth P90 ($) | Full-coverage design | $1,953,370 | $2,169,785 | +$216,415 ($209,609 to $222,846) | 
| wealth P90 ($) | Opt-in design | $1,953,370 | $2,058,575 | +$105,205 ($99,567 to $110,788) | 
| labour's share of money income (%) | Full-coverage design | 82.6% | 52.2% | −30.4 (−30.6 to −30.1) | 
| labour's share of money income (%) | Opt-in design | 82.6% | 71.0% | −11.5 (−11.7 to −11.4) | 

## Unfavourable results, together
- Prices: programme inflation is above no programme in every cell: immaterial at the main row (full backing), 35 to 50 points a year with no backing in the full-coverage design and 19 to 47 in the opt-in design (table above): the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices.
- Wages below full backing: if wages follow half of programme inflation and the rest is never made up, the programme with no backing leaves more people below the cost of living (basket poverty) than no programme does in 2 of the six cells: Reference at 40 years, Stress at 40 years (the supply study, above).
- Automation: in the opt-in design with lost jobs, the rise in basket poverty is larger with the programme than without it in 7 of 12 cells at 20 years; and the programme’s own work produces 6% to 17% of the backing the full-coverage figures assume, at programme inflation of 48 to 69 points a year (automation study, above; the size of the unbacked money in a model with no central-bank response and no expectations, not a forecast of prices).
- Lending: the Creative Collectives’ fund for community businesses helps in no cell and worsens at least two of the six readings in 12 of 12 cells; where capital does hold the share back (Stress, opt-in, 20 years) it changes the programme’s cost by +$412 per adult a year and basket poverty by +0.066 points.
- The yardstick: with pay by household type and the care credit (the reading Claude recommends for the main row), the opt-in design cuts basket poverty by 0.33 to 0.94 points less in every environment and horizon (study above).
- Work: fewer adults work: participation falls (adults who leave work for the programme), with their earnings forgone.
- Mobility: less movement out of the lowest wealth fifth (“stayed in the lowest wealth fifth”, above).
- Adults outside the labour force (disability, early retirement, care, school) stay below the cost of living in a large share of their adult-years even with the programme, far more than adults in the labour force, and more so under the opt-in design than under the full-coverage design (the Question 6 report’s table gives each group).
- Labour’s share of money income falls, partly because the programme’s payments are income that is not wages (they enlarge the total it is measured against) and partly because fewer adults work.
- Stress: the opt-in design’s effects shrink by about two thirds in the Stress environment.
- Financing: 45 of 48 financed poverty and wealth curves are fragile (those that hold: the full-coverage design’s wealth-poverty effect in Reference at 40 years; and the opt-in design’s basic-living effect in Reference, at both horizons), and the opt-in design paid by a contribution on wages raises basket poverty in 4 of its 6 cells.

Work: Reference, 20 years, main row
| Measure | Design | No programme | Programme | Change (points) | 
| employment (% of adult-years) | Full-coverage design | 82.5% | 79.0% | −3.5 (−3.6 to −3.5) | 
| employment (% of adult-years) | Opt-in design | 82.5% | 79.9% | −2.6 (−2.7 to −2.5) | 
| participation (% of adult-years) | Full-coverage design | 82.5% | 79.0% | −3.5 (−3.6 to −3.5) | 
| participation (% of adult-years) | Opt-in design | 82.5% | 79.9% | −2.6 (−2.7 to −2.6) | 
| programme leavers (% of adult-years) | Full-coverage design | 0.0% | 3.5% | +3.5 (3.4 to 3.6) | 
| programme leavers (% of adult-years) | Opt-in design | 0.0% | 2.6% | +2.6 (2.5 to 2.7) | 
| outside the labour force (% of adult-years) | Full-coverage design | 17.3% | 17.3% | +0.0 (0.0 to 0.0) | 
| outside the labour force (% of adult-years) | Opt-in design | 17.3% | 17.3% | +0.0 (0.0 to 0.0) | 

## What no figure here covers
The seed intervals measure the model’s randomness only. They do not cover the choice of main row or full backing (a design statement); the readings the screen held fixed; Stress, which was not screened; or the engine’s structure: a fixed population in the main row (no ageing, births or deaths; added Nov 17, 2026), one price rule for the whole economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub’s statements and measured costs, and 500 adults (a 10,000-adult pair was compared on hours worked, participation and the top 1%’s share of weighted wealth, where it agrees; it did not check the poverty or median-wealth headlines). The financed rows leave out the weighted top tail. The model has not been reviewed by an independent economist.
How the weights are spread. 18 of the 500 simulated adults stand for the very top of the wealth distribution, and their weights differ widely: 13 carry less than 0.1 each, 4 carry more than 2 (the largest is 3.47), and one carries about 1. Together they hold 2.6% of the total weight. The other 482 adults count about once (0.99 to 1.13). Counted this way the 500 adults are as informative as 472.6 adults counted once (the effective sample size), and no adult carries more than 0.69% of the total weight (an adult counted once carries 0.2%). The set of weights is the same in every seed and environment checked; which adults carry them depends on the seed. Measures counted per adult (unweighted) do not use them.
Where each figure comes from (basis class: simulation release and command): the release engine 50bc51d (v5.9.23), seeds 1-500, run on GitHub Actions Nov 21-23, 2026, under the preregistration frozen for the model registered on OSF (prereg/2026-11-s63-round2-freeze.md; osf.io/msdzk; engine 104691f, first published as v5.8) and the release’s own preregistered reruns (prereg/2026-11-s90-private-price-at-sale.md, Amendments 2-6). Results: r2-<part>-<env>-<years>-50bc51d in compassionism-sim-results; tables r2-tables-50bc51d; erosion trace r2-erosion-50bc51d. The v5.9 figures before this release: the same folders ending 104691f. Commands: dev/tools/s64_tables.py, dev/tools/s64_erosion.js, dev/tools/s64_charts.py, dev/tools/r2_study_files.py. Every row is also in “Every preregistered study” below.
 

# The findings page: the central-bank section


## The central bank switch #
 
v5.9 has no central bank in its main row. The central-bank study adds one as a switch: a policy rate set by a Taylor rule (floored at zero, with bond purchases below the floor), which moves deposit and loan rates, refinancing, share and home prices and job loss, and lets households past their borrowing limit sell homes and shares to households with cash. It asks two questions: does the central bank steady households, and does the programme’s share of essentials damp what the central bank and outside shocks do to the cost of basic living? The rule is the same with and without the programme. History follows the actual US path of 2005-2025.

Every figure in this section is a mean over 100 paired runs (seeds 1-100), not the 500 of v5.9’s main row; the intervals measure the model’s randomness over those runs.
- Steadier at the bottom. With the central bank on, a recession year pushes 10.0% of households below the basket line with no programme, 0.5% with the full-coverage design and 5.4% with the opt-in design (Adverse). With the full-coverage design the median adult’s largest fall in real wealth changes by −$21,067 against no programme.
- Less steady in prices. Both designs widen the year-to-year spread of the basket’s price level (full-coverage design: +0.61 points in Adverse; +0.12 in History). In Reference, Adverse and Stress outside inflation is fixed, so the programme’s own price changes are the larger source of price swings there.
- The damping claim is not supported. The design says its share of essentials should damp what the central bank and outside shocks do to the cost of basic living. In this engine the rule moves rates, asset prices and job loss, not the price of essentials, so it cannot show that damping, for either design. That is a limit of the model, not evidence about the world.
- The rule moves wealth up the ladder; the programme shrinks that. Over 2005-2025 with no programme, the rule changes the top 1%’s share of net worth by +0.45 points and the bottom half’s by −0.47; with the full-coverage design on, by +0.31 and −0.16.
- Forced sales. With the rule and no programme, 22.6% of adult-years in History involve a forced sale of real assets by a household past its borrowing limit, bought by households with cash; with the full-coverage design, 1.0%.
- The poverty results barely move. Turning the rule on changes the full-coverage design’s basket poverty by +0.02 points in History and −0.01 in Adverse; under full backing the programme’s own inflation is near zero, so the rule rarely responds to it.
 
DesignFull coverageOpt-in designEnvironmentHistory 2005-2025AdverseStressReference

Full-coverage design, Adverse: the programme’s effect with no central bank and with the rule, and the rule’s own effect (with the rule minus without it) in each run. Means over the same 100 paired seeds (not the 500 of v5.9’s main row).
| Outcome | Programme’s effect, no central bank (95%) | Programme’s effect, the policy-rate rule (95%) | The rule’s own effect, no programme | The rule’s own effect, programme | 
| Below 30 days of basic living (points) (unweighted) | −20.4−20.7 to −20.1 | −20.5−20.8 to −20.2 | +0.1−0.0 to +0.2 | −0.0−0.0 to +0.0 | 
| Below the cost of living (points) (unweighted) | −40.8−41.2 to −40.3 | −40.6−41.0 to −40.2 | −0.2−0.2 to −0.1 | −0.0−0.0 to −0.0 | 
| Children below the cost of living (points) (unweighted) | −50.2−51.0 to −49.3 | −50.0−50.8 to −49.2 | −0.1−0.2 to −0.1 | −0.0−0.0 to +0.0 | 
| Too little wealth, yearly average (points) (unweighted) | −18.9−19.2 to −18.7 | −19.0−19.3 to −18.7 | −0.0−0.2 to +0.1 | −0.1−0.1 to −0.1 | 
| Median real wealth at the end (weighted) | +$198,919+$195,946 to +$201,892 | +$208,372+$205,064 to +$211,679 | +$13,352+$8,990 to +$17,715 | +$22,805+$18,590 to +$27,020 | 
| Programme inflation (points a year) (unweighted) | +0.19+0.19 to +0.19 | +0.19+0.19 to +0.19 | less than 0.01less than 0.01 to less than 0.01 | less than 0.01less than 0.01 to less than 0.01 | 
| Pushed below the basket line in a recession year (points) (weighted) | −9.7−10.5 to −8.8 | −9.5−10.4 to −8.6 | −0.2−0.2 to −0.1 | −0.0−0.0 to +0.0 | 
| Largest fall in real wealth, median adult (weighted) | −$136−$196 to −$76 | −$21,067−$23,780 to −$18,354 | +$41,863+$36,466 to +$47,260 | +$20,931+$18,088 to +$23,775 | 
| Spread of the basket price level’s yearly change (points) (unweighted) | +0.61+0.59 to +0.62 | +0.61+0.60 to +0.62 | less than 0.01less than 0.01 to less than 0.01 | less than 0.01less than 0.01 to less than 0.01 | 
| Top 1% share of net worth at the end (points) (weighted) | −4.54−4.68 to −4.41 | −4.46−4.60 to −4.33 | −0.19−0.34 to −0.04 | −0.11−0.25 to +0.03 | 
| Bottom half’s share of net worth at the end (points) (weighted) | +6.16+5.93 to +6.39 | +6.24+6.00 to +6.48 | −0.09−0.13 to −0.05 | −0.01−0.07 to +0.05 | 
| Adult-years with a forced sale (points) (weighted) | — | −21.80−22.20 to −21.40 | — | — | 
 
How the Federal Reserve is governed, and why the rule is not the Fed

The Board of Governors is appointed by the President and confirmed by the Senate. Each of the twelve Reserve Banks has nine directors, six of them elected by the member banks of its district; since the Dodd-Frank Act (2010), the directors who represent banks no longer vote on choosing the Reserve Bank’s president. The model does not represent these choices: its rule is a fixed formula of inflation and unemployment, the same in every run, so the comparison is between rules, not institutions.

Earlier eras: the Research Hub’s page US Policy Eras and Stability, 1947-2025 compares the postwar eras’ inflation, unemployment, prices, tax rates and health care with 2005-2025, and runs today’s households under each era’s settings. Its engine readings were run without the release’s global settings (the same omission found in the central-bank study) and are being rerun; its descriptive panel is not affected.

How the weights are spread. 18 of the 500 simulated adults stand for the very top of the wealth distribution, and their weights differ widely: 13 carry less than 0.1 each, 4 carry more than 2 (the largest is 3.47), and one carries about 1. Together they hold 2.6% of the total weight. The other 482 adults count about once (0.99 to 1.13). Counted this way the 500 adults are as informative as 472.6 adults counted once (the effective sample size), and no adult carries more than 0.69% of the total weight (an adult counted once carries 0.2%). The set of weights is the same in every seed and environment checked; which adults carry them depends on the seed. Measures counted per adult (unweighted) do not use them.
Where these figures come from (simulation release and command): the release v5.9.23. Central bank off: the main row (the model has no central bank unless this switch adds it), engine 50bc51d, seeds 1-500, results r2-m-<env>-20-50bc51d (file data/studies/r2-effects.json). Central bank on: the central-bank study’s rerun with the release’s settings, engine 50bc51d, seeds 1-100, results s74-final-50bc51d (file data/studies/s74-cb.json; python3 dev/tools/s76_cb_data.py s74-final-50bc51d --check-r2=<folder with r2-m-*-20-50bc51d> --r2-engine=50bc51d). Both in BetterToBest/compassionism-sim-results. Intervals cover the model’s randomness only.
 
