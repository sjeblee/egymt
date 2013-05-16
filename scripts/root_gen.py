#!/usr/bin/python
# -*- coding: utf-8 -*-
#root_gen.py
#Serena Jeblee & Weston Feely
import sys

def main(args):
	#Check required args
	if len(args) < 2:
		print "Usage python root_gen.py part-of-speech >> egy_lex/part-of-speech.lexc"
		return 1
	pos = args[1].lower().capitalize()
	alphabet = set(list(u"ذضصثقفغعهخحجدشسيبلتنمكطءراوزظ"))
	alif = u"ا"
	alif_maq = u"ى"
	ta = u"ت"
	sin = u"س"
	mim = u"م"
	nun = u"ن"
	waw = u"و"
	ya = u"ي"
	tm = u"ة"
	hamza = u"ء"
	longv = set(list(u"او"))
	out = set([])
	if pos == "Noun":
		#Open file and read lines into other_nouns
		other_nouns = open("data/egy/egytrain.nouns").readlines()
		#Remove newline characters and add to output word set
		for item in other_nouns:
			out.add(item.strip())
	for x in alphabet:
		for y in alphabet:
			for z in alphabet:
				#Rule 1: Count number of vowels in possible root
				vflag = 0
				for w in set([x,y,z]):
					if w in longv:
						vflag += 1
				#Rule 2: change final alif to alif-maqsura
				if z == alif:
					z = alif_maq
				#Rule 3: Check for two vowel case, with waw+alif-maqsura, override rule 1
				if (x not in longv) and (y == waw) and (z == alif_maq):
					vflag = 0
				if (not (x==y)) and (not (x==y==z)) and (vflag < 2) and (not (y == hamza)):
					#Add 3-letter root to out list
					out.add((x+y+z).encode('utf-8'))
					#Generate verb forms
					if pos == "Verb":
						out.add((x+alif+y+z).encode('utf-8')) # V3
						if (not (x == hamza)):
							out.add((alif+x+y+z).encode('utf-8')) # V4
							out.add((ta+x+y+z).encode('utf-8')) # V5
							out.add((ta+x+alif+y+z).encode('utf-8')) # V6
							out.add((alif+nun+x+y+z).encode('utf-8')) # V7
							out.add((alif+x+ta+y+z).encode('utf-8')) # V8
							out.add((alif+sin+ta+x+y+z).encode('utf-8')) # V10
					elif pos == "Noun":
						if (not (x == alif)) and (not (y == alif)):
							out.add((x+alif+y+z).encode('utf-8')) # nominalization 
							out.add((mim+x+alif+y+z).encode('utf-8'))
						out.add((x+y+waw+z).encode('utf-8'))
						if (not (x == hamza)):
							out.add((mim+x+y+waw+z).encode('utf-8')) # nominalization 
							out.add((mim+x+y+z).encode('utf-8')) 
							out.add((ta+x+y+ya+z).encode('utf-8'))
							out.add((ta+x+y+z).encode('utf-8'))
						if (not (y == alif)) and (not (z == alif)):
							out.add((x+y+alif+z).encode('utf-8'))
							out.add((x+y+alif+z+ya).encode('utf-8'))
							if (not (x == hamza)):
								out.add((ta+x+y+alif+z).encode('utf-8'))
								out.add((alif+nun+x+y+alif+z).encode('utf-8'))
								out.add((alif+sin+ta+x+y+alif+z).encode('utf-8'))
								if (not (x == alif)) :
									out.add((alif+x+y+alif+z).encode('utf-8'))
					elif pos == "Adj":
						out.add((x+y+z).encode('utf-8'))
						out.add((x+y+ya+z).encode('utf-8'))
						out.add((x+alif+y+ya).encode('utf-8'))
						
	#Print roots to stdout
	for item in out:
		#print item+' '+pos+"Inf;"
		print item+" NegSuffix;"
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
