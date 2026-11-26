#!/bin/bash
# mk.sh COMMIT: a scratch copy of the engine at COMMIT, instrumented (patch.py)
set -e; C=$1; D=/tmp/claude-0/-home-user-research-update/73349efb-8994-5214-9196-6ab48dcc8f11/scratchpad/s103/eng/$C
rm -rf $D; mkdir -p $D; cd /home/user/compassionism-simulation
git archive $C index.html harness.js package.json data dev/tools | tar -x -C $D
python3 /tmp/claude-0/-home-user-research-update/73349efb-8994-5214-9196-6ab48dcc8f11/scratchpad/s103/tools/patch.py $D/index.html
echo $D
