import numpy as np
import sys
import matplotlib.pyplot as plt
#import datastack as ds
from regression import fitting
from plot import readout

data=np.loadtxt(sys.argv[1],dtype='float64')
xdata=data.T[0]
ydata=data.T[1:]
reference=np.loadtxt(sys.argv[2],dtype='float64')
#print reference.shape
#sig_bgd_pair_pre1=np.array([np.arange(7,19),np.repeat(np.arange(0,6),2)])
#print sig_bgd_pair_pre1
#sig_bgd_pair_pre2=np.array([np.arange(19,44),np.repeat(np.arange(44,50)[::-1],4)])
#print sig_bgd_pair_pre2
#sig_bgd_pair=np.vstack((sig_bgd_pair_pre1.T,sig_bgd_pair_pre2.T))
#bgd=np.hstack((np.arange(3,9),np.arange(44,50)))
bgd=np.hstack((np.arange(0,6),np.arange(41,47)))
#bgdsignal=ydata[bgd]/np.array([reference[bgd]]*len(ydata.T)).T
#print bgdsignal
bgdsignal=np.average(ydata[bgd]/np.array([reference[bgd]]*len(ydata.T)).T/53*1000,axis=0)
#plt.plot(xdata,bgdsignal,'-')
#plt.plot(xdata,data.T[1],'-')
#print len(ydata.T)
#plt.show()
#plt.close()
#print bgdsignal
signal=np.arange(6,41)
sig=ydata[signal]/np.array([reference[signal]]*len(ydata.T)).T/53*1000
#sig_bgd_pair.shape(2,24)
#print sig_bgd_pair
binsize=xdata[3]-xdata[2]

dout=np.copy(sig)

#print "#Num kobs(1/ms) height_err m1 c1 popt.a popt.b popt.c perr.a perr.b perr.c residual"
for i in range(0,len(sig)):
    #Sig=(data.T[sig_bgd_pair[i][0]+1]/reference[sig_bgd_pair[i][0]]-data.T[sig_bgd_pair[i][1]+1]/reference[sig_bgd_pair[i][1]])/53*1000
    #Time=data.T[0]
    fit_data=np.vstack((xdata,sig[i]-bgdsignal))
    raw_data=np.copy(fit_data)
    print raw_data
    param_opt=fitting(fit_data.T)
    dout[i]=readout(raw_data.T,param_opt)


np.savetxt(sys.argv[3],np.vstack((xdata,dout)).T,fmt='%.8f')
#    kobs=param_opt.popt[1]
#    height_err=param_opt.popt[0]+param_opt.popt[2]-param_opt.trigger_h
#    print (signal[i]), kobs, height_err, param_opt.m1, param_opt.c1, ' '.join(map(str,param_opt.popt)), ' '.join(map(str,param_opt.perr)), param_opt.residual
#    plot_fit(raw_data.T,param_opt,str(signal[i])+'-fig',binsize)
