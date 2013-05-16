#!/usr/bin/python
# -*- coding: utf-8 -*-
#preprocess.py
#Weston Feely
#3/30/13
import sys, re

#Does text processing for Arabic-English parallel data, splits into two files
def main(args):
	#Check args
	if len(args) < 4:
		print 'Usage: python preprocess.py arabic_english_parallel_data arabic_output_filename english_output_filename'
		return 1
	parallel_file = args[1]
	arabic_file = args[2]
	english_file = args[3]
	#Read in parallel data
	data = open(parallel_file).readlines()
	#Set up regular expressions and monolingual data lists
	repunc = re.compile(u'([\]\[!"\&\'()*,\./:;<=>?@\\^_`{|}~٫«٪٭،٬۔»؛؟]+)',re.U) # match punctuation, capture string
	repunc_ar_remove = re.compile(u'([\]\[!"\&\'()*,\./:;<=>?@\\^_`{|}~٫«٪٭،٬۔»؛؟])+',re.U) # match punctuation, capture singles
	repunc_en_remove = re.compile(u'([\]\[!"\&\'()*,\./:;<=>?@\\^_`{|}~])+',re.U) # match Western punctuation only, capture singles
	renuml = re.compile(u'(\D)(\d)',re.U) # match numbers on left context
	renumr = re.compile(u'(\d)(\D)',re.U) # match numbers on right context
	ar = []
	en = []
	#Loop through parallel data
	for line in data:
		#Remove multiple spaces from line
		line = re.sub('\s+',' ',line)
		#Split line on |||
		lis = line.split(' ||| ')
		ar_sent = lis[0].strip()
		en_sent = lis[1].strip()
		#Do English Text Processing
		#Normalize email addresses in English sentence TODO: adjust patterns for Levantine data
		if re.search('@',en_sent):
			en_sent = re.sub('[A-Za-z0-9\-]+@\w+\.\w+','name@domain.com',en_sent)
			en_sent = re.sub('\(\([A-Za-z0-9\-]+\)\)\(\(@\w+\.com\)\)',' name@domain.com',en_sent)
		#Replace HTML artifacts in English sentence with punctuation characters
		en_sent = re.sub('&apos;',"'",en_sent)
		en_sent = re.sub('&quot;','"',en_sent)
		en_sent = re.sub('&lt;','<',en_sent)
		en_sent = re.sub('&gt;','>',en_sent)
		en_sent = re.sub('&amp;','&',en_sent)
		#Remove multiple punctuation from English sentence
		en_sent = repunc_en_remove.sub(r'\1',en_sent)
		#Lowercase English sentence
		en_sent = en_sent.lower()
		#Do Arabic Text Processing
		#Normalize email addresses in Arabic sentence TODO: adjust patterns for Levantine data
		if re.search('@',ar_sent):
			ar_sent = re.sub('«[\)A-Za-z0-9\-]+@\w+\.\w+»','name@domain.com',ar_sent)
			ar_sent = re.sub('«[A-Za-z0-9\-]+» \.\.\. «@\w+\.\w+»','name@domain.com',ar_sent)		
		#Decode utf-8 line
		ar_sent = ar_sent.decode('utf-8')
		#Tokenize Western and Arabic punctuation, removing multiples
		ar_sent = repunc_ar_remove.sub(r'\1',ar_sent)
		ar_sent = repunc.sub(r' \1 ',ar_sent)
		#Undo punctuation tokenization for email addresses, to agree with English tokenizer
		ar_sent = re.sub('domain \. com','domain.com',ar_sent)
		#Tokenize unicode numbers, keeping sequences of numbers together
		ar_sent = renuml.sub(r'\1 \2',ar_sent)
		ar_sent = renumr.sub(r'\1 \2',ar_sent)
		#Re-encode line as utf-8
		ar_sent = ar_sent.encode('utf-8')
		#Add sentences to lists
		ar.append(ar_sent)
		en.append(en_sent)
	#Write monolingual data to files
	f = open(arabic_file,'w')
	for line in ar:
		f.write(line+'\n')
	f.close()
	f = open(english_file,'w')
	for line in en:
		f.write(line+'\n')
	f.close()		
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
