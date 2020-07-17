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
K_1 = calc_K1(T, S); %no units
pK1 = -log10(K_1); %no units
K_2 = calc_K2(T, S); %no units
pK2 = -log10(K_2); %no units
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1;  %no units
d = .15; % (m)depth of the pond from Weissman

alkin=2; %(meq/L or eq/m3)
alkend=32; %(meq/L or eq/m3)
delalk = 5; %(meq/L or eq/m3)

%kLa = hr-1
%kL = .1 m/hr for kLa = .5 1/hr Weissman 1988 
kLain = 0.1; %(hr-1)
kLaend = .5; %(hr-1)
delkLa = 0.4; %(hr-1)
s_steps = (kLaend - kLain)/delkLa; %(hr-1)
kLa = kLain; %(hr-1)
hold on

for b = 1:s_steps+1
M = {'o', 's', 'd', '^', '*', '.', '+'};
r1 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r1(:,1);
r1(:,1) = [];
r1 = r1*d; %y must be in g/m2*day
figure (b)
hold on
plot(x_axis, r1(:,1), 'Marker', M{1})
plot(x_axis, r1(:,2),'Marker', M{2})
plot(x_axis, r1(:,3),'Marker', M{3})
plot(x_axis, r1(:,4),'Marker', M{4})
plot(x_axis, r1(:,5),'Marker', M{5})
plot(x_axis, r1(:,6),'Marker', M{6})
plot(x_axis, r1(:,7),'Marker', M{7})
kLa = kLa + delkLa;
end
hold on 

kLain = 1.5; %(1/hr) 
kLaend = 3; %(1/hr)
delkLa = 1.5; %(1/hr)
s_steps = (kLaend - kLain)/delkLa; %(1/hr)
kLa = kLain; %(1/hr)
hold on

for b = 1:s_steps+1
r1 = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);
x_axis = r1(:,1);
r1(:,1) = [];
r1 = r1*d; %y must be in g/m2*day
figure (b+2)
hold on
plot(x_axis, r1(:,1), 'Marker', M{1})
plot(x_axis, r1(:,2),'Marker', M{2})
plot(x_axis, r1(:,3),'Marker', M{3})
plot(x_axis, r1(:,4),'Marker', M{4})
plot(x_axis, r1(:,5),'Marker', M{5})
plot(x_axis, r1(:,6),'Marker', M{6})
plot(x_axis, r1(:,7),'Marker', M{7})
kLa = kLa + delkLa;
end
hold on
%kLa = .1 hr-1
figure (1)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 140])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L',...
    'Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L','Alk = 32 meq/L')

%kLa = .5 hr-1
figure (2)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 700])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L',...
    'Alk = 17 meq/L', 'Alk = 22 meq/L', 'Alk = 27 meq/L', 'Alk = 32 meq/L')

%kLa = 1.5 hr-1
figure (3)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 2000])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L', 'Alk = 12 meq/L',...
    'Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L','Alk = 32 meq/L')

%kLa = 3 hr -1
figure (4)
xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
ylim([0 4000])
xlim([6.5 8.5])
legend('Alk = 2 meq/L','Alk = 7 meq/L', 'Alk = 12 meq/L',...
    'Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L','Alk = 32 meq/L')