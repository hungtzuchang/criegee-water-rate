#!/bin/bash

FNAME=$(ls -d *.dat.rebin)

cut -f 1 00.dat.rebin > tmp.txt

for i in $FNAME
do
    cut -f 2 $i | paste -d '\t' tmp.txt - > tmp1.txt
	mv tmp1.txt tmp.txt
done
mv tmp.txt all-C1-data.rebin.txt