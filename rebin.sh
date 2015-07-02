#!/bin/bash

FNAME=$(ls -d C1-${1}*.dat)

# python rebin.py [source data] [bin size] [output name]

for i in $FNAME
do
#    echo $i
#    echo ${i#C1-${1}-000}.rebin
#    ../code/rebin.exe $i ${i#C1-${1}-000}.rebin 40
     python2.7 rebin.py $i 40 ${i#C1-${1}-000}.rebin
done
