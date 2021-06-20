#author: Riley Doyle
#date: 12/14/20
#file: CO2_loss_dynamic_CO2Sys
#status: WORKING

from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program_pHTA import *
from calc_alphas import *
from calc_density import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global k1, k2, k3, k4

T = 20 #kelvins
S = 35 #g/kg
P = 10 #(dbar)
t = T*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
d = 0.15 #m

kLa = 0.5 #1/hr
y1 = 2.128 #1.714 (old algae eqn) #g CO2 per g algae
y2 = 0.3395 #0.1695 (old algae eqn) #g HCO3 as CO2 per g algae

Kh = calc_Kh((T+273.15),S)*(den/1000) #mol/L/atm
Csat = PCO2*Kh*44*1000 #g/m3
P = 0.5 #dbars
TP = 10/10**6 #mol/kg SW
TSi = 30/10**6 #mol/kg SW
TA = 2500/10**6
r_algae = 10 #growth rate
pH = 8
#Output Conditions
Tout = 20
Pout = 0.5

CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
K1 = CO2Sys[0]
K2 = CO2Sys[2]
Caq0 = (CO2Sys[49])*(den)
pK1 = - np.log10(K1)
pK2 = - np.log10(K2)

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


Caq0 = Caq0*44
Cin0 = 0
Closs0 = 0 

x0 = [Caq0, Cin0, Closs0]
t = np.linspace(0,4,100) 

x = odeint(rates, x0, t)

Caq = x[:,0]*d
Cdel = x[:,1]
Closs = x[:,2]
plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.axis([0, 3, 0, 70])
plt.show()

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Caq)
plt.show()
