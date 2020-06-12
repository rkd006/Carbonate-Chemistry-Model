% author: Deborah Sills
% date: 01-26-2013
% file name: alpha1.m
% dependencies: none%Calculate alpha0

%create a function to calculate alpha 1
function alpha1 = calc_alpha1(pH, pK1, pK2)


alpha1 = 1/(10^(-pH)/10^(-pK1) + 1 + 10^(-pK2)/10^(-pH));
