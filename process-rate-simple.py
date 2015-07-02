import numpy as np
import sys
import datastack as ds
from regression import fitting_simple

data=np.loadtxt(sys.argv[1],dtype='float64')
reference=np.loadtxt(sys.argv[2],dtype='float64')
xdata=data.T[0]
ydata=data.T[1:]

#sig_bgd_pair_pre1=np.array([np.arange(6,18),np.repeat(np.arange(0,6),2)])
#print sig_bgd_pair_pre1
#sig_bgd_pair_pre2=np.array([np.arange(18,30),np.repeat(np.arange(30,36)[::-1],2)])
#print sig_bgd_pair_pre2
#sig_bgd_pair=np.vstack((sig_bgd_pair_pre1.T,sig_bgd_pair_pre2.T))
#sig_bgd_pair.shape(2,24)
#print sig_bgd_pair
#bgd=np.hstack((np.arange(3,9),np.arange(44,50)))
bgd=ds.bgdstack()
bgdsignal=np.average(ydata[bgd]/np.array([reference[bgd]]*len(ydata.T)).T/53*1000,axis=0)
#signal=np.arange(9,44)
signal=ds.signalstack()
sig=ydata[signal]/np.array([reference[signal]]*len(ydata.T)).T/53*1000

binsize=xdata[3]-xdata[2]
#print binsize

print "#Num kobs(1/ms) height_err popt.a popt.b popt.c perr.a perr.b perr.c residual"
for i in range(0,len(sig)):
    #Sig=(data.T[sig_bgd_pair[i][0]+1]/reference[sig_bgd_pair[i][0]]-data.T[sig_bgd_pair[i][1]+1]/reference[sig_bgd_pair[i][1]])/53*1000
    #Time=data.T[0]
    fit_data=np.vstack((xdata,sig[i]-bgdsignal))
    #print fit_data
    param_opt=fitting_simple(fit_data.T,binsize)
    kobs=param_opt.popt[1]
    height_err=param_opt.popt[0]+param_opt.popt[2]-param_opt.trigger_h
    print (signal[i]), kobs, height_err, ' '.join(map(str,param_opt.popt)), ' '.join(map(str,param_opt.perr)), param_opt.residual
