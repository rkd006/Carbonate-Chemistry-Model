% author: Riley Doyle
% date: 06-09-2020
% file name: calc_Kh.m
% dependencies: none%Calculate Kh

%create a function to calculate Kh
function Kh = calc_Kh(T, S)

Kh = exp(9345.17/T -60.2409 + 23.3585*log(T/100) + S*(0.023517 -...
    0.00023656*T + 0.0047036*(T/100)^2));
end 
%from Zeebe and Wolf Gladrow (2001) p. 257 Henry's constant