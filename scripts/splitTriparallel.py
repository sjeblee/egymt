#!/usr/bin/python
#splitTriparallel.py
#Weston Feely
#12/9/13
import sys, re, random

def main(args):
	#Check args
	if len(args) < 4:
		print "Usage: python splitTriparallel.py enus.txt msa.txt areg.txt"
		return 1
	a = args[1].strip().rstrip('.txt')
	b = args[2].strip().rstrip('.txt')
	c = args[3].strip().rstrip('.txt')
	a_text = open(args[1]).readlines()
	b_text = open(args[2]).readlines()
	c_text = open(args[3]).readlines()
	assert len(a_text) == len(b_text) == len(c_text)
	num_segments = len(a_text)
	#Set fraction of data to use for train, tune, test
	train_fraction = 0.98
	tune_fraction = 0.01
	test_fraction = 0.01
	assert (train_fraction + tune_fraction + test_fraction) == 1.0
	#Loop through data
	parallel = []
	for i in xrange(num_segments):
		parallel.append((a_text[i],b_text[i],c_text[i]))
	#Shuffle segments
	random.shuffle(parallel)
	#Split shuffled sentences into training and test sets
	num_train = int(num_segments*train_fraction) # number of segments to be in train set
	num_tune = num_train + int(num_segments*tune_fraction) # number of segments to be in tune set	
	train_set = [] # list of string 3-tuples, to write to file as training set
	tune_set = [] # list of string 3-tuples, to write to file as tune set
	test_set = [] # list of string 3-tuples, to write to file as test set
	#Loop through segments
	for i in xrange(num_segments):
		if i < num_train:
			#Put segment in training set
			train_set.append(parallel[i])
		elif i < num_tune:
			#Put segment in tune set
			tune_set.append(parallel[i])
		else:
			#Put segment in test set
			test_set.append(parallel[i])
	#Write sets to file
	a_train_fn = 'train-'+a+'.txt'
	b_train_fn = 'train-'+b+'.txt'
	c_train_fn = 'train-'+c+'.txt'
	a_tune_fn = 'tune-'+a+'.txt'
	b_tune_fn = 'tune-'+b+'.txt'
	c_tune_fn = 'tune-'+c+'.txt'
	a_test_fn = 'test-'+a+'.txt'
	b_test_fn = 'test-'+b+'.txt'
	c_test_fn = 'test-'+c+'.txt'
	#Write training set
	f = open(a_train_fn,'w')
	g = open(b_train_fn,'w')
	h = open(c_train_fn,'w')
	for triple in train_set:
		f.write(triple[0])
		g.write(triple[1])
		h.write(triple[2])
	f.close()
	g.close()
	h.close()
	#Write tune set
	f = open(a_tune_fn,'w')
	g = open(b_tune_fn,'w')
	h = open(c_tune_fn,'w')
	for triple in tune_set:
		f.write(triple[0])
		g.write(triple[1])
		h.write(triple[2])
	f.close()
	g.close()
	h.close()
	#Write test set
	f = open(a_test_fn,'w')
	g = open(b_test_fn,'w')
	h = open(c_test_fn,'w')
	for triple in test_set:
		f.write(triple[0])
		g.write(triple[1])
		h.write(triple[2])
	f.close()
	g.close()
	h.close()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
