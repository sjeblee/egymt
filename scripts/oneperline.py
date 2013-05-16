#!/usr/bin/python
#Create tagger input from plain text file
import sys

#Main function
def main(args):
	if len(args) < 3:
		print 'Usage: python tagging_prep.py input output'
	data = open(args[1],'r').readlines()
	f = open(args[2],'w')
	c = 0
	for line in data:
    		c+=1
    		if line.isspace():
        		f.write('\n')
        		c=0
        		continue
    		line = line.split()
		for word in line:
			f.write(word + '\n')
		f.write('\n')
	f.close()
	return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
