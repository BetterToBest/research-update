"""S30 inputs: Hub figures claimed as simulation results with no basis (or a simulation basis).

Run from research-update with research-hub beside it:
    python3 audits/early/inputs.py
Writes audits/early/inputs.csv.
"""
import csv, os

HUB = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'research-hub')
rows = list(csv.DictReader(open(os.path.join(HUB, 'data', 'claims.csv'))))
keep = [r for r in rows
        if (r['class'] in ('no basis found', 'simulation') and r['claimed'] == 'simulation result')
        or r['page'].endswith('optimal-parameters.json')]
cols = ['id', 'page', 'section', 'figure', 'class', 'claimed', 'action', 'sentence']
with open(os.path.join(os.path.dirname(__file__), 'inputs.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
    w.writeheader()
    w.writerows(keep)
print(len(keep), 'rows')
