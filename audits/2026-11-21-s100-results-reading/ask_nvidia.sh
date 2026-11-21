#!/bin/bash
# usage: ask_nvidia.sh <reader>   (streams packet-<reader>-nvidia.json from NVIDIA's API catalogue; the proxy adds the key;
# the raw stream is saved as reply-<reader>-nvidia.sse and the answer as reply-<reader>-nvidia.md)
cd "$(dirname "$0")"
curl -sS -N --max-time 3000 https://integrate.api.nvidia.com/v1/chat/completions -H 'Content-Type: application/json' -H 'Authorization: Bearer dummy' \
  --data-binary @packet-$1-nvidia.json -o reply-$1-nvidia.sse -w "HTTP %{http_code} in %{time_total}s\n"
python3 - "$1" <<'PY'
import json, sys
n = sys.argv[1]; out, fin = [], None
for line in open('reply-%s-nvidia.sse' % n):
    line = line.strip()
    if not line.startswith('data:') or line == 'data: [DONE]': continue
    c = json.loads(line[5:])['choices']
    if c:
        out.append(c[0].get('delta', {}).get('content') or ''); fin = c[0].get('finish_reason') or fin
open('reply-%s-nvidia.md' % n, 'w').write(''.join(out)); print(fin, len(''.join(out)))
PY
