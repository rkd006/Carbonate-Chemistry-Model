#author = Riley Doyle
#date = 11/23/20
#file = CO2Sys_Program_Cal
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
TP = 10/10**6 #mol/kg SW
TSi = 30/10**6 #mol/kg SW
TA = 1033/10**6 #mol/kg SW
pCO2 = 415/10**6 

#Output Conditions
Tout = 20
Pout = 0.5

#simple calculations of output units: umol/kg SW
CO2Sys = CO2Sys_Program_TApCO2(T, S, P, TP, TSi, TA, pCO2, Tout, Pout)
HCO3in = (CO2Sys[20])*10**6
CO3in = (CO2Sys[21])*10**6
BAlkin = (CO2Sys[22])*10**6
PAlkin = (CO2Sys[24])*10**6
SiAlkin = (CO2Sys[25])*10**6
HCO3out = (CO2Sys[29])*10**6
CO3out = (CO2Sys[30])*10**6
BAlkout = (CO2Sys[31])*10**6
PAlkout = (CO2Sys[33])*10**6
SiAlkout = (CO2Sys[34])*10**6
TA = (CO2Sys[38])*10**6
TC = (CO2Sys[39])*10**6
Revellein = (CO2Sys[40])
OmegaCain = (CO2Sys[41])
OmegaArin = (CO2Sys[42])
xCO2dryin = (CO2Sys[43])*10**6
Revelleout = (CO2Sys[44])
OmegaCaout = (CO2Sys[45])
OmegaArout = (CO2Sys[46])
xCO2dryout = (CO2Sys[47])*10**6
CO2in = (CO2Sys[48])*10**6
CO2out = (CO2Sys[49])*10**6
pHin = (CO2Sys[50])
pHout = (CO2Sys[51])