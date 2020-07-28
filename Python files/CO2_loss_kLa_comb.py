#author: Riley Doyle
#date: 7/15/20
#file: CO2_loss_kLa_comb
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
import numpy as np
import matplotlib.pyplot as plt

T = 20 + 273.15
S = 35
K1 = calc_K1(T,S)
pK1 = -np.log10(K1)
K2 = calc_K2(T,S)
pK2 = -np.log10(K2)
CO2sat = 0.012716352
alkin = 2
alkend = 37
delalk = 5
pHin = 6.5
pHend = 8.2
delpH = 0.1
d = 0.15
kLain = 0.1
kLaend = 0.9
delkLa = 0.4
kLasteps = np.arange(kLain, kLaend, delkLa)
kLa = kLain
for p in kLasteps:
    y = calc_CO2_loss(pK1, pK2, kLa, d, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.ylabel('$CO_2$ loss to the atmosphere (g $m^{-2}$ $day^{-1})$')
    plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L', 'alk = 27 meq/L', 'alk = 32 meq/L'])
    plt.axis([6.5, 8.2, 0, 4000])
    plt.figure()
    kLa = kLa + delkLa
    
kLain = 1.5
kLaend = 4.5
delkLa = 1.5
kLasteps = np.arange(kLain, kLaend, delkLa)
kLa = kLain
for c in kLasteps:
    y = calc_CO2_loss(pK1, pK2, kLa, d, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.ylabel('$CO_2$ loss to the atmosphere (g $m^{-2}$ $day^{-1})$')
    plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L', 'alk = 27 meq/L', 'alk = 32 meq/L'])
    plt.axis([6.5, 8.2, 0, 4000])
    plt.figure()
    kLa = kLa + delkLa
