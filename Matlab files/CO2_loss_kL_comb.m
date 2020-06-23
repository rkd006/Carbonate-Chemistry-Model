% author: Riley Doyle
% date: 06-17-2020
% file name: CO2_loss_comb.m
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

alkin=2; %(eq/m3)
alkend=22;
delalk = 5; 

kLa = .5;
r_kL_1 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);

kLa = 4.5;
r_kL_2 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);

kLa = 8.5;
r_kL_3 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);

x_axis = r_kL_1(:,1);
r_kL_1(:,1) = [];

x_axis2 = r_kL_2(:,1);
r_kL_2(:,1) = [];

x_axis3 = r_kL_3(:,1);
r_kL_3(:,1) = [];

figure(1);
plot(x_axis, r_kL_1)
hold on 
plot(x_axis2, r_kL_2, '--')
hold on
plot(x_axis3, r_kL_3, 'O-')
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kLa = .5 day^{-1}, Alk = 2 meq/L','kLa = .5 day^{-1}, Alk = 7 meq/L','kLa = .5 day^{-1}, Alk = 12 meq/L',...
    'kLa = .5 day^{-1}, Alk = 17 meq/L','kLa = .5 day^{-1}, Alk = 22 meq/L',...
    'kLa = 4.5 day^{-1}, Alk = 2 meq/L','kLa = 4.5 day^{-1}, Alk = 7 meq/L','kLa = 4.5 day^{-1}, Alk = 12 meq/L',...
    'kLa = 4.5 day^{-1}, Alk = 17 meq/L', 'kLa = 4.5 day^{-1}, Alk = 22 meq/L', 'kLa = 8.5 day^{-1}, Alk = 2 meq/L',...
    'kLa = 8.5 day^{-1}, Alk = 7 meq/L', 'kLa = 8.5 day^{-1}, Alk = 12 meq/L', 'kLa = 8.5 day^{-1}, Alk = 17 meq/L',...
    'kLa = 8.5 day^{-1} Alk = 22 meq/L')