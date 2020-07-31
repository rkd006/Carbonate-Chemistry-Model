%author: Riley Doyle
% date: 7/31/20
%file: calc_inorganiccarbon_pond
%status: working

global k1

T = 20 +273.15;
S = 35;
PCO2 = 0.00040;
d = 0.15;

kLa = 0.5;
y1 = 1.714;
y2 = 0.1695;
y3 = 1.88;
Kh = calc_Kh(T,S);
K1 = calc_K1(T,S);
pK1 = -log10(K1);
K2 = calc_K2(T,S);
pK2 = -log10(K2);

alk0 = 2.5;
r_algae = 10;
pH = 8;

alpha0 = calc_alpha0(pH, pK1, pK2);
alpha1 = calc_alpha1(pH, pK1, pK2);
alpha2 = calc_alpha2(pH, pK1, pK2);
OH = 10^-(14-pH)*(10^3);
H = 10^(-pH)*(10^3);

k1 = -(y2*r_algae*(alpha1 + 2*alpha2))/44;
Ct0 = (alk0 - OH + H)/(alpha1 + (2*alpha2));
x0 = (Ct0);
time = linspace(0, 4);
[tout, x] = ode15s(@rates2, time, x0);
xmass = x;
Ct = xmass(:,1);
xmass(:,1) = [];
Ct1 = Ct/d
figure(1)
plot(tout, Ct1)
xlabel('Time (day)')
ylabel('CO_2 (mM)')
ylim([0 16])