#!/bin/bash
# Convert Levantine to be more like Egyptian
# sjeblee@cs.cmu.edu
# Last Modified: 8 May 2013

#TODO
#to be able to: fii
# Em verb -> verb
# shw verb -> verb Ayh
# Aysh verb -> verb Ayh
# rH verb -> H verb
# mA verb -> mA-verb-sh

#word reordering:
# AmtY verb -> verb AmtY
# mA verb -> mA-verb-sh : including fy and End
# HAda, HAdi -> dA, dy, etc : see pg 17 M.Omar
# HA + noun -> noun dA/dy

file="data/egylev/egylevtrain.egylev"

sed 's/ معي / معيا /g' $file | \
sed 's/ وين / فين /g' $file | \
sed 's/ ليش / ليه /g' $file | \
sed 's/شلون/ إزي/g' $file | \
sed 's/ كيف / إزي /g' $file | \
#sed 's/ كيفك / إزيك /g' $file | \
sed 's/ قديش / بكام /g' $file | \
sed 's/ هلق / دلوقتي /g' $file | \
sed 's/ منيح / كويس /g' $file | \
#sed 's/رح [a-z] / ح /g' $file | \ 
sed 's/ مبارح / امبارح /g' $file > data/egylevtrans/egylevtranstrain.egylevtrans

file="data/egylev/egylevdev.egylev"

sed 's/ معي / معيا /g' $file | \
sed 's/ وين / فين /g' $file | \
sed 's/ ليش / ليه /g' $file | \
sed 's/شلون/ إزي/g' $file | \
sed 's/ كيف / إزي /g' $file | \
#sed 's/ كيفك / إزيك /g' $file | \
sed 's/ قديش / بكام /g' $file | \
sed 's/ هلق / دلوقتي /g' $file | \
sed 's/ منيح / كويس /g' $file | \
#sed 's/رح [a-z] / ح /g' $file | \ 
sed 's/ مبارح / امبارح /g' $file > data/egylevtrans/egylevtransdev.egylevtrans

file="data/egylev/egylevtest.egylev"

sed 's/ معي / معيا /g' $file | \
sed 's/ وين / فين /g' $file | \
sed 's/ ليش / ليه /g' $file | \
sed 's/شلون/ إزي/g' $file | \
sed 's/ كيف / إزي /g' $file | \
#sed 's/ كيفك / إزيك /g' $file | \
sed 's/ قديش / بكام /g' $file | \
sed 's/ هلق / دلوقتي /g' $file | \
sed 's/ منيح / كويس /g' $file | \
#sed 's/رح [a-z] / ح /g' $file | \ 
sed 's/ مبارح / امبارح /g' $file > data/egylevtrans/egylevtranstest.egylevtrans



