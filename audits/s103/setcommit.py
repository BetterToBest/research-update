"""setcommit.py SHA FILE...: the scratch engine is not a git checkout, so runManifest() has no commit; write the engine's commit in (metadata only)."""
import json, sys
sha = sys.argv[1]
for f in sys.argv[2:]:
    d = json.load(open(f)); m = d.get('_meta') or d.get('meta') or d
    def fix(x):
        if isinstance(x, dict):
            if 'manifest' in x and isinstance(x['manifest'], dict) and not x['manifest'].get('commit'): x['manifest']['commit'] = sha
            for v in x.values(): fix(v)
    fix(d); json.dump(d, open(f, 'w'))
