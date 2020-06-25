% author: Deborah Sills
% date: 1-26-13
% file name: calc_CO2_loss.m
% dependencies: calc_alpha0, calc_alpha1,calc_alpha2
% output: CO2 losses to the atmosphere

function r = calc_CO2_loss(pK1, pK2, kLa, CO2sat, pHin, pHend, delpH, alkin, alkend, delalk)

%initialize
m_steps = (alkend-alkin)/delalk;
alk = alkin;


n_steps = (pHend - pHin)/delpH;

r = zeros(n_steps+1, m_steps + 2);

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
        loss = kLa*(H2CO3 - CO2sat)*44; %g CO2 per day
        pH = pH + delpH;  %increase pH 

        
        r(c,1)= pH; %record pH
        r(c,p)= loss; %record loss
        
    end
   alk = alk + delalk;
end

