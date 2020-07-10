#author: Riley Doyle
#date: 7/8/20
#file: calc_alphas
#status: working

def calc_alpha0(pH, pK1, pK2):
#calculate alpha0

    alpha0 = 1 /( ((1 + ((10**(-pK1)))/(10**(-pH))) + ((10**(-pK1))*(10**(-pK2))/((10**(-pH))**2))))
    return alpha0

def calc_alpha1(pH, pK1, pK2):
#calculate alpha1

    alpha1 = 1/(10**(-pH)/10**(-pK1) + 1 + 10**(-pK2)/10**(-pH))
    return alpha1

def calc_alpha2(pH, pK1, pK2):
#calculate alpha2

    alpha2 = 1/(1 + 10**(-pH)/10**(-pK2) + (10**(-pH))**2/10**(-pK1)/10**(-pK2))
    return alpha2

