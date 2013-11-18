#!/bin/bash

#Install boost
cd $HOME
wget http://downloads.sourceforge.net/project/boost/boost/1.51.0/boost_1_51_0.tar.gz
tar -xvzf boost_1_51_0.tar.gz
cd boost_1_51_0
./bootstrap.sh
./b2 --with=all --prefix=$HOME/usr/local -j 5 install threading=multi

#Export boost root (put this in your .bashrc)
export BOOST_ROOT=$HOME/usr/local

#Install python
cd $HOME
wget http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz
tar -xvzf Python-2.7.5.tgz
cd Python-2.7.5.tgz
./configure --prefix=$HOME/usr/local && make && make install

#Export new python path (put this in your .bashrc)
export PATH=$HOME/usr/local:$PATH
export PYTHON=$HOME/usr/local/bin/python
alias python="$HOME/usr/local/bin/python"

#Make github folder if necessary
mkdir -p $HOME/github

#Install Moses
cd $HOME/github
git clone https://github.com/moses-smt/mosesdecoder.git
cd mosesdecoder
#Revert Moses version to one that works with our ducttape code
#git reset --hard 8a1e944bb428a0af9f6c82c26e5633361ce4052c
./bjam -j5 --with-boost=$BOOST_ROOT

#Install cdec
cd $HOME/github
git clone https://github.com/redpony/cdec
cd cdec
autoreconf -ifv
./configure --with-boost=$BOOST_ROOT && make
cd python
python setup.py install

#Make a tools folder if necessary
mkdir -p $HOME/tools

#Install ducttape
cd $HOME/tools
wget http://www.cs.cmu.edu/~jhclark/downloads/ducttape-0.3.tgz
tar -xvzf ducttape-0.3.tgz

#Export ducttape path (put this in your .bashrc)
export PATH=$HOME/tools/ducttape-0.3:$PATH

#Install multeval
cd $HOME/github
git clone https://github.com/jhclark/multeval
