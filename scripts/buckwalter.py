#!/usr/bin/python
# -*- coding: utf-8 -*-
#buckwalter.py
#Weston Feely & Serena Jeblee
#6/24/13
import sys, fileinput, unicodedata

arabicChars = {}
punc = set(['.',',','?','!','-','"'])
unbuck = {'$': '\xd8\xb4', "'": '\xd8\xa1', '&': '\xd8\xa4', '*': '\xd8\xb0', '<': '\xd8\xa5', '>': '\xd8\xa3', 'A': '\xd8\xa7', 'E': '\xd8\xb9', 'D': '\xd8\xb6', 'G': '\xda\xaf', 'F': '\xd9\x8b', 'H': '\xd8\xad', 'K': '\xd9\x8d', 'J': '\xda\x86', 'N': '\xd9\x8c', 'S': '\xd8\xb5', 'T': '\xd8\xb7', 'V': '\xef\xad\xaa', 'Y': '\xd9\x89', 'Z': '\xd8\xb8', '_': '\xef\xbb\xbb', 'a': '\xd9\x8e', '`': '\xd9\xb0', 'b': '\xd8\xa8', 'd': '\xd8\xaf', 'g': '\xd8\xba', 'f': '\xd9\x81', 'i': '\xd9\x90', 'h': '\xd9\x87', 'k': '\xd9\x83', 'j': '\xd8\xac', 'm': '\xd9\x85', 'l': '\xd9\x84', 'o': '\xd9\x92', 'n': '\xd9\x86', 'q': '\xd9\x82', 'p': '\xd9\xbe', 's': '\xd8\xb3', 'r': '\xd8\xb1', 'u': '\xd9\x8f', 't': '\xd8\xaa', 'w': '\xd9\x88', 'v': '\xd8\xab', 'y': '\xd9\x8a', 'x': '\xd8\xae', '{': '\xef\xad\x90', 'z': '\xd8\xb2', '}': '\xd8\xa6', '|': '\xd8\xa2', '~': '\xd9\x91'}
buck = {'\xef\xbb\xbb': '_', '\xd8\xaa': 't', '\xd8\xab': 'v', '\xd8\xa8': 'b', '\xd8\xa9': 'p', '\xd8\xae': 'x', '\xd8\xaf': 'd', '\xd8\xac': 'j', '\xd8\xad': 'H', '\xd8\xa2': '|', '\xd8\xa3': '>', '\xd8\xa1': "'", '\xd8\xa6': '}', '\xd8\xa7': 'A', '\xd8\xa4': '&', '\xd8\xa5': '<', '\xd8\xba': 'g', '\xd8\xb8': 'Z', '\xd8\xb9': 'E', '\xd8\xb2': 'z', '\xd8\xb3': 's', '\xd8\xb0': '*', '\xd8\xb1': 'r', '\xd8\xb6': 'D', '\xd8\xb7': 'T', '\xd8\xb4': '$', '\xd8\xb5': 'S', '\xef\xad\xaa': 'V', '\xef\xad\x90': '{', '\xda\x86': 'J', '\xda\xaf': 'G', '\xd9\x89': 'Y', '\xd9\x88': 'w', '\xd9\x8b': 'F', '\xd9\x8a': 'y', '\xd9\x8d': 'K', '\xd9\x8c': 'N', '\xd9\x8f': 'u', '\xd9\x8e': 'a', '\xd9\x81': 'f', '\xd9\x83': 'k', '\xd9\x82': 'q', '\xd9\x85': 'm', '\xd9\x84': 'l', '\xd9\x87': 'h', '\xd9\x86': 'n', '\xd9\x91': '~', '\xd9\x90': 'i', '\xd9\x92': 'o', '\xd9\xbe': 'p', '\xd9\xb0': '`'}

'''
buck = {
'ا':'A',
'ء':'\'',
'آ':'|',
'أ':'>',
'ؤ':'&',
'إ':'<',
'ئ':'}',
'ب':'b',
'ة':'p',
'ت':'t',
'ث':'v',
'ج':'j',
'ح':'H',
'خ':'x',
'د':'d',
'ذ':'*',
'ر':'r',
'ز':'z',
'س':'s',
'ش':'$',
'ص':'S',
'ض':'D',
'ط':'T',
'ظ':'Z',
'ع':'E',
'غ':'g',
'ﻻ':'_',
'ف':'f',
'ق':'q',
'ك':'k',
'ل':'l',
'م':'m',
'ن':'n',
'ه':'h',
'و':'w',
'ى':'Y',
'ي':'y',
'ً':'F',
'ٌ':'N',
'ٍ':'K',
'َ':'a',
'ُ':'u',
'ِ':'i',
'ّ':'~',
'ْ':'o',
'ٰ':'`',
'ﭐ':'{',
'پ':'p',
'چ':'J',
'ﭪ':'V',
'گ':'G',
}
'''

#Returns true if input unicode character is an Arabic unicode character
def isArabicChar(char):
	return arabicChars.setdefault(char, 'ARABIC' in unicodedata.name(char))

#Returns true if any Arabic characters are in the string
def isArabic(arabicString):
	arabicString = arabicString.decode('utf-8')
	for char in arabicString:
		if char.isalpha() and isArabicChar(char):
			return True
	return False

#Converts Arabic string into Buckwalter transliteration
def buckwalter(arabicString):
	outString = ""
	for char in arabicString.decode('utf-8'):
		char = char.encode('utf-8')
		if char in buck:
			outString+=buck[char]
		elif char.isspace() or char in punc:
			outString+=char
		else:
			sys.stderr.write("Error! Unknown Arabic character:"+char+'\n')
			outString+=char
	return outString

#Converts Buckwalter transliteration into Arabic string
def unbuckwalter(buckString):
	outString = ""
	for char in buckString:
		if char in unbuck:
			outString+=unbuck[char]
		elif char.isspace() or char in punc:
			outString+=char
		else:
			sys.stderr.write("Error! Unknown buckwalter character:"+char+'\n')
			outString+=char
	return outString

def main(args):
	#Loop through fileinput
	for line in fileinput.input():
		#Check for any Arabic characters in input string
		if isArabic(line):
			sys.stdout.write(buckwalter(line))
		else:
			sys.stdout.write(unbuckwalter(line))
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
