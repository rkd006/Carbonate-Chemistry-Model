#author: Riley Doyle
#date: 7/10/20
#file: CO2_loss_script
#status: working

#clear all
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
from calc_density import *
from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
import matplotlib.pyplot as plt

T = 20 + 273.15 #kelvins
S = 35 #g/kg
Tc = 20; #celcius
P = 10; #(dbar)
t = Tc*1.00024;
p = P/10;
den = calc_density(S, t, p); #(kg/m3)
K1 = calc_K1(T,S)*(den/1000) #mol/L
pK1 = -np.log10(K1)
K2 = calc_K2(T,S)*(den/1000)#mol/L
pK2 = -np.log10(K2)
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
PCO2 = 0.000416
kLa = 0.5 #1/hr
pHin = 6
pHend = 8.5
delpH = 0.1
d = 0.15
alkin = 2 #meq/L or eq/m3
alkend = 37
delalk = 5

y = calc_CO2_loss(pK1, pK2, Kh, kLa, d, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)

plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L', 'alk = 27 meq/L', 'alk = 32 meq/L'], frameon=False)
plt.show()
