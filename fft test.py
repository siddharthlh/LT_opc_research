
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 1000
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y =  np.sin(50.0 * 2.0*np.pi*x) + np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf,np.abs(yf[:N//2]))
#ax.plot(np.abs(yf))
plt.show()
