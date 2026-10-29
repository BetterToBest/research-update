"""S30 step 2: run the simulation code the Hub papers print, as printed.

Every block below is copied verbatim from the paper (HTML page or PDF; the PDF
text was taken with `pdftotext -layout` and re-indented only where the PDF
layout broke Python indentation). Each block is run twice:
  A. as printed: nothing added (the papers print no imports);
  B. with the obvious imports supplied (`import random`, `import numpy as np`).
Then, where the block defines a callable, it is called with the parameters the
paper states (or none, if it takes none). Results go to stdout and to
audits/early/printed_code.out.

    python3 audits/early/printed_code.py
"""
import io, contextlib, traceback, os

BLOCKS = []

def block(name, source, code, call):
    BLOCKS.append((name, source, code, call))

# economic-modeling-simulation.html, Appendix A.1 (also the PDF section 11.1 variant below)
block('MonteCarloAnalysis (Appendix A.1, HTML)',
      'economic-modeling-simulation.html lines 1194-1237',
'''
class MonteCarloAnalysis:
    def __init__(self, n_iterations=10000):
        self.n_iterations = n_iterations
        self.results = []

    def run_integrated_simulation(self):
        results = []
        for i in range(self.n_iterations):
            scenario = self.generate_scenario()
            outcome = self.calculate_outcome(scenario)
            results.append(outcome)

        return {
            'poverty_elimination': np.percentile([r['poverty_rate'] for r in results], [5, 50, 95]),
            'fiscal_balance': np.percentile([r['fiscal_balance'] for r in results], [5, 50, 95]),
            'gini_reduction': np.percentile([r['gini_improvement'] for r in results], [5, 50, 95]),
            'system_stability': sum(r['stable'] for r in results) / len(results)
        }

    def generate_scenario(self):
        return {
            'basic_amount': random.uniform(800, 1500),
            'ptf_uptake': random.uniform(0.10, 0.30),
            'conversion_rate': random.uniform(0.10, 0.15),
            'automation_level': random.uniform(0.3, 0.7),
            'participation_rate': random.uniform(0.55, 0.95),
            'economic_shock': self.generate_shock()
        }

    def calculate_outcome(self, scenario):
        # Detailed economic modeling calculations
        poverty_rate = self.simulate_poverty_dynamics(scenario)
        fiscal_balance = self.simulate_fiscal_outcomes(scenario)
        gini_coefficient = self.simulate_inequality_effects(scenario)
        stability = self.assess_system_stability(scenario)

        return {
            'poverty_rate': poverty_rate,
            'fiscal_balance': fiscal_balance,
            'gini_improvement': gini_coefficient,
            'stable': stability
        }
''', 'MonteCarloAnalysis(n_iterations=10000).run_integrated_simulation()')

block('CCOAgent (Appendix A.2, HTML)',
      'economic-modeling-simulation.html lines 1240-1280',
'''
class CCOAgent:
    def __init__(self, agent_id, initial_conditions):
        self.id = agent_id
        self.wealth = initial_conditions['wealth']
        self.skills = initial_conditions['skills']
        self.octave_level = 0
        self.collective_membership = None
        self.ptf_participation = False
        self.conversion_rate = 1.0

    def make_decisions(self, environment):
        # Labor supply decision
        work_hours = self.optimize_work_allocation(environment)

        # Participation decision
        participate = self.evaluate_participation_benefit(environment)

        # Housing choice
        housing_choice = self.select_housing_option(environment)

        return {
            'work_hours': work_hours,
            'participate': participate,
            'housing': housing_choice
        }

    def update_state(self, outcomes, environment):
        # Update wealth
        self.wealth += outcomes['income'] - outcomes['consumption']

        # Update octave level based on performance
        if outcomes['quality_score'] > environment['advancement_threshold']:
            self.octave_level = min(self.octave_level + 1, environment['max_octave'])

        # Update conversion rate based on assessment
        self.conversion_rate = self.calculate_conversion_rate(outcomes['assessment'])
''', "CCOAgent(1, {'wealth': 0, 'skills': 1}).make_decisions({})")

block('MonteCarloAnalysis (section 11.1, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 11.1',
'''
class MonteCarloAnalysis:
 def run_integrated_simulation(self):
   results = []
   for i in range(10000):
       scenario = {
           'basic_amount': random.uniform(1000, 1500),
           'ptf_uptake': random.uniform(0.10, 0.25),
           'conversion_rate': random.uniform(0.10, 0.15),
           'automation_level': random.uniform(0.3, 0.7),
           'participation_rate': random.uniform(0.6, 0.95)
       }

       outcome = self.calculate_outcome(scenario)
       results.append(outcome)

   return {
       'poverty_elimination': np.percentile(results, [5, 50, 95]),
       'fiscal_balance': np.percentile(results, [5, 50, 95]),
       'gini_reduction': np.percentile(results, [5, 50, 95]),
       'system_stability': sum(r['stable'] for r in results) / len(results)
   }
''', 'MonteCarloAnalysis().run_integrated_simulation()')

block('calculate_ptf_enhanced_conversion (section 1.2, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 1.2',
'''
def calculate_ptf_enhanced_conversion(member, ptf_participation):
    base_conversion = member.octave_level * member.quality_multiplier

    ptf_multipliers = {
        'ptf_worker': 1.5,     # 50% bonus for PTF employment
        'ptf_resident': 1.2,    # 20% bonus for opted-in housing
        'ptf_board_member': 1.8,     # 80% bonus for governance
        'acre_holder': 1 + (member.acres / 1000) # Scaling with ownership
    }

    total_multiplier = 1.0
    for role, multiplier in ptf_multipliers.items():
        if member.has_role(role):
          total_multiplier *= multiplier

    return base_conversion * total_multiplier
''', None)

block('AcreEquityModel (section 2.2, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 2.2',
'''
class AcreEquityModel:
 def calculate_wealth_growth(self, years):
   initial_acres = 100 # Per resident allocation

   # PTF asset appreciation (conservative 3-5% annually)
   appreciation_rate = 0.04

   # Dividend yield from PTF operations
   dividend_yield = 0.03

   # Compound growth formula
   acre_value = initial_acres * (1 + appreciation_rate) ** years
   dividends = sum([initial_acres * (1 + appreciation_rate) ** t * dividend_yield
              for t in range(years)])

   total_wealth = acre_value + dividends

   return {
       'acre_value': acre_value,
       'cumulative_dividends': dividends,
       'total_wealth': total_wealth,
       'annualized_return': (total_wealth / initial_acres) ** (1/years) - 1
   }
''', 'AcreEquityModel().calculate_wealth_growth(30)')

block('ptf_job_creation (section 4, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 4',
'''
def ptf_job_creation(ptf_assets, automation_level):
 jobs_per_million = {
     'housing_management': 2.5,
     'retail_grocery': 8.0,
     'restaurants': 12.0,
     'maintenance': 3.0,
     'administration': 1.5,
     'transportation': 4.0
 }

 total_jobs = 0
 for sector, ratio in jobs_per_million.items():
     sector_assets = ptf_assets[sector] / 1_000_000
     automation_adjustment = 1 - automation_level[sector]
     total_jobs += sector_assets * ratio * automation_adjustment

 # Quality job multiplier (these are good jobs)
 quality_premium = 1.3

 return total_jobs * quality_premium
''', None)

block('InflationModel (section 5, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 5',
'''
class InflationModel:
 def simulate_with_ptf(self, years=10):
   results = []
   for year in range(years):
     if year < 2:
         # Initial adjustment period
         inflation = 3.5 + random.normal(0, 0.5)
     elif year < 5:
         # Stabilization period
         inflation = 2.5 + random.normal(0, 0.3)
     else:
         # Mature period with PTF anchoring
         inflation = 2.0 + random.normal(0, 0.2)

     # PTF dampening effect
     ptf_dampening = 0.3 * (inflation - 2.0)
     inflation -= ptf_dampening

     results.append(max(0, inflation))

   return results
''', 'InflationModel().simulate_with_ptf(10)')

block('SystemStability (section 7.1, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 7.1',
'''
class SystemStability:
 def calculate_risk_metrics(self):
     return {
         'diversification_index': 0.85, # Multiple wealth channels
         'correlation_risk': 0.25,    # Low correlation between CCO and PTF
         'cascade_probability': 0.05, # Low systemic failure risk
         'recovery_time': 6,         # Months to recover from shock
         'stress_test_pass_rate': 0.92 # 92% of scenarios stable
     }
''', 'SystemStability().calculate_risk_metrics()')

block('carbon_reduction_ptf (section 9.1, PDF)',
      'papers/pdfs/economic-modeling-simulation.pdf section 9.1',
'''
def carbon_reduction_ptf():
 reductions = {
     'concentrated_housing': 0.25,     # 25% reduction
     'shared_transportation': 0.30, # 30% reduction
     'local_food_systems': 0.20,      # 20% reduction
     'efficient_buildings': 0.35,   # 35% reduction
     'circular_economy': 0.15       # 15% reduction
 }

 weighted_reduction = sum(reductions.values()) / len(reductions)
 return weighted_reduction * 0.8 # 80% implementation rate
''', 'carbon_reduction_ptf()')

block('CCOSimulation (Appendix B, PDF)',
      'papers/pdfs/dual-currency-inflation.pdf Appendix B',
'''
class CCOSimulation:
 def __init__(self, params):
   self.B0 = params['basic_unit_amount'] # $1,200
   self.population = params['population']
   self.industries = params['industries']
   self.octave_caps = params['octave_caps']
   self.conversion_rates = range(1, 10) # 1x to 9x
   self.phi = 1.618 # Golden ratio enhancement

 def run_simulation(self, periods):
   for t in range(periods):
     self.distribute_basic_units()
     self.process_conversions()
     self.update_prices()
     self.calculate_inflation()

 def calculate_conversion(self, octave, multiplier, has_beauty):
   base = self.B0 * (2 ** octave)
   rate = multiplier
   if has_beauty:
     rate *= self.phi
   return min(base * rate, self.industry_cap)

 def calculate_inflation(self):
   P_E = self.essential_prices
   P_N = self.nonessential_prices
   weights = self.consumption_weights
   return weighted_average(P_E, P_N, weights)
''', "CCOSimulation({'basic_unit_amount': 1200, 'population': 500, 'industries': [], 'octave_caps': []}).run_simulation(20)")


def run(code, call, env):
    try:
        exec(code, env)
    except Exception as e:
        return 'definition fails: %s: %s' % (type(e).__name__, e)
    if call is None:
        return 'defines only; the paper states no inputs to call it with'
    try:
        out = eval(call, env)
        if isinstance(out, list):
            out = [round(float(x), 3) for x in out]
        elif isinstance(out, dict):
            out = {k: (round(v, 3) if isinstance(v, float) else v) for k, v in out.items()}
        elif isinstance(out, float):
            out = round(out, 4)
        return 'runs: %s -> %r' % (call, out)
    except Exception as e:
        return 'call fails: %s -> %s: %s' % (call, type(e).__name__, e)


def main():
    import random as _random
    import numpy as _np
    lines = []
    for name, source, code, call in BLOCKS:
        lines.append('## ' + name)
        lines.append('source: ' + source)
        lines.append('A (as printed): ' + run(code, call, {}))
        _random.seed(1); _np.random.seed(1)
        lines.append('B (imports supplied): ' + run(code, call, {'random': _random, 'np': _np}))
        if 'random.normal' in code:
            _np.random.seed(1)
            lines.append('C (random = numpy.random, the only reading under which random.normal exists): '
                         + run(code, call, {'random': _np.random, 'np': _np}))
        lines.append('')
    # The printed Gini recurrence (PDF section 6.1) against the projections printed beside it.
    g0, rho = 0.48, 0.03 + 0.02 + 0.01
    printed = {5: 0.38, 10: 0.31, 20: 0.25, 30: 0.22}
    lines.append('## Gini(t) = Gini0 x (1 - rho_CCO - rho_PTF - rho_synergy)^t (section 6.1, PDF)')
    for t, p in printed.items():
        lines.append('year %d: formula %.3f, printed %.2f' % (t, g0 * (1 - rho) ** t, p))
    # The inflation block's expected path (noise has mean zero), against "peak 3.5%, long-term average 2.1%".
    base = [3.5] * 2 + [2.5] * 3 + [2.0] * 5
    exp = [b - 0.3 * (b - 2.0) for b in base]
    lines.append('')
    lines.append('## InflationModel expected path (noise mean zero)')
    lines.append('expected by year: %s; peak %.2f; 10-year mean %.3f; printed: peak 3.5, long-term average 2.1'
                 % ([round(x, 2) for x in exp], max(exp), sum(exp) / len(exp)))
    text = '\n'.join(lines)
    print(text)
    with open(os.path.join(os.path.dirname(__file__), 'printed_code.out'), 'w') as f:
        f.write(text + '\n')


if __name__ == '__main__':
    main()
