import numpy as np
import sys
from regression import fitting
import datastack as ds
#from plot import plot_fit
import matplotlib.pyplot as plt

data=np.loadtxt(sys.argv[1],dtype='float64')
xdata=data.T[0]
ydata=data.T[1:]
reference=np.loadtxt(sys.argv[2],dtype='float64')

#bgd=np.hstack((np.arange(0,7),np.arange(44,50)))
bgd=ds.bgdstack()
bgdsignal=ydata[bgd]/np.array([reference[bgd]]*len(ydata.T)).T/53*1000
binsize=xdata[3]-xdata[2]

for i in range(0,len(bgd)):
    fit_data=np.vstack((xdata,bgdsignal[i]))
    raw_data=np.copy(fit_data)
    param_opt=fitting(fit_data.T,binsize)
    plt.xlabel('Time (ms)')
    plt.ylabel('Abs*1000')
    raw_sub=raw_data[1]-param_opt.m1*raw_data[0]-param_opt.c1
    sub_raw,=plt.plot(raw_data[0],raw_sub,'-')
#    decay_prof_sub=param_opt.popt[0]*np.exp(-fit_data.popt[1]*(decay_range))+fit_data.popt[2]
#    sub_decay,=plt.plot(decay_range,decay_prof_sub,'-',linewidth=2.0,color='red',label='y='+"{:.2f}".format(fit_data.popt[0])+'exp(-'+"{:.2f}".format(fit_data.popt[1])+'x)+'+"{:.2f}".format(fit_data.popt[2]))

#plot a signal trace to compare with background
fit_data=np.vstack((xdata,data.T[10]))
raw_data=np.copy(fit_data)
param_opt=fitting(fit_data.T,binsize)
raw_sub=raw_data[1]-param_opt.m1*raw_data[0]-param_opt.c1
sub_raw,=plt.plot(raw_data[0],raw_sub,'-')


plt.show()    

