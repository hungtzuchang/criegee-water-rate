import numpy as np

#file number of background
def bgdstack():
    return np.hstack((np.arange(3,9),np.arange(44,50)))


#file number of signal
def signalstack():
    return np.arange(9,44)
