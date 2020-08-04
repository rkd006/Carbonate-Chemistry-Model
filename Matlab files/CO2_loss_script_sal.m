%Author: Riley Doyle
%Date: 7/31/20
%Dependent functions: calc_K1, calc_K2, calc_CO2_loss_temp
%Inputs: S, CO2sat, kLa, pH, alk
%Outputs:CO2 loss to atmosphere without algae growth

%delete all figures and variables in the workspace
clear 
close all


%define variables
T = 20 + 273.15; %temp in Kelvins
sin = 25;
send = 45;
dels = 10;
PCO2 = 0.000416;
Tc = 20;
P = 10; %(dbar)
t = Tc*1.00024;
p = P/10;
kLa = 0.5; %(1/hr)
pHin = 6.5; %no units
pHend = 8.5; %no units
delpH = 0.1; %no units
d = .15; %(m) depth of pond
alk = 2.5;

%define r_temp
r_sal = calc_CO2_loss_sal (T, PCO2, t, p, alk, kLa, pHin, pHend, delpH, send, sin, dels);

%modify r for plotting
%x axis is the first column of r
x = r_sal(:,1);
r_sal(:,1) = [];
r = r_sal*d; %(g/m2*day)
L = {'-', '--', '-.'};

%plot CO2 loss vs pH for multiple alkalinities
hold on
plot(x,r(:,1), 'Linestyle', L{1})
plot(x,r(:,2), 'Linestyle', L{2})
plot(x,r(:,3), 'Linestyle', L{3})

xlabel('pH')
ylabel('CO_2 loss to the atmosphere (g m^{-2} day^{-1})')
legend('S = 25 g/kg','S = 35 g/kg','S = 45 g/kg')