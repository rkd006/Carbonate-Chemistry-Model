T = 20 + 273.15; %temp in Kelvin
S = 35; %(salinity in g/kg)
K_1 = calc_K1(T, S); 
pK1 = -log10(K_1);
K_2 = calc_K2(T, S); 
pK2 = -log10(K_2);
CO2sat = 0.012716352; %(mole/m3) saturation concentration of CO2 in water
alk = 2.5; %(eq/m3) from Weissman et al. (1987)
pHin = 6.5;
pHend = 8.5;
delpH = 0.1; 

kLain= 0.5; % (1/hour)
kLaend= 8.5;
delkLa = 2; 

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
              
        r_kL_pH(c,1)= pH %record pH
        r_kL_pH(c,1+p)= loss %record loss
        pH = pH + delpH;  %increase pH 
    end
   kLa = kLa + delkLa;
end
