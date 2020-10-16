%Author:Riley Doyle
%Date: October 9 2020

%delete all variables in the workspace 
clear 

%delete all figures
close all

%delineate range of pHs from 2 to 14
pH_start=2;
pH_end= 14;

%define equilibrium constants 
T = 20 + 273.15;
S = 35;
Tc = 20;
P = 10; %(dbar)
t = Tc*1.00024;
p = P/10;
den = calc_density(S, t, p); %(kg/m3)
K_1 = calc_K1(T, S)*(den/1000);
K_2 = calc_K2(T, S)*(den/1000);
Kh = calc_Kh(T, S); %(mole/kg sol/atm)
Kh = Kh*(den/1000); %(mol/L/atm)
PCO2 = 0.000416; %(atm)

%create 100 linearly spaced points between pH_start and pH_end
vpH = linspace(pH_start, pH_end);

%length of vpH 
p = length(vpH);

%create an 100 by 1 array of zeros 
HCO3 = zeros(p,1);
CO3 = zeros(p,1);
CT = zeros(p,1);
H = zeros(p,1);
H2CO3 = zeros(p,1);

%for each point, calculate the following functions 
for i = 1:p
    H(i) = 10^(-vpH(i));
    H2CO3(i) = (Kh*PCO2);
    HCO3(i) = (((K_1*H2CO3(i))/H(i)));
    CO3(i) =(((K_2*K_2*H2CO3(i))/H(i)^2)); 
     CT(i) = H2CO3(i)+CO3(i)+HCO3(i);
end
H2CO3 = -log10(H2CO3);
HCO3 = -log10(HCO3);
CO3 = -log10(CO3);
CT = -log10(CT);

%interchange the rows and columns of vpH
vpH = transpose(vpH);
%concatenate arrays horizontally
carbonates = horzcat(vpH, H2CO3, HCO3, CO3, CT);

%modify r for plotting
%x axis is the first column of carbonates
x_axis = carbonates(:,1);
carbonates(:,1) = [];

%create a plot
figure(1)
set(gca, 'YDir', 'reverse');
plot(x_axis, carbonates)

%label x and y axis of the figure
xlabel('pH')
ylabel('pC')
legend('H_2CO_3', 'HCO_3^-', 'CO_3^-^2', 'C_T')


%delineate range of pHs from 2 to 14
pH_start=2;
pH_end= 14;

K_1 = calc_K1(T, S)*(den/1000);
pK1 = -log10(K_1);
K_2 = calc_K2(T, S)*(den/1000);
pK2 = -log10(K_2);

%create 100 linearly spaced points between pH_start and pH_end
vpH = linspace(pH_start, pH_end);

%length of vpH 
p = length(vpH);

%create an 100 by 1 array of zeros 
HCO3 = zeros(p,1);
CO3 = zeros(p,1);
CT = zeros(p,1);
H = zeros(p,1);
OH = zeros(p,1);
alpha0 = zeros(p,1);
alpha1 = zeros(p,1);
alpha2 = zeros(p,1);
H2CO3 = zeros(p,1);
alk = 2.5;

%for each point, calculate the following functions 
for i = 1:p
    H(i) = 10^(-vpH(i));
    OH(i) = 10^(-(14-vpH(i)));
    alpha0(i) = calc_alpha0( vpH(i), pK1, pK2);
    alpha1(i) = calc_alpha1( vpH(i), pK1, pK2);
    alpha2(i) = calc_alpha2( vpH(i), pK1, pK2);
    CT(i) = (alk - OH(i) + H(i))*(1/(alpha1(i) + (2*alpha2(i))));
    H2CO3(i) = (alpha0(i)*CT(i));
    HCO3(i) = (alpha1(i)*CT(i));
    CO3(i) = (alpha2(i)*CT(i)); 
end
H2CO3 = -log10(H2CO3);
HCO3 = -log10(HCO3);
CO3 = -log10(CO3);
CT = -log10(CT);
%interchange the rows and columns of vpH
vpH = transpose(vpH);
%concatenate arrays horizontally
carbonates = horzcat(vpH, H2CO3, HCO3, CO3, CT);

%modify r for plotting
%x axis is the first column of carbonates
x_axis = carbonates(:,1);
carbonates(:,1) = [];

%create a plot
figure(2)
set(gca, 'YDir', 'reverse');
plot(x_axis, carbonates)

%label x and y axis of the figure
xlabel('pH')
ylabel('pC')
legend('H_2CO_3', 'HCO_3^-', 'CO_3^-^2', 'C_T')