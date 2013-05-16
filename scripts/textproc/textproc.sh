#!/bin/bash
#textproc.sh
#Weston Feely
#4/8/13

#Check for required arg
if [[ -z "$1" ]]; then
    echo "Usage: ./textproc.sh language_prefix"
    exit 1
fi
lang=$1

#Do text processing on raw data, tokenize Arabic text
#./preprocess.py ../data/egy/egyptian_data.txt ../data/egy/egycorpus.egy ../data/egy/egycorpus.en
#./preprocess.py ../data/lev/levantine_data.txt ../data/lev/levcorpus.lev ../data/lev/levcorpus.en

#Tokenize English text
#~/github/mosesdecoder/scripts/tokenizer/tokenizer.perl -l en < ~/github/sp2013.11-731/project/data/${lang}/${lang}corpus.en > ~/github/sp2013.11-731/project/data/${lang}/${lang}corpus.en.tok

#Fix English tokenization issues
#./fix_en_tok.py ../data/${lang}/${lang}corpus.en.tok ../data/${lang}/${lang}corpus.en

#Randomly split data into training, dev, and test sets
./split_data.py ../data/${lang}/${lang}corpus.${lang} ../data/${lang}/${lang}corpus.en ${lang}
