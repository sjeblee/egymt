#!/bin/bash
#makelm.sh
#Weston Feely
#2/27/14

#Check for required arg1
if [ -z "$1" ]; then
	echo "Usage: ./makelm.sh data.txt"
	exit 1
fi

order="5"
tmp="./tmp"
percent="10%"
data=$1
arpafile="./lm.arpa"
lm_quant_flags="-q 8 -b 8 -a 22"
binfile="./lm.bin"

mkdir -p $tmp

~/github/mosesdecoder/bin/lmplz -o $order -T $tmp -S $percent < $data > $arpafile
~/github/mosesdecoder/bin/build_binary $lm_quant_flags trie $arpafile $binfile