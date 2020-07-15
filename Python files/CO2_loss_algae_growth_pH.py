#author = Riley Doyle
#date = 7/15/20
#file = CO2_loss_algae_growth_pH
#status = not working

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
y1 = 1.1403 
y2 = 0.2406
Kh = calc_Kh(T,S)
K1 = calc_K1(T, S)
pK1 = - np.log10(K1)
K2 = calc_K2(T, S)
pK2 = - np.log10(K2)

Csat = PCO2*Kh*44

alk0 = 2.5
r_algae = 10
kLa = 0.5

pHin = 6
pHend = 9
delpH = 1
pHsteps = np.arange(pHin, pHend, delpH)
C = ['k', 'b', 'r']
b = 0


for p in pHsteps:
    alpha0 = calc_alpha0(p, pK1, pK2)
    alpha1 = calc_alpha1(p, pK1, pK2)
    alpha2 = calc_alpha2(p, pK1, pK2)

    OH = 10**-(14-p)*(10**3)
    H = (10**(-p))*(10**3)
    
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
    plt.ylabel('$CO-2$ (g/$m^2$)')
    plt.plot(t,Cdel, C[b])
    plt.plot(t,Closs, C[b], linestyle='--')
    plt.legend(['$CO_2$ supply for kLa = 0.1 1/hr', '$CO_2$ loss for kLa = 0.1 1/hr',
                '$CO_2$ supply for kLa = 0.5 1/hr', '$CO_2$ loss for kLa = 0.5 1/hr' ])
    b += 1


