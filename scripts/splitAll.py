#!/usr/bin/python
#splitAll.py
#Weston Feely
#1/22/14
import sys, os, re, random, math

def main(args):
	#Check args
	if len(args) < 5:
		print "Usage: python splitAll.py lang1.txt lang2.txt lang3.txt lang4.txt"
		return 1
	apath, a = os.path.split(args[1].rstrip('.txt'))
	bpath, b = os.path.split(args[2].rstrip('.txt'))
	cpath, c = os.path.split(args[3].rstrip('.txt'))
	dpath, d = os.path.split(args[4].rstrip('.txt'))
	a_text = open(args[1]).readlines()
	b_text = open(args[2]).readlines()
	c_text = open(args[3]).readlines()
	d_text = open(args[4]).readlines()
	assert len(a_text) == len(b_text) == len(c_text) == len(d_text)
	num_segments = len(a_text)
	#Set fraction of data to use for train, tune, test
	train_fraction = 0.98
	tune_fraction = 0.01
	test_fraction = 0.01
	assert (train_fraction + tune_fraction + test_fraction) == 1.0
	#Loop through data
	parallel = []
	for i in xrange(num_segments):
		parallel.append((a_text[i],b_text[i],c_text[i],d_text[i]))
	#Shuffle segments
	random.shuffle(parallel)
	#Split shuffled sentences into training and test sets
	num_train = int(num_segments*train_fraction) # number of segments to be in train set
	num_tune = num_train + int(math.ceil(num_segments*tune_fraction)) # number of segments to be in tune set	
	train_set = [] # list of string 4-tuples, to write to file as training set
	tune_set = [] # list of string 4-tuples, to write to file as tune set
	test_set = [] # list of string 4-tuples, to write to file as test set
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
	a_set = os.path.join(apath, a+'-shuffled.txt')
	b_set = os.path.join(bpath, b+'-shuffled.txt')
	c_set = os.path.join(cpath, c+'-shuffled.txt')
	d_set = os.path.join(dpath, d+'-shuffled.txt')
	a_train_fn = os.path.join(apath, 'train-'+a+'.txt')
	b_train_fn = os.path.join(bpath, 'train-'+b+'.txt')
	c_train_fn = os.path.join(cpath, 'train-'+c+'.txt')
	d_train_fn = os.path.join(dpath, 'train-'+d+'.txt')
	a_tune_fn = os.path.join(apath, 'tune-'+a+'.txt')
	b_tune_fn = os.path.join(bpath, 'tune-'+b+'.txt')
	c_tune_fn = os.path.join(cpath, 'tune-'+c+'.txt')
	d_tune_fn = os.path.join(dpath, 'tune-'+d+'.txt')
	a_test_fn = os.path.join(apath, 'test-'+a+'.txt')
	b_test_fn = os.path.join(bpath, 'test-'+b+'.txt')
	c_test_fn = os.path.join(cpath, 'test-'+c+'.txt')
	d_test_fn = os.path.join(dpath, 'test-'+d+'.txt')
	#Write all data
	f = open(a_set,'w')
	g = open(b_set,'w')
	h = open(c_set,'w')
	i = open(d_set,'w')
	for quad in parallel:
		f.write(quad[0])
		g.write(quad[1])
		h.write(quad[2])
		i.write(quad[3])
	f.close()
	g.close()
	h.close()
	i.close()
	#Write training set
	f = open(a_train_fn,'w')
	g = open(b_train_fn,'w')
	h = open(c_train_fn,'w')
	i = open(d_train_fn,'w')
	for quad in train_set:
		f.write(quad[0])
		g.write(quad[1])
		h.write(quad[2])
		i.write(quad[3])
	f.close()
	g.close()
	h.close()
	i.close()
	#Write tune set
	f = open(a_tune_fn,'w')
	g = open(b_tune_fn,'w')
	h = open(c_tune_fn,'w')
	i = open(d_tune_fn,'w')
	for quad in tune_set:
		f.write(quad[0])
		g.write(quad[1])
		h.write(quad[2])
		i.write(quad[3])
	f.close()
	g.close()
	h.close()
	i.close()
	#Write test set
	f = open(a_test_fn,'w')
	g = open(b_test_fn,'w')
	h = open(c_test_fn,'w')
	i = open(d_test_fn,'w')
	for quad in test_set:
		f.write(quad[0])
		g.write(quad[1])
		h.write(quad[2])
		i.write(quad[3])
	f.close()
	g.close()
	h.close()
	i.close()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
