#author = Riley Doyle
#date = 12/11/20
#file = CO2_loss_script_temp_CO2Sys
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
T = 10 #C
P = 0.5 #dbars
TP = 10/10**6 #mol/kg SW
TSi = 30/10**6 #mol/kg SW
Kh = calc_Kh((T+273.15),S) #mol/kg/atm
pCO2 = 0.000415 #atm
CO2sat = pCO2*Kh*10**6 #umol/kg
kLa = 0.5 #1/hr
t = T*1.00024;
p = P/10;
den = calc_density(S, t, p); #(kg/m3)

#Output Conditions
Tout = 20
Pout = 0.5
delpH = 0.1
delTA = 5000/10**6
CO2out = np.zeros([23,7])
loss = np.zeros([23,7])
pHout = np.zeros([23,7])

#figures with different alkalinities
while T <= 30:
    TA = 2000/10**6 #mol/kg SW
    j = 0
    while TA <= 32000/10**6:
        i = 0
        pH = 6
        while pH <= 8.2:
            CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
            CO2out[i,j] = (CO2Sys[49])*10**6
            pHout[i,j] = CO2Sys[50]
            loss[i,j] = (kLa*(CO2out[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
            i = i + 1
            pH = pH + delpH
        TA = TA + delTA
        j = j + 1
    T = T + 10
    plt.plot(pHout, loss)
    plt.xlabel('pH')
    plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
    plt.legend(['alk = 2 meq/kg SW', 'alk = 7 meq/kg SW', 'alk = 12 meq/kg SW', 'alk = 17 meq/kg SW', 'alk = 22 meq/kg SW', 'alk = 27 meq/kg SW', 'alk = 32 meq/kg SW'], frameon=False)
    plt.show()

#figure with different temperatures    
T = 10
j = 0
TA = 2500/10**6
CO2out2 = np.zeros([23,3])
loss2 = np.zeros([23,3])
pHout2 = np.zeros([23,3])
while T <= 50:
    pH = 6
    i  = 0
    while pH <= 8.2:
            CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
            CO2out2[i,j] = (CO2Sys[49])*10**6
            pHout2[i,j] = CO2Sys[50]
            loss2[i,j] = (kLa*(CO2out2[i,j] - CO2sat)*24*44*0.15*den)/10**6 #umol/kg/day to g/m2/day
            i = i + 1
            pH = pH + delpH
    j = j +1
    T = T + 20
plt.figure()
plt.plot(pHout2, loss2)
plt.xlabel('pH')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')
plt.legend(['T= 10 $^o$C', 'T= 30 $^o$C', 'T= 50 $^o$C'])
plt.show()