#author: Riley Doyle
#date: 7/15/20
#file: CO2_loss_range_kLa
#status: working 

#clear all
from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss_kLa import *
from calc_density import *
import numpy as np
import matplotlib.pyplot as plt

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
alk = 2.5
pHin = 6
pHend = 8.2
delpH = 0.1
d = 0.15
kLain = 0.1
kLaend = 0.9
delkLa = 0.4
colormap = np.array(['b', 'r'])
y = calc_CO2_loss_kLa(pK1, pK2, Kh, alk, d, colormap, PCO2, pHin, pHend, delpH, kLain, kLaend, delkLa)

kLain = 1.5
kLaend = 4.5
delkLa = 1.5
colormap = np.array(['c','y'])
y = calc_CO2_loss_kLa(pK1, pK2, Kh, alk, d, colormap, PCO2, pHin, pHend, delpH, kLain, kLaend, delkLa)

plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['kLa = 0.1 1/hr', 'kLa = 0.5 1/hr', 'kLa = 1.5 1/hr', 'kLa = 3 1/hr'], frameon=False)
plt.show()

