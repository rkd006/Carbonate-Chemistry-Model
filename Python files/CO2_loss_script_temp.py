#author: Riley Doyle
#date: 7/28/20
#file: CO2_loss_script_temp
#status: working 

#clear all
from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
from calc_density import *
import numpy as np
import matplotlib.pyplot as plt
from calc_CO2_loss_temp import *

#figures with different alkalinities
T = 10 + 273.15
while T <= 30 + 273.15:
    S = 35
    Tc = T - 273.15; #celcius
    P = 10; #(dbar)
    t = Tc*1.00024;
    p = P/10;
    den = calc_density(S, t, p); #(kg/m3)
    K1 = calc_K1(T,S)*(den/1000) #mol/L
    pK1 = -np.log10(K1)
    K2 = calc_K2(T,S)*(den/1000) #mol/L
    pK2 = -np.log10(K2)
    Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
    PCO2 = 0.000416
    alkin = 2
    alkend = 27
    delalk = 5
    pHin = 6
    pHend = 8.2
    delpH = 0.1
    d = 0.15
    kLa = 0.5*(1.024**((T-273.15)-20))
    y = calc_CO2_loss(pK1, pK2, Kh, kLa, d, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
    plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L'], frameon=False)
    plt.figure()
    T += 10

#figure with different temperatures
Tin = 10 + 273.15
Tend = 70 + 273.15
delT = 20
S = 35
PCO2 = 0.000416
alk = 2.5
pHin = 6
pHend = 8.5
delpH = 0.1
d = 0.15
y =calc_CO2_loss_temp (PCO2, alk, d, pHin, pHend, delpH, S, Tin, Tend, delT)
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['T= 10 $^o$C', 'T= 30 $^o$C', 'T= 50 $^o$C'])
plt.axis([6, 8.3,0,200])
plt.show()