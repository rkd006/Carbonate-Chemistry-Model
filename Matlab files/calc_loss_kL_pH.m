% author: Riley Doyle
% date: 06-17-2020
% file name: calc_loss_kL_pH.m
% output: Calculate loss with different kL values and pHs

function r_kL_pH = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLaend, kLain, delkLa)

%initialize
m_steps = (kLaend-kLain)/delkLa;
kLa = kLain;


n_steps = (pHend - pHin)/delpH;

r_kL_pH = zeros(n_steps+1, m_steps+1);

for p = 1:m_steps+1
    
    pH = pHin;
    
    for c = 1:n_steps+1
    
        %calculate alphas
        alpha0 = calc_alpha0(pH, pK1, pK2);
        alpha1 = calc_alpha1(pH, pK1, pK2);
        alpha2 = calc_alpha2(pH, pK1, pK2);
        
        %calculate H+ and OH and CT
        H = 10^(-pH);
        OH = 10^(-(14-pH));
        bt = (1/(alpha1 + (2.*alpha2)));
        tp = (alk - OH + H);
        CT = tp * bt;
        
        %calculate dissolved CO2 concentration
        H2CO3 = alpha0*CT;
        
        %calculate loss of CO2 per hour
        loss = kLa*(H2CO3 - CO2sat)*44*24; %g CO2 per day
              
        r_kL_pH(c,1)= pH; %record pH
        r_kL_pH(c,1+p)= loss; %record loss
        pH = pH + delpH;  %increase pH 
    end
   kLa = kLa + delkLa;
end
end

