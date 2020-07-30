#author: Riley Doyle
#date: 7/29/20
#file: calc_CO2_loss_sal
#status: working

import numpy as np
import matplotlib.pyplot as plt
from calc_Ks import *
from calc_alphas import *


def calc_CO2_loss_sal (pK1, pK2, alk, d, CO2sat, pHin, pHend, delpH, kLa, T, Sin, Send, delS):
    L = np.array(['-', '--', '-.', ':', '--'])
    pH = np.arange(pHin, pHend, delpH)
    Ssteps = np.arange(Sin, Send, delS)
    nSsteps = len(Ssteps)
    y = np.zeros((nSsteps, len(pH)))
    i = 0
    for c in Ssteps:
        K1 = calc_K1(T,c)
        pK1 = -np.log10(K1)
        K2 = calc_K2(T,c)
        pK2 = -np.log10(K2)
        alpha0 = calc_alpha0(pH, pK1, pK2)
        alpha1 = calc_alpha1(pH, pK1, pK2)
        alpha2 = calc_alpha2(pH, pK1, pK2)
            
        H = 10**(-pH)
        OH = 10**(-(14-pH))
        bt = (1/(alpha1 + (2*alpha2)))
        tp = (alk - OH + H)
        CT = tp * bt
            
        H2CO3 = alpha0*CT
        y[i,:] = kLa*(H2CO3 - CO2sat)*24*44
        y = y*d
        plt.plot(pH, y[i,:].T, linestyle=L[i])
        i += 1