%function for the right hand side of the ODE system for inorganic carbon
%calculation
function y = rates2(t,x)
    global k1
    Ct = x(1);
    dCtdt = k1;
    y = [dCtdt];
end