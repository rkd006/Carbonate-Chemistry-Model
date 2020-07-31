#author: Riley Doyle
#date: 7/28/20
#file: subplot_algal_growth_range
#status: working 

from calc_Ks import *
from calc_alphas import *
from rates import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global k1, k2, k3, k4

T = 20 + 273.15
S = 35
PCO2 = 0.00040
d = 0.15
y1 = 1.714 #g CO2 per g algae
y2 = 0.1695 #g HCO3 as CO2 per g algae
Kh = calc_Kh(T,S)
K1 = calc_K1(T, S)
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)
pK2 = - np.log10(K2)
Csat = PCO2*Kh*44
alk0 = 2.5
pH = 8

alpha0 = calc_alpha0(pH, pK1, pK2)
alpha1 = calc_alpha1(pH, pK1, pK2)
alpha2 = calc_alpha2(pH, pK1, pK2)

OH = 10**-(14-pH)*(10**3)
H = (10**(-pH))*(10**3)
it = 0
kLa = 0.5
rin = 10 
rend = 25
delr = 5
rsteps = np.arange(rin, rend, delr)
c = 1
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3),sharex= True, sharey= True)
for p in rsteps:
    k1 = alpha0/(alpha1 + 2*alpha2)*y2*p
    k2 = (kLa*d*24)
    k3 = (kLa*d*24)*Csat
    k4 = (y1 + y2)*p - y2*p*(alpha1 + 2*alpha2)

    Caq0 = ((alk0 - OH + H)*alpha0/(alpha1 + 2*alpha2))*44
    Cin0 = 0
    Closs0 = 0 
    def rates(x,t):
        Caq = x[0]
        Cdel = x[1]
        Closs = x[2]
        dCaqdt = -k1
        dCdeldt = ((k2 *Caq) - k3) + k4
        dClossdt = (k2 *Caq) - k3
        return [dCaqdt, dCdeldt, dClossdt]
    
    x0 = [Caq0, Cin0, Closs0]
    t = np.linspace(0,4,100) 
    x = odeint(rates, x0, t)
    Caq = x[:,0]
    Cdel = x[:,1]
    Closs = x[:,2]
    plt.subplot(1,3,c) 
    plt.xlabel('time (days)')
    plt.ylabel('CO$_2$ (g/m$^2$)')
    plt.plot(t,Cdel)
    plt.plot(t,Closs, linestyle='--')
    plt.axis([0, 4, 0, 140])
    c += 1
    
plt.subplot(1,3,1)
plt.text(2, 150, str('(a)'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,3,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(2, 150, str('(b)'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(2, 150, str('(c)'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['CO$_2$ supply', 'CO$_2$ loss'], frameon=False)
plt.show()