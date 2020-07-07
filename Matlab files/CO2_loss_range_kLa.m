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
K_1 = calc_K1(T, S); %no units
pK1 = -log10(K_1); %no units
K_2 = calc_K2(T, S); %no units
pK2 = -log10(K_2); %no units
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
d = .15; % (m) depth of the pond from Weissman
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1; %no units
kLain= 0.1; %(1/hr)
kLaend= 0.5; %(1/hr)
delkLa = 0.4; %(1/hr)
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
%kL = 0.04 m/hr from Weissman et. al. 1987

r_range_kLa = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLaend, kLain, delkLa);
x_axis = r_range_kLa(:,1);
r_range_kLa(:,1) = [];
CO2_loss = r_range_kLa(:,(1:2));
r_range_kLa(:,(1:2)) = [];
CO2_loss = CO2_loss*d; %y must be in g/m2*day
plot(x_axis, CO2_loss);

hold on 

kLain= 1.5; %(1/hr)
kLaend= 5; %(1/hr)
delkLa = 3.5; %(1/hr)

r_range_kLa = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLaend, kLain, delkLa);
x_axis = r_range_kLa(:,1);
r_range_kLa(:,1) = [];
CO2_loss = r_range_kLa(:,(1:2));
r_range_kLa(:,(1:2)) = [];
CO2_loss = CO2_loss*d; %y must be in g/m2*day
plot(x_axis, CO2_loss);


figure(1)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 400])
xlim([6.6 8.1])
legend('kLa = 0.1 hr^{-1}','kLa = 0.5 hr^{-1}','kLa = 1.5 hr^{-1}','kLa = 5.0 hr^{-1}')
