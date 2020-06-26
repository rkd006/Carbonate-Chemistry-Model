%Author:Deborah Sills
%Date January 27 2013
%Dependent functions: calc_K1, calc_K2, calc_CO2_loss
%Inputs: T, S, pK1, pK2, CO2sat, kLa, pH, alk
%Outputs:CO2 loss to atmosphere without algae growth

%delete all figures and variables in the workspace
clear 
close all


%define variables
T = 20 + 273.15; %temp in Kelvins
S = 35; %(salinity in g/kg)
K_1 = calc_K1(T, S); 
pK1 = -log10(K_1);
K_2 = calc_K2(T, S); 
pK2 = -log10(K_2);
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
kLa = 12; %(1/day)
pHin = 6.5;
pHend = 8.5;
delpH = 0.1; 

alkin=2; % (eq/m3 or meq/L)
alkend=32;
delalk = 5; 

%define r
r = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);

%modify r for plotting
%x axis is the first column of r
x_axis = r(:,1);
r(:,1) = [];

%plot CO2 loss vs pH for multiple alkalinities
plot(x_axis, r)

xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-3} day^{-1})')
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L','Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L', 'Alk = 32 meq/L')

