#author: Riley Doyle
#date: 8/7/20
#file: specific_growth
#status: WORKING

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#spirulina platensis

#monod model 
umax = 3.2424
Ki = 13.9136
Iin = 0
Iend = 101
delI = 1
Isteps = np.arange(Iin, Iend, delI)
I = Isteps
u = ((umax)) * (I/(I + Ki))

#modified aiba model
K1 = (200.1/24)
K2 = (0.1110/24)
u2 = (I)/(K1 + K2*(I**2))

#Bannister model
m = 0.9868 
K1 = 14.4256
u3 = (umax*I)/((K1**m + I**m)**(1/m))

#aiba model
K1 = 182.6
K2 = 0.0975
umax = 0.9923*24
u4 = (umax*I)/(K1 + I + K2*(I**2))

#open pond
umax = 3.2424
Is = 50
T = 25
K = 0.007
Topt = 20
f = I/Is*np.exp(1-I/Is)
h = np.exp(-K*(T-Topt)**2)
u5 = umax*f*h

plt.figure()
plt.plot(I, u)
plt.plot(I, u2)
plt.plot (I, u3)
plt.plot(I, u4)
plt.plot (I, u5)
plt.xlabel('light intensity (W/m$^2$)')
plt.ylabel('specific growth rate (day$^{-1})$')
plt.legend(['Monod model', 'Modified Aiba Model', 'Bannister Model', 'Aiba model', 'Boriah model'], frameon=False)
plt.axis([0, 100, 0, 3])
plt.show()

#Beer Lambert Law
I0 = 100 #W/m2
o = 0.175 #m2/g
X = 50 #g/m3
z = np.arange(0, 0.15, 0.01)
I = I0/np.exp(o*X*z)
plt.plot(z, I)
plt.xlabel('position (cm)')
plt.ylabel('Light Intensity (W m$^{-2})$')
plt.show()
