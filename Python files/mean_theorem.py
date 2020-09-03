#author: Riley Doyle
#date: 9/3/20
#file: mean_theorem
#status: NOT WORKING

import numpy as np
import scipy.integrate as integrate

#define variables
kd = 0 #1/day #not added yet
K = 160 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
I = 100 #W/m2
C = ((umax*I)/(I + Ki))

#solve for C1
t = 0
X = 0.04 #g/m2
C1 = -(np.log10((K/X)+1) + C*t)


#function for biomass density
X = lambda x:(K/(np.exp(-(C*t + C1)) - 1))

#limits
a = 0
b = 4

integral = integrate.quad(X, a, b)
print (integral)

meanbiomass = (1/(b - a))*integral[0]
print (meanbiomass)