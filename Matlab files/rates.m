%function for the right hand side of the ODE system
function rhs = rates(t, x) 
  global k1 k2 k3 k4
  
  %na is the unknown aka Caq is collected in a vector x
  na = x(1);
  nb = x(2);
  nc = x(3);
  
  %equations 15, 18 and 19 in the report
  r1 = k1;       %rate of Caq removed due to alkalinity consumption by algae Eq(15) in report
  r2 =(k2*na - k3) + k4; % C needed to be delivered to satisfy growth (CO2 and HCO3-), diffusion out of pond
  r3 = k2*na - k3;      % loss of CO2 to the atmosphere
  
  rhs = [-r1; r2; r3];
  
  
    
        