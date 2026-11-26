#!/bin/bash
# tables.sh STUDY VARIANT: the study's own table tool on the rerun outputs, into t/STUDY-VARIANT/
S=/tmp/claude-0/-home-user-research-update/73349efb-8994-5214-9196-6ab48dcc8f11/scratchpad/s103; st=$1; V=$2; D=$S/t/$st-$V; rm -rf $D; mkdir -p $D; O=$S/out
declare -A EN=([s58]=74ca1a8 [s67]=985f0c3 [s60]=69f69f5 [s62]=3500d0b [s72]=df9cfbe [s73]=d12fd0f); SHA=$(git -C /home/user/compassionism-simulation rev-parse ${EN[$st]})
for f in $O/$st*-$V.json $O/$st*-$V.d/*.json; do [ -f "$f" ] && python3 $S/tools/setcommit.py $SHA "$f"; done
case $st in
 s58) for e in ref adv st; do ln -s $O/s58-$e-$V.json $D/s58-price-$e.json; done; python3 $S/eng/74ca1a8/dev/tools/s58_table.py $D ;;
 s67) for e in ref adv st; do ln -s $O/s67-$e-$V.json $D/s67-price-$e.json; done; python3 $S/eng/985f0c3/dev/tools/s67_table.py $D $S/t/s58-$V ;;
 s60) for e in ref adv st; do ln -s $O/s60-$e-$V.json $D/s60-bargain-$e.json; done; ln -s $O/s60v-ref-$V.json $D/s60-validate-ref.json; python3 $S/eng/69f69f5/dev/tools/s60_table.py $D $D/tables.md ;;
 s62) for e in ref adv st; do ln -s $O/s62-$e-$V.json $D/s62-ptf-ops-$e.json; done; python3 $S/eng/3500d0b/dev/tools/s62_table.py $D $D/tables.md ;;
 s72) for e in ref adv st; do cp $O/s72p-$e-$V.d/*.json $O/s72f-$e-$V.d/*.json $O/s72fn-$e-$V.d/*.json $D/ 2>/dev/null; done; (cd $S/eng/df9cfbe && node dev/tools/s72_table.js $D) ;;
 s73) for e in ref adv st; do cp $O/s73-$e-$V.d/*.json $D/; done; (cd $S/eng/d12fd0f && node dev/tools/s73_table.js $D) ;;
esac
ls $D
