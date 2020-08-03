% author: Deborah Sills
% date: 1-26-13
% file name: calc_CO2_loss.m
% dependencies: calc_alpha0, calc_alpha1,calc_alpha2
% output: CO2 losses to the atmosphere

function r = calc_CO2_loss(pK1, pK2, Kh, kLa, PCO2, pHin, pHend, delpH, alkin, alkend, delalk)

%initialize
m_steps = (alkend-alkin)/delalk;
alk = alkin;


n_steps = (pHend - pHin)/delpH;

r = zeros(n_steps+1, 1+m_steps);

for p = 1:1+m_steps
    
    pH = pHin;
    
    for c = 1:n_steps+1
    
        %calculate alphas
        alpha0 = calc_alpha0(pH, pK1, pK2);
        alpha1 = calc_alpha1(pH, pK1, pK2);
        alpha2 = calc_alpha2(pH, pK1, pK2);
        CO2sat = PCO2*Kh*1000; %(mole/m3) saturation concentration of CO2 in water
        
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
              
        r(c,1)= pH; %record pH
        r(c,1+p)= loss; %record loss
        pH = pH + delpH;  %increase pH 
    end
   alk = alk + delalk;
end
end

