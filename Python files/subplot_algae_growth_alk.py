#author = Riley Doyle
#date = 7/28/20
#file = subplot_algae_growth_alk
#status = Working

from calc_Ks import *
from calc_alphas import *
from rates import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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

pH = 8
r_algae = 10
kLa = 0.5
delkLa = 2.5
c = 1
plt.subplots(nrows = 1, ncols = 2, figsize=(12, 3),sharex= True, sharey= True)
while kLa <= 3:
    alk0 = 2
    delalk = 5
    C = ['k', 'b', 'r']
    b = 0
    while alk0 <= 7:

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
        
        plt.subplot(1, 2, c)
        plt.xlabel('time (days)')
        plt.ylabel('CO$_2$ (g/m$^2$)')
        plt.plot(t,Cdel, C[b])
        plt.plot(t,Closs, C[b], linestyle='--')
        plt.axis([0, 4, 0, 170])
        b += 1
        alk0 += delalk
    kLa += delkLa
    c += 1
plt.subplot(1,2,1)
plt.text(2, 175, str('(a)'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,2,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(2, 175, str('(b)'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['CO$_2$ supply for alk = 2 meq/L', 'CO$_2$ loss for alk = 2 meq/L',
            'CO$_2$ supply for alk = 7 meq/L', 'CO$_2$ loss for alk = 7 meq/L'], frameon=False)
plt.show()