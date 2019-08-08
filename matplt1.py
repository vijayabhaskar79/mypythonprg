import matplotlib.pyplot as plt
import numpy as np
tau, n = 10, 1024 # 10 second signal with 1024 points
T = tau/n # sampling interval
t = np.arange(n)*T
a = 4 # amplitude
x = a*np.sin(40*np.pi*t) # 20 Hz sine with amplitude a
# New correct behavior: Amplitude at 20 Hz is a/2
plt.magnitude_spectrum(x, Fs=1/T, sides='onesided', scale='linear')
# Original behavior: Amplitude at 20 Hz is (a/2)*(n/2) for a Hanning window
w = np.hanning(n) # default window is a Hanning window
plt.magnitude_spectrum(x*np.sum(w), Fs=1/T, sides='onesided', scale='linear')
plt.show()