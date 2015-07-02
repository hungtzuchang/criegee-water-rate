import numpy as np
import matplotlib.pyplot as plt
import sys

data=np.loadtxt(sys.argv[1])

fit=np.polyfit(data.T[0],data.T[1],2)
fitline1=fit[0]*np.square(data.T[0])+fit[1]*data.T[0]+fit[2]
residual1=np.sqrt(np.sum(np.square(fitline1-data.T[1]))/len(data.T[0]))
fit2=np.polyfit(data.T[0],data.T[2],2)
fitline2=fit2[0]*np.square(data.T[0])+fit2[1]*data.T[0]+fit2[2]
residual2=np.sqrt(np.sum(np.square(fitline2-data.T[1]))/len(data.T[0]))
plt.xlabel('[$H_2O$] ($10^{15}$)')
plt.ylabel('$k_{obs}$ ($s^{-1}$)')
rate,=plt.plot(data.T[0],data.T[1],'ro',color='red',label='processed')
fit_rate,=plt.plot(data.T[0],fitline1,'-',color='red',label='processed fit,res='+"{:.2f}".format(residual1))
rate_simple,=plt.plot(data.T[0],data.T[2],'g^',linewidth=2.0,label='direct',color='blue')
fit_rate_simple,=plt.plot(data.T[0],fitline2,'-',color='blue',label='direct fit,res='+"{:.2f}".format(residual2))
plt.legend(handles=[rate,fit_rate,rate_simple,fit_rate_simple],loc=4)
plt.text(1,1500,'$y$='+"{:.2E}".format(fit[0])+'$x^2+$'+"{:.2f}".format(fit[1])+'$x$+'+"{:.2f}".format(fit[2]),color='red')
plt.text(1,1300,'$y$='+"{:.2E}".format(fit2[0])+'$x^2+$'+"{:.2f}".format(fit2[1])+'$x$+'+"{:.2f}".format(fit2[2]),color='blue')
plt.savefig(sys.argv[2],format='eps')
plt.close()
