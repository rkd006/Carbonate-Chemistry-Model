% Author:Deborah Sills
% Date January 27 2013
%Dependent functions: rates, calc_K1, calc_K2, calc_Kh, calc_alpha0,
    %calc_alpha1, calc_alpha2
%Inputs: T, S, pCO2, pH, kLa, y_2, y_1, k1, k2, k3, k4, Csat, pk1, pk2, d, alk0, r_algae
%Outputs: CO2 losses to the atmospher vs. time, CO2 requirements vs. time

%delete all figures and variables in the workspace
clear
close all

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
kLa = 10; %1/day (Weismann et al., 1987 pg. 6 at bottom)

%Stoicheometric constants for algal growth
y_2 = 0.2427; %g bicarbonate per g algae from stoicheometry
y_1 = 1.1503;  %g CO2 per g algae from stoicheometry



Kh = calc_Kh(T, S);
%units of Kh mole/kg sol/atm

%carbonic acid/bicarbonate equilibrium
K_1 = calc_K1(T, S); 

pK1=-log10(K_1);  

%bicarbonate/carbonate equlibrium
K_2 = calc_K2(T, S);

pK2= -log10(K_2); 

Csat = PCO2*Kh*44;  %g/kg

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
Caq0=((alk0 - OH + H)*alpha0/(alpha1+2*alpha2))*44; %g/m3
Cin0 = 0;
Closs0 = 0;

 % rate constants for odes
%delivery requirements for the algal pond
%rate of Caq removed due to alkalinity consumption by algae Eq(15)
k1 = y_2*r_algae*alpha0/(alpha1+2*alpha2);
% k2-k3 = C needed to be delivered to satisfy diffusion out of pond Eq(19)
k2 = kLa;  
k3 = kLa*Csat; %k2*x-k3 = rate of C loss due to the atmosphere
k4 = (y_1 + y_2*(1 - alpha1 - 2*alpha2))*r_algae; 

% create array of times for output
time = linspace(0, 4);  %4 days

%Set initial conditions
%Caq = dissolved concentation
%Cin = CO2 supply
%Closs = CO2 losses
x0 = [Caq0; Cin0; Closs0];


%Solve ODEs with the ode15s solver
%returns output arrays of tout and x
%rates is the ODE system, time is the x values, x0 is the initial conditions
[tout, x] = ode15s(@rates, time, x0);
xmass = x;

%eff= xmass(end,3)/xmass(end,2)
CO2aq = xmass(:,1);
xmass(:,1) = [];
%create array 100x1 
CO2sat = Csat*ones(length(CO2aq),1);


%table = [tout, x];%modify plot and plot only CO2 loss and delivery requirements
figure(1);
plot(tout, xmass)
xlabel('Time (day)')
ylabel('CO_2 (g m^{-2})')
legend('CO_2 supply required', 'CO_2 loss to atmosphere')

figure(2);
plot(tout, CO2aq)
xlabel('Time (day)')
ylabel('CO_2 (g m^{-2})')
hold on
plot(tout, CO2sat, 'r--')
legend('dissolved CO_2 concentration', 'saturation concentration of CO_2')