#author: Riley Doyle
#date: 7/16/20
#file: CO2_loss_kLa_simple
#status: working

#clear all
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import matplotlib.pyplot as plt
from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss_kLa import *
from calc_CO2_loss_alk import *
from calc_density import *

T = 20 + 273.15
S = 35
Tc = 20; #celcius
P = 10; #(dbar)
t = Tc*1.00024;
p = P/10;
den = calc_density(S, t, p); #(kg/m3)
K1 = calc_K1(T,S)*(den/1000) #mol/L
pK1 = -np.log10(K1)
K2 = calc_K2(T,S)*(den/1000) #mol/L
pK2 = -np.log10(K2)
PCO2 = 0.000416
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
d = 0.15
kLain = 0.1
kLaend = 2.1
alk = 2.5
pHin = 6.5
pHend = 8.5
delpH = 0.1
delkLa = 0.4
y = calc_CO2_loss_kLa(pK1, pK2, Kh, alk, d, PCO2, pHin, pHend, delpH, kLain, kLaend, delkLa)
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['kLa = 0.1 hr$^{-1}$', 'kLa = 0.5 hr$^{-1}$', 'kLa = 0.9 hr$^{-1}$', 
            'kLa = 1.3 hr$^{-1}$', 'kLa = 1.7 hr$^{-1}$'])
plt.show()
pH = 8
alkin = 2
alkend = 32
delalk = 2

y = calc_CO2_loss_alk (pK1, pK2, pH, Kh, d, PCO2, alkin, alkend, delalk, kLain, kLaend, delkLa)
plt.legend(['kLa = 0.1 hr$^{-1}$', 'kLa = 0.5 hr$^{-1}$', 'kLa = 0.9 hr$^{-1}$', 
            'kLa = 1.3 hr$^{-1}$', 'kLa = 1.7 hr$^{-1}$'])
plt.xlabel('alkalinity')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')