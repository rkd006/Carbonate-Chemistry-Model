#author = Riley Doyle
#date = 12/4/20
#file = CO2Sys_Program_pHTA
#status = working
#Taken From Pierrot, D. E. Lewis,and D. W. R. Wallace. 2006. MS Excel Program Developed for 
#CO2 System Calculations. ORNL/CDIAC-105a. Carbon Dioxide Information Analysis Center, 
#Oak Ridge National Laboratory, U.S. Department of Energy, Oak Ridge, Tennessee. 
#doi: 10.3334/CDIAC/otg.CO2SYS_XLS_CDIAC105a

import numpy as np
from CO2Sys_functions import *
from constants import *
def CO2Sys_Program_pHTA(T, S, P, TP, TSi, TA, Tout, Pout, pH):
    ## Inputs
    RGasConstant = 83.1451 
    sqrSal = np.sqrt(S)
    Tk = T + 273.15 #K
    Pbar = P/10 #bars
    RT = RGasConstant*Tk
    
    ## Constants at Input Conditions
    [K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, KSi, TS, KS, TF, KF, VPFac, FugFac, fH, pHfactor, FREEtoTOT, SWStoTOT] = constants(Tk, T, S, sqrSal, P, Pbar, RT)
    
    ## In
    TCin  = CalculateTCfromTApH(TA, pH, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    TC = TCin
    fCO2 =  CalculatefCO2fromTCpH(TC, pH, K1, K2, K0)
    pCO2 = fCO2/FugFac
    [HCO3in, CO3in, BAlkin, OHin, PAlkin, SiAlkin, Hfreein, HSO4in, HFin] = CalculateAlkParts(pH, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    CO2in = TCin - CO3in - HCO3in
    Revellein = RevelleFactor(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    [OmegaCain, OmegaArin] = CaSolubility(S, Tk, RT, TC, pH, sqrSal, T, Pbar, K0, K1, K2)
    xCO2dryin = pCO2/VPFac 
    TCin = TC
    
    #Output 
    T = Tout
    Tk = T + 273.15 #K
    P = Pout #dbars
    Pbar = P/10 #bars
    RT = RGasConstant*Tk
    ## Constants at Ouput Conditions
    [K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, KSi, TS, KS, TF, KF, VPFac, FugFac, fH, pHfactor, FREEtoTOT, SWStoTOT] = constants(Tk, T, S, sqrSal, P, Pbar, RT)
    
    ## Out
    TCout = TC
    fCO2out =  CalculatefCO2fromTCpH(TC, pH, K1, K2, K0)
    pCO2out = fCO2out/FugFac
    [HCO3out, CO3out, BAlkout, OHout, PAlkout, SiAlkout, Hfreeout, HSO4out, HFout] = CalculateAlkParts(pH, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    CO2out = TCout - CO3out - HCO3out
    Revelleout = RevelleFactor(TA, TC, K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, TP, TSi, KSi, TS, KS, TF, KF)
    [OmegaCaout, OmegaArout] = CaSolubility(S, Tk, RT, TC, pH, sqrSal, T, Pbar, K0, K1, K2)
    xCO2dryout = pCO2out/VPFac 
    return [K1, K0, K2, TB, KB, KW, KP1, KP2, KP3, KSi, TS, KS, TF, KF, VPFac, FugFac, fH, pHfactor, FREEtoTOT, SWStoTOT, HCO3in, CO3in, BAlkin, OHin, PAlkin, SiAlkin, Hfreein, HSO4in, HFin, HCO3out, CO3out, BAlkout, OHout, PAlkout, SiAlkout, Hfreeout, HSO4out, HFout, TA, TC, Revellein, OmegaCain, OmegaArin,xCO2dryin, Revelleout, OmegaCaout, OmegaArout,xCO2dryout, CO2in, CO2out, pH, pCO2out]