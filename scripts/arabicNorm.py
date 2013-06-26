#!/usr/bin/python
# -*- coding: utf-8 -*-
#arabicNorm.py
#Weston Feely
#6/26/13
import sys, re, fileinput

#Compile diacritics regex
diacritics = ur'[\u0610\u0611\u0612\u0613\u0614\u0615\u0616\u0617\u0618\u0619\u061a\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652\u0653\u0654\u0655\u0656\u0657\u0658\u0659\u065a\u065b\u065c\u065d\u065e\u065f\u0670\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06df\u06e0\u06e1\u06e2\u06e3\u06e4\u06e7\u06e8\u06ea\u06eb\u06ec\u06ed]'
norm = re.compile(diacritics)

#Normalize Arabic text string, by removing diacritics, replacing diacriticized alif, ha, ya, waw with standard versions
def normArabic(arabicString):
	#Strip whitespace, ZWNJ, and non-break space from arabicString
	arabicString = arabicString.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v')
	#Remove all diacritics
	arabicString = norm.sub(ur'',arabicString).encode('utf-8')
	#Normalize alif
	arabicString = re.sub('أ','ا',arabicString)
	arabicString = re.sub('إ','ا',arabicString)
	arabicString = re.sub('آ','ا',arabicString)
	#Normalize ha
	arabicString = re.sub('ۀ','ه',arabicString)
	#Normalize ya
	arabicString = re.sub('ي','ﻯ',arabicString)
	arabicString = re.sub('ئ','ﻯ',arabicString)
	#Normalize waw
	arabicString = re.sub('ؤ','و',arabicString)
	return arabicString

def main(args):
	output = []
	#Perform normalization on fileinput (stdin or args)
	for line in fileinput.input():
		output.append(normArabic(line))
	#Write output to filename specified by user
	for line in output:
		print line
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
