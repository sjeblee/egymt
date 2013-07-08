#!/bin/bash

cat $1 | ./tokenizer.sed | sed -e 's/\(\.\)\([^0-9]\)/\1 \2/g' | sed -e 's/\([^0-9]\)\(\.\)/\1 \2/g' | sed -e 's/\s\+/ /g'
