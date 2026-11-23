#!/bin/bash
# usage: ask.sh <reader>   (posts packet-<reader>.json to OpenRouter's free tier; the proxy adds the key; reply saved as reply-<reader>.json)
cd "$(dirname "$0")"
curl -sS --max-time 3000 https://openrouter.ai/api/v1/chat/completions -H 'Content-Type: application/json' -H 'Authorization: Bearer dummy' \
  --data-binary @packet-$1.json -o reply-$1.json -w "HTTP %{http_code} in %{time_total}s\n"
python3 -c "import json,sys; d=json.load(open('reply-$1.json')); c=d['choices'][0]; open('reply-$1.md','w').write(c['message'].get('content') or ''); print(c.get('finish_reason'), len(c['message'].get('content') or ''), d.get('usage'))" 2>&1
