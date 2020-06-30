% author: Riley Doyle
% date: 06-17-2020
% file name: CO2_loss_kL.m
% dependencies: calc_loss_kL_pH, calc_loss_kL_alk, calc_K1, calc_K2
% input: T, S, pK1, pK2, CO2sat, kLa, pH, alk
% output: CO2 losses without algae growth with different pH and alk separately

%delete all figures and variables in the workspace
clear 
close all

%define variables
T = 20 + 273.15; %temp in Kelvin
S = 35; %(salinity in g/kg)
K_1 = calc_K1(T, S); 
pK1 = -log10(K_1);
K_2 = calc_K2(T, S); 
pK2 = -log10(K_2);
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
pHin = 6.5;
pHend = 8.5;
delpH = 0.1; 

kLain= 0.5; % (1/hour)
kLaend= 8.5;
delkLa = 2; 

r_kL_pH = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLain, kLaend, delkLa);

x = r_kL_pH(:,1);
r_kL_pH(:,1) = [];


pH = 8;
alkin=2; % (eq/m3)
alkend=32;
delalk = 2;
r_kL_alk = calc_loss_kL_alk (pK1, pK2, CO2sat, alkin, alkend, delalk, kLain, kLaend, delkLa, pH);
x2 = r_kL_alk(:,1);
r_kL_alk(:,1) = [];

%without alkalinity 
figure(1);
plot(x, r_kL_pH);
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kLa = 0.5 1/day', 'kLa = 2.5 1/day', 'kLa = 4.5 1/day', 'kLa = 6.5 1/day', 'kLa = 8.5 1/day')

%without pH
figure(2)
plot(x2, r_kL_alk);
xlabel('alkalinity') 
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kLa = 0.5 1/day', 'kLa = 2.5 1/day', 'kLa = 4.5 1/day', 'kLa = 6.5 1/day', 'kLa = 8.5 1/day')


