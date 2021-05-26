#author: Riley Doyle
#date: 3/8/2021
#file: CO2_loss_sump_kinetics
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
kLa = 1.5 #1/hr
y1 = 2.128 #1.714 (old algae eqn) #g CO2 per g algae
y2 = 0.3395 #0.1695 (old algae eqn) #g HCO3 as CO2 per g algae
Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = - np.log10(K2)
Csat = PCO2*Kh*44*1000 #g/m3
alk0 = 2.5 #eq/m3
pH = 8
alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)
OH = 10**-(14-pH)*(10**3)
Hw = (10**(-pH))*(10**3)
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
H = 0.15 #depth of water (m)
V = W*L*H #volume of pond (m3)
A = V/H #area of pond (m2)
vb = 30*864 #CO2 gas bubble terminal velocity (cm/s to m/day)
alpha6 = 0.96 #pressure correction factor
db = 2/1000 #diameter of CO2 gas bubble (mm to m)
v = 25*864 #water velocity (cm/s to m/day)
pi = math.pi
yin = 1 #CO2 molar fraction in
denCO2 = A/2040 #convert g/m2/day to m3/day using density of CO2 (g/m3)
Csat = PCO2*Kh*44*1000 #g/m3
y1 = 2.128 #g CO2 per g algae
y2 = 0.3395 #g HCO3 as CO2 per g algae
#algae kinetic parameters
umax = 3.2424 #1/day
I = 100 #W/m2
kd = 0 #1/day
K = 60 #g/m2
Ki = 13.9136 #W/m2

#Constants
k1 = alpha0/(alpha1 + 2*alpha2)*y2
k2 = (kLa*H*24)
k3 = (kLa*H*24)*Csat
k4 = (y1 + y2)
k5 = y2*(alpha1 + 2*alpha2)
C2 = Pg/(Rg*Tg)
C3 = (Rg*Tg*He)/Pg
C4 = (yin*Pg)/(He*Rg*Tg)
C5 = -kLg*W*H*Ws/He
    
#solve ODEs
def sump_kinetics(x,t):
    X = x[0]
    P = x[1]
    Caq = x[5]
    Cin = x[2]
    dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
    dPdt = dXdt
    dCsupdt = (k4*P - k5*P) + (k2 *Caq) - k3
    dCdeldt = (1/A)*((dCsupdt*denCO2)*C2*(yin - (C3*((Caq/44) + (C4 - (Caq/44))*np.exp(C5*(dCsupdt*denCO2)*(1-((alpha6*(dCsupdt*denCO2))/(alpha6*(dCsupdt*denCO2) + (v)*Ws*W)))*((pi*((db)**2)/(Ws*W*((vb - v)))*(dCsupdt*denCO2))/(pi*(((db)**3)/6)*(1-((alpha6*(dCsupdt*denCO2))/(alpha6*(dCsupdt*denCO2) + (v)*Ws*W))))))))))*44
    dClossdt = (k2 *Caq) - k3 + (dCsupdt - dCdeldt)
    dCaqdt = -k1*P #- (dClossdt) + dCdeldt
    return [dXdt, dPdt, dCsupdt, dCdeldt, dClossdt, dCaqdt]

Caq0 = ((alk0 - OH + Hw)*alpha0/(alpha1 + 2*alpha2))*44 #g/m3
Cin0 = 0
Cdel0 = 0 
Closs0 = 0 
X0 = 0.1
P0 = 0
x0 = [X0, P0, Cin0, Cdel0, Closs0, Caq0]
t = np.linspace(0,3,100)
x = odeint(sump_kinetics, x0, t)

X = x[:,0]
P = x[:, 1]
Caq = x[:,5]
Cin = x[:,2]
Cdel = x[:,3]
Closs = x[:,4]

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t, Cin)
plt.plot(t, Closs)
#plt.axis([0, 3, 0, 100])
plt.legend(['CO$_2$ supply required', 'CO$_2$ losses'], frameon=False)
plt.show()

plt.plot(t,Caq)
plt.show()
#determine loss (percent)
loss = (Closs[99]/Cin[99])*100
print (loss)
