#author: Riley Doyle
#date: 7/29/20
#file: subplot_temp
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
import numpy as np
from rates import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#without algal growth
T = 10 + 273.15
b = 1
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3),sharex= True, sharey= True)
while T <= 30 + 273.15:
    S = 35
    K1 = calc_K1(T,S)
    pK1 = -np.log10(K1)
    K2 = calc_K2(T,S)
    pK2 = -np.log10(K2)
    CO2sat = 0.012716352
    alkin = 2
    alkend = 27
    delalk = 5
    pHin = 6
    pHend = 8.2
    delpH = 0.1
    d = 0.15
    kLa = 0.5
    plt.subplot(1,3,b)
    y = calc_CO2_loss(pK1, pK2, kLa, d, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.axis([6, 8.2, 0, 1750])
    T += 10
    b += 1

plt.subplot(1,3,1)
plt.text(7.3, 1800, str('(a)'), fontsize=10, fontweight='bold', ha='center')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')

plt.subplot(1,3,2)
plt.text(7.3, 1800, str('(b)'), fontsize=10, fontweight='bold', ha='center')
plt.gca().axes.get_yaxis().set_visible(False)

plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(7.3, 1800, str('(c)'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L'])
plt.show()

#with algal growth
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3),sharex= True, sharey= True)
Tin = 10 + 273.15
Tend = 40 + 273.15
delT = 10
Tsteps = np.arange(Tin, Tend, delT)
c = 1
for p in Tsteps:
    S = 35
    PCO2 = 0.00040
    d = 0.15
    kLa = 0.5
    y1 = 1.714 #g CO2 per g algae
    y2 = 0.1695 #g HCO3 as CO2 per g algae
    Kh = calc_Kh(p,S)
    K1 = calc_K1(p, S)
    pK1 = - np.log10(K1)
    K2 = calc_K2(p, S)
    pK2 = - np.log10(K2)
    
    Csat = PCO2*Kh*44
    
    alk0 = 2.5
    r_algae = 10
    pH = 8
    
    alpha0 = calc_alpha0(pH, pK1, pK2)
    alpha1 = calc_alpha1(pH, pK1, pK2)
    alpha2 = calc_alpha2(pH, pK1, pK2)
    
    OH = 10**-(14-pH)*(10**3)
    H = (10**(-pH))*(10**3)
    k1 = alpha0/(alpha1 + 2*alpha2)*y2*r_algae
    k2 = (kLa*d*24)
    k3 = (kLa*d*24)*Csat
    k4 = (y1 + y2)*r_algae - y2*r_algae*(alpha1 + 2*alpha2)

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
    plt.plot(t,Cdel)
    plt.plot(t,Closs, linestyle='--')
    plt.axis([0, 4, 0, 70])
    c += 1

plt.subplot(1,3,1)
plt.text(2, 80, str('(a)'), fontsize=10, fontweight='bold', ha='center')
plt.ylabel('CO$_2$ (g m$^{-2}$')

plt.subplot(1,3,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(2, 80, str('(b)'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(2, 80, str('(c)'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['CO$_2$ supply', 'CO$_2$ loss'])
plt.show()