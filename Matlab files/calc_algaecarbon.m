%author: Riley Doyle
% date: 7/31/20
%file: calc_algaecarbon
%status: working

r_algae = 10; %g/m2/day
d = 0.15; %m
day = 4; 

%formula using for algae:
%C100H183O48N11P

M1 = 2336; %molar mass of algae (g/mol)
M2 = 1200; %molar mass of C in algae (g/mol)
M3 = 12; %molar mass of C

carbon = ((r_algae/d)*4)/(10^3)*(M2/M1); %g of C/L

carbon = (carbon/M3)*(10^3) %mM