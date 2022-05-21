import tkinter as tk
from tkinter import filedialog
import numpy as np
from Functions import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



# Prompt user for file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Three Column CSV", "*.csv")])
print(file_path)

# Load Data (assumes three column array)
t,x_bf,y_bf = np.genfromtxt(file_path, delimiter=',', unpack=True)

fc =24.97  #1x in Hz (input)
lc = 24.95 #low cuttoff frequency 
hc=25      #high cuttoff frequency 

fs, dt, df, tw = signal_stats(t)

#butter worth band pass to only plot for 1X frequency component 
#using high and low cuttoff frequencies to confine the 1x frequency 
x_fltrd = oneX_filter(x_bf, lc, hc, fs, fc)
y_fltrd = oneX_filter(y_bf, lc, hc, fs, fc)

# Filtring for a single orbit
x_sngl, y_sngl = single_orbit(x_fltrd, y_fltrd, fs, fc)

#Plotting
fig, (ax0,ax1,ax2) = plt.subplots(nrows=1, ncols=3, figsize=(12,5), sharex=True)
fig.suptitle('Orbit Analysis')

#data before filtering
ax0.set_title('Orbit Before Filtering')
ax0.plot(x_bf, y_bf, linewidth=1, alpha=0.7)

#maintain equal aspect between x and y
ax0.set_aspect('equal', adjustable='box')

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax0.spines['left'].set_position('center')
ax0.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax0.spines['right'].set_color('none')
ax0.spines['top'].set_color('none')

# Showing x and y ticks
ax0.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax0.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax0.axes.xaxis.set_ticklabels([])
ax0.axes.yaxis.set_ticklabels([])

#data after filtering
ax1.set_title('Orbit After Filtering')
ax1.plot(x_fltrd, y_fltrd, linewidth=1, alpha=0.7)

#maintain equal aspect between x and y
ax1.set_aspect('equal', adjustable='box')


# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

# Showing x and y ticks
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])

#single orbit
ax2.set_title('Single Orbit')
ax2.plot(x_sngl, y_sngl, linewidth=1, alpha=0.7)

#maintain equal aspect between x and y
ax2.set_aspect('equal', adjustable='box')

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

# Showing x and y ticks
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.axes.xaxis.set_ticklabels([])
ax2.axes.yaxis.set_ticklabels([])

plt.show()

