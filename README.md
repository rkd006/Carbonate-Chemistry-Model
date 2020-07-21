# Carbonate Chemistry Model
The objective of this project is to create a carbonate chemistry model that predicts CO2 losses to the atmosphere from algae raceway ponds. It is funded by the U.S. Department of Energy.
[image of pond] (https://sites.nicholas.duke.edu/odar/files/2018/03/Algae-pond-johnson-1.jpg)

## Table of contents
* [Revelant Information and Equations](#relevant-information-and-equations)
* [Technologies](#technologies)
* [Output of Each File](#output-of-each-file)
* [Authors](#authors)

## Relevant Information and Equations

## Technologies
Project is created with:
* MATLAB version: R2020a
* Python version: 3.7 
* Anaconda package with numpy and matplotlib

## Output of Each File
### MATLAB:
- calc_alpha0: creates a function to calculate alpha0  
- calc_alpha1: creates a function to calculate alpha1
- calc_alpha2: creates a function to calculate alpha2
- calc_alphas: calculate CO2 losses to the atmossphere numerically
- calc_CO2_loss: creates a function to calculate the CO2 losses to the atmosphere with inputs of pH and alkalinity ranges
- calc_CO2_loss_kLa: creates a function to calculate the CO2 losses to the atmosphere with inputs of pH and kLa ranges
- calc_K1: creates a function to calculate K1
- calc_K2: creates a function to calculate K2
- calc_Kh: creates a function to calculate Kh
- calc_CO2_loss_alk: creates a function to calculate the CO2 losses to the atmosphere with inputs of kLa and alk ranges
- plot_carbonates: figure that plots the distribution of carbonate species (H2CO3*, HCO3, CO3)
- rates: creates a function to calculate the system of ODEs

#### *with algal growth:*

- CO2_loss_algal_growth_alk: multiple figures that plot CO2 requirements and losses over four days at several alkalinites for different kLa values
- CO2_loss_algal_growth_kLa: figure that plots CO2 requirements and losses over four days for several kLa values
- CO2_loss_algal_growth_pH: figure that plots CO2 requirements and losses over four days for several pHs
- CO2_loss_algal_growth_range: figure that plots CO2 requirements and losses over four days for several algal growth rates
- CO2_loss_dynamic: figure that plots CO2 requirements and losses over four days and figure that plots CO2 concentration over four days

#### *without algal growth:*

- CO2_loss_kLa_comb: multiple figures that plot CO2 losses to the atmosphere at different alkalinities and pHs for different kLa values
- CO2_loss_kLa_simple: figure that plots CO2 losses to the atmopshere for different alkalinities and figure that plots CO2 losses to the atmosphere for different pHs
- CO2_loss_range_kLa: figure that plots CO2 losses to the atmosphere at different kLa values and pHs
- CO2_loss_script: figure that plots CO2 losses to the atmosphere at different alkalinities and pHs

### Python:

*see MATLAB files outputs above for replicates if not stated below*

- calc_[carbon]_pond: calculate carbon concentration in the pond numerically and figure that plots carbon concentration over four days
- calc_alphas: creates functions to calculate alpha0, alpha1, alpha2
- calc_Ks: creates functions to calculate K1, K2, Kh
- CO2_loss_dynamic_y3: igure that plots CO2 requirements and losses over four days and figure that plots CO2 concentration over four days for a combined y3 

## Authors
Deborah Sills

Riley Doyle


