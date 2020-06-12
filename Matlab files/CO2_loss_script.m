%script to calculate CO2 loss to atmosphere

%delete all figures and variables in the workspace
clear all
close all


%define variables
T = 20 + 273.15;
S = 35;
K_1 = calc_K1(T, S); 
pK1 = -log10(K_1);
K_2 = calc_K2(T, S); 
pK2 = -log10(K_2);
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
%kL = 5.6; %(m/day) from Hérron et al. (2012)
A = 10000; %(m2) area of the pond
kL = 0.96; %m/day
%alk = 2.5; %(eq/m3) from Weissman et al. (1987)
pHin = 6.5;
pHend = 8.5;
delpH = 0.1; %

alkin=2; %eq/m3)
alkend=32;
delalk = 5; %

%define r
r = calc_CO2_loss(pK1, pK2, kL, A, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
%r = calc_CO2_loss(pk1, pk2, kLa, CO2sat, pHin, pHend,delpH, alkin, alkend, delalk);

%modify r for plotting
%x axis is the first column of r
x_axis = r(:,1);
r(:,1) = [];

%plot CO2 loss vs pH for multiple alkalinities
plot(x_axis, r)

xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L','Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L', 'Alk = 32 meq/L')

