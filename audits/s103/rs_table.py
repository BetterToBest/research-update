"""rs_table.py FILES: the recession-slack reading's effect on its own path: counted minus not counted, paired by seed, mean and largest |difference|,
at the nesting point (k 1, r a h 0) and at the capacity rule's main values; with the nesting point against today's rule for reference."""
import json, sys, math
K = ['endoAnn', 'pLev20', 'pov', 'fgt0PY', 'medWealthReal', 'hhCostPY', 'prSlk']
for f in sys.argv[1:]:
    d = json.load(open(f)); R = d['rows']; m = d['_meta']; print('==', f.split('/')[-1], 'seeds', m['seeds'])
    for a, b, lab in [('nest-rs1', 'nest-rs0', 'nesting point: slack counted - not'), ('cap-rs1', 'cap-rs0', 'main values: slack counted - not'), ('nest-rs0', 'c22', 'nesting point (not counted) - today\'s rule')]:
        out = []
        for k in K:
            if k not in R[a] or k not in R[b]: continue
            x, y = R[a][k], R[b][k]; dd = [u - v for u, v in zip(x, y)]; n = len(dd)
            mean = sum(dd)/n; mx = max(abs(z) for z in dd); nz = sum(1 for z in dd if z != 0)
            rel = max(abs(u - v)/max(1e-300, abs(v)) for u, v in zip(x, y)) if k in ('pLev20',) else None
            out.append('%s mean %.3g max|d| %.3g (%d seeds differ)%s' % (k, mean, mx, nz, '' if rel is None else ', max rel %.2e' % rel))
        print('  ' + lab + ':\n    ' + '\n    '.join(out))
    s = R['cap-rs1'].get('prSlk')
    if s: print('  recession idle share (prSlk), main values: mean %.4f, seeds with any > 0: %d' % (sum(s)/len(s), sum(1 for z in s if z > 0)))
