#!/usr/bin/python
#Place every word in text file into a new file, with one word per line
import sys

#Main function
def main(args):
	if len(args) < 3:
		print "Usage: python oneperline.py input_file output_file"
		return 1
	data = open(args[1]).readlines()
	f = open(args[2],'w')
	for line in data:
    		if line.isspace():
        		f.write('\n')
        		continue
		for word in line.split():
			f.write(word+'\n')
		f.write('\n')
	f.close()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
