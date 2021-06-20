#author: Riley Doyle
#date: 8/22/20
#file: algae_productivity_monod
#status: WORKING

#clear all
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

d = 0.15 #m
kd = 0 #1/day #not added yet
K = 135 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
Iin = 100 #W/m2
Iend = 500
delI = 100
Isteps = np.arange(Iin, Iend, delI)
for p in Isteps:
    def kinetics(s,t):
        X = s[0]
        dXdt = (((umax*p)/(p + Ki))-kd)*(1-(X/K))*X
        return [dXdt]
    
    X0 = 0.1 #g/m2
    s0 = [X0]
    t = np.linspace(0,3,100)
    n = np.arange(0, 100, 1) 
    s1 = odeint(kinetics, s0, t)
    X = s1[:,0]
    
    P = np.zeros((100,1))
    for i in n:
        P[i] = X[i]/t[i]
        
    plt.plot(t, P)
    plt.xlabel('time (days)')
    plt.ylabel('Productivity (g m$^{-2}$ day$^{-1}$)')
    plt.legend(['I = 100 W/m$^{2}$', 'I = 200 W/m$^{2}$', 'I = 300 W/m$^{2}$', 'I = 400 W/m$^{2}$'], frameon=False)
    plt.axis([0.3, 3, 0, 45])
plt.show()