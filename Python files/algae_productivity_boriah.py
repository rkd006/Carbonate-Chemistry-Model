#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity_boriah
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

K = 0.007
Topt = 20 #celcius
Tin = 5
Tend = 30
delT = 1
Tsteps = np.arange(Tin, Tend, delT)
T = Tsteps
h = np.exp(-K*(T-Topt)**2)

plt.plot(T, h)
plt.xlabel('Temperature')
plt.ylabel('h(t)')
plt.show()

divIin = 0 
divIend = 1
deldivI = 0.01
umax = 1.44
divIsteps = np.arange(divIin, divIend, deldivI)
divI = divIsteps
f = divI*np.exp(1-divI)
u = umax*f
plt.plot(divI, f)
plt.xlabel('I/Is')
plt.ylabel('f(I)')
plt.show()

I = 10 #W/m2
Is = 20
divI = I/Is
T = 25 #celcius
umax = 1.44 #1/day
h = np.exp(-K*(T-Topt)**2)
f = divI*np.exp(1-divI)
u = umax*f*h


def product(b,t):
    B = b[0]
    dBdt = u*B
    return [dBdt]

B0 = 0.4 #g/m3
b0 = [B0]
t = np.linspace(0,4,100) 
b = odeint(product, b0, t)
X = b[:,0]
n = np.arange(0, 100, 1)
P = (X[n] - X[n-1])/(t[n] - t[n-1])
avg = np.average(P)
print (avg)

plt.plot(t, b[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Concentration (g m$^{-3}$)')
plt.show()

#population dynamics model
C = 1000
def product(b,t):
    B = b[0]
    dBdt = u*(1-(B/C))*B
    return [dBdt]

B0 = 1 #g/m3
b0 = [B0]
t = np.linspace(0,4,400) 
b = odeint(product, b0, t)
X = b[:,0]
n = np.arange(0, 400, 1)
P = (X[n] - X[n-1])/(t[n] - t[n-1])
avg = np.average(P)
print (avg)

plt.plot(t, b[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Concentration (g m$^{-3}$)') 
plt.show()

