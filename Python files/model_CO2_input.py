#author = Riley Doyle
#date = 10/13/20
#file = model_CO2_input
#status = working

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from pandas import *

#Stiochiometric ratios
CO2coef = 452
HCO3coef = 52
algaecoef = 4

#Molecular Weights
algaeMW = 2336 #g/mol
CO2MW = 44 #g/mol
HCO3MW = 61 #g/mol

#Given
T = 20 + 273.15
S = 35
CO2g = 0.006 #M
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = -np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = -np.log10(K2)
CO2aq = Kh*CO2g
efficiency = 95
CO2sat = Kh*PCO2
y1 = CO2coef/algaecoef
y2 = HCO3coef/algaecoef

#initial conditions
step = 0.5
end = 3.5
num = 8
algaegrowth = np.linspace(0, end, num)
CO2aqw = np.zeros(num)
HCO3 = np.zeros(num)
H = np.zeros(num)
pH = np.zeros(num)
CO2aqw0 = CO2aq*(efficiency/100)
HCO30 = 0.02

#Calculations
i = 0
for p in algaegrowth:
    CO2aqw[i] = CO2aqw0 - ((y1)*((p/1000)/algaeMW))
    HCO3[i] = HCO30 + ((y2)*((p/1000)/algaeMW))
    H[i] = (K1*CO2aqw[i])/HCO3[i]
    pH[i] = -np.log10(H[i])
    i = i + 1
  
data = {'algae growth (mg/L)': algaegrowth, 'CO2 (M)': CO2aqw, 'HCO3 (M)': HCO3, 'pH': pH}
table1 = pandas.DataFrame(data=data)
print (table1)