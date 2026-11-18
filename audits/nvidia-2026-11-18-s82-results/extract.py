#!/usr/bin/env python3
"""Extract the reply (answer and reasoning) word for word from the streamed response nemotron/stream.txt."""
import json, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nemotron')
c, r, fin = [], [], None
for ln in open(os.path.join(H, 'stream.txt'), encoding='utf-8'):
    ln = ln.strip()
    if not ln.startswith('data: ') or ln == 'data: [DONE]':
        continue
    ch = json.loads(ln[6:])['choices']
    if not ch:
        continue
    d = ch[0].get('delta', {})
    c.append(d.get('content') or ''); r.append(d.get('reasoning_content') or '')
    fin = ch[0].get('finish_reason') or fin
open(os.path.join(H, 'reply_content.md'), 'w', encoding='utf-8').write(''.join(c))
open(os.path.join(H, 'reply_reasoning.md'), 'w', encoding='utf-8').write(''.join(r))
print('finish_reason %s; answer %d characters; reasoning %d characters' % (fin, len(''.join(c)), len(''.join(r))))
