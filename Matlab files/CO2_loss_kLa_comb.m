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
d = .2; %depth of the pond from Weissman

alkin=2; %(eq/m3)
alkend=32;
delalk = 5; 

%kLa = hr-1
%kL = .1 m/hr for kLa = .5 1/hr Weissman 1988 
kLain = 0.1;
kLaend = .5;
delkLa = 0.4;
s_steps = (kLaend - kLain)/delkLa;
kLa = kLain;
hold on

for b = 1:s_steps+1
r_kL_1 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r_kL_1(:,1);
r_kL_1(:,1) = [];
CO2_loss = r_kL_1(:,(1:7));
r_kL_1(:,(1:7)) = [];
CO2_loss = CO2_loss*d; %y must be in g/m2*day
figure (b)
plot(x_axis, CO2_loss)
kLa = kLa + delkLa;
end
hold on 

kLain = 1.5; %(1/hr) 
kLaend = 4.5;
delkLa = 3;
s_steps = (kLaend - kLain)/delkLa;
kLa = kLain;
hold on

for b = 1:s_steps+1
r_kL_1 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r_kL_1(:,1);
r_kL_1(:,1) = [];
CO2_loss = r_kL_1(:,(1:7));
r_kL_1(:,(1:7)) = [];
CO2_loss = CO2_loss*d; %y must be in g/m2*day
figure (b+2)
plot(x_axis, CO2_loss)
kLa = kLa + delkLa;
end
hold on
%kLa = .1 hr-1
figure (1)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 180])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L',...
    'Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L','Alk = 32 meq/L')

%kLa = .5 hr-1
figure (2)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 900])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L',...
    'Alk = 17 meq/L', 'Alk = 22 meq/L', 'Alk = 27 meq/L', 'Alk = 32 meq/L')

%kLa = 1.5 hr-1
figure (3)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 2600])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L', 'Alk = 12 meq/L',...
    'Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L','Alk = 32 meq/L')

%kLa = 4.5 hr -1
figure (4)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 8000])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L', 'Alk = 12 meq/L',...
    'Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L','Alk = 32 meq/L')