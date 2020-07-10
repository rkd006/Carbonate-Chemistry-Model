#author: Riley Doyle
#date: 7/8/20
#file: calc_Ks
#status: working

import numpy as np

def calc_K1(T, S): #calculate K1
    K1 = np.exp((2.83655 - (2307.1266/T) - (1.5529413*(np.log(T))) - ((S**0.5)*(0.207608410 + (4.0484/T))) 
    + (0.0846834*S) - (0.00654208*(S**(3/2))) + np.log(1-(0.001005*S))))
    return(K1)
    
def calc_K2(T, S): #calculate K2
    K2 = np.exp((-9.226508 - (3351.6106/T) - (0.2005743*np.log(T)) - ((S**0.5)*(0.106901773 + (23.9722/T))) 
    + (0.1130822*S) - (0.00846934*(S**(3/2))) + np.log(1-(0.001005*S))))
    return(K2)

def calc_Kh(T, S): #calculate Kh
    Kh = np.exp(((9345.17/T) - 60.2409 + (23.3585*np.log(T/100)) + S*(0.023517 - (0.00023656*T) + 0.0047036*((T/100)**2))))
    return(Kh)