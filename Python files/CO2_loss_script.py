#author: Riley Doyle
#date: 7/10/20
#file: CO2_loss_script
#status: NOT WORKING YET

import numpy as np
from calc_Ks import *
from calc_alphas import *
from calc_CO2_loss import *
import matplotlib.pyplot as plt

T = 20 + 273.15
S = 35
K1 = calc_K1(T,S)
pK1 = -np.log10(K1)
K2 = calc_K2(T,S)
pK2 = -np.log10(K2)
CO2sat = 0.012716352
kLa = 0.5
pHin = 6
pHend = 8
delpH = 0.1
d = 0.15

alkin = 2
alkend = 32
delalk = 5

r = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)

x_axis = r[:,1]
r = r*d 

plt.plot(x_axis, r)
plt.xlabel('pH')
plt.ylabel('CO2 loss')
plt.show()
