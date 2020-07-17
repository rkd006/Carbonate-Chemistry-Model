%function for the right hand side of the ODE system
function rhs = rates(t, x) 
  global k1 k2 k3 k4
  
  %the unknowns 
  Caq = x(1);
  Cdel = x(2);
  Closs = x(3);
  
  %equations 15, 18 and 19 in the report
  dCaqdt = k1;       %rate of Caq removed due to alkalinity consumption by algae Eq(15) in report
  dCdeldt =(k2*Caq - k3) + k4; % C needed to be delivered to satisfy growth (CO2 and HCO3-), diffusion out of pond
  dClossdt = k2*Caq - k3;      % loss of CO2 to the atmosphere
  
  rhs = [-dCaqdt; dCdeldt; dClossdt];
  
  
    
        