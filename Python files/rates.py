#author: Riley Doyle
#date: 7/15/20
#file: rates
#status:WORKING

def rates(x,t):
    global k1, k2, k3, k4
    Caq = x[0]
    Cdel = x[1]
    Closs = x[2]
    dCaqdt = -k1
    dCdeldt = ((k2 *Caq) - k3) + k4
    dClossdt = (k2 *Caq) - k3
    return [dCaqdt, dCdeldt, dClossdt]
