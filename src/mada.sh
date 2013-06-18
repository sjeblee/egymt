#!/bin/bash
# sjeblee@cs.cmu.edu
# Run MADA

data="/home/serena/github/EMA/data"

cd ~/MADA-3.2/

echo "running MADA..."

echo "egytrain"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/egy/egytrain.egy outputdir=output &> mada_log_egytrain.txt

cp output/egytrain.egy.bw.mada.tok $data/egy/

echo "egydev"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/egy/egydev.egy outputdir=output &> mada_log_egydev.txt

cp output/egydev.egy.bw.mada.tok $data/egy/

echo "egytest"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/egy/egytest.egy outputdir=output &> mada_log_egytest.txt

cp output/egytest.egy.bw.mada.tok $data/egy/

echo "levtrain"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/lev/levtrain.lev outputdir=output &> mada_log_levtrain.txt

cp output/levtrain.lev.bw.mada.tok $data/lev/

echo "levdev"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/lev/levdev.lev outputdir=output/split &> mada_log_levdev.txt

cp output/split/levdev.lev.bw.mada.tok $data/lev/

echo "levtest"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/lev/levtest.lev outputdir=output/split &> mada_log_levtest.txt

cp output/split/levtest.lev.bw.mada.tok $data/lev/

echo "egylevtrain"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/egylev/egylevtrain.egylev outputdir=output/split &> mada_log_egylevtrain.txt

cp output/split/egylevtrain.egylev.bw.mada.tok $data/egylev/

echo "egylevdev"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/egylev/egylevdev.egylev outputdir=output &> mada_log_egylevdev.txt

cp output/egylevdev.egylev.bw.mada.tok $data/egylev/

echo "egylevtest"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/egylev/egylevtest.egylev outputdir=output &> mada_log_egylevtest.txt

cp output/egylevtest.egylev.bw.mada.tok $data/egylev/

echo "converting back to Arabic script..."

cd ..
javac ConvertMADA.java

echo "egy"
java ConvertMADA $data/egy/egytrain.egy.bw.mada.tok $data/egy/egytrain.egy
java ConvertMADA $data/egy/egydev.egy.bw.mada.tok $data/egy/egydev.egy
java ConvertMADA $data/egy/egytest.egy.bw.mada.tok $data/egy/egytest.egy

echo "lev"
java ConvertMADA $data/lev/levtrain.lev.bw.mada.tok $data/lev/levtrain.lev
java ConvertMADA $data/lev/levdev.lev.bw.mada.tok $data/lev/levdev.lev
java ConvertMADA $data/lev/levtest.lev.bw.mada.tok $data/lev/levtest.lev

echo "egylev"
java ConvertMADA $data/egylev/egylevtrain.egylev.bw.mada.tok $data/egylev/egylevtrain.egylev
java ConvertMADA $data/egylev/egylevdev.egylev.bw.mada.tok $data/egylev/egylevdev.egylev
java ConvertMADA $data/egylev/egylevtest.egylev.bw.mada.tok $data/egylev/egylevtest.egylev

echo "done."









