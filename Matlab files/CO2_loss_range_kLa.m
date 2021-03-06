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
Tc = 20;
P = 10; %(dbar)
t = Tc*1.00024;
p = P/10;
den = calc_density(S, t, p); %(kg/m3)
K_1 = calc_K1(T, S)*(den/1000); %no units
pK1 = -log10(K_1); %no units
K_2 = calc_K2(T, S)*(den/1000); %no units
pK2 = -log10(K_2); %no units
Kh = calc_Kh(T,S)*(den/1000);
PCO2 = 0.000416;
d = .15; % (m) depth of the pond from Weissman
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1; %no units
kLain= 0.1; %(1/hr)
kLaend= 0.5; %(1/hr)
delkLa = 0.4; %(1/hr)
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
%kL = 0.04 m/hr from Weissman et. al. 1987

r = calc_CO2_loss_kLa (pK1, pK2, Kh, PCO2, alk, pHin, pHend, delpH, kLaend, kLain, delkLa);
x_axis = r(:,1);
r(:,1) = [];
r =r*d; %y must be in g/m2*day
plot(x_axis, r(:,1), '-');
hold on
plot(x_axis, r(:,2), '--');
hold on 

kLain= 1.5; %(1/hr)
kLaend= 3; %(1/hr)
delkLa = 1.5; %(1/hr)

r = calc_CO2_loss_kLa (pK1, pK2, Kh, PCO2, alk, pHin, pHend, delpH, kLaend, kLain, delkLa);
x_axis = r(:,1);
r(:,1) = [];
r =r*d; %y must be in g/m2*day
plot(x_axis, r(:,1), '-.');
hold on
plot(x_axis, r(:,2), '--');
hold on 


figure(1)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 300])
xlim([6.5 8.1])
legend('kLa = 0.1 hr^{-1}','kLa = 0.5 hr^{-1}','kLa = 1.5 hr^{-1}','kLa = 3.0 hr^{-1}')
