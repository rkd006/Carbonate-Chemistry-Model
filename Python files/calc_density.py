# author: Riley Doyle
# date: 8/4/20
# file name: calc_density
#output: Calculate density of seawater
# from UNESCO,1983
#valid for salinities between 0 and 42, temperatures between 2 and 40 [◦C] and pressures
#between 0 and 10000

def calc_density(S, t, p):
    Bw = (8.50935*10**(-5))+ (-6.12293*10**(-6))*t + (5.2787*10**(-8))*(t**2)
    Aw = 3.239908 + (1.43713*10**(-3))*t + (1.16092*10**(-4))*(t**2) + (-5.77905*10**(-7))*(t**3)
    Kw = 19652.21 + 148.4206*t + -2.327105*(t**2) + (1.360477*10**(-2))*(t**3) + (-5.155288*10**(-5))*(t**4)
    B = Bw + ((-9.9348*10**(-7)) + (2.0816*10**(-8))*t + (9.1697*10**(-10))*(t**2))*S
    A = Aw + ((2.2838*10**(-3)) + (-1.0981*10**(-5))*t + (-1.6078*10**(-6))*(t**2))*S + (1.91075*10**(-4))*(S**(3/2))
    K0 = Kw + ((54.6746) + (-0.603459)*t + (1.09987*10**(-2))*(t**2) + (-6.1670*10**(-7))*(t**3))*S + ((7.944*10**(-2)) + (1.6483*10**(-2))*t + (-5.3009*10**(-4))*(t**2))*(S**(3/2))
    Kp = K0 + A*p + B*(p**2)
    pw = 999.842594 + (6.793952*10**(-2))*t + (-9.095290*10**(-3))*(t**2) + (1.001685*10**(-4))*(t**3) + (-1.120083*10**(-6))*(t**4) + (6.536332*10**(-9))*(t**5)
    p0 = pw + ((8.24493*10**(-1)) + (-4.0899*10**(-3))*t + (7.6438*10**(-5))*(t**2) + (-8.2467*10**(-7))*(t**3) + (5.3875*10**(-9))*(t**4))*S + ((-5.72466*10**(-3)) + (1.0227*10**(-4))*t + (-1.6546*10**(-6))*(t**2))*(S**(3/2)) + (4.8314*10**(-4))*(S**2)
    den = (p0)/(1-(p/Kp))
    return (den)