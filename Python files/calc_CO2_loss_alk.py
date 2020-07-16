#author: Riley Doyle
#date: 7/16/20
#file: calc_CO2_loss_alk
#status:working

import numpy as np
import matplotlib.pyplot as plt
from calc_Ks import *
from calc_alphas import *


def calc_CO2_loss_alk (pK1, pK2, pH, d, CO2sat, alkin, alkend, delalk, kLain, kLaend, delkLa):
    alk = np.arange(alkin, alkend, delalk)
    kLasteps = np.arange(kLain, kLaend, delkLa)
    nkLasteps = len(kLasteps)
    y = np.zeros((nkLasteps, len(alk)))
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
        i += 1
    y = y*d
    plt.plot(alk, y.T )