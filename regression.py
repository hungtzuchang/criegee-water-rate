import numpy as np
#import sys

#data=np.loadtxt(sys.argv[1],dtype='float64')

#data=a.T
#print data

import collections
Fit_Param = collections.namedtuple('Fit_Param', ['trigger','trigger_h','m1','c1','m2','c2','popt','popv','perr','residual'])

from scipy.optimize import curve_fit
def fit_exp(x,a,b,c):
    return a*np.exp(-b*x)+c

def fitting_simple(data,binsize):
    trigger=data.T[1].argmax(axis=0)
    #print trigger

    #binsize=0.02
    decay_data=data[trigger:(trigger+round(15/binsize))]
    trigger_h = decay_data.T[1][0]

    popt,popv=curve_fit(fit_exp,decay_data.T[0],decay_data.T[1],[30,1,10])
    perr = np.sqrt(np.diag(popv)) #stdev
    residual=np.sqrt(np.sum(np.square(decay_data.T[1]-fit_exp(decay_data.T[0],popt[0],popt[1],popt[2])))/len(decay_data.T[0]))
    #print popt
    #print perr
    return Fit_Param(trigger,trigger_h,0,0,0,0,popt,popv,perr,residual)
    

def fitting(data,binsize):
    trigger=data.T[1].argmax(axis=0)
    #print trigger

    #binsize=0.02
    pre_decay_data=data[:(trigger-round(5/binsize))]
    #print pre_decay_data.T
    #print data[(trigger-round(5/binsize))], data[(trigger+round(15/binsize))]
    post_decay_data=data[(trigger+round(15/binsize)):]
    decay_data=data[trigger:(trigger+round(15/binsize))]

    A=np.vstack([pre_decay_data.T[0],np.ones(len(pre_decay_data.T[0]))]).T
    #y=mx+c
    m1,c1=np.linalg.lstsq(A,pre_decay_data.T[1])[0]
    #print m1, c1
    A=np.vstack([post_decay_data.T[0],np.ones(len(post_decay_data.T[0]))]).T
    m2,c2=np.linalg.lstsq(A,post_decay_data.T[1])[0]
    #print m2, c2

#cm=(m1+m2)/2
#mm=(c1+c2)/2

    decay_data.T[1]-=decay_data.T[0]*m1+c1*np.ones(len(decay_data.T[0]))
    decay_pre_fit=decay_data.T
    decay_pre_fit[0]-=decay_data.T[0][0]*np.ones(len(decay_data.T[0]))
    trigger_h = decay_data.T[1][0]

    popt,popv=curve_fit(fit_exp,decay_pre_fit[0],decay_pre_fit[1])
    perr = np.sqrt(np.diag(popv)) #stdev
    residual=np.sqrt(np.sum(np.square(decay_pre_fit[1]-fit_exp(decay_pre_fit[0],popt[0],popt[1],popt[2])))/len(decay_pre_fit[0]))
    #print popt
    #print perr
    return Fit_Param(trigger,trigger_h,m1,c1,m2,c2,popt,popv,perr,residual)
