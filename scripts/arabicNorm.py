#!/usr/bin/python
# -*- coding: utf-8 -*-
#arabicNorm.py
#Weston Feely
#7/22/13
import sys, re, fileinput, argparse

#Get arguments from command line
parser = argparse.ArgumentParser(description='Normalize Arabic or Farsi text.')
parser.add_argument('-f', '--farsi', action='store_true',
                   help='input is Farsi text (default: input is Arabic text)')
parser.add_argument('-b', '--blockEllipsis', action='store_true',
                   help='block ellipsis normalization (default: sequence of full stops normalized to ellipsis character)')
parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()

#Compile diacritics regex
diacritics = ur'[\u0610\u0611\u0612\u0613\u0614\u0615\u0616\u0617\u0618\u0619\u061a\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652\u0653\u0654\u0655\u0656\u0657\u0658\u0659\u065a\u065b\u065c\u065d\u065e\u065f\u0670\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06df\u06e0\u06e1\u06e2\u06e3\u06e4\u06e7\u06e8\u06ea\u06eb\u06ec\u06ed]'
normaccents = re.compile(diacritics,flags=re.U)
numerals = {ur'\u0660':ur'0',ur'\u0661':ur'1',ur'\u0662':ur'2',ur'\u0663':ur'3',ur'\u0664':ur'4',
ur'\u0665':ur'5',ur'\u0666':ur'6',ur'\u0667':ur'7',ur'\u0668':ur'8',ur'\u0669':ur'9',
ur'\u06f0':ur'0',ur'\u06f1':ur'1',ur'\u06f2':ur'2',ur'\u06f3':ur'3',ur'\u06f4':ur'4',
ur'\u06f5':ur'5',ur'\u06f6':ur'6',ur'\u06f7':ur'7',ur'\u06f8':ur'8',ur'\u06f9':ur'9'}
letters = {ur'\u0622':ur'\u0627',ur'\u0623':ur'\u0627',ur'\u0625':ur'\u0627',ur'\u0624':ur'\u0648',ur'\u0626':ur'\u064a',ur'\06c0':ur'\u0674'}

#Normalize Arabic text string, by removing diacritics, replacing diacriticized alif, ha, ya, waw with standard versions
def norm_arabic(arabicString, far=False, blockEllipsis=False):
	#Strip whitespace, ZWNJ, and non-break space from arabicString
	arabicString = arabicString.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v')
	#Remove all diacritics
	arabicString = normaccents.sub(ur'',arabicString)
	#Normalize Arabic numerals
	for num in numerals:
		arabicString = re.sub(num,numerals[num],arabicString,flags=re.U)	
	#Normalize Arabic letters (robust to diacritic removal)
	for letter in letters:
		arabicString = re.sub(letter,letters[letter],arabicString,flags=re.U)
	#Normalize Arabic ya (ya -> alif maksura at end of word)
	arabicString = re.sub(ur'\u064a\b',ur'\u0649',arabicString,flags=re.U)
	#Optional: normalize Farsi ye (ya and alif maksura --> Farsi ye)
	if far:
		arabicString = re.sub(ur'\u064a',ur'\u06cc',arabicString,flags=re.U)
		arabicString = re.sub(ur'\u0649',ur'\u06cc',arabicString,flags=re.U)
		arabicString = re.sub(ur'\ufeef',ur'\u06cc',arabicString,flags=re.U)
	#Normalize ellipsis (sequence of full stops becomes ellipsis)
	if not blockEllipsis:
		arabicString = re.sub(ur'([\.\u06d4\u2026]+( )?[\.\u06d4\u2026]+)+',ur'\u2026',arabicString)
	#Re-encode as utf-8
	arabicString = arabicString.encode('utf-8')
	return arabicString

def main(args):
	output = []
	#Perform normalization on infile
	if type(args.infile) is file:
		#Input is stdin
		for line in args.infile:
				output.append(norm_arabic(line, args.farsi, args.blockEllipsis))
	else:
		#Input is list of files
		for f in args.infile:
			for line in f:
				output.append(norm_arabic(line, args.farsi, args.blockEllipsis))
	#Write output to filename specified by user
	for line in output:
		print line
	return 0

if __name__ == '__main__':
	sys.exit(main(args))
