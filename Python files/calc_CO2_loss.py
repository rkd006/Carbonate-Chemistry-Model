#author: Riley Doyle
#date: 7/10/20
#file: calc_CO2_loss
#status: NOT WORKING YETa

import numpy as np
import matplotlib.pyplot as plt
from calc_Ks import *
from calc_alphas import *


def calc_CO2_loss(pK1, pK2, kLa, d, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk):
    pH = np.arange(pHin, pHend, delpH)
    alksteps = np.arange(alkin, alkend, delalk)
    nalksteps = len(alksteps)
    y = np.zeros((nalksteps, len(pH)))
    i = 0
    for c in alksteps:
        alpha0 = calc_alpha0(pH, pK1, pK2)
        alpha1 = calc_alpha1(pH, pK1, pK2)
        alpha2 = calc_alpha2(pH, pK1, pK2)
            
        H = 10**(-pH)
        OH = 10**(-(14-pH))
        bt = (1/(alpha1 + (2*alpha2)))
        tp = (c - OH + H)
        CT = tp * bt
            
        H2CO3 = alpha0*CT
        y[i,:] = kLa*(H2CO3 - CO2sat)*24*44
        i += 1
    y = y*d
    plt.plot(pH, y.T )