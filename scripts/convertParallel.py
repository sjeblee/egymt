#!/usr/bin/python
#convertParallel.py
#Weston Feely
#11/30/13
import sys

def main(args):
	if len(args) < 3:
		print "Usage: python convertParallel.py src.txt tgt.txt outfilename"
		return 1
	srctext = open(args[1]).readlines()
	tgttext = open(args[2]).readlines()
	assert len(srctext) == len(tgttext)
	f = open(args[3], 'w')
	for i in xrange(len(srctext)):
		f.write(srctext[i].rstrip()+" ||| "+tgttext[i])
	f.close()
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))
