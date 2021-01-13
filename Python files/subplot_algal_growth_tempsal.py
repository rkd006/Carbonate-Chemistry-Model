#author: Riley Doyle
#date: 8/3/20
#file: subplot_algal_growth_tempsal
#status: working 

from calc_Ks import *
from calc_alphas import *
from calc_density import *
from rates import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global k1, k2, k3, k4
c = 1
plt.subplots(nrows = 1, ncols = 2, figsize=(9, 3),sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)
Tin = 10 + 273.15
Tend = 50 + 273.15
delT = 20
Tsteps = np.arange(Tin, Tend, delT)
C = ['k', 'r']
b = 0
for a in Tsteps:
    S = 35
    Tc = a - 273.15
    P = 10 #(dbar)
    t = Tc*1.00024
    p = P/10
    den = calc_density(S, t, p) #(kg/m3)
    PCO2 = 0.000416
    d = 0.15
    kLa = 1.5*(1.024**((Tc)-20))
    y1 = 2.128 #1.714 (old algae eqn) #g CO2 per g algae
    y2 = 0.3395 #0.1695 (old algae eqn) #g HCO3 as CO2 per g algae
    Kh = calc_Kh(a,S)*(den/1000) #mol/L/atm
    K1 = calc_K1(a, S)*(den/1000) #mol/L
    pK1 = - np.log10(K1)
    K2 = calc_K2(a, S)*(den/1000) #mol/L
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
    plt.subplot(1,2,c)
    plt.xlabel('time (days)')
    plt.ylabel('CO$_2$ (g/m$^2$)')
    plt.plot(t,Cdel, C[b])
    plt.plot(t,Closs, C[b], linestyle='--')
    plt.legend(['CO$_2$ supply for T = 10 $^o$C', 'CO$_2$ loss for T = 10 $^o$C',
                'CO$_2$ supply for T = 30 $^o$C', 'CO$_2$ loss for T = 30 $^o$C'],
               frameon=False, bbox_to_anchor=(.4, 1.3), bbox_transform=plt.gcf().transFigure)
    b += 1
    
c += 1
Sin = 25
Send = 65
delS = 20
Ssteps = np.arange(Sin, Send, delS)
C = ['b', 'c']
b = 0
for a in Ssteps:
    T = 20 + 273.15
    Tc = 20
    P = 10 #(dbar)
    t = Tc*1.00024
    p = P/10
    den = calc_density(a, t, p) #(kg/m3)
    PCO2 = 0.000416
    d = 0.15
    kLa = 1.5*(1.024**((Tc)-20))
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
    
    plt.xlabel('time (days)')
    plt.ylabel('CO$_2$ (g/m$^2$)')
    plt.subplot(1,2,c)
    plt.plot(t,Cdel, C[b])
    plt.plot(t,Closs, C[b], linestyle='--')
    plt.legend(['CO$_2$ supply for S = 25 g/kg', 'CO$_2$ loss for S = 25 g/kg',
                'CO$_2$ supply for S = 45 g/kg', 'CO$_2$ loss for S = 45 g/kg'],
               frameon=False, bbox_to_anchor=(.8, 1.3), bbox_transform=plt.gcf().transFigure)
    b += 1
    
plt.subplot(1,2,1)
plt.text(1, 65, str('(a) Temperature'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,2,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1, 65, str('(b) Salinity'), fontsize=10, fontweight='bold', ha='center')
plt.show()