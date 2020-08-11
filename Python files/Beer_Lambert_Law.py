#author: Riley Doyle
#date: 8/11/20
#file: Beer_Lambert_Law
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt

#Beer Lambert Law
#constant concentration 
I0 = 100 #W/m2
o = 0.175 #m2/g
X = 50 #g/m3
z = np.arange(0, 0.15, 0.01)
I = I0/np.exp(o*X*z)

X = 100 #g/m3
I2 = I0/np.exp(o*X*z)

X = 150 #g/m3
I3 = I0/np.exp(o*X*z)

plt.plot(z, I)
plt.plot(z, I2)
plt.plot(z, I3)
plt.xlabel('position (cm)')
plt.ylabel('Light Intensity (W m$^{-2})$')
plt.legend(['X = 50 g/m$^3$', 'X = 100 g/m$^3$', 'X = 150 g/m$^3$'], frameon=False)
plt.axis([0, 0.15, 0, 100])
plt.show()

#changing concentration
