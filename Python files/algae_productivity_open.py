#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity_open
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
plt.figure()
plt.plot(divI, u)
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

B0 = 0.4 #g/m2
b0 = [B0]
t = np.linspace(0,4,100) 
b = odeint(product, b0, t)
plt.plot(t, b[:,0])

plt.xlabel('time')
plt.ylabel('Biomass Productivity (g m$^{-2}$ day$^{-1})$')
plt.show()
