#!/usr/bin/python
#extract_data.py
#Weston Feely
#5/17/13
import sys, re

def main(args):
	if len(args) < 2:
		print "Usage: extract_data.py bbn.xml"
		return 1
	data = open(args[1]).readlines()
	egycorpus_egy = []
	egycorpus_en = []
	levcorpus_lev = []
	levcorpus_en = []
	ar_buff = ''
	en_buff = ''
	dialect = ''	
	for line in data:
		#Identify dialect
		if re.search("<DIALECT>",line):
			#New entry, append Arabic and English string buffers to lists
			if dialect == "EGYPTIAN":
				egycorpus_egy.append(ar_buff)
				egycorpus_en.append(en_buff)
			elif dialect == "LEVANTINE":
				levcorpus_lev.append(ar_buff)
				levcorpus_en.append(en_buff)
			#Reset Arabic and English string buffers
			ar_buff = ''
			en_buff = ''
			#Save dialect for new entry into dialect string
			dialect = re.search('(?<=\>)[^\<]+',line).group(0)
		#Check for Source sentence
		elif re.search("<SOURCE>",line):
			#Get new Arabic string
			ar_buff = re.search('(?<=\>)[^\<]+',line).group(0)
			#Strip whitespace, ZWNJ, non-break-space from Arabic string		
			ar_buff = ar_buff.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v').encode('utf-8')
		#Check for Target sentence
		elif re.search("<TARGET>",line):
			#Get new English string
			en_buff = re.search('(?<=\>)[^\<]+',line).group(0)
			#Strip whitespace, ZWNJ, non-break-space from English string
			en_buff = en_buff.decode('utf-8').strip(u'\xa0\u200c \t\n\r\f\v').encode('utf-8')
	#Append last sentence pair to lists
	if dialect == "EGYPTIAN":
		egycorpus_egy.append(ar_buff)
		egycorpus_en.append(en_buff)
	elif dialect == "LEVANTINE":
		levcorpus_lev.append(ar_buff)
		levcorpus_en.append(en_buff)
	#Write lists to file
	f = open('../data/egy/egycorpus.egy','w')
	for line in egycorpus_egy:
		f.write(line+'\n')
	f.close()
	f = open('../data/egy/egycorpus.en','w')	
	for line in egycorpus_en:
		f.write(line+'\n')
	f.close()
	f = open('../data/lev/levcorpus.lev','w')	
	for line in levcorpus_lev:
		f.write(line+'\n')
	f.close()	
	f = open('../data/lev/levcorpus.en','w')
	for line in levcorpus_en:
		f.write(line+'\n')
	f.close()
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
