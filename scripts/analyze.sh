#!/bin/bash
#Script to run foma analyzer on Egyptian Arabic

foma -l egy.foma

#Preprocess data
#./oneperline.py data/egy/egytrain.egy data/egy/egytrain.egy.one
#./oneperline.py data/egy/egydev.egy data/egy/egydev.egy.one
#./oneperline.py data/egy/egytest.egy data/egy/egytest.egy.one
#./oneperline.py data/lev/levtrain.lev data/lev/levtrain.lev.one
#./oneperline.py data/lev/levdev.lev data/lev/levdev.lev.one
#./oneperline.py data/lev/levtest.lev data/lev/levtest.lev.one
./oneperline.py data/egylev/egylevtrain.egylev data/egylev/egylevtrain.egylev.one
./oneperline.py data/egylev/egylevdev.egylev data/egylev/egylevdev.egylev.one
./oneperline.py data/egylev/egylevtest.egylev data/egylev/egylevtest.egylev.one

#Run foma
#cat data/egy/egytrain.egy.one | flookup -x egy.bin > temp.egytrain
#cat data/egy/egydev.egy.one | flookup -x egy.bin > temp.egydev
#cat data/egy/egytest.egy.one | flookup -x egy.bin > temp.egytest
#cat data/lev/levtrain.lev.one | flookup -x egy.bin > temp.levtrain
#cat data/lev/levdev.lev.one | flookup -x egy.bin > temp.levdev
#cat data/lev/levtest.lev.one | flookup -x egy.bin > temp.levtest
cat data/egylev/egylevtrain.egylev.one | flookup -x egyan.bin > temp.egylevtrainan
cat data/egylev/egylevdev.egylev.one | flookup -x egyan.bin > temp.egylevdevan
cat data/egylev/egylevtest.egylev.one | flookup -x egyan.bin > temp.egylevtestan

#Run postprocessor
javac PostProcess.java
#java PostProcess data/egy/egytrain.egy.one temp.egytrain data/egy/egytrain.egy.mish
#java PostProcess data/egy/egydev.egy.one temp.egydev data/egy/egydev.egy.mish
#java PostProcess data/egy/egytest.egy.one temp.egytest data/egy/egytest.egy.mish
#java PostProcess data/lev/levtrain.lev.one temp.levtrain data/lev/levtrain.lev.mish
#java PostProcess data/lev/levdev.lev.one temp.levdev data/lev/levdev.lev.mish
#java PostProcess data/lev/levtest.lev.one temp.levtest data/lev/levtest.lev.mish
java PostProcess data/egylev/egylevtrain.egylev.one temp.egylevtrainan data/egylev/egylevantrain.egylevan
java PostProcess data/egylev/egylevdev.egylev.one temp.egylevdevan data/egylev/egylevandev.egylevan
java PostProcess data/egylev/egylevtest.egylev.one temp.egylevtestan data/egylev/egylevantest.egylevan

#Cleanup
#rm temp.*
