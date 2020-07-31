%Author: Riley Doyle
%Date: 7/31/20
%Dependent functions: calc_K1, calc_K2, calc_CO2_loss_temp
%Inputs: S, CO2sat, kLa, pH, alk
%Outputs:CO2 loss to atmosphere without algae growth

%delete all figures and variables in the workspace
clear 
close all


%define variables
Tin = 10 + 273.15; %temp in Kelvins
Tend = 30 + 273.15;
delT = 10;
S = 35; %(salinity in g/kg)
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
kLa = 0.5; %(1/hr)
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1; %no units
d = .15; %(m) depth of pond
alk = 2.5;

%define r_temp
r_temp = calc_CO2_loss_temp (S, CO2sat, alk, kLa, pHin, pHend, delpH, Tend, Tin, delT);

%modify r for plotting
%x axis is the first column of r
x = r_temp(:,1);
r_temp(:,1) = [];
r = r_temp*d; %(g/m2*day)
L = {'-', '--', '-.'};

%plot CO2 loss vs pH for multiple alkalinities
hold on
plot(x,r(:,1), 'Linestyle', L{1})
plot(x,r(:,2), 'Linestyle', L{2})
plot(x,r(:,3), 'Linestyle', L{3})

xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
legend('T = 10 ^oC','T = 20 ^oC','T = 30 ^oC')