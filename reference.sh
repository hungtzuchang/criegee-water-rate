#!/bin/bash

FNAME=$(ls -d C2*.dat)

for i in $FNAME
do
#    python2.7 reference.py $i >> reference.data
    python2.7 reference.py $i >> $1
done
