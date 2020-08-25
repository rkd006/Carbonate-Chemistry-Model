#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#from Lee et. al. 2015 and Lee et. al. 1986
#Biomass Density
#monod model 
d = 0.15 #m
kd = 0.3 #1/day
K = 120 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
I = 100 #W/m2
def kinetics(s,t):
    X = s[0]
    dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
    return [dXdt]

X0 = 0.04 #g/m2
s0 = [X0]
t = np.linspace(0,4,100)
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
plt.axis([0, 4, 0, 120])
plt.legend(['Monod', 'Modified Aiba', 'Boriah'], frameon=False)
plt.xlabel('time (days)')
plt.ylabel('Biomass Density (g m$^{-2}$)')
plt.show()

#calculate areal productivity

#Monod
P1 = np.zeros((100,1))
for i in n:
    P1[i] = s1[i]/t[i]
Pavg1 = (s1[99] - s1[1])/(t[99] - t[1])
print (Pavg1)

#Aiba
P2 = np.zeros((100,1))
for i in n:
    P2[i] = s2[i]/t[i]
Pavg2 = (s2[99] - s2[1])/(t[99] - t[1])
print (Pavg2)

#Boriah
P3 = np.zeros((100,1))
for i in n:
    P3[i] = b[i]/t[i]
Pavg2 = (b[99] - b[1])/(t[99] - t[1])
print (Pavg2)

plt.plot(t, P1)
plt.plot(t, P2)
plt.plot(t, P3)
plt.xlabel('time (days)')
plt.ylabel('Productivity (g m$^{-2}$ day$^{-1}$)')
plt.axis([0.3, 3, 0, 30])
plt.legend(['Monod', 'Modified Aiba', 'Boriah'], frameon=False)
plt.show()