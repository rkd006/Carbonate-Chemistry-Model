#author: Riley Doyle
#date: 6/6/21
#file: CO2_loss_dynamic_monod_CO2Sys
#status: WORKING

#monod model with CO2Sys

#clear all
from IPython import get_ipython
get_ipython().magic('reset -sf')

#get functions
from calc_Ks import *
from calc_alphas import *
from calc_density import *
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program_TApCO2 import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from inputpCO2_CO2loss import *

#input conditions
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
I = 100 #W/m2
kd = 0 #1/day
K = 200 #g/m2
Ki = 13.9136 #W/m2

kLa = 3 #1/hr
y1 = 1.714 #g CO2 per g algae
y2 = 0.1695 #g HCO3 as CO2 per g algae

P = 0.5 #dbars
TP = 10/10**6 #mol/kg SW
TSi = 30/10**6 #mol/kg SW
TA = 2500/10**6
#Output Conditions
Tout = 20
Pout = 0.5

Kh = calc_Kh((T),S)*(den/1000) #mol/L/atm
Csat = PCO2*Kh*44*1000 #g/m3

#calculate
#pCO2 = 50000 uatm roughly equals pH = 6
pCO2 = 50000/10**6
CO2output = inputpCO2_CO2loss(Tc, S, P, TP, TSi, TA, pCO2, Tout, Pout, den, kLa, d, y1, y2, Csat, umax, I, kd, K, Ki)
t = CO2output[0]
Cdel = CO2output[4]
Closs = CO2output[5]

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.show()

#pCO2 = 5000 uatm roughly equals pH = 7
pCO2 = 5000/10**6
CO2output = inputpCO2_CO2loss(Tc, S, P, TP, TSi, TA, pCO2, Tout, Pout, den, kLa, d, y1, y2, Csat, umax, I, kd, K, Ki)
t = CO2output[0]
Cdel = CO2output[4]
Closs = CO2output[5]

#pCO2 = 500 uatm roughly equals pH = 8
plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.show()

pCO2 = 500/10**6
CO2output = inputpCO2_CO2loss(Tc, S, P, TP, TSi, TA, pCO2, Tout, Pout, den, kLa, d, y1, y2, Csat, umax, I, kd, K, Ki)
t = CO2output[0]
Cdel = CO2output[4]
Closs = CO2output[5]

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.show()

