#author = Riley Doyle
#date = 11/21/20
#file = CO2Sys_functions
#status = working
## Functions for CO2Sys
import numpy as np

def CalculatepHfCO2fromTATC(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
# Inputs: pHScale%, WhichKs%, WhoseKSO4%, TA, TC, Sal, K(), T(), TempC, Pdbar
# Outputs: pH, fCO2
# This calculates pH and fCO2 from TA and TC at output conditions.
    pH   = CalculatepHfromTATC(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    fCO2 = CalculatefCO2fromTCpH(TC, pH, K1, K2, K0)
    return [pH, fCO2]


def CalculatepHfromTATC(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
    # This calculates pH from TA and TC using K1 and K2 by Newton's method.
    pHGuess     = 8
    pHTol       = 0.0001
    ln10        = np.log(10)
    pH = pHGuess
    deltapH     = pHTol+1
    while np.any(np.abs(deltapH) > pHTol):
        H         = 10**(-pH)
        Denom     = (H*H + K1*H + K1*K2)
        CAlk      = TC*K1*(H + 2*K2)/Denom
        BAlk      = TB*KB/(KB + H)
        OH        = KW/H
        PhosTop   = KP1*KP2*H + 2*KP1*KP2*KP3 - H*H*H
        PhosBot   = H*H*H + KP1*H*H + KP1*KP2*H + KP1*KP2*KP3
        PAlk      = TP*PhosTop/PhosBot
        SiAlk     = TSi*KSi/(KSi + H)
        FREEtoTOT = (1 + TS/KS)
        Hfree     = H/FREEtoTOT
        HSO4      = TS/(1 + KS/Hfree)
        HF        = TF/(1 + KF/Hfree)
        Residual  = TA- CAlk - BAlk - OH - PAlk - SiAlk + Hfree + HSO4 + HF
        Slope     = ln10*(TC*K1*H*(H*H + K1*K2 + 4*H*K2)/Denom/Denom + BAlk*H/(KB + H) + OH + H)
        deltapH   = Residual/Slope
        while np.any(np.abs(deltapH) > 1):
            deltapH =deltapH/2
        pH = pH + deltapH
    return pH

def CalculatefCO2fromTCpH(TC, pH, K1, K2, K0):
    #This calculates fCO2 from TC and pH, using K0, K1, and K2.
    H  = 10**(-pH)
    fCO2 = TC*H*H/(H*H + K1*H + K1*K2)/K0
    return fCO2
    
def CalculateTCfromTApH(TA, pH, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
    #This calculates TC from TA and pH.
    H         = 10**(-pH)
    BAlk      = TB*KB/(KB + H)
    OH        = KW/H
    PhosTop   = KP1*KP2*H + 2*KP1*KP2*KP3 - H*H*H
    PhosBot   = H*H*H + KP1*H*H + KP1*KP2*H + KP1*KP2*KP3
    PAlk      = TP*PhosTop/PhosBot
    SiAlk     = TSi*KSi/(KSi + H)
    FREEtoTOT = (1 + TS/KS)
    Hfree     = H/FREEtoTOT
    HSO4      = TS/(1 + KS/Hfree)
    HF        = TF/(1 + KF/Hfree)
    CAlk      = TA - BAlk - OH - PAlk - SiAlk + Hfree + HSO4 + HF
    TC   = CAlk*(H*H + K1*H + K1*K2)/(K1*(H + 2*K2))
    return TC

def CalculatepHfromTAfCO2(TA, fCO2,K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
    # This calculates pH from TA and fCO2 using K1 and K2 by Newton's method.
    pHGuess    = 8
    pHTol      = 0.0001
    ln10       = np.log(10)
    pH = pHGuess
    deltapH = pHTol+pH
    while np.any(np.abs(deltapH) > pHTol):
        H         = 10**(-pH)
        HCO3      = (K0*K1*fCO2)/H
        CO3       = (K0*K1*K2*fCO2)/(H*H)
        CAlk      = HCO3 + 2*CO3
        BAlk      = TB*KB/(KB + H)
        OH        = KW/H
        PhosTop   = KP1*KP2*H + 2*KP1*KP2*KP3 - H*H*H
        PhosBot   = H*H*H + KP1*H*H + KP1*KP2*H + KP1*KP2*KP3
        PAlk      = TP*PhosTop/PhosBot
        SiAlk     = TSi*KSi/(KSi + H)
        FREEtoTOT = (1 + TS/KS)
        Hfree     = H/FREEtoTOT
        HSO4      = TS/(1 + KS/Hfree)
        HF        = TF/(1 + KF/Hfree)
        Residual  = TA - CAlk - BAlk - OH - PAlk - SiAlk + Hfree + HSO4 + HF
        Slope     = ln10*(HCO3 + 4*CO3 + BAlk*H/(KB + H) + OH + H)
        deltapH   = Residual/Slope
        while np.any(np.abs(deltapH) > 1):
            deltapH=deltapH/2
        pH = pH + deltapH
    return pH

def CalculateTAfromTCpH(TC, pH,K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
    #This calculates TA from TC and pH.
    H         = 10**(pH)
    CAlk      = TC*K1*(H + 2*K2)/(H*H + K1*H + K1*K2)
    BAlk      = TB*KB/(KB + H)
    OH        = KW/H
    PhosTop   = KP1*KP2*H + 2*KP1*KP2*KP3 - H*H*H
    PhosBot   = H*H*H + KP1*H*H + KP1*KP2*H + KP1*KP2*KP3
    PAlk      = TP*PhosTop/PhosBot
    SiAlk     = TSi*KSi/(KSi + H)
    FREEtoTOT = (1 + TS/KS)
    Hfree     = H/FREEtoTOT
    HSO4      = TS/(1 + KS/Hfree)
    HF        = TF/(1 + KF/Hfree)
    TA    = CAlk + BAlk + OH + PAlk + SiAlk - Hfree - HSO4 - HF
    return TA

def CalculatepHfromTCfCO2(TC, fCO2, K1, K2, K0):
    #This calculates pH from TC and fCO2 using K0, K1, and K2 by solving the
    #quadratic in H: fCO2.*K0 = TC.*H.*H./(K1.*H + H.*H + K1.*K2).
    RR = K0*fCO2/TC
    Discr = (K1*RR)*(K1*RR) + 4*(1 - RR)*(K1*K2*RR)
    H = 0.5*(K1*RR + np.sqrt(Discr))/(1 - RR)
    pH = np.log(H)/np.log(0.1)
    return pH

def CalculateTCfrompHfCO2(pH, fCO2, K1, K2, K0):
    #This calculates TC from pH and fCO2, using K0, K1, and K2.
    H       = 10**(-pH)
    TC = K0*fCO2*(H*H + K1*H + K1*K2)/(H*H)
    return TC

def RevelleFactor(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
    TC0 = TC
    dTC = 0.000001
    TC = TC0 + dTC
    pH= CalculatepHfromTATC(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    fCO2c= CalculatefCO2fromTCpH(TC, pH, K1, K2, K0)
    fCO2plus = fCO2c
    TC = TC0 - dTC
    pH= CalculatepHfromTATC(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    fCO2c= CalculatefCO2fromTCpH(TC, pH, K1, K2, K0)
    fCO2minus = fCO2c
    Revelle = (fCO2plus - fCO2minus)/dTC/((fCO2plus + fCO2minus)/TC)
    return Revelle

def CalculateAlkParts(pH, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF):
    #This calculates the various contributions to the alkalinity
    H         = 10**(-pH)
    HCO3      = TC*K1*H/(K1*H + H*H + K1*K2)
    CO3       = TC*K1*K2/(K1*H + H*H + K1*K2)
    BAlk      = TB*KB/(KB + H)
    OH        = KW/H
    PhosTop   = KP1*KP2*H + 2*KP1*KP2*KP3 - H*H*H
    PhosBot   = H*H*H + KP1*H*H + KP1*KP2*H + KP1*KP2*KP3
    PAlk      = TP*PhosTop/PhosBot
    SiAlk     = TSi*KSi/(KSi + H)
    FREEtoTOT = (1 + TS/KS)
    Hfree     = H/FREEtoTOT
    HSO4      = TS/(1 + KS/Hfree); 
    HF        = TF/(1 + KF/Hfree); 
    return [HCO3, CO3, BAlk, OH, PAlk, SiAlk, Hfree, HSO4, HF]

def CaSolubility(S, Tk, RT, TC, pH, sqrSal, T, Pbar, K0, K1, K2):
    Ca = 0.02128/40.087*(S/1.80655)
    logKCa = -171.9065 - 0.077993*Tk + 2839.319/Tk
    logKCa = logKCa + 71.595*np.log(Tk)/np.log(10)
    logKCa = logKCa + (-0.77712 + 0.0028426*Tk + 178.34/Tk)*sqrSal
    logKCa = logKCa - 0.07711*S + 0.0041249*sqrSal*S
    KCa = 10**(logKCa)
    logKAr = -171.945 - 0.077993*Tk + 2903.293/Tk
    logKAr = logKAr + 71.595*np.log(Tk)/np.log(10)
    logKAr = logKAr + (-0.068393 + 0.0017276*Tk + 88.135/Tk)*sqrSal
    logKAr = logKAr - 0.10018*S + 0.0059415*sqrSal*S
    KAr    = 10**(logKAr)
    #Pressure Correction
    deltaVKCa = -48.76 + 0.5304*T
    KappaKCa  = (-11.76 + 0.3692*T)/1000
    lnKCafac  = (-deltaVKCa + 0.5*KappaKCa*Pbar)*Pbar/RT
    KCa       = KCa*np.exp(lnKCafac)
    deltaVKAr = deltaVKCa + 2.8
    KappaKAr  = KappaKCa
    lnKArfac  = (-deltaVKAr + 0.5*KappaKAr*Pbar)*Pbar/RT
    KAr       = KAr*np.exp(lnKArfac)
    H = 10**(-pH)
    CO3 = TC*K1*K2/(K1*H + H*H + K1*K2)
    omegaCa = CO3*Ca/KCa
    omegaAr = CO3*Ca/KAr
    return [omegaCa, omegaAr]

def FindpHOnAllScales(pH, pHScale, TS, KS, TF, KF, fH):
    #This takes the pH on the given scale and finds the pH on all scales.
    FREEtoTOT = (1 + TS/KS)
    SWStoTOT  = (1 + TS/KS)/(1 + TS/KS + TF/KF)
    if pHScale==1:
        factor = 0
    elif pHScale==2: #"pHsws"
        factor = -np.log(SWStoTOT)/np.log(0.1)
    elif pHScale==3: #"pHfree"
        factor = -np.log(FREEtoTOT)/np.log(0.1)
    elif pHScale==4:  #"pHNBS"
        factor = -np.log(SWStoTOT)/np.log(0.1) + np.log(fH)/np.log(0.1)
    pHtot  = pH    - factor
    pHNBS  = pHtot - np.log(SWStoTOT)/np.log(0.1) + np.log(fH)/np.log(0.1)
    pHfree = pHtot - np.log(FREEtoTOT)/np.log(0.1)
    pHsws  = pHtot - np.log(SWStoTOT)/np.log(0.1)
    return [pHtot, pHsws, pHfree, pHNBS]
