#author: Riley Doyle
#date: 7/29/20
#file: subplot_temp
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
import numpy as np
import matplotlib.pyplot as plt
T = 10 + 273.15
b = 1
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3),sharex= True, sharey= True)
while T <= 30 + 273.15:
    S = 35
    K1 = calc_K1(T,S)
    pK1 = -np.log10(K1)
    K2 = calc_K2(T,S)
    pK2 = -np.log10(K2)
    CO2sat = 0.012716352
    alkin = 2
    alkend = 27
    delalk = 5
    pHin = 6
    pHend = 8.2
    delpH = 0.1
    d = 0.15
    kLa = 0.5
    plt.subplot(1,3,b)
    y = calc_CO2_loss(pK1, pK2, kLa, d, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.axis([6, 8.2, 0, 1750])
    T += 10
    b += 1

plt.subplot(1,3,1)
plt.text(7.3, 1800, str('(a)'), fontsize=10, fontweight='bold', ha='center')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')

plt.subplot(1,3,2)
plt.text(7.3, 1800, str('(b)'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,3,3)
plt.text(7.3, 1800, str('(c)'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L'])
plt.show()