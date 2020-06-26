% Author: Riley Doyle
% Date: June 25 2020
%Dependent function: rates, calc_K1, calc_K2, calc_Kh, calc_alpha0,
    %calc_alpha1, calc_alpha2
%Inputs: pH, kLa, y_2, y_1, k1, k2, k3, k4, Csat, pk1, pk2, d, alk0, r_algae
%Outputs: CO2 losses to the atmospher vs. time, CO2 requirements vs. time
    %with different kLa values 

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

%Stoicheometric constants for algal growth
y_2 = 0.004547; %moles bicarbonate per g algae from stoicheometry
y_1 = 0.02558;  %moles CO2 per g algae from stoicheometry


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
pH= 9; 

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

% molecular weights  g/mol
MA = 1; %didn't have to scale
MB = 44;  %CO2 
MC = 44;  %CO2 

% create array of times for output
time = linspace(0, 4);  %4 days

%Set initial conditions
%Caq = dissolved concentation
%Cin = CO2 supply
%Closs = CO2 losses
x0 = [Caq0; Cin0; Closs0];

kLain = .5;
kLaend = 100.5;
delkLa = 20;
s_steps = (kLaend - kLain)/delkLa;
kLa = kLain;

%Solve ODEs with the ode15s solver
%returns output arrays of tout and x
%rates is the ODE system, time is the x values, x0 is the initial conditions
for b = 1:s_steps+1
    % rate constants for odes
%delivery requirements for the algal pond
%rate of Caq removed due to alkalinity consumption by algae Eq(15)
k1 = y_2*r_algae*alpha0/(alpha1+2*alpha2);
% k2-k3 = C needed to be delivered to satisfy diffusion out of pond Eq(19)
k2 = kLa;  
k3 = kLa*Csat; %k2*x-k3 = rate of C loss due to the atmosphere
k4 = (y_1 + y_2*(1 - alpha1 - 2*alpha2))*r_algae; 
[tout, x] = ode15s(@rates, time, x0);

% convert from moles to mass
%scale each column of x (species) by its mol wt
xmass = x*diag([MA, MB, MC]);

CO2aq = xmass(:,1);
xmass(:,1) = [];
CO2req = xmass(:,1);
xmass(:,1) = [];
CO2loss = xmass(:,1);
xmass(:,1) = [];
%modify plot and plot only CO2 loss and delivery requirements
figure(1)
plot(tout, CO2req)
hold on
plot(tout, CO2loss, '--') 
hold on 
kLa = kLa + delkLa;
end

figure(1)
xlabel('Time (day)')
ylabel('CO_2 (g m^{-3})')
legend('CO_2 supply for kLa = 0.5 hr^{-1}', 'CO_2 loss for kLa = 0.5 hr^{-1}',...
    'CO_2 supply for kLa = 20.5 hr^{-1}', 'CO_2 loss for kLa = 20.5 hr^{-1}',...
    'CO_2 supply for kLa = 40.5 hr^{-1}', 'CO_2 loss for kLa = 40.5 hr^{-1}',...
    'CO_2 supply for kLa = 60.5 hr^{-1}', 'CO_2 loss for kLa = 60.5 hr^{-1}',...
    'CO_2 supply for kLa = 80.5 hr^{-1}', 'CO_2 loss for kLa = 80.5 hr^{-1}',...
    'CO_2 supply for kLa = 100.5 hr^{-1}', 'CO_2 loss for kLa = 100.5 hr^{-1}')


