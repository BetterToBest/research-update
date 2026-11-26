"""pair.py A.json B.json: per row, how many per-seed values differ between two runs of the same job, and the largest relative difference."""
import json, sys
def rows(f):
    d = json.load(open(f)); return d['rows'] if 'rows' in d else d
a, b = rows(sys.argv[1]), rows(sys.argv[2]); tot = 0
for r in a:
    nd = n = 0; mx = 0; mk = None
    for k, v in a[r].items():
        if not isinstance(v, list): continue
        for x, y in zip(v, b[r][k]):
            n += 1
            if x != y and not (x != x and y != y):
                nd += 1; d = abs(x - y)/max(1e-12, abs(x))
                if d > mx: mx, mk = d, k
    tot += nd; print('%-12s values %6d differ %6d max rel %.2e %s' % (r, n, nd, mx, mk or ''))
print('total differing', tot)
