#author: Riley Doyle
#date: 8/7/20
#file: monod_simple
#status: WORKING

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

umax = 1.44 #1/day
Ki = 178.7/4.6 #W/m2
Iin = 0
Iend = 401
delI = 1
delta = 1.066
T = 20
Tr = 20
Isteps = np.arange(Iin, Iend, delI)
I = Isteps
u = ((umax)) * (I/(I + Ki))*(delta**(T-Tr))
plt.figure()
plt.plot(I, u)
plt.xlabel('light intensity (W/m$^2$)')
plt.ylabel('specific growth rate (day$^{-1})$')
plt.show()

#Beer Lambert Law
from scipy import integrate
I0 = 13.06 #W/m2
o = 0.175 #m2/g
X = 50 #g/m3
z = np.arange(0, 0.18, 0.01)
I = I0*np.exp(-o*X*z)
I_int = integrate.cumtrapz(I, z, initial=0)
plt.plot(z, I_int)
plt.xlabel('position (cm)')
plt.ylabel('Light Intensity (W m$^{-2})$')
plt.show()

umax = 1.44
I = 186
Ki = 178.7/4.6
delta = 1.066
T = 20
Tr = 20
def kinetics(s,t):
    global umax, X0, Y, Ks
    X = s[0]
    dXdt = ((umax*X))*(I/(I + Ki))*(delta**(T-Tr))
    return [dXdt]

X0 = .4

s0 = [X0]
t = np.linspace(0,4,100) 

s = odeint(kinetics, s0, t)
plt.plot(t, s[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Productivity (g m$^{-2}$ day$^{-1})$')
plt.show()
