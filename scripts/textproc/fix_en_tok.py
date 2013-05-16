#!/usr/bin/python
#fix_en_tok.py
#Weston Feely
#3/30/13
import sys, re

#Fixes HTML artifacts in output from Moses English tokenizer
def main(args):
	#Check args
	if len(args) < 3:
		print 'Usage: python fix_en_tok.py tokenized_english_file fixed_tokenization_file'
		return 1
	in_file = args[1]
	out_file = args[2]
	#Read in English data
	data = open(in_file).readlines()
	#Loop through English data
	output = []
	for en_sent in data:
		en_sent = en_sent.strip()
		#Replace HTML artifacts in English sentence with punctuation characters
		en_sent = re.sub('&apos;',"'",en_sent)
		en_sent = re.sub('&quot;','"',en_sent)
		en_sent = re.sub('&lt;','<',en_sent)
		en_sent = re.sub('&gt;','>',en_sent)
		en_sent = re.sub('&amp;','&',en_sent)
		#Lowercase English sentence
		en_sent = en_sent.lower()
		#Add sentence to output list
		output.append(en_sent)
	#Write output to file
	f = open(out_file,'w')
	for line in output:
		f.write(line+'\n')
	f.close()		
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
