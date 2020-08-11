#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#monod model 
umax = 3.2424
Ki = 13.9136 #W/m2 181.02407
I = 100 #W/m2
def kinetics(s,t):
    X = s[0]
    dXdt = ((umax*I)/(I + Ki))*X
    return [dXdt]

X0 = 0.4 #g/m3
s0 = [X0]
t = np.linspace(0,4,100)
n = np.arange(0, 100, 1) 
s1 = odeint(kinetics, s0, t)
X = s1[:,0]
P = (X[n] - X[n-1])/(t[n] - t[n-1])
avg = np.average(P)
print (avg)

#aiba model
K1 = 182.6
K2 = 0.0975 #17969
umax = 0.9923*24
I = 100 #W/m2
def kinetics(s,t):
    X = s[0]
    dXdt = (umax*I)/(K1 + I + K2*(I**2))*X
    return [dXdt]

X0 = 0.4 #g/m3
s0 = [X0] 
s2 = odeint(kinetics, s0, t)
X = s2[:,0]
P = (X[n] - X[n-1])/(t[n] - t[n-1])
avg = np.average(P)
print (avg)

#boriah model
umax = 3.2424
K = 0.007
Topt = 20 #celcius
I = 50 #W/m2 15.2458
Is = 100
divI = I/Is
T = 20 #celcius
h = np.exp(-K*(T-Topt)**2)
f = divI*np.exp(1-divI)
u = umax*f*h

def product(b,t):
    B = b[0]
    dBdt = u*B
    return [dBdt]

B0 = 0.4 #g/m3
b0 = [B0]
b = odeint(product, b0, t)
B = b[:,0]
P = (B[n] - B[n-1])/(t[n] - t[n-1])
avg = np.average(P)
print (avg)

plt.plot(t, s1[:,0])
plt.plot(t, s2[:,0])
plt.plot(t, b[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Concentration (g m$^{-3}$)')
plt.axis([0, 3, 0, 2000])
plt.legend(['Monod', 'Aiba', 'Boriah'], frameon=False)
plt.show()