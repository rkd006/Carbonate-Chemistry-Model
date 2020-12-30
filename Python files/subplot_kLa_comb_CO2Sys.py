#author = Riley Doyle
#date = 12/14/20
#file = subplot_kLa_comb_CO2Sys
#status = working

import numpy as np
import matplotlib.pyplot as plt
from calc_Ks import *
from calc_density import *
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program_pHTA import *

#Input Conditions
S = 35 #g/kg
T = 20 #C
P = 0.5 #dbars
TP = 10/10**6 #mol/kg SW
TSi = 30/10**6 #mol/kg SW
Kh = calc_Kh((T+273.15),S) #mol/kg/atm
pCO2 = 0.000415 #atm
CO2sat = pCO2*Kh*10**6 #umol/kg
t = T*1.00024;
p = P/10;
den = calc_density(S, t, p); #(kg/m3)

#Output Conditions
Tout = 20
Pout = 0.5
delpH = 0.1
CO2out = np.zeros([18,7])
loss = np.zeros([18,7])
pHout = np.zeros([18,7])
kLa  = 3
#simple calculations of output units: umol/kg SW
plt.subplots(nrows = 1, ncols = 2, figsize=(9, 3),sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)
plt.subplot(1,2,2)
TA = 2000/10**6 #mol/kg SW
delTA = 5000/10**6
j = 0
while TA <= 32000/10**6:
    i = 0
    pH = 6.5
    while pH <= 8.2:
        CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
        CO2out[i,j] = (CO2Sys[49])*10**6
        pHout[i,j] = CO2Sys[50]
        loss[i,j] = (kLa*(CO2out[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
        i = i + 1
        pH = pH + delpH
    TA = TA + delTA
    j = j + 1
plt.plot(pHout[:,0], loss[:,0], 'b-')
plt.plot(pHout[:,1], loss[:,1], 'r--')
plt.plot(pHout[:,2], loss[:,2], 'k-.')
plt.plot(pHout[:,3], loss[:,3], 'c:')
plt.plot(pHout[:,4], loss[:,4], 'm--')
plt.plot(pHout[:,5], loss[:,5], 'y-')
plt.plot(pHout[:,6], loss[:,6], 'g-.')
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlabel('pH')
plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L', 'alk = 27 meq/L', 'alk = 32 meq/L'], frameon=False)
plt.axis([6.5, 8.2, 0, 4000])
plt.text(6.9, 3600, str('(b) k$_L$a = 3 hr$^{-1}$'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,2,1)    
kLa  = 0.5
#simple calculations of output units: umol/kg SW
TA = 2000/10**6 #mol/kg SW
delTA = 5000/10**6
j = 0
while TA <= 32000/10**6:
    i = 0
    pH = 6.5
    while pH <= 8.2:
        CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
        CO2out[i,j] = (CO2Sys[49])*10**6
        pHout[i,j] = CO2Sys[50]
        loss[i,j] = (kLa*(CO2out[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
        i = i + 1
        pH = pH + delpH
    TA = TA + delTA
    j = j + 1
plt.plot(pHout[:,0], loss[:,0], 'b-')
plt.plot(pHout[:,1], loss[:,1], 'r--')
plt.plot(pHout[:,2], loss[:,2], 'k-.')
plt.plot(pHout[:,3], loss[:,3], 'c:')
plt.plot(pHout[:,4], loss[:,4], 'm--')
plt.plot(pHout[:,5], loss[:,5], 'y-')
plt.plot(pHout[:,6], loss[:,6], 'g-.')
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.axis([6.5, 8.2, 0, 4000])
plt.text(6.9, 3600, str('(a) k$_L$a = 0.5 hr$^{-1}$'), fontsize=10, fontweight='bold', ha='center')
plt.show()