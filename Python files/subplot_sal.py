#author: Riley Doyle
#date: 7/29/20
#file: subplot_sal
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_density import *
from calc_CO2_loss import *
import numpy as np
from rates import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Without algal growth
S = 25
b = 1
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3),sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)
while S <= 45:
    T = 20 + 273.15
    Tc = 20
    P = 10 #(dbar)
    t = Tc*1.00024
    p = P/10
    den = calc_density(S, t, p) #(kg/m3)
    PCO2 = 0.000416
    Kh = calc_Kh(T,S)*(den/1000) #mol/L/atm
    K1 = calc_K1(T, S)*(den/1000) #mol/L
    pK1 = - np.log10(K1)
    K2 = calc_K2(T, S)*(den/1000) #mol/L
    pK2 = - np.log10(K2)
    alkin = 2
    alkend = 27
    delalk = 5
    pHin = 6
    pHend = 8.2
    delpH = 0.1
    d = 0.15
    kLa = 0.5
    plt.subplot(1,3,b)
    y = calc_CO2_loss(pK1, pK2, Kh, kLa, d, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)
    plt.xlabel('pH')
    plt.axis([6, 8.2, 0, 1500])
    S += 10
    b += 1

plt.subplot(1,3,1)
plt.text(6.55, 1380, str('(a) S = 25 g/kg'), fontsize=10, fontweight='bold', ha='center')
plt.ylabel('CO$_2$ loss to the atmosphere (g m$^{-2}$ day$^{-1})$')

plt.subplot(1,3,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(6.55, 1380, str('(b) S = 35 g/kg'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(6.55, 1380, str('(c) S = 45 g/kg'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['alk = 2 meq/L', 'alk = 7 meq/L', 'alk = 12 meq/L', 'alk = 17 meq/L', 'alk = 22 meq/L'], frameon=False)
plt.show()

#with algal growth
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3),sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)
Sin = 25
Send = 55
delS = 10
Ssteps = np.arange(Sin, Send, delS)
b = 1
for a in Ssteps:
    T = 20 + 273.15
    Tc = 20
    P = 10 #(dbar)
    t = Tc*1.00024
    p = P/10
    den = calc_density(a, t, p) #(kg/m3)
    PCO2 = 0.000416
    d = 0.15
    kLa = 0.5
    y1 = 2.128 #1.714 (old algae eqn) #g CO2 per g algae
    y2 = 0.3395 #0.1695 (old algae eqn) #g HCO3 as CO2 per g algae
    Kh = calc_Kh(T,a)*(den/1000) #mol/L/atm
    K1 = calc_K1(T, a)*(den/1000) #mol/L
    pK1 = - np.log10(K1)
    K2 = calc_K2(T, a)*(den/1000) #mol/L
    pK2 = - np.log10(K2)
    
    Csat = PCO2*Kh*44*1000
    
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
    
    plt.subplot(1,3,b)
    plt.xlabel('time (days)')
    plt.plot(t,Cdel)
    plt.plot(t,Closs, linestyle='--')
    plt.axis([0, 4, 0, 80])
    b += 1

plt.subplot(1,3,1)
plt.text(1, 74, str('(a) S = 25 g/kg'), fontsize=10, fontweight='bold', ha='center')
plt.ylabel('CO$_2$ (g m$^{-2}$')

plt.subplot(1,3,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1, 74, str('(b) S = 35 g/kg'), fontsize=10, fontweight='bold', ha='center')

plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1, 74, str('(c) S = 45 g/kg'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['CO$_2$ supply', 'CO$_2$ loss'], frameon=False, bbox_to_anchor=(.78, .84),
           bbox_transform=plt.gcf().transFigure)
plt.show()