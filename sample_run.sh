#!/bin/sh

# This file is a sample for analyzing the data of simplest Criegee intermediate with water

# Note: C1-> signal-reference, C2-> reference, C3-> signal

# rebin.sh shall rebin all C1 data 
# Usage: sh rebin.sh [date of data]
sh rebin.sh 0626

REF_NAME="reference.data"
# reference.sh shall take average value of all C2 voltage and write to output file '$REF_NAME'
sh reference.sh $REF_NAME

JOIN_C1_REBIN_NAME="all-C1-data.rebin.txt"
# joinfile.sh joins all rebinned C1 data into a single file $JOIN_C1_REBIN_NAME
sh joinfile.sh $JOIN_C1_REBIN_NAME

# Clean up rebin data
#rm *.dat.rebin

# rate without tilted background correction
python2.7 process-rate-simple.py $JOIN_C1_REBIN_NAME $REF_NAME > rate-simple.txt

# rate with tilted background correction
python2.7 process-rate.py $JOIN_C1_REBIN_NAME $REF_NAME > rate.txt

# plot background signal
#python2.7 process-background.py $JOIN_C1_REBIN_NAME $REF_NAME
