#author: Riley Doyle
#date: 7/15/20
#file: CO2_loss_range_kLa
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss_kLa import *
import numpy as np
import matplotlib.pyplot as plt

T = 20 + 273.15
S = 35
K1 = calc_K1(T,S)
pK1 = -np.log10(K1)
K2 = calc_K2(T,S)
pK2 = -np.log10(K2)
CO2sat = 0.012716352
alk = 2.5
pHin = 6.5
pHend = 8.2
delpH = 0.1
d = 0.15
kLain = 0.1
kLaend = 0.9
delkLa = 0.4

y = calc_CO2_loss_kLa(pK1, pK2, alk, d, CO2sat, pHin, pHend, delpH, kLain, kLaend, delkLa)

kLain = 1.5
kLaend = 4.5
delkLa = 1.5
y = calc_CO2_loss_kLa(pK1, pK2, alk, d, CO2sat, pHin, pHend, delpH, kLain, kLaend, delkLa)

plt.xlabel('pH')
plt.ylabel('$CO_2$ loss to the atmosphere (g $m^{-2}$ $day^{-1})$')
plt.legend(['kLa = 0.1 1/hr', 'kLa = 0.5 1/hr', 'kLa = 1.5 1/hr', 'kLa = 3 1/hr'])
plt.show()

