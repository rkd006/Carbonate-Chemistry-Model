%Author:Deborah Sills
%Date January 27 2013
%Dependent functions: calc_K1, calc_K2, calc_alpha0, calc_alpha1,
    %calc_alpha2
%Inputs: T, S, pK1, pK2, kL, A, CO2sat, alk, pH
%Outputs: CO2 losses to the atmosphere in mol/h

%delete figures and variables in workspace
clear 
close all

% define variables pH, pk1, pk2, CO2sat, kL, A and Alk
pH = 8;
T = 20 + 273.15;
S = 35;
K_1 = calc_K1(T, S); 
pK1 = -log10(K_1);
K_2 = calc_K2(T, S); 
pK2 = -log10(K_2);
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
kL = 0.23245276; %(m/h) from Hérron et al. (2012)
A = 1000;
alk = 2.5; %(eq/m3) from Weissman et al. (1987)

%define variables alpha0, alpha1, alpha2
alpha0 = calc_alpha0(pH, pK1, pK2);

alpha1 = calc_alpha1(pH, pK1, pK2);

alpha2 = calc_alpha2(pH, pK1, pK2);

%define variables H and OH
H = 10^(-pH);
OH = 10^(-(14-pH));

%define variable CT
CT = (alk - OH + H)/(alpha0 + alpha1 + alpha2);

%define variables H2CO3, HCO3 and CO3
H2CO3 = alpha0*CT;
HCO3 = alpha1*CT;
CO3 = alpha2*CT;

%define variable r_CO2loss, the mass transfer of CO2
r_CO2loss = kL*A*(H2CO3 - CO2sat) %moles CO2 per h
