
% Author:Deborah Sills
% Date January 27 2013
%Dependent function: rates
%Inputs: pH, kL, y_2, y_1, Csat, pk1, pk2, A, d, alk0, r_algae
%Outputs: CO2 losses to the atmospher vs. time, CO2 requirements vs. time

%delete all figures and variables in the workspace
clear all
close all
clc

%define variables as global, a variable that is shared by the function and
%workspace
global k1 k2 k3 k4 

%Environmental conditions
T = 20 + 273.15; %temp in Kelvins
S = 35; %(salinity in g/kg)
PCO2 = 0.00040; %atm (need to correct for temp, very crude approx)

%Pond characteristics
d = 0.15; %m depth of pond

%mass transfer coefficient for CO2 out of pond
kLa = 0.96; %1/day (Weismann et al., 1987 pg. 6 at bottom)

%Stoicheometric constants for algal growth
y_2 = 0.008849558; %moles bicarbonate per g algae from stoicheometry
y_1 = 0.0354;  %moles CO2 per g algae from stoicheometry
%Csat = 0.01272; %moles/m3 from somewhere; to do: make temperature dependent


Kh = calc_Kh(T, S);
%units of Kh mole/kg sol/atm

%carbonic acid/bicarbonate equilibrium
K_1 = calc_K1(T, S); 

pK1=-log10(K_1);  

%bicarbonate/carbonate equlibrium
K_2 = calc_K2(T, S);

pK2= -log10(K_2); 

Csat = PCO2*Kh;  %moles/kg

%%%%%Inputs%%%%%%
%Assumptions & initial conditions in moles per sample volume

alk0 = 2.5;  %eq/m3
r_algae = 10;  % growth rate g/m2/day; assume
pH=9; 

%Calculate alphas 
alpha0 = calc_alpha0(pH,pK1, pK2);
alpha1 = calc_alpha1(pH,pK1, pK2);
alpha2 = calc_alpha2(pH,pK1, pK2);

%Calculate [H+] and [OH-]
OH=10^-(14-pH)*10^3; %moles/m3
H=(10^(-pH))*10^3;  %moles/m3
        
%Initial Conditions       
Caq0=(alk0 - OH + H)*alpha0/(alpha1+2*alpha2); %mole/m3
Cin0 = 0;
Closs0 = 0;

% rate constants for odes
%rate of Caq removed due to alkalinity consumption by algae Eq(15)
k1 = y_2*r_algae*alpha0/(alpha1+2*alpha2);
% k2-k3 = C needed to be delivered to satisfy diffusion out of pond Eq(19)
k2 = kLa;  
k3 = kLa*Csat;
% rate of C loss due to 
k4 = (y_1 + y_2*(1 - alpha1 - 2*alpha2))*r_algae; 

% molecular weights  g/mol
MA = 1;% CO2
MB = 44;  % CO2
MC = 44;  % CO2

% create array of times for output
time = linspace(0, 4);  %4 days

%Set initial conditions
x0 = [Caq0; Cin0; Closs0];

%Solve ODEs with the ode15s solver
%returns output arrays of tout and x
%rates is the ODE system, time is the x values, x0 is the initial conditions
[tout, x] = ode15s(@rates, time, x0);

% convert from moles to mass
%scale each column of x (species) by its mol wt
xmass = x*diag([MA, MB, MC]);

%eff= xmass(end,3)/xmass(end,2)
CO2aq = xmass(:,1);

%create
CO2sat = Csat*ones(length(CO2aq),1);


table = [tout, x];
%modify plot and plot only CO2 loss and delivery requirements
xmass(:,1) = [];
figure(1);
plot(tout, xmass)
xlabel('Time (day)')
ylabel('CO_2 (g m^{-2})')
legend('CO_2 supply required', 'CO_2 loss to atmosphere')

figure(2);
plot(tout, CO2aq)
xlabel('Time (day)')
ylabel('CO_2 (mole m^{-3})')
hold on
plot(tout, CO2sat, 'r--')
