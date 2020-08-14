#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#monod model 
d = 0.15 #m
kd = 0.1 #1/day
K = 90 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
I = 40 #W/m2
def kinetics(s,t):
    X = s[0]
    dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
    return [dXdt]

X0 = 0.006 #g/m2
s0 = [X0]
t = np.linspace(0,10,1000)
n = np.arange(0, 100, 1) 
s1 = odeint(kinetics, s0, t)
X = s1[:,0]

#modified aiba model
K1 = (200.1/24)
K2 = (0.1110/24)
u2 = (I)/(K1 + K2*(I**2))
def kinetics(s,t):
    X = s[0]
    dXdt = (u2-kd)*(1-(X/K))*X
    return [dXdt]

s0 = [X0] 
s2 = odeint(kinetics, s0, t)
X = s2[:,0]

#boriah model
umax = 3.2424
Kt = 0.007
Topt = 20 #celcius
Is = 80
divI = I/Is
T = 20 #celcius
h = np.exp(-Kt*(T-Topt)**2)
f = divI*np.exp(1-divI)
u = umax*f*h

def product(b,t):
    X = b[0]
    dBdt = (u-kd)*(1-(X/K))*X
    return [dBdt]

b0 = [X0]
b = odeint(product, b0, t)
B = b[:,0]


plt.plot(t, s1[:,0])
plt.plot(t, s2[:,0])
plt.plot(t, b[:,0])
plt.axis([0, 6, 0, 100])
plt.legend(['Monod', 'Modified Aiba', 'Boriah'], frameon=False)
plt.xlabel('time (days)')
plt.ylabel('Biomass Density (g m$^{-2}$)')
plt.show()