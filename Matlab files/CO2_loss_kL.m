% author: Riley Doyle
% date: 06-09-2020
% file name: CO2_loss_kL.m
% dependencies: calc_loss_kL

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
A = 10000; %(m2) area of the pond
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
pHin = 6.5;
pHend = 8.5;
delpH = 0.1; 

kLin= 0.5; %m/day
kLend= 8.5;
delkL = 2; 

r_kL_pH = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLin, kLend, delkL);

x_axis1 = r_kL_pH(:,1);
r_kL_pH(:,1) = [];

pH = 8;
alkin=2; %eq/m3)
alkend=32;
delalk = 2;
r_kL_alk = calc_loss_kL_alk (pK1, pK2,CO2sat, alkin, alkend, delalk, kLin, kLend, delkL, pH);
x_axis2 = r_kL_alk(:,1);
r_kL_alk(:,1) = [];

%without alkalinity 
figure(1);
plot(x_axis1, r_kL_pH);
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kL = 0.5 m/day', 'kL = 2.5 m/day', 'kL = 4.5 m/day', 'kL = 6.5 m/day', 'kL = 8.5 m/day')

%without pH
figure(2)
plot(x_axis2, r_kL_alk);
xlabel('alkalinity') 
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kL = 0.5 m/day', 'kL = 2.5 m/day', 'kL = 4.5 m/day', 'kL = 6.5 m/day', 'kL = 8.5 m/day')

