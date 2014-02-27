#!/bin/bash
#align.sh
#Weston Feely
#12/5/13

#Check for required arg1
if [ -z "$1" ]; then
	echo "Usage: ./align.sh parallelCorpus.txt"
	exit 1
fi

mkdir -p tmp

~/github/cdec/word-aligner/fast_align -d -v -o -i $1 > tmp/fwd_align.txt
~/github/cdec/word-aligner/fast_align -r -d -v -o -i $1 > tmp/rev_align.txt
~/github/cdec/utils/atools -i tmp/fwd_align.txt -j tmp/rev_align.txt -c grow-diag-final-and > align.txt
