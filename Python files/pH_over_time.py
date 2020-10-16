#author: Riley Doyle
#date: 10/7/20
#file: pH_over_time
#status: WORKING

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

T = 20 + 273.15 #kelvins
S = 35 #g/kg
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
d = 0.15 #m
y2 = 0.1695 #g HCO3 as CO2 per g algae

Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = - np.log10(K2)
Csat = PCO2*Kh*44*1000 #g/m3

alk0 = 2.5
r_algae = 10

def rates(x,t):
    Caq = x[0]
    HCO3 = x[1]
    H = x[2]
    alpha0 = calc_alpha0(- np.log10(H), pK1, pK2)
    alpha1 = calc_alpha1(- np.log10(H), pK1, pK2)
    alpha2 = calc_alpha2(- np.log10(H), pK1, pK2)
    dCaqdt = -(alpha0/(alpha1+2*alpha2))*y2*r_algae
    dHCO3dt = -(1+(alpha1/(2*alpha2)))*y2*r_algae
    dHdt = -(K1*Caq)/HCO3
    return [dCaqdt, dHCO3dt, dHdt]

H0 = 10**(-8)
Caq0 = Csat
HCO30 = 300


x0 = [Caq0, HCO30, H0]
t = np.linspace(0,4,100) 

x = odeint(rates, x0, t)

Caq = x[:,0]
HCO3 = x[:,1]
H = x[:,2]
pH = -np.log10(H)
plt.xlabel('time (days)')
plt.ylabel('pH')
plt.plot(t, pH)
plt.show()
