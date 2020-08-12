#author: Riley Doyle
#date: 8/8/20
#file: CO2_loss_dynamic_monod
#status: WORKING

#monod model

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global k1, k2, k3, k4

T = 20 + 273.15 #kelvins
S = 35 #g/kg
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
d = 0.15 #m
umax = 3.2424 #1/day
I = 30 #W/m2
Ki = 13.9136 #178.7/4.6 #W/m2

kLa = 3 #1/hr
y1 = 1.714 #g CO2 per g algae
y2 = 0.1695 #g HCO3 as CO2 per g algae

Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = - np.log10(K2)

Csat = PCO2*Kh*44*1000 #g/m3
alk0 = 2.5 #eq/m3
pH = 8

alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)

OH = 10**-(14-pH)*(10**3)
H = (10**(-pH))*(10**3)

k1 = alpha0/(alpha1 + 2*alpha2)*y2
k2 = (kLa*d*24)
k3 = (kLa*d*24)*Csat
k4 = (y1 + y2)
k5 = y2*(alpha1 + 2*alpha2)
k6 = umax*(I/(I + Ki))

def rate_kinetics(x,t):
    global k1, k2, k3, k4, u
    X = x[0]
    Caq = x[1]
    Cdel = x[2]
    Closs = x[3]
    dXdt = k6*(X)
    dCaqdt = -k1*dXdt
    dCdeldt = ((k2 *Caq) - k3) + (k4*dXdt - k5*dXdt)
    dClossdt = (k2 *Caq) - k3
    return [dXdt, dCaqdt, dCdeldt, dClossdt]

X0 = 0.006 #g/m2
Caq0 = ((alk0 - OH + H)*alpha0/(alpha1 + 2*alpha2))*44 #g/m3
Cin0 = 0
Closs0 = 0 

x0 = [X0, Caq0, Cin0, Closs0]
t = np.linspace(0.01,4,100) 
n = np.arange(0, 100, 1)
x = odeint(rate_kinetics, x0, t)
X = x[:,0]
Caq = x[:,1]
Cdel = x[:,2]
Closs = x[:,3]

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.axis([0, 4, 0, 75])
plt.show()

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Caq)
plt.show()