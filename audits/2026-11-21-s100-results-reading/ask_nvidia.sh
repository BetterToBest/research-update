#!/bin/bash
# usage: ask_nvidia.sh <reader>   (posts packet-<reader>-nvidia.json to NVIDIA's API catalogue; the proxy adds the key; reply saved as reply-<reader>-nvidia.json)
cd "$(dirname "$0")"
curl -sS --max-time 3000 https://integrate.api.nvidia.com/v1/chat/completions -H 'Content-Type: application/json' -H 'Authorization: Bearer dummy' \
  --data-binary @packet-$1-nvidia.json -o reply-$1-nvidia.json -w "HTTP %{http_code} in %{time_total}s\n"
python3 -c "import json,sys; d=json.load(open('reply-$1-nvidia.json')); c=d['choices'][0]; open('reply-$1-nvidia.md','w').write(c['message'].get('content') or ''); print(c.get('finish_reason'), len(c['message'].get('content') or ''), d.get('usage'))" 2>&1
