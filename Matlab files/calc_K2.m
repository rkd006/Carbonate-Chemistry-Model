% author: Riley Doyle
% date: 06-09-2020
% file name: calc_K2.m
% output: Calculate K2

function K2 = calc_K2(T, S)

K2 = exp(-9.226508 - 3351.6106/T - 0.2005743*log(T) - ...
    S^0.5*(0.106901773 + 23.9722/T) + 0.1130822*S - 0.00846934*S^(3/2) +...
    log(1-0.001005*S));
end 
%Carbonate dissociation constants from Zeebe and Wolf Gladrow (2001) p.255
%units mol/kg or mol/L