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
pHin = 7.5;
pHend = 8.5;
delpH = 0.1;  
%alk = 2.5; %(eq/m3) from Weissman et al. (1987)
alk = 2;

%kL = 0.04 m/hr from Weissman et. al. 1987
kLain= 0.5; % units of 1/hour
kLaend= 200.5;
delkLa = 20; 

r_range_kL = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLain, kLaend, delkLa);

x = r_range_kL(:,1);
r_range_kL(:,1) = [];
CO2_loss = r_range_kL(:,(1:11));
r_range_kL(:,(1:11)) = [];
CO2_loss = CO2_loss*24;
figure(1)
plot(x, CO2_loss)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-3} day^{-1})')
legend('kLa = 0.5 hr^{-1}','kLa = 20.5 hr^{-1}','kLa = 40.5 hr^{-1}','kLa = 60.5 hr^{-1}',...
    'kLa = 80.5 hr^{-1}','kLa = 100.5 hr^{-1}','kLa = 120.5 hr^{-1}','kLa = 140.5 hr^{-1}',...
    'kLa = 160.5 hr^{-1}','kLa = 180.5 hr^{-1}','kLa = 200.5 hr^{-1}')
