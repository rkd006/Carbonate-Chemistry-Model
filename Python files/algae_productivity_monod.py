#author: Riley Doyle
#date: 8/22/20
#file: algae_productivity_monod
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

d = 0.15 #m
kd = 0.3 #1/day
K = 500 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
Iin = 40 #W/m2
Iend = 80
delI = 10
Isteps = np.arange(Iin, Iend, delI)
for p in Isteps:
    def kinetics(s,t):
        X = s[0]
        dXdt = (((umax*p)/(p + Ki))-kd)*(1-(X/K))*X
        return [dXdt]
    
    X0 = 0.06 #g/m2
    s0 = [X0]
    t = np.linspace(0,4,100)
    n = np.arange(0, 100, 1) 
    s1 = odeint(kinetics, s0, t)
    X = s1[:,0]
    
    P1 = np.zeros((100,1))
    for i in n:
        P1[i] = s1[i]/t[i]
    Pavg1 = (P1[99] - P1[1])/(t[99] - t[1])
    print (Pavg1)

    plt.plot(t, P1)
    plt.xlabel('time (days)')
    plt.ylabel('Productivity (g m$^{-2}$ day$^{-1}$)')
    plt.legend(['I = 40 W/m$^{2}$', 'I = 50 W/m$^{2}$', 'I = 60 W/m$^{2}$', 'I = 70 W/m$^{2}$'], frameon=False)
    plt.axis([0.3, 4, 0, 80])
plt.show()