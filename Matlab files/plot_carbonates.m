%Author:Deborah Sills
%Date January 27 2013
%Dependent functions: calc_K1, calc_K2, calc_alpha0, calc_alpha1,
%calc_alpha2
%Inputs: T, S, pH_start, pH_end, pK1, pK2
%Outputs: plot relative amounts of H2CO3, HCO3-, CO3-2

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
pK1 = -log10(K_1);
K_2 = calc_K2(T, S)*(den/1000);
pK2 = -log10(K_2);

%create 100 linearly spaced points between pH_start and pH_end
vpH = linspace(pH_start, pH_end);

%length of vpH 
p = length(vpH);

%create an 100 by 1 array of zeros 
H2CO3 = zeros(p,1);
HCO3 = zeros(p,1);
CO3 = zeros(p,1);

%for each point, calculate the following functions 
for n = 1:p
    H2CO3(n) = calc_alpha0( vpH(n), pK1, pK2);
    HCO3(n) = calc_alpha1( vpH(n), pK1, pK2);
    CO3(n) = calc_alpha2( vpH(n), pK1, pK2);   
end

%interchange the rows and columns of vpH
vpH = transpose(vpH);
%concatenate arrays horizontally
carbonates = horzcat(vpH, H2CO3, HCO3, CO3);

%modify r for plotting
%x axis is the first column of carbonates
x_axis = carbonates(:,1);
carbonates(:,1) = [];

%create a plot
plot(x_axis, carbonates)

%label x and y axis of the figure
xlabel('pH')
ylabel('Fraction Carbonate Species')
legend('H_2CO_3', 'HCO_3^-', 'CO_3^-^2')