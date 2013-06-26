#!/usr/bin/python
#englishNorm.py
#Weston Feely
#6/26/13
import sys, re, fileinput

#Normalize English text string, by replacing HTML artifacts with punctuation marks
def normEnglish(enString):
	#Strip whitespace from English string
	enString = enString.strip()
	#Replace HTML artifacts with punctuation
	enString = re.sub('&apos;',"'",enString)
	enString = re.sub('&quot;','"',enString)
	enString = re.sub('&lt;','<',enString)
	enString = re.sub('&gt;','>',enString)
	enString = re.sub('&amp;','&',enString)
	#Lowercase English sentence
	enString = enString.lower()
	return enString

def main(args):
	output = []
	#Perform normalization on fileinput (stdin or args)
	for line in fileinput.input():
		output.append(normEnglish(line))
	#Write output to filename specified by user
	for line in output:
		print line
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
