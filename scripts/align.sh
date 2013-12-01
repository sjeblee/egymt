#!/bin/bash
#align.sh
#Weston Feely
#11/30/13

mkdir -p tmp

~/github/cdec/word-aligner/fast_align -d -v -o -i $1 > tmp/fwd_align.txt
~/github/cdec/word-aligner/fast_align -r -d -v -o -i $1 > tmp/rev_align.txt
~/github/cdec/utils/atools -i tmp/fwd_align.txt -j tmp/rev_align.txt -c grow-diag > align.txt