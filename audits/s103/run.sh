#!/bin/bash
# run.sh TAG ENGDIR VARIANT(orig|fix) CMD...   (CMD relative to ENGDIR; OUT replaced by the output file)
S=/tmp/claude-0/-home-user-research-update/73349efb-8994-5214-9196-6ab48dcc8f11/scratchpad/s103; T=$1; E=$2; V=$3; shift 3
O=$S/out/$T-$V.json; L=$S/out/$T-$V.log; mkdir -p $S/out/$T-$V.d; C="$@"; C="${C//OUTD/$S/out/$T-$V.d}"; C="${C//OUT/$O}"
cd $S/eng/$E; if [ $V = fix ]; then export S103_FIX=1; else export S103_LOG=$S/out/$T-borrow.jsonl; rm -f $S103_LOG; fi
echo "$(date -u +%FT%TZ) $E $V $C" > $L; node $C >> $L 2>&1; echo "exit $? $(date -u +%FT%TZ)" >> $L
