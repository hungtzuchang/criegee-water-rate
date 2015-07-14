import matplotlib.pyplot as plt
import numpy as np

def readout(raw_data,fit_data):
#    print raw_data
    raw_sub=raw_data.T[1]-fit_data.m1*raw_data.T[0]-fit_data.c1
    return raw_sub


def plot_trace(raw_data,fit_data):
    binsize=0.02
    plt.xlabel('Time (ms)')
    plt.ylabel('Abs')
    raw_sub=raw_data.T[1]-fit_data.m1*raw_data.T[0]-fit_data.c1
    start=fit_data.trigger-100
    end=fit_data.trigger+round(11/binsize)+49
    plt.plot(raw_data.T[0][start:end],raw_sub[start:end]/1000,'-')


def plot_fit(raw_data,fit_data,name):
    binsize=0.02
    plt.subplot(211)
    raw=plt.plot(raw_data.T[0],raw_data.T[1],'-')
    pre_range=raw_data.T[0][:fit_data.trigger-50]
    fit_pre,=plt.plot(pre_range,fit_data.m1*pre_range+fit_data.c1,'-',linewidth=2.0,color='yellow',label='y='+"{:.2f}".format(fit_data.m1)+'x+'+"{:.2f}".format(fit_data.c1))
    post_range=raw_data.T[0][fit_data.trigger+round(15/binsize)+50:]
    fit_post,=plt.plot(post_range,fit_data.m2*post_range+fit_data.c2,'-',linewidth=2.0,color='green')
    decay_range=raw_data.T[0][fit_data.trigger:fit_data.trigger+round(15/binsize)]
    decay_profile=fit_data.popt[0]*np.exp(-fit_data.popt[1]*(decay_range))+fit_data.popt[2]+fit_data.m1*decay_range+fit_data.c1
    fit_decay,=plt.plot(decay_range,decay_profile,'-',linewidth=2.0,color='red')
    plt.legend(handles=[fit_pre])
    plt.subplot(212)
    plt.xlabel('Time (ms)')
    plt.ylabel('Abs*1000')
    raw_sub=raw_data.T[1]-fit_data.m1*raw_data.T[0]-fit_data.c1
    sub_raw,=plt.plot(raw_data.T[0],raw_sub,'-')
    decay_prof_sub=fit_data.popt[0]*np.exp(-fit_data.popt[1]*(decay_range))+fit_data.popt[2]
    sub_decay,=plt.plot(decay_range,decay_prof_sub,'-',linewidth=2.0,color='red',label='y='+"{:.2f}".format(fit_data.popt[0])+'exp(-'+"{:.2f}".format(fit_data.popt[1])+'x)+'+"{:.2f}".format(fit_data.popt[2]))
    plt.legend(handles=[sub_decay])
    plt.savefig(name+'.eps',format='eps')
    plt.close()
