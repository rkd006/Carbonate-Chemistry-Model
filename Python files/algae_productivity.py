#author: Riley Doyle
#date: 8/10/20
#file: algae_productivity
#status: WORKING

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#monod model 
umax = 1.44#3.2424 # 1/day
Ki = 178.7/4.6#13.9136*4 #W/m2
I = 140 #W/m2
def kinetics(s,t):
    global umax, X0, Y, Ks
    X = s[0]
    dXdt = ((umax*I)/(I + Ki))*X
    return [dXdt]

X0 = 0.4 #g/m2

s0 = [X0]
t = np.linspace(0,4,100) 

s = odeint(kinetics, s0, t)
plt.plot(t, s[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Productivity (g m$^{-2}$ day$^{-1})$')
plt.show()

#modified aiba model
K1 = 200.1/24
K2 = 0.1110/24
I = 140 #W/m2
def kinetics(s,t):
    global umax, X0, Y, Ks
    X = s[0]
    dXdt = (I)/(K1 + K2*(I**2))*X
    return [dXdt]

X0 = 0.4 #g/m2

s0 = [X0]
t = np.linspace(0,4,100) 

s = odeint(kinetics, s0, t)
plt.plot(t, s[:,0])
plt.xlabel('time')
plt.ylabel('Biomass Productivity (g m$^{-2}$ day$^{-1})$')
plt.show()