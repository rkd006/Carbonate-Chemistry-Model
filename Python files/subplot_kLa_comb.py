#author: Riley Doyle
#date: 7/27/20
#file: subplot_kLa_comb
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

T = 20 + 273.15
S = 35
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
K1 = calc_K1(T,S)*(den/1000) #mol/L
pK1 = -np.log10(K1)
K2 = calc_K2(T,S)*(den/1000) #mol/L
pK2 = -np.log10(K2)
PCO2 = 0.000416
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
alkin = 2
alkend = 37
delalk = 5
pHin = 6.5
pHend = 8.2
delpH = 0.1
d = 0.15
plt.subplots(nrows = 1, ncols = 2, figsize=(9, 3),sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)
plt.subplot(1,2,2)
kLa = 3
y1 = calc_CO2_loss(pK1, pK2, Kh, kLa, d, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlabel('pH')
plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L', 'alk = 27 meq/L', 'alk = 32 meq/L'], frameon=False)
plt.axis([6.5, 8.2, 0, 4000])
plt.text(6.9, 3600, str('(b) k$_L$a = 3 hr$^{-1}$'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,2,1)
kLa = 0.5
y2 = calc_CO2_loss(pK1, pK2, Kh, kLa, d, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.axis([6.5, 8.2, 0, 4000])
plt.text(6.9, 3600, str('(a) k$_L$a = 0.5 hr$^{-1}$'), fontsize=10, fontweight='bold', ha='center')
plt.show()