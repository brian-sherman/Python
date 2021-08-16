"""
Define a function compute_gas_volume that returns the volume of a gas given parameters 
pressure, temperature, and moles. 
Use the gas equation PV = nRT, 
where P is pressure in Pascals, 
V is volume in cubic meters, 
n is number of moles, 
R is the gas constant 8.3144621 ( J / (mol*K)), and 
T is temperature in Kelvin.

"""

gas_const = 8.3144621

def compute_gas_volume(pressure, temperature, moles):
    volume = (moles * gas_const * temperature) / pressure
    return volume

gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')