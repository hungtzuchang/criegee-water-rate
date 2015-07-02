import numpy as np
import sys

data=np.loadtxt(sys.argv[1],dtype='float64')
print np.sum(data.T[1])/len(data.T[1])*1000
