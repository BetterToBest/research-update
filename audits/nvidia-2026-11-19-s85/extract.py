"""Extract the streamed reply into reply_content.md and reply_reasoning.md (S85 prereg reading)."""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); c, r, fin = [], [], None
for line in open(os.path.join(H, 'nemotron', 'stream.txt')):
    line = line.strip()
    if not line.startswith('data: ') or line == 'data: [DONE]': continue
    d = json.loads(line[6:])
    for ch in d.get('choices', []):
        dl = ch.get('delta', {}); c.append(dl.get('content') or ''); r.append(dl.get('reasoning_content') or ''); fin = ch.get('finish_reason') or fin
open(os.path.join(H, 'nemotron', 'reply_content.md'), 'w').write(''.join(c)); open(os.path.join(H, 'nemotron', 'reply_reasoning.md'), 'w').write(''.join(r))
print('finish_reason', fin, 'content', len(''.join(c)), 'reasoning', len(''.join(r)))
