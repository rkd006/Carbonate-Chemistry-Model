#author: Riley Doyle
#date: 10/7/20
#file: pH_over_time
#status: WORKING

from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Stiochiometric ratios
CO2coef = 452
HCO3coef = 52
algaecoef = 4

#Molecular Weights
algaeMW = 2336 #g/mol
CO2MW = 44 #g/mol
HCO3MW = 61 #g/mol

#Given
T = 20 + 273.15
S = 35
CO2g = 0.006 #M
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
K2 = calc_K2(T, S)*(den/1000) #mol/L
y1 = CO2coef/algaecoef
y2 = HCO3coef/algaecoef
CO2g = 0.006 #M
CO2aq = Kh*CO2g
efficiency = 95
r_algae = (1/1000)/algaeMW #mol/L/hr
CO2 = CO2aq*(efficiency/100)

def carbon(x,t):
        HCO3 = x[0]
        CO2 = x[1]
        dHCO3dt = y2*r_algae
        dCO2dt = -y1*r_algae
        return [dHCO3dt, dCO2dt]
    
HCO30 = 0.02 #mol/L
CO20 = CO2aq*(efficiency/100) #mol/L
    
x0 = [HCO30, CO20]
t = np.linspace(0,4, 101) 
    
x = odeint(carbon, x0, t)
    
HCO3 = x[:,0]
CO2 = x[:,1]

plt.xlabel('time (hrs)')
plt.ylabel('HCO$_3$$^-$ (g/m$^3$)')
plt.plot(t, HCO3)
plt.show()

plt.plot(t, CO2)
plt.xlabel('time (hrs)')
plt.ylabel('CO$_2$ (g/m$^3$)')
plt.show()

H = (CO2*K1)/HCO3 #M
pH = -np.log10(H)
plt.plot(t, pH)
plt.xlabel('time (hrs)')
plt.ylabel('pH')
plt.show()

umax = 3.2424 #1/day
I = 100 #W/m2
kd = 0 #1/day
K = 135 #g/m2
Ki = 13.9136 #W/m2
def carbongrowth(x,t):
    X = x[0]
    P = x[1]
    HCO3 = x[2]
    CO2 = x[3]
    dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
    dPdt = dXdt
    dHCO3dt = y2*P
    dCO2dt = -y1*P
    return [dXdt, dPdt, dHCO3dt, dCO2dt]

X0 = (0.1/1000)/algaeMW
P0 = 0
HCO30 = 0.02 #mol/L
CO20 = CO2aq*(efficiency/100) #mol/L

x0 = [X0, P0, HCO30, CO20]
t = np.linspace(0,4, 101) 

x = odeint(carbongrowth, x0, t)

X = x[:,0]
P = x[:,1]
HCO3 = x[:,2]
CO2 = x[:,3]

H2 = (CO2*K1)/HCO3 #M
pH2 = -np.log10(H2)
plt.plot(t, pH2)
plt.xlabel('time (hrs)')
plt.ylabel('pH')
plt.show()