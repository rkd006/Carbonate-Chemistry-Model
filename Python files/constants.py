#author = Riley Doyle
#date = 11/21/20
#file = constants
#status = working
import numpy as np

def constants(Tk, T, S, sqrSal, P, Pbar, RT):
    #K1 and K2 from Mehrback refit  by Dickson and Millero
    pK1 = 3670.7/Tk - 62.008 + 9.7944*np.log(Tk) - 0.0118*S + 0.000116*S**2
    K1 = 10**(-pK1)
    pK2 = 1394.7/Tk + 4.777 - 0.0184*S + 0.000118*S**2
    K2 = 10**(-pK2)
    ## KSO4 from Dickson and TB from Upstorm
    TB = 0.0004157*S/35 #mol/kg SW
    TF = (0.000067/18.998)*(S/1.80655) #mol/kg SW
    TS = (0.14/96.062)*(S/1.80655) #mol/kg SW
    TK100 = Tk/100
    lnK0 = -60.2409 + 93.451/TK100 + 23.3585*np.log(TK100) + S*(0.023517 - 0.023656 * TK100 + 0.0047036 * TK100**2) #mol/kg SW/atm
    K0 = np.exp(lnK0)
    IonS = 19.924*S / (1000 - 1.005*S)
    lnKS = -4276.1/Tk + 141.328 - 23.093*np.log(Tk) +(-13856/Tk + 324.57 - 47.986*np.log(Tk))*np.sqrt(IonS) +(35474/Tk - 771.54 + 114.723*np.log(Tk))*IonS +(-2698/Tk)*np.sqrt(IonS)*IonS + (1776/Tk)*IonS**2
    KS = np.exp(lnKS)* (1 - 0.001005* S) 
    lnKF = 1590.2/Tk - 12.641 + 1.525*IonS**0.5
    KF   = np.exp(lnKF)*(1 - 0.001005*S)
    SWStoTOT  = (1 + TS/KS)/(1 + TS/KS + TF/KF)
    FREEtoTOT =  1 + TS/KS
    fH = 1.2948 - 0.002036*Tk + (0.0004607 - 0.000001475*Tk)*S**2
    lnKBtop = -8966.9 - 2890.53*sqrSal - 77.942*S +1.728*sqrSal*S - 0.0996*S**2
    lnKB = lnKBtop/Tk + 148.0248 + 137.1942*sqrSal +1.62142*S + (-24.4344 - 25.085*sqrSal - 0.2474*S)*np.log(Tk) + 0.053105*sqrSal*Tk
    KB = np.exp(lnKB)/SWStoTOT
    lnKW = 148.9802 - 13847.26/Tk - 23.6521*np.log(Tk) +(-5.977 + 118.67/Tk + 1.0495*np.log(Tk))*sqrSal - 0.01615*S
    KW = np.exp(lnKW)
    lnKP1 = -4576.752/Tk + 115.54 - 18.453*np.log(Tk) + (-106.736/Tk +0.69171)*sqrSal + (-0.65643/Tk - 0.01844)*S
    KP1 = np.exp(lnKP1)
    lnKP2 = -8814.715/Tk + 172.1033 - 27.927*np.log(Tk) + (-160.34/Tk +1.3566)*sqrSal + (0.37335/Tk- 0.05778)*S
    KP2 = np.exp(lnKP2)
    lnKP3 = -3070.75/Tk - 18.126 + (17.27039/Tk + 2.81197)*sqrSal +(-44.99486/Tk - 0.09984)*S
    KP3 = np.exp(lnKP3)
    lnKSi = -8904.2/Tk + 117.4 - 19.334*np.log(Tk) + (-458.79/Tk +3.5913)*np.sqrt(IonS) + (188.74/Tk - 1.5998)*IonS+(-12.1652/Tk + 0.07871)*IonS**2
    KSi = np.exp(lnKSi)*(1 - 0.001005*S)
    deltaV  = -25.5 + 0.1271*T
    Kappa   = (-3.08 + 0.0877*T)/1000
    lnK1fac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    deltaV  = -15.82 - 0.0219*T
    Kappa = (1.13 - 0.1475*T)/1000
    lnK2fac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects on KB
    deltaV  = -29.48 + 0.1622*T - 0.002608*T**2
    Kappa   = -2.84/1000
    lnKBfac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects on KW
    deltaV  = -20.02 + 0.1119*T - 0.001409*T**2
    Kappa   = (-5.13 + 0.0794*T)/1000
    lnKWfac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects on KF
    deltaV = -9.78 - 0.009*T - 0.000942*T**2
    Kappa = (-3.91 + 0.054*T)/1000
    lnKFfac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects on KS
    deltaV = -18.03 + 0.0466*T + 0.000316*T**2
    Kappa = (-4.53 + 0.09*T)/1000
    lnKSfac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects On KP1
    deltaV = -14.51 + 0.1211*T - 0.000321*T**2
    Kappa  = (-2.67 + 0.0427*T)/1000
    lnKP1fac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects On KP2
    deltaV = -23.12 + 0.1758*T - 0.002647*T**2
    Kappa  = (-5.15 + 0.09*T)/1000
    lnKP2fac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Pressure Effects On KP3
    deltaV = -26.57 + 0.202*T - 0.003042*T**2
    Kappa  = (-4.08 + 0.0714*T)/1000
    lnKP3fac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    #Presure Effects on KSi
    deltaV = -29.48 + 0.1622*T - 0.002608*T**2
    Kappa  = -2.84/1000
    lnKSifac = (-deltaV + 0.5*Kappa*Pbar)*Pbar/RT
    # Correct Ks for Pressure
    K1fac  = np.exp(lnK1fac)
    K1  = K1*K1fac
    K2fac  = np.exp(lnK2fac)
    K2  = K2*K2fac
    KWfac  = np.exp(lnKWfac)
    KW  = KW*KWfac
    KBfac  = np.exp(lnKBfac)
    KB  = KB*KBfac
    KFfac  = np.exp(lnKFfac)
    KF  = KF*KFfac
    KSfac  = np.exp(lnKSfac)
    KS  = KS*KSfac
    KP1fac = np.exp(lnKP1fac)
    KP1 = KP1*KP1fac
    KP2fac = np.exp(lnKP2fac)
    KP2 = KP2*KP2fac
    KP3fac = np.exp(lnKP3fac)
    KP3 = KP3*KP3fac
    KSifac = np.exp(lnKSifac)
    KSi = KSi*KSifac
    # Correct pHScale Conversions For Pressure
    SWStoTOT  = (1 + TS/KS)/(1 + TS/KS + TF/KF)
    FREEtoTOT =  1 + TS/KS
    pHfactor = 1
    # Calculate Fugacity Constants
    Delta = (57.7 - 0.118*Tk)
    b = -1636.75 + 12.0408*Tk - 0.0327957*Tk**2 + 3.16528*0.00001*Tk**3
    P1atm = 1.01325
    FugFac = np.exp((b + 2*Delta)*P1atm/RT)
    # Calculate VPFac
    VPWP = np.exp(24.4543 - 67.4509*(100/Tk) - 4.8489*np.log(Tk/100))
    VPCorrWP = np.exp(-0.000544*S)
    VPSWWP = VPWP*VPCorrWP
    VPFac = 1 - VPSWWP # this assumes 1 atmosphere
    return [K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, KSi, TS, KS, TF, KF, VPFac, FugFac, fH, pHfactor, FREEtoTOT, SWStoTOT]