function rhs = rates(t, x) 
  global k1 k2 k3 k4
  
  na = x(1);
  nb = x(2);
  nc = x(3);
  
  r1 = k1;       %rate of Caq removed due to alkalinity consumption by algae Eq(15) in report
  r2 = k2*na - k3 + k4; % C needed to be delivered to satisfy growth (CO2 and HCO3-), diffusion out of pond
  r3 = k2*na - k3;      % 
  
  rhs = [-r1; r2; r3];
  
  
    
        