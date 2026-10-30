"""S31: first appearance of each S30 figure in a claude.ai conversations.json export.
usage: python3 -I provenance_scan.py conversations.json out.json
Writes only counts, dates, sender, tool kind and conversation id prefix. No chat text."""
import json, re, sys, collections
conv = json.load(open(sys.argv[1]))
N = r'[\s\S]{0,100}'
FIG = {
 '85% poverty reduction': r'85\s*%'+N+r'(poverty|reduc)|(poverty|reduc)'+N+r'85\s*%',
 '98% poverty reduction/elimination': r'98\s*%'+N+r'(poverty|elimin|reduc)|(poverty|elimin|reduc)'+N+r'98\s*%',
 '$37,000 median wealth': r'\$\s?37,?(000|k)\b|\b37,000\b',
 '$82,000 median wealth': r'\$\s?82,?(000|k)\b|\b82,000\b',
 'interval $64,000-$103,000': r'64,?000'+N+r'103,?000|\$64k'+N+r'\$103k',
 '65% lower inflation': r'65\s*%'+N+r'inflation|inflation'+N+r'65\s*%',
 '10,000 iterations': r'10,?000\+?\s*(monte|iteration|simulation|run)',
 'elasticity -0.71': r'[-−–]\s?0\.71\b',
 'Gini 0.28': r'gini'+N+r'0\.28\b|0\.28\b'+N+r'gini',
 '30% participation': r'30\s*%'+N+r'particip|particip'+N+r'30\s*%',
 '55% participation': r'55\s*%'+N+r'particip|particip'+N+r'55\s*%',
 '75% participation': r'75\s*%'+N+r'particip|particip'+N+r'75\s*%',
 'theta 0.15-0.25': r'(theta|θ)'+N+r'0\.15'+N+r'0\.25|0\.15\s*[-–]\s*0\.25',
 '94% stability': r'94\s*%'+N+r'stabil|stabil'+N+r'94\s*%',
 '92% scenarios stable': r'92\s*%'+N+r'(scenario|stable|stress)|(scenario|stable|stress)'+N+r'92\s*%',
 '88% work participation': r'88\s*%'+N+r'(work|particip|employ)|(work|particip|employ)'+N+r'88\s*%',
 '45% carbon reduction': r'45\s*%'+N+r'carbon|carbon'+N+r'45\s*%',
 'cco-ptf-simulation package': r'cco[-_]ptf[-_]simulation',
}
FIG = {k: re.compile(v, re.I) for k, v in FIG.items()}
def blocks(m):
    names = {}
    for b in m['content']:
        if b['type'] == 'tool_use': names[b.get('id')] = b.get('name')
    for b in m['content']:
        t = b['type']
        if t == 'text': yield 'text', b.get('text') or ''
        elif t == 'tool_use':
            yield 'in:' + str(b.get('name')), json.dumps(b.get('input'), ensure_ascii=False)
        elif t == 'tool_result':
            yield 'out:' + str(b.get('name') or names.get(b.get('tool_use_id'))), json.dumps(b.get('content'), ensure_ascii=False)
res = {}
for f, rx in FIG.items():
    hits = []
    for c in conv:
        used = {}
        for m in sorted(c['chat_messages'], key=lambda m: m['created_at']):
            for kind, txt in blocks(m):
                if kind.startswith('in:bash_tool'): used.setdefault('bash_before', m['created_at'])
                if rx.search(txt):
                    hits.append(dict(conv=c['uuid'][:8], when=m['created_at'], sender=m['sender'], kind=kind,
                                     bash_in_conv_before=('bash_before' in used and used['bash_before'] <= m['created_at'])))
    hits.sort(key=lambda h: h['when'])
    res[f] = dict(n=len(hits), convs=len({h['conv'] for h in hits}),
                  first=hits[0] if hits else None,
                  first_user=next((h for h in hits if h['sender'] == 'human'), None),
                  first_assistant=next((h for h in hits if h['sender'] == 'assistant'), None),
                  in_bash_output=[h for h in hits if h['kind'] == 'out:bash_tool'][:3],
                  in_source_output=[h for h in hits if h['kind'].split(':')[0] == 'out' and h['kind'] in
                                    ('out:web_fetch','out:web_search','out:project_knowledge_search')][:3],
                  n_bash_in_conv_before=sum(h['bash_in_conv_before'] for h in hits))
json.dump(res, open(sys.argv[2], 'w'), indent=1)
