%author: Riley Doyle
% date: 06-22-2020
% file name: calc_loss_kL_comb
% dependencies: none
function r_kL_comb = calc_CO2_kL_comb(pK1, pK2, kLin, kLend, delkL, A, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk)

kL = kLin;
s_steps = (kLend-kLin)/delkL;

for f = 1:s_steps
    
    r_kL_comb = calc_CO2_loss(pK1, pK2, kL, A, CO2sat, pHin,pHend, delpH, alkin, alkend, delalk);
   kL = kL + delkL;
end
end 