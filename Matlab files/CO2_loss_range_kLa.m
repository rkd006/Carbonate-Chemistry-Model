% author: Riley Doyle
% date: 06-22-2020
% file name: CO2_loss_range_kLa
% dependencies: calc_CO2_loss, calc_K1, calc_K2

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
a = 1000;
pHin = 6.5;
pHend = 8.5;
delpH = 0.1;  
alk = 2.5;

kLain= 0; %1/hour
kLaend= 600;
delkLa = 50; 

r_range_kL = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLain, kLaend, delkLa);

x = r_range_kL(:,1);
r_range_kL(:,1) = [];

figure(1)
plot(x, r_range_kL)