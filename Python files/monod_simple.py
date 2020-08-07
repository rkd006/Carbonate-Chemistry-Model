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
Isteps = np.arange(Iin, Iend, delI)
I = Isteps
u = ((umax)) * (I/(I + Ki))
plt.figure()
plt.plot(I, u)
plt.xlabel('light intensity (W/m$^2$)')
plt.ylabel('specific growth rate (day$^{-1})$')
plt.show()

umax = 1#1.44
X = 0
I = 130 #186
Ki = 200 #178.7/4.6
def kinetics(s,t):
    global umax, X0, Y, Ks
    X = s[0]
    dXdt = ((umax*X))*(I/(I + Ki))
    return [dXdt]

X0 = 10

s0 = [X0]
t = np.linspace(0,4,100) 

s = odeint(kinetics, s0, t)
plt.plot(t, s[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Productivity (g m$^{-2}$ day$^{-1})$')
plt.show()
