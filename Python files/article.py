#author: Riley Doyle
#date: 10/7/20
#file: pH_over_time
#status: WORKING

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

T = 20 + 273.15 #kelvins
R = 8.31451 #J/mol
S = 35 #g/kg
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
d = 0.15 #m
#y2 = 0.1695 #g HCO3 as CO2 per g algae
Kw = 10**(-14)

Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
K1 = calc_K1(T, S)*(den/1000) #mol/L
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)*(den/1000) #mol/L
pK2 = - np.log10(K2)
#Csat = PCO2*Kh*44*1000 #g/m3

kp1 = np.exp(1246.98 - (6.19*10**(4))/T - 183*np.log(T))
km1 = kp1/K1*(den/1000)
kp4 = ((499002.24*np.exp((4.2986*10**(-4)*S**2+.0000575499*S)))*np.exp(-90166.83/(R*T))/Kw)*(den/1000)
km4 = (kp4*Kw)/K1
kp5H = 5*10**10*(den/1000)
km5H = kp5H*K2
kp5OH = 6*10**9*(den/1000)
km5OH = (kp5OH/Kw)/K2
kp6 = 1.4*10**(-3)*(den/1000)
km6 = kp6/Kw*(den/1000)


def rates(x,t):
    CO2 = x[0]
    HCO3 = x[1]
    CO3 = x[2]
    H = x[3]
    OH = x[4]
    dCO2dt = ((km1*H)+km4)*HCO3 - (kp1+(kp4*OH))*CO2
    dHCO3dt = (kp1+(kp4*OH))*CO2 - ((km1*H)+km4)*HCO3 + ((kp5H*H)+kp5OH)*CO3 - (km5H+(kp5OH*OH))*HCO3
    dCO3dt = (km5H+(kp5OH*OH))*HCO3 - ((kp5H*H)+km5OH)*CO3
    dHdt = kp1*CO2 - km1*H*HCO3 + km5H*HCO3 - kp5H*H*CO3 + kp6 + km6*H*OH
    dOHdt = km4*HCO3 - kp4*OH*CO2 - kp5OH*OH*HCO3 + km5OH*CO3 + kp6 + km6*H*OH
    return [dCO2dt, dHCO3dt, dCO3dt, dHdt, dOHdt]

H0 = 10**(-8)
CO20 = 0
HCO30 = 0
CO30 = .005
OH0 = Kw/10**(-8)


x0 = [CO20, HCO30, CO30, H0, OH0]
t = np.linspace(0,4,100) 

x = odeint(rates, x0, t)

C02 = x[:,0]
HCO3 = x[:,1]
CO3 = x[:,2]
H = x[:,3]
OH = x[:,4]
pH = -np.log10(H)
plt.xlabel('time (days)')
plt.ylabel('pH')
plt.plot(t, pH)
#https://reader.elsevier.com/reader/sd/pii/S0304420305001684?token=BA5BE8F1457D7C7E3A64862024B7616AA8561DEE32E89635303ACF94DF2C45F873F44F00D9BC3AF1FB9C79B9462EA697
plt.show()