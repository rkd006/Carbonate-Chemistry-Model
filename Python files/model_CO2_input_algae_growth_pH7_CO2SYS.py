#author = Riley Doyle
#date = 12/7/20
#file = model_CO2_input_algae_growth_pH7_CO2SYS
#status = working

from IPython import get_ipython
get_ipython().magic('reset -sf')

from calc_Ks import *
from calc_density import *
import numpy as np
from pandas import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program_pHTA import *

#Stiochiometric ratios
CO2coef = 452
HCO3coef = 52
algaecoef = 4

#Molecular Weights
algaeMW = 2336 #g/mol
CO2MW = 44 #g/mol
HCO3MW = 61 #g/mol

#Given
T = 20 
S = 35 #g/kg
P = 0.5 #dbars
TP = 10/10**6 #mol/kg SW
TSi = 30/10**6 #mol/kg SW
t = T*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
Tout = 20
Pout = 0.5
TA = 2350/10**6 #mol/kg SW
pH = 7.2
CO2Sys = CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH)
PCO2 = 0.000416 #atm
Kh = calc_Kh((T+273.15),S) #mol/kg/atm
CO2sat = Kh*PCO2*den/1000 #mol/L
y1 = CO2coef/algaecoef #mol/mol
y2 = HCO3coef/algaecoef #mol/mol
d = 0.15 #m
kLa = 0.5 #1/hr 
kLa = kLa*d*24 #m/day

#solving for algae growth
umax = 3.2424 #1/day
I = 100 #W/m2
kd = 0 #1/day
K = 350 #g/m3
Ki = 13.9136 #W/m2
def algaegrowth(x,t):
    X = x[0]
    dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
    return [dXdt]
X0 = 0.1
x0 = [X0]
t = np.linspace(0,3,10000) 
x = odeint(algaegrowth, x0, t)
X = (x[:,0])/algaeMW/1000 #mol/L

def algaegrowth2(x,t):
    X2 = x2[0]
    dX2dt = (((umax*I)/(I + Ki))-kd)*(1-(X2/K))*X2
    return [dX2dt]
X20 = 0.1
x20 = [X20]
t2 = np.linspace(0, 3+(3/(10000-1)), 10000+1)  
x2 = odeint(algaegrowth, x20, t2)
X2 = (x2[:,0])/algaeMW/1000 #mol/L

#initial conditions
CO2aq = np.zeros(len(X)+1)
CO2del = np.zeros(len(X)+1)
CO2req = np.zeros(len(X)+1)
CO2delcum = np.zeros(len(X)+1)
CO2reqcum = np.zeros(len(X)+1)
HCO3 = np.zeros(len(X)+1)
H = np.zeros(len(X)+1)
pH = np.zeros(len(X)+1)
loss = np.zeros(len(X)+1)
alk = TA*den/1000 #eq/L
K1 = CO2Sys[0]
CO2aq[0] = (CO2Sys[49])*den/1000 #mol/L
pH[0] = 7.2
HCO3[0] = (CO2Sys[29])*den/1000 #mol/L
CO2reqcum[0] = 0
CO2req[0] = 0
CO2del[0] = 0
CO2delcum[0] = 0
loss[0] = 0 
additionalCO2 = Kh*0.002 #mol/L

#Calculations
i = 0
for p in X:
    if H[i] < 10**-7.2:
        step = X2[i+1] - X[i]
        CO2aq[i+1] = CO2aq[i] + additionalCO2
        loss[i+1] = kLa*((CO2aq[i+1] - CO2sat)*1000)*(t2[i+1])
        loss[i+1] = np.clip(loss[i+1],loss[i], 1000)
        CO2del[i+1] = additionalCO2
        CO2req[i+1] = additionalCO2 + ((loss[i+1] - loss[i])/d/1000)
        CO2reqcum[i+1] = sum(CO2req)
        CO2delcum[i+1] = sum(CO2del)
        CO2aq[i+1] = CO2aq[i+1] - (y1)*(step) #- ((loss[i+1] - loss[i])/d/1000)
        HCO3[i+1] = HCO3[i] + ((y2)*((step)))
        H[i+1] = (K1*CO2aq[i+1])/HCO3[i+1]
        pH[i+1] = -np.log10(H[i+1])
    else:
        step = X2[i+1] - X[i]
        CO2aq[i+1] = CO2aq[i] - ((y1)*(step))
        HCO3[i+1] = HCO3[i] + ((y2)*((step)))
        H[i+1] = (K1*CO2aq[i+1])/HCO3[i+1]
        pH[i+1] = -np.log10(H[i+1])
        loss[i+1] = loss[i]
        CO2reqcum[i+1] = sum(CO2req)
        CO2delcum[i+1] = sum(CO2del)
    i = i + 1
data = {'CO2 (M)': CO2aq, 'HCO3 (M)': HCO3, 'pH': pH}
table1 = pandas.DataFrame(data=data)
print (table1)

loss = loss*CO2MW
CO2reqcum = CO2reqcum*CO2MW*d*1000
CO2delcum = CO2delcum*CO2MW*d*1000
plt. plot(t2, CO2reqcum)
plt.plot(t2, loss)
plt.xlabel('time (days)')
plt.ylabel('cummulative CO$_2$ (g/m$^2$)')
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.show()

X = X*algaeMW*d*1000
plt.plot(t, X)
plt.xlabel('time (days)')
plt.ylabel('biomass concentration (g/m$^2$)')
plt.show()

plt.plot(t2, pH)
plt.xlabel('time (days)')
plt.ylabel('pH')
plt.show()

CO2aq = CO2aq*CO2MW*d*1000
plt.plot(t2, CO2aq)
plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.show()

HCO3 = HCO3*HCO3MW*d*1000
plt.plot(t2, HCO3)
plt.xlabel('time (days)')
plt.ylabel('HCO$_3$$^-$ (g/m$^2$)')
plt.show()