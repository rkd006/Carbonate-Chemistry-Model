#author: Riley Doyle
#date: 7/21/20
#file: calc_[inorganiccarbon]_pond
#status: WORKING

from calc_Ks import *
from calc_alphas import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global k1, k2, k3, k4

T = 20 + 273.15 #kelvins
S = 35 #g/kg
PCO2 = 0.00040 #atm
d = 0.15 #m

kLa = 0.5 #1/hr
y1 = 1.714
y2 = .1695
y3 = 1.88

Kh = calc_Kh(T,S)
K1 = calc_K1(T, S)
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)
pK2 = - np.log10(K2)

alk0 = 2.5 #
r_algae = 10
pH = 8

alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)

OH = 10**-(14-pH)*(10**3) #moles/m3
H = (10**(-pH))*(10**3) #moles/m3

k1 = -(y2*r_algae*(alpha1 + 2*alpha2))/44 #mol/m2/day

def rates(x,t):
    global k1, k2, k3, k4
    Ct = x[0]
    dCtdt = k1
    return [dCtdt]

Ct0 = (alk0 - OH + H)/(alpha1 + (2*alpha2))

x0 = [Ct0]
t = np.linspace(0,4,100) 

x = odeint(rates, x0, t)

Ct = x[:,0]

Ct1 = ((Ct/d)) #mM
print (Ct1[99])
plt.xlabel('time (days)')
plt.ylabel('[inorganic carbon] (mM)')
plt.plot(t, Ct1)
plt.axis([0, 4, 0, 16])
plt.show()