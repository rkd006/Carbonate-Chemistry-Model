% author: Riley Doyle
% date: 06-17-2020
% file name: CO2_loss_comb.m
% dependencies: calc_CO2_loss, calc_K1, calc_K2
% input: T, S, pK1, pK2, CO2sat, kLa, pH, alk
% output: CO2 losses without algae growth with different pH and alk together

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
pHin = 6.5;
pHend = 8.5;
delpH = 0.1;  

alkin=2; %(eq/m3)
alkend=22;
delalk = 5; 

kLain = .5;
kLaend = 8.5;
delkLa = 4;
s_steps = (kLaend - kLain)/delkLa;
kLa = kLain;
hold on

for b = 1:s_steps+1
r_kL_1 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r_kL_1(:,1);
r_kL_1(:,1) = [];
plot(x_axis, r_kL_1)
kLa = kLa + delkLa;
end

xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-3} day^{-1})')
legend('kLa = .5 day^{-1}, Alk = 2 meq/L','kLa = .5 day^{-1}, Alk = 7 meq/L','kLa = .5 day^{-1}, Alk = 12 meq/L',...
    'kLa = .5 day^{-1}, Alk = 17 meq/L','kLa = .5 day^{-1}, Alk = 22 meq/L',...
    'kLa = 4.5 day^{-1}, Alk = 2 meq/L','kLa = 4.5 day^{-1}, Alk = 7 meq/L','kLa = 4.5 day^{-1}, Alk = 12 meq/L',...
    'kLa = 4.5 day^{-1}, Alk = 17 meq/L', 'kLa = 4.5 day^{-1}, Alk = 22 meq/L', 'kLa = 8.5 day^{-1}, Alk = 2 meq/L',...
    'kLa = 8.5 day^{-1}, Alk = 7 meq/L', 'kLa = 8.5 day^{-1}, Alk = 12 meq/L', 'kLa = 8.5 day^{-1}, Alk = 17 meq/L',...
    'kLa = 8.5 day^{-1} Alk = 22 meq/L')