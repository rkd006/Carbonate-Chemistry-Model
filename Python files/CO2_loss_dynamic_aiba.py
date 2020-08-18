#author: Riley Doyle
#date: 8/12/20
#file: CO2_loss_dynamic_aiba
#status: WORKING

#modified aiba model

from calc_Ks import *
from calc_alphas import *
from calc_density import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

T = 20 + 273.15 #kelvins
S = 35 #g/kg
Tc = 20
P = 10 #(dbar)
t = Tc*1.00024
p = P/10
den = calc_density(S, t, p) #(kg/m3)
PCO2 = 0.000416 #atm
d = 0.15 #m
I = 30 #W/m2
kd = 0.3 #1/day
K = 80 #g/m2

kLa = 3 #1/hr
y1 = 1.714 #g CO2 per g algae
y2 = 0.1695 #g HCO3 as CO2 per g algae

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
H = (10**(-pH))*(10**3)

k1 = alpha0/(alpha1 + 2*alpha2)*y2
k2 = (kLa*d*24)
k3 = (kLa*d*24)*Csat
k4 = (y1 + y2)
k5 = y2*(alpha1 + 2*alpha2)
K1 = (200.1/24)
K2 = (0.1110/24)
k6 = (((I)/(K1 + K2*(I**2)))-kd)

K1 = (200.1/24)
K2 = (0.1110/24)
u2 = (I)/(K1 + K2*(I**2))
def kinetics(s,t):
    X = s[0]
    dXdt = (u2-kd)*(1-(X/K))*X
    return [dXdt]

X0 = 0.006 #g/m2
s0 = [X0]
t = np.linspace(0,4,100)
n = np.arange(0, 100, 1) 
s1 = odeint(kinetics, s0, t)
X = s1[:,0]

for i in n:
    P = s1[i]/t[i]
    def rate_kinetics(x,t):
        global k1, k2, k3, k4, u
        X = x[0]
        Caq = x[1]
        Cdel = x[2]
        Closs = x[3]
        dXdt = X*P*(1-(X/K))
        dCaqdt = -k1*X*P
        dCdeldt = ((k2 *Caq) - k3) + (k4*X*P - k5*X*P)
        dClossdt = (k2 *Caq) - k3
        return [dXdt, dCaqdt, dCdeldt, dClossdt]
    
    X0 = 0.006 #g/m2
    Caq0 = ((alk0 - OH + H)*alpha0/(alpha1 + 2*alpha2))*44 #g/m3
    Cin0 = 0
    Closs0 = 0 
    
    x0 = [X0, Caq0, Cin0, Closs0]
    t = np.linspace(0,4,100) 
    n = np.arange(0, 100, 1)
    x = odeint(rate_kinetics, x0, t)
    X = x[:,0]
    Caq = x[:,1]
    Cdel = x[:,2]
    Closs = x[:,3]

plt.xlabel('time (days)')
plt.ylabel('CO$_2$ (g/m$^2$)')
plt.plot(t,Cdel)
plt.plot(t, Closs)
plt.legend(['CO$_2$ supply required', 'CO$_2$ loss to atmosphere'], frameon=False)
plt.axis([0, 3, 0, 160])
plt.show()