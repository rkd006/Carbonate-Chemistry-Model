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
K_1 = calc_K1(T, S); %no units
pK1 = -log10(K_1); %no units
K_2 = calc_K2(T, S); %no units
pK2 = -log10(K_2); %no units
Kh = calc_Kh(T,S);
PCO2 = 0.000416;
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
d = .15; %(m) depth of the pond
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1; %no units

kLain= 0.5; %(1/hr)
kLaend= 8.5; %(1/hr)
delkLa = 2; %(1/hr)

r_kL_pH = calc_CO2_loss_kLa (pK1, pK2, Kh, PCO2, alk, pHin, pHend, delpH, kLaend, kLain, delkLa);

x = r_kL_pH(:,1);
r_kL_pH(:,1) = [];
r_kL_pH = r_kL_pH*d; %(g/m2*day)

pH = 8; %no units
alkin=2; %(eq/m3 or meq/L)
alkend=32; %(eq/m3 or meq/L)
delalk = 2; %(eq/m3 or meq/L)
r_kL_alk = calc_CO2_loss_alk (pK1, pK2, Kh, PCO2, alkin, alkend, delalk, kLain, kLaend, delkLa, pH);
x2 = r_kL_alk(:,1);
r_kL_alk(:,1) = [];
r_kL_alk = r_kL_alk*d;

%without alkalinity 
figure(1);
hold on 
plot(x, r_kL_pH(:, 1), '-', 'color', 'b');
plot(x, r_kL_pH(:, 2), '--', 'color', 'm');
plot(x, r_kL_pH(:, 3), '-.', 'color', 'g');
plot(x, r_kL_pH(:, 4), '-', 'color', 'r');
plot(x, r_kL_pH(:, 5), '--', 'color', 'k');
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kLa = 0.5 1/hr', 'kLa = 2.5 1/hr', 'kLa = 4.5 1/hr', 'kLa = 6.5 1/hr', 'kLa = 8.5 1/hr')
xlim([6.5 8.2])
ylim([0 1000])

%without pH
figure(2)
hold on 
plot(x2, r_kL_alk(:, 1), '-', 'color', 'b');
plot(x2, r_kL_alk(:, 2), '--', 'color', 'm');
plot(x2, r_kL_alk(:, 3), '-.', 'color', 'g');
plot(x2, r_kL_alk(:, 4), '-', 'color', 'r');
plot(x2, r_kL_alk(:, 5), '--', 'color', 'k');
xlabel('alkalinity') 
ylabel('CO_2 loss to the atmosphere (g m^-2 day^-1)')
legend('kLa = 0.5 1/hr', 'kLa = 2.5 1/hr', 'kLa = 4.5 1/hr', 'kLa = 6.5 1/hr', 'kLa = 8.5 1/hr')


