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
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
alkin = alk;
alkend = alk;
delalk = alk;
%kL = 0.04 m/hr from Weissman et. al. 1987
kLain= 0.1; % units of 1/hour
kLaend= 0.5;
delkLa = 0.4; 

s_steps = (kLaend - kLain)/delkLa;
kLa = kLain;
hold on

for b = 1:s_steps+1
r_range_kLa = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r_range_kLa(:,1);
r_range_kLa(:,1) = [];
CO2_loss = r_range_kLa(:,1);
r_range_kLa(:,1) = [];
plot(x_axis, CO2_loss);
kLa = kLa + delkLa;
end


kLain= 1.5; % units of 1/hour
kLaend= 35.5;
delkLa = 17;
s_steps = (kLaend - kLain)/delkLa;
kLa = kLain;

for b = 1:s_steps+1
r_range_kLa = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r_range_kLa(:,1);
r_range_kLa(:,1) = [];
CO2_loss = r_range_kLa(:,1);
r_range_kLa(:,1) = [];
plot(x_axis, CO2_loss);
kLa = kLa + delkLa;
end

figure(1)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-3} day^{-1})')
legend('kLa = 0.1 hr^{-1}','kLa = 0.5 hr^{-1}','kLa = 1.5 hr^{-1}','kLa = 18.5 hr^{-1}',...
    'kLa = 30.5 hr^{-1}')
