#!/bin/bash

cd $HOME

#Install boost
wget http://downloads.sourceforge.net/project/boost/boost/1.51.0/boost_1_51_0.tar.gz
tar -xvzf boost_1_51_0.tar.gz
cd boost_1_51_0
./bootstrap.sh
./b2 --with=all --prefix=$HOME/usr/local -j 5 install threading=multi

#Export boost root (put this in your .bashrc)
export BOOST_ROOT=$HOME/usr/local

#Move to github folder
mkdir $HOME/github
cd $HOME/github

#Install Moses
git clone https://github.com/moses-smt/mosesdecoder.git
cd mosesdecoder
./bjam -j5 --with-boost=$BOOST_ROOT

cd $HOME/github

#Install cdec
git clone https://github.com/redpony/cdec
cd cdec
autoreconf -ifv
./configure --prefix=$HOME/usr/local && make

#Install python
cd $HOME
wget http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz
tar -xvzf Python-2.7.5.tgz
cd Python-2.7.5.tgz
./configure --prefix=$HOME/usr/local && make && make install

#Export new python path (put this in your .bashrc)
export PATH=$HOME/usr/local:$PATH
#alias python="python2.7"

#Install ducttape
cd $HOME/github
git clone https://github.com/jhclark/ducttape.git

#Export ducttape path (put this in your .bashrc)
export PATH=$HOME/github/ducttape:$PATH

#Install multeval
cd $HOME/github
git clone https://github.com/jhclark/multeval
