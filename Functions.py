from scipy import signal

#############################################################################

def signal_stats(a):
    """
    a is the time column.
    
          sr - sample rate
          dt - time step
          df - frequency window
          tw - time window

    """
   
    dur = a[-1]
    dt = dur / float(len(a))
    fs = 1 / dt
    df = fs/len(a)
    tw = 1/df
    
    return fs, dt, df,tw

#############################################################################


def oneX_filter(data, lowcut, highcut, fs, fc, order=1):
    """
    This function filters the raw data of the shaft at 1x
    
    data is the raw data to be filtere
    lowcut - low cutoff frequency
    highcut - high cuttoff frequency
    fs - sampling rate / frequency
    fc - rotational speed in rps
    order - filter order = 1 by default
    
    """
    # Detrending Removing DC offset
    data_dtrd = signal.detrend(data)
    
    # Butterworth low pass filter to remove frequencies higher than 1x
    b2,a2 = signal.butter(6,fc/(fs/2),'low')
    data_lpf= signal.lfilter(b2,a2,data_dtrd)

    nyq = 0.5 * fs  #nyquest criteria
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='bandstop')
    data_fltrd = signal.lfilter(b, a, data_lpf)
    
    return data_fltrd

#############################################################################

def single_orbit (x_fltrd, y_fltrd, fs, fc):
    
    """
    this function takes:
        x_fltrd - filtered data in x axis
        y_fltrd - filtered data in y axis
        fs - sampling frequency 
        fc - rotational speed in rps
        
    and returns the x and y data for one revolution
    to be plotted as a single orbit
    
    """
    n = int(fs/fc)    #no. of points that represent a single orbit
    nx = len(x_fltrd) #no. of data points of x_fltrd 
    ns = int(nx/3)    #index of the starting point 
    
    if (len(x_fltrd)> 4*n):
        x_sngl = x_fltrd[ns:ns+n]
        y_sngl = y_fltrd[ns:ns+n]
        return x_sngl, y_sngl
    else:
        x_sngl = x_fltrd[0:n]
        y_sngl = y_fltrd[0:n]
        return x_sngl, y_sngl
    