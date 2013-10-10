#!/bin/bash
# sjeblee@cs.cmu.edu
# Run MADA

data="/home/serena/github/EMA/data/7515"
cd $data
mkdir -p mada
cd ~/MADA-3.2/

echo "running MADA..."

echo "train"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/artrain.ar outputdir=output &> mada_log_artrain.txt

cp output/artrain.ar.bw.mada.tok $data/mada/artrain.ar

echo "dev"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/ardev.ar outputdir=output &> mada_log_ardev.txt

cp output/ardev.ar.bw.mada.tok $data/mada/ardev.ar

echo "artest"
perl MADA+TOKAN.pl config=config-files/template.madaconfig file=$data/artest.ar outputdir=output &> mada_log_artest.txt

cp output/artest.ar.bw.mada.tok $data/mada/artest.ar

echo "Cleaning up..."
#cd $data
#mkdir -p mada

#cd /home/serena/github/EMA/src
#javac ConvertMADA.java

#java ConvertMADA $data/artrain.ar.bw.mada.tok $data/artrain.ar $data/mada/artrain.ar
#java ConvertMADA $data/ardev.ar.bw.mada.tok $data/ardev.ar $data/mada/ardev.ar
#java ConvertMADA $data/artest.ar.bw.mada.tok $data/artest.ar $data/mada/artest.ar
cd $data
#rm *.mada.tok
cp artest.en mada/
cp ardev.en mada/
cp artrain.en mada/

echo "done."









