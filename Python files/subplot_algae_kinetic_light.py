#author: Riley Doyle
#date: 8/23/20
#file: subplot_algae_kinetic_light
#status: WORKING

#monod model

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
umax = 3.2424 #1/day
kd = 0.3 #1/day
K = 500 #g/m2
Ki = 13.9136 #W/m2

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

c = 1
I = 10 #W/m2
b = 1
plt.subplots(nrows = 1, ncols = 3, figsize=(12, 3), sharex= True, sharey= True)
plt.subplots_adjust(wspace = 0.05)
while I <= 50:
    def kinetics(s,t):
        x = s[0]
        dxdt = (((umax*I)/(I + Ki))-kd)*(1-(x/K))*x
        return [dxdt]
    
    x0 = 0.06 #g/m2
    s0 = [x0]
    t = np.linspace(0,4,100)
    n = np.arange(0, 100, 1) 
    s1 = odeint(kinetics, s0, t)
    x = s1[:,0]
    
    for i in n:
        P = s1[i]/t[i]
        def rate_kinetics(x,t):
            X = x[0]
            Caq = x[1]
            Cdel = x[2]
            Closs = x[3]
            dXdt = X*P*(1-(X/K))
            dCaqdt = -k1*P
            dCdeldt = ((k2 *Caq) - k3) + (k4*P - k5*P)
            dClossdt = (k2 *Caq) - k3
            return [dXdt, dCaqdt, dCdeldt, dClossdt]
        
        Caq0 = ((alk0 - OH + H)*alpha0/(alpha1 + 2*alpha2))*44 #g/m3
        Cin0 = 0
        Closs0 = 0 
        
        x10 = [x0, Caq0, Cin0, Closs0]
        t = np.linspace(0,4,100)
        x = odeint(rate_kinetics, x10, t)
        X = x[:,0]
        Caq = x[:,1]
        Cdel = x[:,2]
        Closs = x[:,3]
    plt.figure(b)
    plt.subplot(1, 3, c)
    plt.ylabel('CO$_2$ (g/m$^2$)')
    plt.axis([0, 3, 0, 500])
    plt.plot(t,Cdel)
    plt.plot(t, Closs)
    
    plt.figure(b+1, figsize=(12, 3))
    plt.subplot(1, 3, c)
    plt.xlabel('time (days)')
    plt.ylabel('CO$_2$ (g/m$^2$)')
    plt.axis([0, 3, 0, 4])
    plt.plot(t, Closs)
    c +=1
    I += 20
    
plt.figure(b)
plt.subplot(1,3,1)
plt.text(1.5, 550, str('(a) I = 10 W/m$^2$'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,3,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1.5, 550, str('(b) I = 20 W/m$^2$'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1.5, 550, str('(b) I = 50 W/m$^2$'), fontsize=10, fontweight='bold', ha='center')
plt.legend(['CO$_2$ supply', 'CO$_2$ loss'], frameon=False)

plt.figure(b+1)
plt.subplot(1,3,1)
plt.text(1.5, 4.3, str('(a) I = 10 W/m$^2$'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,3,2)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1.5, 4.3, str('(b) I = 20 W/m$^2$'), fontsize=10, fontweight='bold', ha='center')
plt.subplot(1,3,3)
plt.gca().axes.get_yaxis().set_visible(False)
plt.text(1.5, 4.3, str('(b) I = 50 W/m$^2$'), fontsize=10, fontweight='bold', ha='center')
plt.show()