#author = Riley Doyle
#date = 10/13/20
#file = model_CO2_input_algae_growth
#status = working

from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from pandas import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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
CO2g = 0.005 #atm
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
d = 0.15
kLa = 0.5
kLa = kLa*d*24

#solving for algae growth
umax = 3.2424 #1/day
I = 100 #W/m2
kd = 0 #1/day
K = 300 #g/m3
Ki = 13.9136 #W/m2
def algaegrowth(x,t):
    X = x[0]
    dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
    return [dXdt]
X0 = 0.1
x0 = [X0]
t = np.linspace(0,3,10000) 
x = odeint(algaegrowth, x0, t)
X = (x[:,0]/1000)/algaeMW

def algaegrowth2(x,t):
    X2 = x2[0]
    dX2dt = (((umax*I)/(I + Ki))-kd)*(1-(X2/K))*X2
    return [dX2dt]
X20 = 0.1
x20 = [X20]
t2 = np.linspace(0, 3+(3/(10000-1)), 10000+1)  
x2 = odeint(algaegrowth, x20, t2)
X2 = (x2[:,0]/1000)/algaeMW

#initial conditions
CO2aqw = np.zeros(len(X)+1)
CO2needcum = np.zeros(len(X)+1)
CO2reqcum = np.zeros(len(X)+1)
alpha1 = np.zeros(len(X)+1)
alpha2 = np.zeros(len(X)+1)
losscum = np.zeros(len(X)+1)
HCO3 = np.zeros(len(X)+1)
H = np.zeros(len(X)+1)
pH = np.zeros(len(X)+1)
loss = np.zeros(len(X)+1)
CO2aqw[0] = CO2aq*(efficiency/100)
CO2reqcum[0] = 0
CO2needcum[0] = 0
HCO3[0] = 0.02
H[0] = (K1*CO2aqw[0])/HCO3[0]
pH[0] = -np.log10(H[0])
loss[0] = 0 
losscum[0] = loss[0]
additionalCO2 = CO2aq*(efficiency/100)

#Calculations
i = 0
for p in X:
    if H[i] > 10**-8.2:
        step = X2[i+1] - X[i]
        CO2aqw[i+1] = CO2aqw[i] - ((y1)*(step))
        CO2aqw[i+1] = np.clip(CO2aqw[i+1], 0, 1000)
        HCO3[i+1] = HCO3[i] + ((y2)*((step)))
        H[i+1] = (K1*CO2aqw[i+1])/HCO3[i+1]
        pH[i+1] = -np.log10(H[i+1])
        losscum[i+1] = sum(loss)
        CO2reqcum[i+1] = sum(CO2needcum)
        i = i + 1
    else:
        step = X2[i+1] - X[i]
        loss[i] = kLa*((additionalCO2 - CO2aqw[i]) - CO2sat)*t2[i]
        losscum[i+1] = sum(loss)
        CO2aqw[i+1] = CO2aqw[i] + additionalCO2  - ((y1)*(step))
        HCO3[i+1] = HCO3[i] + ((y2)*((step)))
        H[i+1] = (K1*CO2aqw[i+1])/HCO3[i+1]
        pH[i+1] = -np.log10(H[i+1])
        CO2needcum[i+1] = additionalCO2 + loss[i]
        CO2reqcum[i+1] = sum(CO2needcum)
        i = i + 1

data = {'CO2 (M)': CO2aqw, 'HCO3 (M)': HCO3, 'pH': pH}
table1 = pandas.DataFrame(data=data)
print (table1)

losscum = losscum*CO2MW*1000*d
CO2reqcum = CO2reqcum*CO2MW*d*1000
plt. plot(t2, CO2reqcum)
plt.plot(t2, losscum)
plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.show()

X = X*algaeMW*1000*d
plt.plot(t, X)
plt.xlabel('time (days)')
plt.ylabel('biomass concentration (g/m$^2$)')
plt.show()

plt.plot(t2, pH)
plt.xlabel('time (days)')
plt.ylabel('pH')
plt.show()

CO2aqw = CO2aqw*CO2MW*1000
plt.plot(t2, CO2aqw)
plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (mg/L)')
plt.show()

HCO3 = HCO3*HCO3MW*1000
plt.plot(t2, HCO3)
plt.xlabel('time (days)')
plt.ylabel('HCO$_3$$^-$ (mg/L)')
plt.show()