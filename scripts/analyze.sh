#!/bin/bash
#Script to run foma analyzer on Egyptian Arabic
#location: /scripts/

data="../data"
suf="lte"

#Convert Lev to Egy
./levtoegy.sh $data/egy/egytrain.egy
./levtoegy.sh $data/egy/egydev.egy
./levtoegy.sh $data/egy/egytest.egy
./levtoegy.sh $data/lev/levtrain.egy
./levtoegy.sh $data/lev/levdev.egy
./levtoegy.sh $data/lev/levtest.egy
./levtoegy.sh $data/egylev/egylevtrain.egy
./levtoegy.sh $data/egylev/egylevdev.egy
./levtoegy.sh $data/egylev/egylevtest.egy

#Preprocess data
./oneperline.py $data/egy/egytrain.egy.$suf $data/egy/egytrain.egy.one
./oneperline.py $data/egy/egydev.egy.$suf $data/egy/egydev.egy.one
./oneperline.py $data/egy/egytest.egy.$suf $data/egy/egytest.egy.one
./oneperline.py $data/lev/levtrain.lev.$suf $data/lev/levtrain.lev.one
./oneperline.py $data/lev/levdev.lev.$suf $data/lev/levdev.lev.one
./oneperline.py $data/lev/levtest.lev.$suf $data/lev/levtest.lev.one
./oneperline.py $data/egylev/egylevtrain.egylev.$suf $data/egylev/egylevtrain.egylev.one
./oneperline.py $data/egylev/egylevdev.egylev.$suf $data/egylev/egylevdev.egylev.one
./oneperline.py $data/egylev/egylevtest.egylev.$suf $data/egylev/egylevtest.egylev.one

#Run foma
cd ../src/
foma -l egy.foma
cat $data/egy/egytrain.egy.one | flookup -x egy.bin > temp.egytrain
cat $data/egy/egydev.egy.one | flookup -x egy.bin > temp.egydev
cat $data/egy/egytest.egy.one | flookup -x egy.bin > temp.egytest
cat $data/lev/levtrain.lev.one | flookup -x egy.bin > temp.levtrain
cat $data/lev/levdev.lev.one | flookup -x egy.bin > temp.levdev
cat $data/lev/levtest.lev.one | flookup -x egy.bin > temp.levtest
cat $data/egylev/egylevtrain.egylev.one | flookup -x egyan.bin > temp.egylevtrainan
cat $data/egylev/egylevdev.egylev.one | flookup -x egyan.bin > temp.egylevdevan
cat $data/egylev/egylevtest.egylev.one | flookup -x egyan.bin > temp.egylevtestan

#Run postprocessor
javac PostProcess.java
java PostProcess $data/egy/egytrain.egy.one temp.egytrain $data/egy/egytrain.egy.mish
java PostProcess $data/egy/egydev.egy.one temp.egydev $data/egy/egydev.egy.mish
java PostProcess $data/egy/egytest.egy.one temp.egytest $data/egy/egytest.egy.mish
java PostProcess $data/lev/levtrain.lev.one temp.levtrain $data/lev/levtrain.lev.mish
java PostProcess $data/lev/levdev.lev.one temp.levdev $data/lev/levdev.lev.mish
java PostProcess $data/lev/levtest.lev.one temp.levtest $data/lev/levtest.lev.mish
java PostProcess $data/egylev/egylevtrain.egylev.one temp.egylevtrainan $data/egylev/egylevantrain.egylevan
java PostProcess $data/egylev/egylevdev.egylev.one temp.egylevdevan $data/egylev/egylevandev.egylevan
java PostProcess $data/egylev/egylevtest.egylev.one temp.egylevtestan $data/egylev/egylevantest.egylevan

#Cleanup
rm temp.*
cd ..
rm data/egy/*.one
rm data/lev/*.one
rm data/egylev/*.one

rm data/egy/*.$suf
rm data/lev/*.$suf
rm data/egylev/*.$suf

