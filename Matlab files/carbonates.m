function rhs = carbonates(t, x) 
  global kp1 km1 kp4 km4 kp5H km5H kp5OH km5OH kp6 km6 
  
  %the unknowns 
  CO2 = x(1);
  HCO3 = x(2);
  CO3 = x(3);
  H = x(4);
  OH = x(5);
  
  dCO2dt = (km1*H+km4)*HCO3 - (kp1+kp4*OH)*CO2;
  dHCO3dt = (kp1+kp4*OH)*CO2 - (km1*H+km4)*HCO3 + (kp5H*H+kp5OH)*CO3 - (km5H+kp5OH*OH)*HCO3;
  dCO3dt = (km5H+kp5OH*OH)*HCO3 - (kp5H*H+km5OH)*CO3;
  dHdt = kp1*CO2 - km1*H*HCO3 + km5H*HCO3 - kp5H*H*CO3 + kp6 - km6*H*OH;
  dOHdt = km4*HCO3 - kp4*OH*CO2 - kp5OH*OH*HCO3 + km5OH*CO3 + kp6 - km6*H*OH;
  rhs = [dCO2dt; dHCO3dt; dCO3dt; dHdt; dOHdt];
  