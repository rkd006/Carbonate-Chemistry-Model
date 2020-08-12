#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#monod model 
d = 0.15 #m
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
I = 30 #W/m2
def kinetics(s,t):
    X = s[0]
    dXdt = ((umax*I)/(I + Ki))*X
    return [dXdt]

X0 = 0.006 #g/m3
s0 = [X0]
t = np.linspace(0,4,100)
n = np.arange(0, 100, 1) 
s1 = odeint(kinetics, s0, t)
X = s1[:,0]

#aiba model
K1 = 182.6
K2 = 0.0975 
umax = 0.9923*24
def kinetics(s,t):
    X = s[0]
    dXdt = (umax*I)/(K1 + I + K2*(I**2))*X
    return [dXdt]

s0 = [X0] 
s2 = odeint(kinetics, s0, t)
X = s2[:,0]

#boriah model
umax = 3.2424
K = 0.007
Topt = 20 #celcius
Is = 80
divI = I/Is
T = 20 #celcius
h = np.exp(-K*(T-Topt)**2)
f = divI*np.exp(1-divI)
u = umax*f*h

def product(b,t):
    X = b[0]
    dBdt = u*X
    return [dBdt]

b0 = [X0]
b = odeint(product, b0, t)
B = b[:,0]


plt.plot(t, s1[:,0])
plt.plot(t, s2[:,0])
plt.plot(t, b[:,0])
plt.axis([0, 4, 0, 80])
plt.legend(['Monod', 'Aiba', 'Boriah'], frameon=False)
plt.xlabel('time')
plt.ylabel('Biomass Density (g m$^{-2}$)')
plt.show()