#!/usr/bin/python
# -*- coding: utf-8 -*-
#arabicTokenize.py
#Weston Feely
#6/26/13
import sys, re, fileinput, string

#Compile digit and punctuation regex
num = ur''+string.digits
arpunc = ur'\u2039\u203a\u00ab\u00bb\u2026\u0609\u060a\u060c\u060d\u061b\u061f\u066a\u066c\u066d\u06d4'
arnum = ur'\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9'
tok = re.compile(ur'([%s' % re.escape(string.punctuation) + num + arpunc + arnum + ur'])')

#Tokenize Arabic string (insert spaces around numbers and punctuation)
def tokArabic(arabicString):
	#Strip whitespace, ZWNJ, and non-break space from arabicString, decode from utf-8
	arabicString = arabicString.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v')
	#Tokenize numbers and punctuation
	arabicString = tok.sub(ur' \1 ', arabicString)
	#Re-encode string as utf-8
	arabicString = arabicString.encode('utf-8')
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
