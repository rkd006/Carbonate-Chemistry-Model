#author = Riley Doyle
#date = 12/1/20
#file = CO2Sys_Program_plots
#status = working

import numpy as np
import matplotlib.pyplot as plt
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program_TApCO2 import *

#Input Conditions
S = 35 #g/kg
T = 20 #C
P = 0.5 #dbars
TP = 10/10**6 #umol/kg SW
TSi = 30/10**6 #umol/kg SW
TA = 2350/10**6 #umol/kg SW

#Output Conditions
Tout = 20
Pout = 0.5

#Case 1
pCO2 = 0 #uatm
delpCO2 = 10000/10**6
TC = np.zeros([100,1])
pH = np.zeros([100,1])
i = 0
while pCO2 <= 1:
    CO2Sys = CO2Sys_Program_TApCO2(T, S, P, TP, TSi, TA, pCO2, Tout, Pout)
    TC[i] = (CO2Sys[39])*10**6
    pH[i] = (CO2Sys[51])
    pCO2 = pCO2 + delpCO2
    i = i + 1

#Case 2
pCO2 = 0
TA = 2000/10**6
delTA = 280/10**6
TC2 = np.zeros([100,1])
pH2 = np.zeros([100,1])
i = 0
while pCO2 <= 1:
    CO2Sys = CO2Sys_Program_TApCO2(T, S, P, TP, TSi, TA, pCO2, Tout, Pout)
    TC2[i] = (CO2Sys[39])*10**6
    pH2[i] = (CO2Sys[51])
    pCO2 = pCO2 + delpCO2
    TA = TA + delTA
    i = i + 1
      
plt.figure()
pCO2 = np.arange(0, 1, delpCO2)
plt.plot(pCO2, TC)
plt. plot(pCO2, TC2)
plt.xlabel('pCO2 (atms)')
plt.ylabel('TC (umol/kg SW)')
plt.show()

plt.figure()
plt.plot(pCO2, pH)
plt.plot(pCO2, pH2)
plt.xlabel('pCO2 (atms)')
plt.ylabel('pH')
plt.show()