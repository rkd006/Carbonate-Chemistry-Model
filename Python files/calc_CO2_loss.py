#author: Riley Doyle
#date: 7/10/20
#file: calc_CO2_loss
#status: NOT WORKING YET

import numpy as np
from calc_Ks import *
from calc_alphas import *

def calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk):
    m_steps = ((alkend-alkin)//delalk)
    alk = alkin
    n_steps = ((pHend - pHin)//delpH)
    r = np.zeros(shape= n_steps, m_steps, dtype = int)
    for p in range(0,m_steps):
        pH = pHin
        for c in range(0,n_steps):
            alpha0 = calc_alpha0(pH, pK1, pK2)
            alpha1 = calc_alpha1(pH, pK1, pK2)
            alpha2 = calc_alpha2(pH, pK1, pK2)
            
            H = 10**(-pH)
            OH = 10**(-(14-pH))
            bt = (1/(alpha1 + (2*alpha2)))
            tp = (alk - OH + H)
            CT = tp * bt
            
            H2CO3 = alpha0*CT
            
            loss = kLa*(H2CO3 - CO2sat)*24*44
            r(c,0) = pH
            r(c,p) = loss
            pH = pH +delpH
        alk = alk + delalk

