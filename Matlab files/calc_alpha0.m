% author: Deborah Sills
% date: 01-26-2013
% file name: calc_alpha0.m
% output: Calculate alpha 0

function alpha0 = calc_alpha0(pH, pK1, pK2)
alpha0 = 1 / (1 + 10^(-pK1)/(10^(-pH)) + 10^(-pK1)*10^(-pK2)/(10^(-pH))^ 2);
