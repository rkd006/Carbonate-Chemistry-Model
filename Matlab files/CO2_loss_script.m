%Author:Deborah Sills
%Date January 27 2013
%Dependent functions: calc_K1, calc_K2, calc_CO2_loss
%Inputs: T, S, pK1, pK2, CO2sat, kLa, pH, alk
%Outputs:CO2 loss to atmosphere without algae growth

%delete all figures and variables in the workspace
clear 
close all


%define variables
T = 20 + 273.15; %temp in Kelvins
S = 35; %(salinity in g/kg)
K_1 = calc_K1(T, S); %no units
pK1 = -log10(K_1); %no units
K_2 = calc_K2(T, S); %no units
pK2 = -log10(K_2); %no units
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
kLa = 0.5; %(1/hr)
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1; %no units
d = .15; %(m) depth of pond

alkin=2; %(eq/m3 or meq/L)
alkend=32; %(eq/m3 or meq/L)
delalk = 5; %(eq/m3 or meq/L)

%define r
r = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk);

%modify r for plotting
%x axis is the first column of r
x = r(:,1);
r(:,1) = [];
r = r*d; %(g/m2*day)
M = {'o', 's', 'd', '^', '*', '.', '+'};

%plot CO2 loss vs pH for multiple alkalinities
hold on
plot(x,r(:,1),'Marker', M{1})
plot(x,r(:,2),'Marker', M{2})
plot(x,r(:,3),'Marker', M{3})
plot(x,r(:,4),'Marker', M{4})
plot(x,r(:,5),'Marker', M{5})
plot(x,r(:,6),'Marker', M{6})
plot(x,r(:,7),'Marker', M{7})

xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
legend('Alk = 2 meq/L','Alk = 7 meq/L','Alk = 12 meq/L','Alk = 17 meq/L','Alk = 22 meq/L','Alk = 27 meq/L', 'Alk = 32 meq/L')
ylim([0 700])
