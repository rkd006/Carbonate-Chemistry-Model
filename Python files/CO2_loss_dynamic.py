#author: Riley Doyle
#date: 7/15/20
#file: CO2_loss_dynamic
#status: WORKING

from calc_Ks import *
from calc_alphas import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global k1, k2, k3, k4

T = 20 + 273.15 #kelvins
S = 35 #g/kg
PCO2 = 0.00040 #atm
d = 0.15 #m

kLa = 0.5 #1/hr
y1 = 1.714 #g CO2 per g algae
y2 = 0.1695 #g HCO3 as CO2 per g algae

Kh = calc_Kh(T,S)
K1 = calc_K1(T, S)
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)
pK2 = - np.log10(K2)

Csat = PCO2*Kh*44 #g/m3

alk0 = 2.5
r_algae = 10
pH = 8

alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)

OH = 10**-(14-pH)*(10**3)
H = (10**(-pH))*(10**3)

k1 = alpha0/(alpha1 + 2*alpha2)*y2*r_algae
k2 = (kLa*d*24)
k3 = (kLa*d*24)*Csat
k4 = (y1 + y2)*r_algae - y2*r_algae*(alpha1 + 2*alpha2)

def rates(x,t):
    global k1, k2, k3, k4
    Caq = x[0]
    Cdel = x[1]
    Closs = x[2]
    dCaqdt = -k1
    dCdeldt = ((k2 *Caq) - k3) + k4
    dClossdt = (k2 *Caq) - k3
    return [dCaqdt, dCdeldt, dClossdt]


Caq0 = ((alk0 - OH + H)*alpha0/(alpha1 + 2*alpha2))*44
Cin0 = 0
Closs0 = 0 

x0 = [Caq0, Cin0, Closs0]
t = np.linspace(0,4,100) 

x = odeint(rates, x0, t)

Caq = x[:,0]
Cdel = x[:,1]
Closs = x[:,2]
plt.xlabel('time (days)')
plt.ylabel('$CO_2$ (g/$m^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['$CO_2$ supply required', '$CO_2$ loss to atmosphere'])
plt.show()

plt.xlabel('time (days)')
plt.ylabel('$CO_2$ (g/$m^2$)')
plt.plot(t,Caq)
plt.show()

