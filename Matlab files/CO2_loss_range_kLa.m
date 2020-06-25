% author: Riley Doyle
% date: 06-22-2020
% file name: CO2_loss_range_kLa
% dependencies: calc_loss_kL_pH, calc_K1, calc_K2
% input: T, S, pK1, pK2, CO2sat, kLa, pH, alk
% output:CO2 losses without algae growth with range of kLa

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
pHin = 8;
pHend = 8.5;
delpH = 0.1;  
alk = 2.5; %(eq/m3) from Weissman et al. (1987)

%kL = 0.04 m/hr from Weissman et. al. 1987
kLain= 0; % units of 1/hour
kLaend= 600;
delkLa = 50; 

r_range_kL = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLain, kLaend, delkLa);


x = r_range_kL(:,1);
r_range_kL(:,1) = [];

figure(1)
plot(x, r_range_kL)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-3} day^{-1})')
legend('kLa = 0 hr^{-1}','kLa = 50 hr^{-1}','kLa = 100 hr^{-1}','kLa = 150 hr^{-1}',...
    'kLa = 200 hr^{-1}','kLa = 250 hr^{-1}','kLa = 300 hr^{-1}','kLa = 350 hr^{-1}',...
    'kLa = 400 hr^{-1}','kLa = 450 hr^{-1}','kLa = 500 hr^{-1}','kLa = 550 hr^{-1}','kLa = 600 hr^{-1}')
