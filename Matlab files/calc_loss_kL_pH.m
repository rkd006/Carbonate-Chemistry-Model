% author: Riley Doyle
% date: 06-17-2020
% file name: calc_loss_kL_pH.m
% output: Calculate loss with different kL values and pHs

function r_kL_pH = calc_loss_kL_pH (pK1, pK2, CO2sat, alk, pHin, pHend, delpH, kLain, kLaend, delkLa)

m_steps = (kLaend-kLain)/delkLa;



n_steps = (pHend - pHin)/delpH;

r_kL_pH = zeros(n_steps+1, m_steps+2);
kLa = kLain;
for p = 1:m_steps+2
   
    pH = pHin;
    
    for c = 1:n_steps+1
    
        %calculate alphas
        alpha0 = calc_alpha0(pH, pK1, pK2);
        alpha1 = calc_alpha1(pH, pK1, pK2);
        alpha2 = calc_alpha2(pH, pK1, pK2);
        
        %calculate H+ and OH and CT
        H = 10^(-pH);
        OH = 10^(-(14-pH));
        CT= (alk - OH + H)/(alpha0 + alpha1 + alpha2);
        
        %calculate dissolved CO2 concentration
        H2CO3 = alpha0*CT;
        HCO3 = alpha1*CT;
        CO3 = alpha2*CT;
        
        %calculate loss of CO2 per hour
        loss = kLa*(H2CO3 - CO2sat)*44; %g CO2 
        pH = pH + delpH;  %increase pH 

        
        r_kL_pH(c,1)= pH; %record pH
        r_kL_pH(c,p)= loss; %record loss
    
    end 
   kLa = kLa + delkLa;
end

