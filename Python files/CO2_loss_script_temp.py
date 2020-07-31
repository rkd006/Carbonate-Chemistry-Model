#author: Riley Doyle
#date: 7/28/20
#file: CO2_loss_script_temp
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
import numpy as np
import matplotlib.pyplot as plt
from calc_CO2_loss_temp import *

#figures with different alkalinities
T = 10 + 273.15
while T <= 30 + 273.15:
    S = 35
    K1 = calc_K1(T,S)
    pK1 = -np.log10(K1)
    K2 = calc_K2(T,S)
    pK2 = -np.log10(K2)
    Kh = calc_Kh(T,S)
    PCO2 = 0.000416
    CO2sat = PCO2*Kh #mole/m3
    print (CO2sat)
    alkin = 2
    alkend = 27
    delalk = 5
    pHin = 6
    pHend = 8.2
    delpH = 0.1
    d = 0.15
    kLa = 0.5
    y = calc_CO2_loss(pK1, pK2, kLa, d, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
    plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L'], frameon=False)
    plt.figure()
    T += 10

#figure with different temperatures
Tin = 10 + 273.15
Tend = 40 + 273.15
delT = 10
S = 35
PCO2 = 0.000416
alk = 2.5
pHin = 6
pHend = 8.2
delpH = 0.1
d = 0.15
kLa = 0.5
y = calc_CO2_loss_temp (PCO2, alk, d, CO2sat, pHin, pHend, delpH, kLa, S, Tin, Tend, delT)
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['T = 10 $^o$C', 'T = 20 $^o$C', 'T = 30 $^o$C'], frameon=False)
plt.show()