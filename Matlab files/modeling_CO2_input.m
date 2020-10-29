clear

%Stiochiometric ratios
CO2coef = 452;
HCO3coef = 52;
algaecoef = 4;

%Molecular Weights
algaeMW = 2336; %g/mol
CO2MW = 44; %g/mol
HCO3MW = 61; %g/mol

%Given
T = 20 + 273.15;
S = 35;
CO2g = 0.006; %M
Tc = 20;
P = 10; %(dbar)
t = Tc*1.00024;
p = P/10;
den = calc_density(S, t, p); %(kg/m3)
PCO2 = 0.000416; %atm
Kh = calc_Kh(T,S)*(den/1000); %mol/L/atm
K1 = calc_K1(T, S)*(den/1000); %mol/L
pK1 = -log10(K1);
K2 = calc_K2(T, S)*(den/1000); %mol/L
pK2 = -log10(K2);
CO2aq = Kh*CO2g;
efficiency = 95;
CO2sat = Kh*PCO2;
y1 = CO2coef/algaecoef;
y2 = HCO3coef/algaecoef;

%initial conditions
step = 0.5;
end0 = 20;
algaegrowth = 0:step:end0;
CO2aqw = zeros(length(algaegrowth),1);
HCO3 = zeros(length(algaegrowth),1);
H = zeros(length(algaegrowth),1);
pH = zeros(length(algaegrowth),1);
CO2aqw(1) = CO2aq*(efficiency/100);
HCO3(1) = 0.02;
H(1) = (K1*CO2aqw(1))/HCO3(1);
pH(1) = -log10(H(1));
additionalCO2 = 0.0002;

%Calculations
for p = 1:length(algaegrowth)
    if pH <= 8.2
        CO2aqw(p+1) = CO2aqw(p) - ((y1)*((step/1000)/algaeMW));
        HCO3(p+1) = HCO3(p) + ((y2)*((step/1000)/algaeMW));
        H(p+1) = (K1*CO2aqw(p+1))/HCO3(p+1);
        pH(p+1) = -log10(H(p+1));
    elseif pH(p) > 8.2 && pH(p) < 8.4
        CO2aqw(p+1) = CO2aqw(p) + additionalCO2;
        HCO3(p+1) = HCO3(p) + ((y2)*((step/1000)/algaeMW));
        H(p+1) = (K1*CO2aqw(p+1))/HCO3(p+1);
        pH(p+1) = -log10(H(p+1));
    else
        CO2aqw(p+1) = CO2aqw(p) - ((y1)*((step/1000)/algaeMW));
        HCO3(p+1) = HCO3(p) + ((y2)*((step/1000)/algaeMW));
        H(p+1) = (K1*CO2aqw(p+1))/HCO3(p+1);
        pH(p+1) = -log10(H(p+1));
    end
end
