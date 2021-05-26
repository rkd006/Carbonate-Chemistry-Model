#author: Riley Doyle
#date: 2/13/2021
#file: CO2_loss_sump
#status: working

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().magic('reset -sf')

#model incorporates details of models from Malek et al, 2016 and Ketheesan and Nirmalakhandan, 2013

#Define parameters
T = 20 + 273.15 #kelvins
S = 35 #g/kg
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = - np.log10(K2)
Csat = PCO2*Kh*44*1000 #g/m3
alk0 = 2.5 #mol/m3
pH = 8
alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)
OH = 10**-(14-pH)*(10**3) #mol/m3
Hw = (10**(-pH))*(10**3) #mol/m3
Cco2 = ((alk0 - OH + Hw)*alpha0/(alpha1 + 2*alpha2)) #mol/m3
Pg = 1.2 #pressure of CO2 gas (atm)
Tg = 316 #temperature of CO2 gas (K)
Rg = 0.000082 #universal gas constant (atm*m3/mol/K)
He = 0.8317 #Henry's constant 
kLg = 9.59 #mass transfer for gas-to-liquid transfer (m/day)
Ws = 0.65 #width of sump (m)
Ls = 1 #length of sump (m)
W = 2.5 #width of pond/depth of sump (m)
L = 50 #length of pond (m)
kLa = 1.5*24 #1/day
H = 0.15 #depth of water (m)
V = W*L*H #volume of pond (m3)
vb = 30*864 #CO2 gas bubble terminal velocity (cm/s to m/day)
alpha6 = 0.96 #pressure correction factor
db = 2/1000 #diameter of CO2 gas bubble (mm to m)
v = 25*864 #water velocity (cm/s to m/day)
pi = math.pi
yin = 1 #CO2 molar fraction in
denCO2 = V/2040 ##convert g/m2/day to m3/day using density of CO2 (g/m3)
Csat = PCO2*Kh*44*1000 #g/m3
y1 = 2.128 #g CO2 per g algae
y2 = 0.3395 #g HCO3 as CO2 per g algae


r_algae = 10 #g/m2/day
Mc = r_algae*W*L #(g/day)

#Constants
k1 = (alpha0/(alpha1 + 2*alpha2)*y2*Mc)/V
k2 = kLa
k3 = kLa*Csat
C1 = ((y1 + y2)*Mc - y2*Mc*(alpha1 + 2*alpha2))/V  
C2 = Pg/(Rg*Tg)
C3 = (Rg*Tg*He)/Pg
C4 = (yin*Pg)/(He*Rg*Tg)
C5 = -kLg*W*H*Ws/He

#solve ODEs
def supply(x,t):
    Csup = x[0]
    Cdel = x[1]
    Closs = x[2]
    Caq = x[3]
    dCsupdt = C1 + ((k2 *Caq) - k3)
    dCdeldt =  (1/V)*((dCsupdt*denCO2)*C2*(yin - (C3*((Caq/44) + (C4 - (Caq/44))*np.exp(C5*(dCsupdt*denCO2)*(1-((alpha6*(dCsupdt*denCO2))/(alpha6*(dCsupdt*denCO2) + (v)*Ws*W)))*((pi*((db)**2)/(Ws*W*((vb - v)))*(dCsupdt*denCO2))/(pi*(((db)**3)/6)*(1-((alpha6*(dCsupdt*denCO2))/(alpha6*(dCsupdt*denCO2) + (v)*Ws*W))))))))))*44
    dClossdt = ((k2 *Caq) - k3) + (dCsupdt - dCdeldt)
    dCaqdt = -k1
    return [dCsupdt, dCdeldt, dClossdt, dCaqdt]

Csup0 = 0
Cdel0 = 0
Closs0 = 0 
Caq0 = Cco2*44 #g/m3


x0 = [Csup0, Cdel0, Closs0, Caq0]
t = np.linspace(0,3,100) 
x = odeint(supply, x0, t)

Csup = x[:,0]*H 
Cdel = x[:,1]*H
Caq = x[:,3]*H
Closs = x[:,2]*H

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Csup)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ losses'], frameon=False)
#plt.axis([0, 3, 0, 70])
plt.show()

plt.plot(t,Caq)
plt.show()
#determine loss (percent)
loss = (Closs[99]/Csup[99])*100
print (loss)
