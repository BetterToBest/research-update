#!/bin/bash
S=/tmp/claude-0/-home-user-research-update/73349efb-8994-5214-9196-6ab48dcc8f11/scratchpad/s103; C=$1; D=$S/bis/$C
[ -d $D ] || { mkdir -p $D; (cd /home/user/compassionism-simulation && git archive $C index.html harness.js package.json data | tar -x -C $D); }
echo "$C $(timeout 600 node $S/tools/rs39.js $D 2>&1 | tail -1)"
