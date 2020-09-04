#author: Riley Doyle
#date: 9/3/20
#file: mean_value_theorem
#status: NOT WORKING

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#define variables
kd = 0 #1/day #not added yet
K = 135 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
X0 = 0.1 #g/m2
t = np.linspace(0, 3, 100)
Iin = 100 #W/m2
Iend = 500
delI = 100
Isteps = np.arange(Iin, Iend, delI)
for p in Isteps:
    C = ((umax*p)/(p + Ki))-kd
    #function for biomass density
    for i in t:
        X = (X0*K)/(X0 + (K - X0)*np.exp(-(C*t)))
    plt.plot(t,X)
    plt.axis([0, 3, 0, 135])
    plt.legend(['I = 100 W/m$^{2}$', 'I = 200 W/m$^{2}$', 'I = 300 W/m$^{2}$', 'I = 400 W/m$^{2}$'], frameon=False)
    plt.xlabel('time (days)')
    plt.ylabel('Biomass Density (g m$^{-2}$)')
    
    X = lambda t:(X0*K)/(X0 + (K - X0)*np.exp(-(C*t)))
    #limits
    a = 0
    b = 3
    
    integral = integrate.quad(X, a, b)
    meanbiomass = (1/(b - a))*integral[0]
    meanproductivity = meanbiomass/(b - a)
    print (meanproductivity)