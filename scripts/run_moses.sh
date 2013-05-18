#!/bin/bash
#run_moses.sh
#Weston Feely
#5/17/13
#This script runs Moses, which should be installed in moses_dir, on the data in data_dir/language
#The language data folder is expected to contained files called:
# ${language}train.${language}
# ${language}train.en
# ${language}dev.${language}
# ${language}dev.en
# ${language}test.${language}
# ${language}test.en

#Check for required arg1
if [ -z "$1" ]; then
	echo "Usage: ./run_moses.sh language moses_dir data_dir"
	exit 1
fi

#Setup language and default moses and data paths
lang=$1
moses_dir=`readlink -f ~/github/mosesdecoder`
data_dir=`readlink -f ../data`

#Check for optional arg2 and arg3
if [ ! -z "$2" ]; then
	if [ -d "$2" ]; then
		#Change moses directory to user-specified dir
		moses_dir=`readlink -f $2`
	fi
fi
if [ ! -z "$3" ]; then
	if [ -d "$3" ]; then
		#Change data directory to user-specified dir
		data_dir=`readlink -f $3`
	fi
fi

#Get start time and print current time
T="$(date +%s)"
date

#Set up data filenames
train=${lang}train
#train_fr=${lang}train.${lang} # unnecessary variable, but this file must exist in ${data_dir}/${lang}
train_en=${lang}train.en
dev_fr=${lang}dev.${lang}
dev_en=${lang}dev.en
test=${lang}test
test_fr=${lang}test.${lang}
test_en=${lang}test.en

################TRAINING################
echo "Moses Training phase"
#Make corpus folder for language model
mkdir -p ${moses_dir}/corpus
mkdir -p ${moses_dir}/corpus/${lang}

#Make arpa language model for moses
echo "Creating ngram LM based on English side of training data..."
ngram-count -unk -text ${data_dir}/${lang}/${train_en} -lm ${moses_dir}/corpus/${lang}/en.arpa

#Convert LM to binary format
${moses_dir}/bin/build_binary ${moses_dir}/corpus/${lang}/en.arpa ${moses_dir}/corpus/${lang}/en.binlm

mkdir -p ${moses_dir}/working
mkdir -p ${moses_dir}/working/${lang}

cd ${moses_dir}/working/${lang} # keep this line uncommented for all runs

#Run Moses translation model training
echo "Training models using training set..."
nohup nice ${moses_dir}/scripts/training/train-model.perl -root-dir train -corpus ${data_dir}/${lang}/${train} -f ${lang} -e en -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:3:${moses_dir}/corpus/${lang}/en.binlm:8 -external-bin-dir ${moses_dir}/tools -cores 2 >& ${moses_dir}/working/${lang}/training.out #&

################TUNING################
echo "Moses Tuning phase"
#Run Moses tuning for translation model
echo "Tuning models using dev set..."
nohup nice ${moses_dir}/scripts/training/mert-moses.pl ${data_dir}/${lang}/${dev_fr} ${data_dir}/${lang}/${dev_en} ${moses_dir}/bin/moses train/model/moses.ini --mertdir ${moses_dir}/bin/ --decoder-flags="-threads 4" &> mert.out #&

#Binarise phrase table and lexical reordering models
echo "Binarising phrase table and lexical reordering models..."
mkdir -p ${moses_dir}/working/${lang}/binarised-model
${moses_dir}/bin/processPhraseTable -ttable 0 0 train/model/phrase-table.gz -nscores 5 -out binarised-model/phrase-table
${moses_dir}/bin/processLexicalTable -in train/model/reordering-table.wbe-msd-bidirectional-fe.gz -out binarised-model/reordering-table

#Edit moses.ini to point to binarised files
moses_dir_for_sed=$(echo ${moses_dir} | sed 's/\//\\\//g')
sed -i "s/^0 0 0 5 ${moses_dir_for_sed}\/working\/${lang}\/train\/model\/phrase-table.gz$/1 0 0 5 ${moses_dir_for_sed}\/working\/${lang}\/binarised-model\/phrase-table/" ${moses_dir}/working/${lang}/train/model/moses.ini
sed -i "s/^0-0 wbe-msd-bidirectional-fe-allff 6 ${moses_dir_for_sed}\/working\/${lang}\/train\/model\/reordering-table.wbe-msd-bidirectional-fe.gz$/0-0 wbe-msd-bidirectional-fe-allff 6 ${moses_dir_for_sed}\/working\/${lang}\/binarised-model\/reordering-table/" ${moses_dir}/working/${lang}/train/model/moses.ini

################TESTING################
echo "Moses Testing phase"
#Filter model for testing
echo "Filtering model for testing..."
${moses_dir}/scripts/training/filter-model-given-input.pl filtered-${test} mert-work/moses.ini ${data_dir}/${lang}/${test_fr} -Binarizer ${moses_dir}/bin/processPhraseTable
#${moses_dir}/scripts/training/filter-model-given-input.pl filtered-${test} train/model/moses.ini ${data_dir}/${lang}/${test_fr} -Binarizer ${moses_dir}/bin/processPhraseTable

#Translate test set and get BLEU score
echo "Translating test set..."
nohup nice ${moses_dir}/bin/moses -f ${moses_dir}/working/${lang}/filtered-${test}/moses.ini < ${data_dir}/${lang}/${test_fr} > ${moses_dir}/working/${lang}/${test}.translated.en 2> ${moses_dir}/working/${lang}/${test}.out #&
echo "Scoring translation using BLEU..."
${moses_dir}/scripts/generic/multi-bleu.perl -lc ${data_dir}/${lang}/${test_en} < ${moses_dir}/working/${lang}/${test}.translated.en > ${moses_dir}/working/${lang}/${lang}_results.txt
echo "BLEU score written to ${moses_dir}/working/${lang}/${lang}_results.txt"
cat ${moses_dir}/working/${lang}/${lang}_results.txt

#Let user know we've finished, and print time elapsed
echo "Done!"
T="$(($(date +%s)-T))"
date
printf "Time elapsed: %02d:%02d:%02d:%02d\n" "$((T/86400))" "$((T/3600%24))" "$((T/60%60))" "$((T%60))"
