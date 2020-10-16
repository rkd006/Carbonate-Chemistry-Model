% Author: Riley Doyle
% Date: October 8, 2020
%Dependent functions: rates, calc_K1, calc_K2, calc_Kh, calc_alpha0,
    %calc_alpha1, calc_alpha2, calc_density
%Inputs: T, S, pCO2, pH, kLa, y_2, y_1, k1, k2, k3, k4, Csat, pk1, pk2, d, alk0, r_algae
%Outputs: CO2 losses to the atmospher vs. time, CO2 requirements vs. time

%delete all figures and variables in the workspace
clear
close all

%define variables as global, a variable that is shared by the function and
%workspace
global kp1 km1 kp4 km4 kp5H km5H kp5OH km5OH kp6 km6 


%Environmental conditions
T = 20 + 273.15; %temp in Kelvins
S = 35; %(salinity in g/kg)
R = 8.314;
Kw = exp(148.96502 - 13847.26/T - 23.6521*log(T)+ (118.67/T-5.977+1.0495*log(T))*S^(1/2)-0.01615*S);
Kb = exp((-8966.90-2890.53*S^(1/2)-77.942*S+1.728*S^(3/2)-0.0996*S^2)/T+148.0248+137.1942*S^(1/2)+1.62142*S-(24.4344+25.085*S^(1/2)+0.2474*S)*log(T)+0.053105*S^(1/2)*T); 



Kh = calc_Kh(T, S); %(mole/kg sol/atm)

%carbonic acid/bicarbonate equilibrium
K1 = calc_K1(T, S); %(mol/kg)
pK1= -log10(K1); %(mol/kg)

%bicarbonate/carbonate equlibrium
K2 = calc_K2(T, S); %(mol/kg)
pK2= -log10(K2); %(mol/kg)

%Initial Conditions       
CO20 = 0.00000085;
HCO30 = 0;
CO30 = 0;
H0 = 10^(-8);
OH0 = Kw/H0;

% rate constants for odes
kp1 = exp(1246.98 - (6.19*10^(4))/T - 183*log(T));
km1 = kp1/K1;
kp4 = (4.7*10^7)*exp(-23200/(R*T));
km4 = kp4*Kw/K1;
kp5H = 5*10^10;
km5H = kp5H*K2;
kp5OH = 6*10^9;
km5OH = kp5OH*Kw/K2;
kp6 = 1.4*10^(-3);
km6 = kp6/Kw;

% create array of times for output
time = linspace(0,60);  %time

%Set initial conditions
x0 = [CO20; HCO30; CO30; H0; OH0];


%Solve ODEs with the ode15s solver
%returns output arrays of tout and x
%rates is the ODE system, time is the x values, x0 is the initial conditions
[tout, x] = ode15s(@carbonates, time, x0);
xmass = x;
H = xmass(:,4);
xmass(:,4) = [];
%create array 100x1 
pH = -log10(H);
pHCO3 = -log10(xmass(:,2));
pCO2 = -log10(xmass(:,1));
pCO3 = -log10(xmass(:,3));
pOH = -log10(xmass(:,4));

figure(1);
plot(tout, pH)
xlabel('Time (seconds)')
ylabel('pH')
