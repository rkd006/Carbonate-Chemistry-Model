#author: Riley Doyle
#date: 7/16/20
#file: calc_CO2_loss_kLa
#status: working

import numpy as np
import matplotlib.pyplot as plt
from calc_Ks import *
from calc_alphas import *


def calc_CO2_loss_kLa (pK1, pK2, alk, d, colormap, CO2sat, pHin, pHend, delpH, kLain, kLaend, delkLa):
    #colormap = np.array(['b', 'r', 'k', 'c','y'])
    L = np.array(['-', '--', '-.', ':', '--'])
    pH = np.arange(pHin, pHend, delpH)
    kLasteps = np.arange(kLain, kLaend, delkLa)
    nkLasteps = len(kLasteps)
    y = np.zeros((nkLasteps, len(pH)))
    i = 0
    for c in kLasteps:
        alpha0 = calc_alpha0(pH, pK1, pK2)
        alpha1 = calc_alpha1(pH, pK1, pK2)
        alpha2 = calc_alpha2(pH, pK1, pK2)
            
        H = 10**(-pH)
        OH = 10**(-(14-pH))
        bt = (1/(alpha1 + (2*alpha2)))
        tp = (alk - OH + H)
        CT = tp * bt
            
        H2CO3 = alpha0*CT
        y[i,:] = c*(H2CO3 - CO2sat)*24*44
        y = y*d
        plt.plot(pH, y[i,:].T, c=colormap[i], linestyle=L[i])
        i += 1


