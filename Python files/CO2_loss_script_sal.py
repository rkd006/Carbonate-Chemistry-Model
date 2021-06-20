#author: Riley Doyle
#date: 7/28/20
#file: CO2_loss_script_sal
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
from calc_CO2_loss_sal import *

#figures with different alkalinities
S = 25
while S <= 45:
    T = 20 + 273.15
    Tc = 20; #celcius
    P = 10; #(dbar)
    t = Tc*1.00024;
    p = P/10;
    den = calc_density(S, t, p); #(kg/m3)
    K1 = calc_K1(T,S)*(den/1000) #mol/L
    pK1 = -np.log10(K1)
    K2 = calc_K2(T,S)*(den/1000) #mol/L
    pK2 = -np.log10(K2)
    Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
    PCO2 = 0.000416
    alkin = 2
    alkend = 27
    delalk = 5
    pHin = 6
    pHend = 8.2
    delpH = 0.1
    d = 0.15
    kLa = 0.5
    y = calc_CO2_loss(pK1, pK2, Kh, kLa, d, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
    plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L'], frameon=False)
    plt.figure()
    S += 10

#figure with different salinities
Sin = 25
Send = 55
delS = 10
T = 20 + 273.15    
PCO2 = 0.000416
alk = 2.5
pHin = 6
pHend = 8.2
delpH = 0.1
d = 0.15
kLa = 0.5
y = calc_CO2_loss_sal (pK1, pK2, alk, d, PCO2, pHin, pHend, delpH, kLa, T, Sin, Send, delS)
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['S = 25 g/kg', 'S = 35 g/kg', 'S = 45 g/kg'], frameon=False)
plt.show()