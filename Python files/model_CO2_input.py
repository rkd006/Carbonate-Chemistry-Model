#author = Riley Doyle
#date = 10/13/20
#file = model_CO2_input
#status = working

from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from pandas import *
import matplotlib.pyplot as plt

#Stiochiometric ratios
CO2coef = 452
HCO3coef = 52
algaecoef = 4

#Molecular Weights
algaeMW = 2336 #g/mol
CO2MW = 44 #g/mol
HCO3MW = 61 #g/mol

#Given
step = 0.05
end = 48
r_algae_hr = 2
points_hr = r_algae_hr/step
T = 20 + 273.15
S = 35
CO2g = 0.006 #atm
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
kLa = (0.5/24)/points_hr 

#initial conditions
algaegrowth = np.arange(0,end,step)
CO2aqw = np.zeros(len(algaegrowth)+1)
HCO3 = np.zeros(len(algaegrowth)+1)
H = np.zeros(len(algaegrowth)+1)
pH = np.zeros(len(algaegrowth)+1)
loss = np.zeros(len(algaegrowth)+1)
CO2aqw[0] = CO2aq*(efficiency/100)
HCO3[0] = 0.02
H[0] = (K1*CO2aqw[0])/HCO3[0]
pH[0] = -np.log10(H[0])
loss[0] = kLa*(CO2aqw[0] - CO2sat) #M
additionalCO2 = 0.00002

#Calculations
i = 0
m = 0
for p in algaegrowth:
    if pH[i] >= 8.2 or m == 1:
            CO2aqw[i+1] = CO2aqw[i] + additionalCO2 - ((y1)*((step/1000)/algaeMW))
            HCO3[i+1] = HCO3[i] + ((y2)*((step/1000)/algaeMW))
            H[i+1] = (K1*CO2aqw[i+1])/HCO3[i+1]
            pH[i+1] = -np.log10(H[i+1])
            loss[i+1] = kLa*(CO2aqw[i+1] - CO2sat)
            i = i + 1
            if pH[i] > 8:
                m = 1
            else:
                m = 0
    else:
        CO2aqw[i+1] = CO2aqw[i] - ((y1)*((step/1000)/algaeMW))
        HCO3[i+1] = HCO3[i] + ((y2)*((step/1000)/algaeMW))
        H[i+1] = (K1*CO2aqw[i+1])/HCO3[i+1]
        pH[i+1] = -np.log10(H[i+1])
        loss[i+1] = kLa*(CO2aqw[i+1] - CO2sat)
        i = i + 1   

algaegrowth = np.arange(0, end+step, step)
data = {'algae growth (mg/L)': algaegrowth, 'CO2 (M)': CO2aqw, 'HCO3 (M)': HCO3, 'pH': pH}
table1 = pandas.DataFrame(data=data)
print (table1)

#Let's say that algae grows 2 mg/L a hr
r_algae_hr = 2
points_hr = r_algae_hr/step
tend = ((end/step)+1)/points_hr
num = int(tend*points_hr)
t = np.linspace(0, tend, num)
plt.plot(t, pH)
plt.xlabel('time (hrs)')
plt.ylabel('pH')
plt.show()

CO2aqw = CO2aqw*CO2MW*1000
plt.plot(t, CO2aqw)
plt.xlabel('time (hrs)')
plt.ylabel('CO$_2$ (mg/L)')
plt.show()

HCO3 = HCO3*HCO3MW*1000
plt.plot(t, HCO3)
plt.xlabel('time (hrs)')
plt.ylabel('HCO$_3$$^-$ (mg/L)')
plt.show()

loss = loss*CO2MW*1000
plt.plot(t, loss)
plt.xlabel('time (hrs)')
plt.ylabel('CO$_2$ loss to atmosphere (mg/L)')
plt.show()
