import pandas as pd
#from openpyxl import load_workbook
import scipy.fftpack
import json
import numpy as np
import math
from matplotlib import pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

df = pd.read_excel('accelerometer data.xlsx', sheet_name='accdata')
iw = np.array([])
#print(df)
k3  = df.values
for k in k3:
    iw  = np.append(iw,k)


n = k3.size
timestep = 1/12000
xf = np.linspace(0.0, 1.0/(2.0*timestep), n/2)
yf = scipy.fftpack.fft(iw)
fig, ax = plt.subplots()
ax.plot(xf,(2/n)*abs(yf[:n//2]))
plt.show()

nval = find_nearest(xf,500)
print(nval)
nwhere  = np.where(xf == nval )
print(nwhere)
print(yf[nwhere])
print(yf.size)

