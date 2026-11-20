"""Send a packet to an outside model and save the reply word for word (S94, Nov 20, 2026).
  python3 -I ask.py nvidia|openrouter <model id> <packet file> <tag> [max_tokens]
NVIDIA: integrate.api.nvidia.com (key added by the proxy), streamed. OpenRouter: openrouter.ai, ids ending ':free' only (the money rule).
Writes <tag>/request.json, <tag>/stream.txt or reply.json, <tag>/reply_content.md, <tag>/reply_reasoning.md, <tag>/status.txt."""
import json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); prov, model, packet, tag = sys.argv[1:5]; mt = int(sys.argv[5]) if len(sys.argv) > 5 else 40000
if prov == 'openrouter': assert model.endswith(':free'), 'only :free ids (the money rule)'
url = {'nvidia': 'https://integrate.api.nvidia.com/v1/chat/completions', 'openrouter': 'https://openrouter.ai/api/v1/chat/completions'}[prov]
d = os.path.join(HERE, tag); os.makedirs(d, exist_ok=True)
stream = prov == 'nvidia'
req = {'model': model, 'messages': [{'role': 'user', 'content': open(os.path.join(HERE, packet)).read()}], 'max_tokens': mt, 'temperature': 0.3, 'stream': stream}
json.dump(req, open(os.path.join(d, 'request.json'), 'w'))
log, content, reasoning = [], '', ''
for attempt in range(1, 4):
    out = os.path.join(d, 'stream.txt' if stream else 'reply.json')
    r = subprocess.run(['curl', '-sS', '-N', '-m', '2400', url, '-H', 'Content-Type: application/json', '-d', '@' + os.path.join(d, 'request.json'), '-o', out, '-w', '%{http_code}'],
                       capture_output=True, text=True)
    log.append('attempt %d: http %s %s' % (attempt, r.stdout.strip(), r.stderr.strip()[:200]))
    if stream:
        fin = None
        for line in open(out, errors='ignore'):
            if not line.startswith('data: ') or line.strip() == 'data: [DONE]': continue
            try: ch = json.loads(line[6:])['choices'][0]
            except Exception: continue
            dl = ch.get('delta', {}); content += dl.get('content') or ''; reasoning += dl.get('reasoning_content') or dl.get('reasoning') or ''; fin = ch.get('finish_reason') or fin
        log.append('finish_reason %s' % fin)
        if content: break
    else:
        try: R = json.load(open(out))
        except Exception as e: R = {}; log.append('unreadable: %s' % e)
        if 'choices' in R:
            m = R['choices'][0]['message']; content = m.get('content') or ''; reasoning = m.get('reasoning') or ''
            log.append('finish_reason %s; usage %s; served by %s' % (R['choices'][0].get('finish_reason'), json.dumps(R.get('usage'))[:300], R.get('model'))); break
        log.append('error: ' + json.dumps(R.get('error', R))[:400])
    time.sleep(60)
open(os.path.join(d, 'reply_content.md'), 'w').write(content); open(os.path.join(d, 'reply_reasoning.md'), 'w').write(reasoning)
log.append('content characters %d; reasoning characters %d' % (len(content), len(reasoning)))
open(os.path.join(d, 'status.txt'), 'w').write('\n'.join(log) + '\n')
