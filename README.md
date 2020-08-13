# Carbonate Chemistry Model
The objective of this project is to create a carbonate chemistry model that predicts CO2 losses to the atmosphere and CO2 requirements as function of pH, alkalinity, kLa, temperature and salinity from algae raceway ponds. It is funded by the U.S. Department of Energy and part of the MAGIC (Marine Algae Industrialization Consortium) project headed by Duke University and Professor Zachary Johnson.

## Table of Contents
* [Revelant Information and Equations](#relevant-information-and-equations)
* [Technologies](#technologies)
* [Usage](#usage)
* [Output of Each File](#output-of-each-file)
* [Authors](#authors)

## Relevant Information and Equations
In most natural systems, acid buffering capacity is predominately made up by the carbonate system, which consists of four species - dissolved carbon dioxide, carbonic acid, bicarbonate and carbonate. Carbonic acid exists in only very small quantities and to simplify we define it as follows:

<img src="images/eq1.PNG" width = 700> 

CT is defined as the total concentration of carbonate species in solution:

<img src="images/eq2.PNG" width = 700> 

In addition, the carbonate species are related to each other through the following equilibrium relationships:

<img src="images/screenshot1.PNG" width = 700>

the molar concentration of each carbonate species is dependent on pH as shown below:

<img src="images/eq3.PNG" width = 725> 


<img src="images/eq5.PNG" width = 725> 


Mass transfer of carbon dioxide is a function of alkalinity and pH, based on the following equation:

<img src="images/eq9.PNG" width = 708>

Dissolved carbon dioxide concentration can be calculated as follows:

<img src="images/eq10.PNG" width = 708> 

The effect of pH, alkalinity, and algal growth rates on carbon dioxide requirements and losses to the atmosphere were modeled for a raceway pond and operated in batch mode for 4 days. A mass balance on alkalinity and the aqueous concentration of carbon dioxide results in the following equation:

<img src="images/eq11.PNG" width = 708> 

A mass balance on Ct and rearranging results in the following equation for carbon dioxide requirements:

<img src="images/eq12.PNG" width = 708>

*excerpted from Sills' 2013 report*
## Technologies
This project is created with:
* MATLAB version: R2020a
* Python version: 3.7 
* Anaconda package with numpy and matplotlib

## Usage
To run this project, you can:
1. To clone with HTTPS, click on:

<img src="images/code.PNG" width = 100>
 
2. clone using git:
```
git clone https://github.com/rkd006/Carbonate-Chemistry-Model

```

## Output of Each File
### MATLAB:

*python code is recently updated*

- calc_alpha0: creates a function to calculate alpha0  
- calc_alpha1: creates a function to calculate alpha1
- calc_alpha2: creates a function to calculate alpha2
- calc_alphas: calculate CO2 losses to the atmossphere numerically
- calc_density: calculate the density of seawater
- calc_CO2_loss: creates a function to calculate the CO2 losses to the atmosphere with inputs of pH and alkalinity ranges
- calc_CO2_loss_kLa: creates a function to calculate the CO2 losses to the atmosphere with inputs of pH and kLa ranges
- calc_K1: creates a function to calculate K1
- calc_K2: creates a function to calculate K2
- calc_Kh: creates a function to calculate Kh
- calc_CO2_loss_alk: creates a function to calculate the CO2 losses to the atmosphere with inputs of kLa and alk ranges
- calc_CO2_loss_temp: creates a function to calculate the CO2 losses to the atmosphere with inputs of pH and temperature ranges
- calc_CO2_loss_sal: creates a function to calculate the CO2 losses to the atmosphere with inputs of pH and salinity ranges
- calc_inorganiccarbon_pond: calculates inorganic carbon concentration in the pond at four days numerically and figure that plots the inorganic carbon concentration over four days
- calc_algaecarbon: calculates the carbon concentration in algae at four days numerically 
- plot_carbonates: figure that plots the distribution of carbonate species (H2CO3*, HCO3, CO3)
- rates: creates a function to calculate the system of ODEs
- rates2: creates a function to calulate the ODE for calc_inorganiccarbon_pond

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
- CO2_loss_script_temp: multiple figures that plot CO2 losses to the atmosphere at different alkalinities and pHs for different temperatures
- CO2_loss_script_sal: multiple figures that plot CO2 losses to the atmosphere at different alkalinities and pHs for different salinities

### Python:
*updated recently*

*see MATLAB files outputs above for replicates if not stated below*

- calc_alphas: creates functions to calculate alpha0, alpha1, alpha2
- calc_Ks: creates functions to calculate K1, K2, Kh
- CO2_loss_dynamic_y3: figure that plots CO2 requirements and losses over four days and figure that plots CO2 concentration over four days for a combined y3 
- subplot_sal: a) creates multiple subplots side by side of the figures from CO2_loss_script_sal b) creates multiple subplots side by side of the figures from CO2_loss_algal_growth_sal
- subplot_temp: a) creates multiple subplots side by side of the figures from CO2_loss_script_temp b) creates multiple subplots side by side of the figures from CO2_loss_algal_growth_temp
- CO2_loss_algal_growth_temp: figure that plots CO2 requirements and losses over four days for several temperatures
- CO2_loss_algal_growth_sal: figure that plots CO2 requirements and losses over four days for several salinities

#### *subplots:*

- subplot_algal_growth_pH: creates multiple subplots side by side of the figures from CO2_loss_algal_growth_pH for kLa = 0.5 1/hr and alkalinity = 2.5 eq/m3
- subplot_algal_growth_range: creates multiple subplots side by side of the figures from CO2_loss_algal_growth_range for kLa = 0.5 1/hr, and alkalinity = 3.5 eq/m3 at pH = 6, 7, and 8
- subplot_algal_growth_alk: creates multiple subplots side by side of the figures from CO2_loss_algal_growth_alk for kLa = 0.5 1/hr, kLa = 3 1/hr, alkalinity = 2 and 32 eq/m3 at pH = 6, 7, and 8
- subplot_kLa_comb: creates multiple subplots side by side of the figures of kLa = 0.5 1/hr and kLa = 3 1/hr from CO2_loss_kLa_comb
- subplot_algal_growth_tempsal: create subplots side by side of the figures from CO2_loss_algal_growth_temp and CO2_loss_algal_growth_sal

#### *with algal growth kinetics:*

- specific_growth_rate: calculated the specific growth rate as a function of light intensity based on different models
- algae_productiivity: calculate biomass productivity as a function of time based on different models
- algae_productivity_boriah: calculate biomass productivity as a function of time based on the model presented in "Modeling Algae Growth in an Open-Channel Raceway" by Scott C. James and Varun Boriah
- CO2_loss_dynamic_monod: figure that plots CO2 requirements and losses over four days and figure that plots CO2 concentration over four days, which includes algal growth kinetics based on Monod
- CO2_loss_dynamic_boriah: figure that plots CO2 requirements and losses over four days and figure that plots CO2 concentration over four days, which includes algal growth kinetics based on boriah
- Beer_Lambert_Law: figure that plots light intensity as a function of position for constant biomass concentration 
- CO2_loss_dynamic_aiba: figure that plots CO2 requirements and losses over four days, which includes algal growth kinetics based on the modified aiba model


## Authors
- Deborah Sills
  - Assistant Professor in the Civil and Environmental Engineering Department at Bucknell University
  - [her website](https://deborahsills.com/)
- Riley Doyle
  - Undergraduate Student at Bucknell University, majoring in environmental engineering and graduating in 2022
  - email: rkd006@bucknell.edu
  - [LinkedIn](https://www.linkedin.com/in/riley-doyle-591565196/)


