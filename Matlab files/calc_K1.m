% author: Riley Doyle
% date: 06-09-2020
% file name: calc_K1.m
% output: Calculate K1

function K1 = calc_K1(T, S)


K1 = exp(2.83655 - 2307.1266/T - 1.5529413*log(T) - S^0.5*(0.207608410...
    + 4.0484/T) + 0.0846834*S - 0.00654208*S^(3/2) + log(1-0.001005*S));

end 
%Carbonate dissociation constants from Zeebe and Wolf Gladrow (2001) p.255