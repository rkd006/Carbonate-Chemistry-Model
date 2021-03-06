% author: Riley Doyle
% date: 7/31/20
% file name: calc_CO2_loss_sal
% output: Calculate loss with different temp values and pHs

function r_sal = calc_CO2_loss_sal (T, PCO2, t, p, alk, kLa, pHin, pHend, delpH, send, sin, dels)

%initialize
m_steps = (send-sin)/dels;
S = sin;

n_steps = (pHend - pHin)/delpH;
r_sal = zeros(n_steps+1, 1+m_steps);

for n = 1:1+m_steps
    
    pH = pHin;
    
    for c = 1:n_steps+1
        den = calc_density(S, t, p);
        K_1 = calc_K1(T, S)*(den/1000); %no units
        pK1 = -log10(K_1); %no units
        K_2 = calc_K2(T, S)*(den/1000); %no units
        pK2 = -log10(K_2); %no units
        Kh = calc_Kh(T,S)*(den/1000);
        CO2sat = PCO2*Kh*1000; %(mole/m3) saturation concentration of CO2 in water
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
              
        r_sal(c,1)= pH; %record pH
        r_sal(c,1+n)= loss; %record loss
        pH = pH + delpH;  %increase pH 
    end
   S = S + dels;
end
end
