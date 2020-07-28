#author = Riley Doyle
#date = 7/15/20
#file = CO2_loss_algae_growth_pH
#status = working

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

alk0 = 2.5
r_algae = 10
kLa = 0.1
delkLa = 0.4

while kLa <= .5:
    pH = 6
    delpH = 1
    C = ['k', 'b', 'r']
    b = 0
    while pH <= 8:
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
        
        plt.figure()
        plt.plot(t,Cdel, C[b])
        plt.plot(t,Closs, C[b], linestyle='--')
        plt.xlabel('time (days)')
        plt.ylabel('$CO_2$ (g/$m^2$)')
        plt.axis([0, 4, 0, 700])
        plt.legend(['$CO_2$ supply', '$CO_2$ loss'])
        plt.subplot(1, 2, 1)
        plt.subplot(1, 2, 2)

        b += 1
        pH += delpH
    plt.figure()
    kLa += delkLa
