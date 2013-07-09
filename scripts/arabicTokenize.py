#!/usr/bin/python
# -*- coding: utf-8 -*-
#arabicTokenize.py
#Weston Feely
#7/8/13
import sys, re, fileinput

#Compile digit and punctuation regex
num = ur'0123456789'
arnum = ur'\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9'
arpunc = ur'\u2039\u203a\u00ab\u00bb\u2026\u0609\u060a\u060c\u060d\u061b\u061e\u061f\u066a\u066b\u066c\u066d'
punctok = re.compile(ur'([%s' % re.escape('!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~') + arpunc + ur'])',flags=re.U)
numtokleft = re.compile(ur'([^\.\u06d4\d])([' + num + arnum + ']+)',flags=re.U)
numtokright = re.compile(ur'([' + num + arnum + ur']+)([^\.\u06d4\d])',flags=re.U)
dottokleft = re.compile(ur'(\D)([\.\u06d4])',flags=re.U)
dottokright = re.compile(ur'([\.\u06d4])(\D)',flags=re.U)
finaldottok = re.compile(ur'([\.\u06d4])$',flags=re.U)

#Tokenize Arabic string (insert spaces around numbers and punctuation)
def tokArabic(arabicString):
	#Strip whitespace, ZWNJ, and non-break space from arabicString, decode from utf-8
	arabicString = arabicString.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v')
	#Tokenize numbers and punctuation
	arabicString = punctok.sub(ur' \1 ', arabicString)
	arabicString = numtokleft.sub(ur'\1 \2', arabicString)
	arabicString = numtokright.sub(ur'\1 \2', arabicString)
	arabicString = dottokleft.sub(ur'\1 \2', arabicString)
	arabicString = dottokright.sub(ur'\1 \2', arabicString)
	arabicString = finaldottok.sub(ur' \1', arabicString)
	#Strip whitespace, ZWNJ, and non-break space from arabicString, encode as utf-8
	arabicString = arabicString.strip(u'\xa0\u200c \t\n\r\f\v').encode('utf-8')
	#Remove multiple spaces
	arabicString = re.sub('\s+',' ',arabicString)
	return arabicString

def main(args):
	output = []
	#Perform tokenization on fileinput (stdin or args)
	for line in fileinput.input():
		output.append(tokArabic(line))
	#Write output to filename specified by user
	for line in output:
		print line
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
