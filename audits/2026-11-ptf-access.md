# Who can buy at PTF prices, and what the 40% test counts (Nov 7, 2026)

Raised by Duke in Chat after the community-layer report (S38), before the Simulation release (S7). This note says what the engine does, what the Hub says, Claude's reading of the design, and what changes. It changes the model of the design, not the design.

## The question

S38 found the community layer changes nothing material, and offered a likely reason, not tested: with the layer, 81% of PTF members get the food price cut, but only 11% live where the synergy coefficient θ applies, and members are only about a fifth of adults.

Duke's answer (Nov 7): in the design anyone can join, and anyone can shop at a PTF business, a grocer for example, paying in dollars or in Basic Units (BU).

## What the engine does (engine `ce8d030`, read in the code)

In the engine, "PTF member" stands for "PTF customer" everywhere. Non-members never pay PTF prices.

- **Membership.** A yes-or-no status for each adult, decided by the household head. The starting share comes from the environment (18% of adults in Reference and Adverse, 8% in Stress; study I sets 10%, 30% and 50%). Each year a non-member joins with probability 0.005 + 0.05 × the member share (the community's share with the layer, the population's without), plus 0.015 if precarious (`PTF_BASS_Q`, Bass 1969). With SZH on, θ draws more adults in. Joining is capped by PTF capacity: members never exceed the larger of last year's count and c × adults, where c = min(1, c0 + capital per adult ÷ $18,862) (ledger d101). Members leave at 3.2% a year.
- **The PTF price cut** on food and utilities, at the Hub's ε (about 9% of a member's basket on average, `pfCut`): members only. The engine's own test says so: "no one outside PTF gets one".
- **The ESP split's PTF price share:** members only. Duke's confirmed answer on Oct 1 (d98) was every adult, in proportion to essentials spending; on the same day Claude changed it, under the delegation, to members only "for consistency", because the PTFs' share of the premium is sized on the BU that members spend (Simulation `dev/DECISIONS.md`, Step 1). Every adult remains a sensitivity row (`cust: 'all'`). Duke's d99 (one price for BU and cash) stands.
- **PTF capacity** is counted in members served.
- **The two density tests** (ε falls from 2.64 to 1.65 below 40%; θ is zero below 55%) read the member share of adults: of the population without the layer, of each community with it. S37's reading 2 made this explicit: placing PTF businesses in a zone was modelled as grouping PTF members into one community.
- **θ's add-on** to the conversion rate goes to members only.

## What the Hub says

- Glossary, *Public Trust Foundations*: PTF businesses (grocers, counter-service restaurants, utilities, transport, childcare, clinics, schools) accept BU as payment, operate not-for-profit, are governed by stakeholders ("employees, customers, and community representatives"), and complement private markets. Customers are named apart from the governing members.
- FAQ: PTF governance includes "regular customers".
- Glossary: every resident receives an equal initial allocation from non-housing PTFs; housing PTF acres go only to opted-in residents.
- BLEI paper, section 6.1: "Below approximately 40% PTF merchant participation in a given zone, ε falls toward 1.5–1.8× as insufficient volume prevents Mondragon-equivalent overhead reduction." The same paragraph: "below 55% participation density, cooperative synergies do not activate."
- Nothing in the Hub makes membership a condition of buying at a PTF.

## Claude's reading of the design (each a modelling assumption unless stated)

1. **Anyone may buy at a PTF, in dollars or BU, at one posted price.** Not an assumption: Duke, Nov 7, and ledger d98 and d99.
2. **What limits the reach of PTF prices is how much of a zone's essentials the PTFs can supply, not who has signed up.** Each adult buys that share of their food and utilities at PTF prices. Cautious: no one buys more than the zone's share, and shopping in another zone stays unmodelled (as in S37).
3. **The 40% test counts the PTFs' share of a zone's essential sales** ("merchant participation", as written). A share of sales rather than a count of shops, because the paper's reason is volume.
4. **The 55% test for θ counts the same share.** It sits in the same paragraph, about the same network, and the Hub names no other quantity.
5. **Membership keeps only what the Hub ties to members:** governance, and housing PTF (PTH). The session that builds the switch lists every member-only rule in the engine (price cut, ESP price share and its sizing, capacity, θ's add-on, the workforce option, PTH's member basket) and states for each whether it is a customer rule (opened to every shopper) or a membership rule (kept). Where the Hub is silent, it takes the reading with the smaller effect and labels it.
6. **Start and growth (revised after Duke's answer, Nov 7).** The environments' starting shares (18%, 8%) are read as the PTFs' starting share of essential sales. The share then grows as far as three things allow, whichever binds first: **capacity** (capital: the sourced rule, d101), **operations** (a PTF expands only where its sales cover its operating costs), and **market demand** (how much of their essentials shoppers choose to buy at PTFs at PTF prices). Imitation stays only for membership, which no longer moves prices. The engine has no PTF operating accounts and no shopper choice between PTF and private sellers today, so S55 adds both, each with sourced figures or labelled design parameters that are swept. Where the Hub is silent, the reading with the smaller effect is taken.

## What this changes, and what it does not

- **S36 and S38 stand as published**, for the mechanism as modelled (research rule 1). The frozen batch is not revised.
- **It is a model change,** so it gets a switch, `PTF_ACCESS`: `'members'` (today; the guard test proves it bit-identical) and `'open'` (this reading). Then a dated amendment to the study programme and the community-layer addendum, a pilot, the rows at 500 seeds on GitHub Actions (free), and a report beside S36 and S38.
- **No expected result.** Open access spreads the price cut over every adult at the zone's share instead of over a fifth of adults in full, and the tests may pass where member shares never reached 40% or 55%. The capacity rule may still bind. The study decides.
- **The release (S7) waits for it** and carries both readings behind the switch, so the Hub's PTF figures (S25, S40) do not rest on a reading Duke has said is wrong. S5 and S39 can run meanwhile.

## Plan: S55 · Open PTF access (opus, xhigh; may take 2-3 sessions)

Waits on: nothing (D16 answered Nov 7). S7 waits on S55. Likely 3 sessions: design and switch; growth rule and amendments; run and report.

1. Read the engine's member-only rules and write the table in reading 5 into the Simulation's `dev/DECISIONS.md`.
2. Build `PTF_ACCESS` behind the switch, with the guard test (off = bit-identical) and unit tests: open access gives every adult in a zone the same share at PTF prices; the tests read the sales share; nothing changes in the no-programme run.
3. Build the growth rule of reading 6: PTF operating accounts (sales against operating costs, from the cost structure the BLEI paper cites or outside sector data, opened and cited) and shoppers' demand at PTF prices (a sourced response to the price gap, or a labelled design parameter, swept). Each behind `PTF_ACCESS: 'open'`; unit tests for each limit binding alone.
4. Before any run, dated amendments (research-update `prereg/`): the release row, the PTF and SZH cells Q2 needs, studies G-J's layer rows under `'open'`, and the fixed-share sweep (10% to 100% in steps of 10, growth off; Duke, D16); three environments; 20 and 40 years; 10,000 adults for the headline; seeds 1-500, paired with the frozen rows. Pilot on Actions at reduced seeds first. A run-manifest amendment covers the new jobs.
5. Run on Actions; report open against members on every preregistered outcome, nulls included.
6. The report shows the fixed-share curve with intervals and says which of capacity, operations and demand binds, by environment and year.

## Duke's answers (ledger D16, Nov 7)

- Reading 2 (prices reach every adult for the zone's PTF share): **yes.**
- Readings 3 and 4 (both tests count the PTFs' share of a zone's essential sales): accepted, and **sweep the share up to 100%** for analysis. Claude's reading: rows that hold the zone's PTF share fixed at 10%, 20%, ..., 100%, with the growth rule off, so the study shows the whole response curve, including what happens as the share crosses 40% and 55%, separately from how fast a real network would grow.
- Reading 5 (membership keeps only governance and housing PTF): **yes.**
- Reading 6 (starting shares as sales shares that grow with capacity): **yes with capacity, and market demand, capital and operations are factors too.** Reading 6 above is revised to that.
