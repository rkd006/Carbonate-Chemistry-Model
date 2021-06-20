#author: Riley Doyle
#date: 10/6/20
#file: pCpHdiagram
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
alk = 2.5
                

pH_start = 0
pH_end = 14
vpH = np.linspace(pH_start, pH_end)
p = len(vpH)

H2CO3 = np.zeros([p,1])
HCO3 = np.zeros([p,1])
CO3 = np.zeros([p,1])

for n in range(0,p):
    alpha0 = calc_alpha0(vpH, pK1, pK2)
    alpha1 = calc_alpha1(vpH, pK1, pK2)
    alpha2 = calc_alpha2(vpH, pK1, pK2)
    CO2sat = PCO2*Kh*1000 #mole/m3
                
    H = 10**(-vpH)
    OH = 10**(-(14-vpH))
    bt = (1/(alpha1 + (2*alpha2)))
    tp = (alk - OH + H)
    CT = tp * bt
    H2CO3 = -np.log10(alpha0*CT)
    HCO3 = -np.log10(alpha1*CT)
    CO3 = -np.log10(alpha2*CT)
    CT = -np.log10(CT)

vpH = np.transpose(vpH)
carbonates = np.concatenate((H2CO3, HCO3, CO3))

x_axis = vpH

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x_axis, H2CO3, label='H$_{2}$CO$_{3}$')
ax.plot(x_axis, HCO3, 'r', label='HCO$_3$$^{-}$')
ax.plot(x_axis, CO3, 'k', label='CO$_3$$^{-2}$')
ax.plot(x_axis, CT, label='C$_{t}$')
ax.set_xticks([2,4,6,8,10,12,14])
ax.set_ylim([14,-6])
ax.legend()
plt.xlabel('pH')
plt.ylabel('pC')
plt.show()
