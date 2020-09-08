#author: Riley Doyle
#date: 9/8/20
#file: temperature_function
#status: working

import numpy as np
from calc_density import *
from calc_Ks import *
from calc_alphas import *
import matplotlib.pyplot as plt

#plotting Csat as a function of Temperature
S = 35 #g/kg
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
T = np.linspace((20 + 273.15), (45 + 273.15), 100) #in Kelvins
Tcel = T - 273.15
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
Csat = PCO2*Kh*44*1000 #g/m3
plt.plot(Tcel, Csat)
plt.xlabel('Temperature, T (C)')
plt.ylabel('Saturation Concentration of CO$_2$, C$_{sat}$ (g/m$_3$)')
plt.show()

#plotting carbonate species as a function of temp
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3), sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.2)
alk = 2.5
pH = 8
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = - np.log10(K2)
alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)
OH = 10**-(14-pH)*(10**3)
H = (10**(-pH))*(10**3)
Ct = (alk - OH + H)/(alpha1 + 2*alpha2)

plt.subplot(1, 3, 1)
H2CO3 = (alpha0*Ct)
plt.plot(Tcel, H2CO3)
plt.xlabel('Temperature, T (C)')
plt.ylabel('Concentration (M)')
plt.text(30, 0.017, str('(a) H$_2$CO$_3$$^*$'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1, 3, 2)
HCO3 = (alpha1*Ct)
plt.plot(Tcel, HCO3)
plt.xlabel('Temperature, T (C)')
plt.text(30, 2.12, str('(b) HCO$_3$$^-$'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1, 3, 3)
CO3 = (alpha2*Ct)
plt.plot(Tcel, CO3)
plt.xlabel('Temperature, T (C)')
plt.text(30, 0.435, str('(c) CO$_3$$^{-2}$'), fontsize=10, fontweight='bold', ha='center')
plt.show()

plt.plot(Tcel, H2CO3, Tcel, HCO3, Tcel, CO3)
plt.xlabel('Temperature, T (C)')
plt.ylabel('Concentration (M)')
plt.legend(['H$_2$CO$_3$$^*$', 'HCO$_3$$^-$', 'CO$_3$$^{-2}$'])
plt.show()