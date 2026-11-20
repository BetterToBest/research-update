"""Send packet.md to an OpenRouter free model and save the reply word for word.
  python3 -I ask.py <model id ending :free> <tag> [max_tokens]
Writes <tag>/request.json, <tag>/reply.json (raw), <tag>/reply_content.md, <tag>/reply_reasoning.md, <tag>/status.txt. Only ids ending ':free' are sent."""
import json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); model, tag = sys.argv[1], sys.argv[2]; mt = int(sys.argv[3]) if len(sys.argv) > 3 else 30000
assert model.endswith(':free'), 'only :free ids (the money rule)'
d = os.path.join(HERE, tag); os.makedirs(d, exist_ok=True)
req = {'model': model, 'messages': [{'role': 'user', 'content': open(os.path.join(HERE, 'packet.md')).read()}], 'max_tokens': mt, 'temperature': 0.3}
json.dump(req, open(os.path.join(d, 'request.json'), 'w'))
log = []
for attempt in range(1, 5):
    r = subprocess.run(['curl', '-sS', '-m', '1500', 'https://openrouter.ai/api/v1/chat/completions', '-H', 'Content-Type: application/json', '-d', '@' + os.path.join(d, 'request.json'),
                        '-o', os.path.join(d, 'reply.json'), '-w', '%{http_code}'], capture_output=True, text=True)
    code = r.stdout.strip(); log.append('attempt %d: http %s %s' % (attempt, code, r.stderr.strip()[:200]))
    try: R = json.load(open(os.path.join(d, 'reply.json')))
    except Exception as e: R = {}; log.append('unreadable reply: %s' % e)
    if 'choices' in R: break
    log.append('error: ' + json.dumps(R.get('error', R))[:400]); time.sleep(90)
if 'choices' in R:
    ch = R['choices'][0]; m = ch['message']
    open(os.path.join(d, 'reply_content.md'), 'w').write(m.get('content') or ''); open(os.path.join(d, 'reply_reasoning.md'), 'w').write(m.get('reasoning') or '')
    log.append('finish_reason %s; usage %s; served by %s' % (ch.get('finish_reason'), json.dumps(R.get('usage'))[:300], R.get('model')))
    log.append('content characters %d; reasoning characters %d' % (len(m.get('content') or ''), len(m.get('reasoning') or '')))
open(os.path.join(d, 'status.txt'), 'w').write('\n'.join(log) + '\n')
