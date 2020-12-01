#author = Riley Doyle
#date = 12/1/20
#file = CO2Sys_Program_plots
#status = working

import numpy as np
import matplotlib.pyplot as plt
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program import *

#Input Conditions
S = 35 #g/kg
T = 20 #C
P = 0.5 #dbars
TP = 10/10**6 #umol/kg SW
TSi = 30/10**6 #umol/kg SW
TA = 2350/10**6 #umol/kg SW
pCO2 = 0 #uatm
delpCO2 = 10000/10**6
TC = np.zeros([100,1])
pH = np.zeros([100,1])
i = 0

#Output Conditions
Tout = 20
Pout = 0.5

while pCO2 < 1:
    CO2Sys = CO2Sys_Program(T, S, P, TP, TSi, TA, pCO2, Tout, Pout)
    pCO2 = pCO2 + delpCO2
    TC[i] = (CO2Sys[39])*10**6
    pH[i] = (CO2Sys[51])
    i = i + 1

plt.figure()
pCO2 = np.arange(0, 1, delpCO2)
plt.plot(pCO2, TC)
plt.xlabel('pCO2 (atms)')
plt.ylabel('TC (umol/kg SW)')
plt.show()

plt.figure()
plt.plot(pCO2, pH)
plt.xlabel('pCO2 (atms)')
plt.ylabel('pH')
plt.show()