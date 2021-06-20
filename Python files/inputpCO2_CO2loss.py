#author: Riley Doyle
#date: 6/20/21
#file: inputpCO2_CO2loss
#status: WORKING

from calc_Ks import *
from calc_alphas import *
from calc_density import *
from CO2Sys_functions import *
from constants import *
from CO2Sys_Program_TApCO2 import *
import numpy as np
from scipy.integrate import odeint

def inputpCO2_CO2loss(Tc, S, P, TP, TSi, TA, pCO2, Tout, Pout, den, kLa, d, y1, y2, Csat, umax, I, kd, K, Ki):
    CO2Sys = CO2Sys_Program_TApCO2(Tc, S, P, TP, TSi, TA, pCO2, Tout, Pout)
    K1 = CO2Sys[0]
    K2 = CO2Sys[2]
    Caqout = (CO2Sys[49])*(den)
    pK1 = - np.log10(K1)
    pK2 = - np.log10(K2)
    pH = CO2Sys[51]
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
    
    def rate_kinetics(x,t):
        X = x[0]
        P = x[1]
        Caq = x[2]
        Cdel = x[3]
        Closs = x[4]
        dXdt = (((umax*I)/(I + Ki))-kd)*(1-(X/K))*X
        dPdt = dXdt
        dCaqdt = -k1*P
        dCdeldt = ((k2 *Caq) - k3) + (k4*P - k5*P)
        dClossdt = (k2 *Caq) - k3
        return [dXdt, dPdt, dCaqdt, dCdeldt, dClossdt]
            
    Caq0 = Caqout*44 #g/m3
    Cin0 = 0
    Closs0 = 0 
    X0 = 0.04
    P0 = 0
    x0 = [X0, P0, Caq0, Cin0, Closs0]
    t = np.linspace(0,3,100)
    x = odeint(rate_kinetics, x0, t)
    
    X = x[:,0]
    P = x[:, 1]
    Caq = x[:,2]
    Cdel = x[:,3]
    Closs = x[:,4]
    return [t, X, P, Caq, Cdel, Closs]