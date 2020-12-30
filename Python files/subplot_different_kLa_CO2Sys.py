#author = Riley Doyle
#date = 12/14/20
#file = subplot_different_kLa_CO2Sys
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
TA = 2500/10**6 #mol/kg SW
CO2out1 = np.zeros([23,7])
loss1 = np.zeros([23,7])
pHout1 = np.zeros([23,7])
j = 0
plt.subplots(nrows = 1, ncols = 2, figsize=(9, 3),sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)

plt.subplot(1,2,1)
kLa = 0.1
delkLa = 0.4
while kLa <= 0.5:
    i = 0
    pH = 6
    while pH <= 8.2:
        CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
        CO2out1[i,j] = (CO2Sys[49])*10**6
        pHout1[i,j] = CO2Sys[50]
        loss1[i,j] = (kLa*(CO2out1[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
        i = i + 1
        pH = pH + delpH
    kLa = kLa + delkLa
    j = j + 1

CO2out2 = np.zeros([23,7])
loss2 = np.zeros([23,7])
pHout2 = np.zeros([23,7])
j = 0
kLa = 1.5
delkLa = 1.5
while kLa <= 3:
    i = 0
    pH = 6
    while pH <= 8.2:
        CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
        CO2out2[i,j] = (CO2Sys[49])*10**6
        pHout2[i,j] = CO2Sys[50]
        loss2[i,j] = (kLa*(CO2out2[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
        i = i + 1
        pH = pH + delpH
    kLa = kLa + delkLa
    j = j + 1
    
plt.plot(pHout1[:,0], loss1[:,0], 'b')
plt.plot(pHout1[:,1], loss1[:,1], 'r--')
plt.plot(pHout2[:,0], loss2[:,0], 'c')
plt.plot(pHout2[:,1], loss2[:,1], 'y--')
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.axis([6, 8.2, 0, 2500])
plt.text(7.1, 2600, str('(a) alkalinity = 2.5 meq L$^{-1}$'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,2,2)
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
TA = 7000/10**6 #mol/kg SW
CO2out1 = np.zeros([23,7])
loss1 = np.zeros([23,7])
pHout1 = np.zeros([23,7])
j = 0
kLa = 0.1
delkLa = 0.4
while kLa <= 0.5:
    i = 0
    pH = 6
    while pH <= 8.2:
        CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
        CO2out1[i,j] = (CO2Sys[49])*10**6
        pHout1[i,j] = CO2Sys[50]
        loss1[i,j] = (kLa*(CO2out1[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
        i = i + 1
        pH = pH + delpH
    kLa = kLa + delkLa
    j = j + 1

CO2out2 = np.zeros([23,7])
loss2 = np.zeros([23,7])
pHout2 = np.zeros([23,7])
j = 0
kLa = 1.5
delkLa = 1.5
while kLa <= 3:
    i = 0
    pH = 6
    while pH <= 8.2:
        CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
        CO2out2[i,j] = (CO2Sys[49])*10**6
        pHout2[i,j] = CO2Sys[50]
        loss2[i,j] = (kLa*(CO2out2[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
        i = i + 1
        pH = pH + delpH
    kLa = kLa + delkLa
    j = j + 1
    
plt.plot(pHout1[:,0], loss1[:,0], 'b')
plt.plot(pHout1[:,1], loss1[:,1], 'r--')
plt.plot(pHout2[:,0], loss2[:,0], 'c')
plt.plot(pHout2[:,1], loss2[:,1], 'y--')
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.gca().axes.get_yaxis().set_visible(False)
plt.axis([6, 8.2, 0, 2500])
plt.xlabel('pH')
plt.legend(['kLa = 0.1 1/hr', 'kLa = 0.5 1/hr', 'kLa = 1.5 1/hr', 'kLa = 3 1/hr'], frameon=False)
plt.text(7.1, 2600, str('(b) alkalinity = 7 meq L$^{-1}$'), fontsize=10, fontweight='bold', ha='center')
plt.show()