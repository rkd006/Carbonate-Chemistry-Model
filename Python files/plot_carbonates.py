#author: Riley Doyle
#date: 7/9/20
#file: plot_carbonates
#status: working

import matplotlib.pyplot as plt
import numpy
import math
from calc_Ks import *
from calc_alphas import *

pH_start = 2
pH_end = 14

T = 20 + 273.15
S = 35
K_1 = calc_K1(T,S)
pK1 = -math.log10(K_1)
K_2 = calc_K2(T,S)
pK2 = -math.log10(K_2)

vpH = numpy.linspace(pH_start, pH_end)

p = len(vpH)

H2CO3 = numpy.zeros([p,1])
HCO3 = numpy.zeros([p,1])
CO3 = numpy.zeros([p,1])

for n in range(0,p):
    H2CO3 = calc_alpha0(vpH, pK1, pK2)
    HCO3 = calc_alpha1(vpH, pK1, pK2)
    CO3 = calc_alpha2(vpH, pK1, pK2)

vpH = numpy.transpose(vpH)
carbonates = numpy.concatenate((H2CO3, HCO3, CO3))

x_axis = vpH

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x_axis, H2CO3, label='$H_{2}CO_{3}$')
ax.plot(x_axis, HCO3, 'r', label='$HCO_3^{-}$')
ax.plot(x_axis, CO3, 'k', label='$CO_3^{-2}$')
ax.set_xticks([2,4,6,8,10,12,14])
ax.legend()
plt.xlabel('pH')
plt.ylabel('Fraction Carbonate Species')
plt.show()



