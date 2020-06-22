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
alkend=32;
delalk = 10; 

kL = .5;
r_kL_1 = calc_CO2_loss(pK1, pK2, kL, a, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);

kL = 4.5;
r_kL_2 = calc_CO2_loss(pK1, pK2, kL, a, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);

kL = 8.5;
r_kL_3 = calc_CO2_loss(pK1, pK2, kL, a, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);

x_axis = r_kL_1(:,1);
r_kL_1(:,1) = [];

%combine figure 1 and 2 
figure(1);
plot(x_axis, r_kL_1)
hold on 
plot(x_axis, r_kL_2)
hold on
plot(x_axis, r_kL_3)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kL = .5 m/day, Alk = 2 meq/L','kL = .5 m/day, Alk = 7 meq/L','kL = .5 m/day, Alk = 12 meq/L',...
    'kL = .5 m/day, Alk = 17 meq/L','kL = .5 m/day, Alk = 22 meq/L','kL = .5 m/day, Alk = 27 meq/L'...
    , 'kL = .5 m/day, Alk = 32 meq/L', 'kL = 4.5 m/day, Alk = 2 meq/L','kL = 4.5 m/day, Alk = 7 meq/L','kL = 4.5 m/day, Alk = 12 meq/L',...
    'kL = 4.5 m/day, Alk = 17 meq/L','kL = 4.5 m/day, Alk = 22 meq/L','kL = 4.5 m/day, Alk = 27 meq/L'...
    , 'kL = 4.5 m/day, Alk = 32 meq/L', 'kL = 8.5 m/day, Alk = 2 meq/L','kL = 8.5 m/day, Alk = 7 meq/L','kL = 8.5 m/day, Alk = 12 meq/L',...
    'kL = 8.5 m/day, Alk = 17 meq/L','kL = 8.5 m/day, Alk = 22 meq/L','kL = 8.5 m/day, Alk = 27 meq/L'...
    , 'kL = 8.5 m/day, Alk = 32 meq/L')
