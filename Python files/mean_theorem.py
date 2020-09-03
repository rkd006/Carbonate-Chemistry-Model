#author: Riley Doyle
#date: 9/3/20
#file: mean_theorem
#status: WORKING

d = 0.15 #m
kd = 0 #1/day #not added yet
K = 160 #g/m2
umax = 3.2424 #1/day
Ki = 13.9136 #W/m2
I = 100 #W/m2
X0 = 0.04 #g/m2
C = ((umax*I)/(I + Ki))
dX/dt = C*(1-(X/K))*X
X = K/(np.exp(-(C*t + C1))-1)