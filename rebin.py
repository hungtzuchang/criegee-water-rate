import numpy as np
import sys

data=np.loadtxt(sys.argv[1],dtype='float64')
binsize=int(sys.argv[2])
binnum=len(data.T[0])/binsize
binlen=binsize*binnum
#rebin_a=np.arange(0,binnum)
xdata=data.T[0][0:binlen].reshape(binnum,binsize)
#print xdata
ydata=data.T[1][0:binlen].reshape(binnum,binsize)
xrebin=np.mean(xdata,axis=1)
yrebin=np.mean(ydata,axis=1)
#print xrebin
np.savetxt(sys.argv[3],np.array([xrebin,yrebin]).T,fmt='%.10f')
