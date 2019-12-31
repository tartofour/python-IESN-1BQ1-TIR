#!/usr/bin/env python3

temperature_kelvin = float(input("Entrez une t° en Kelvin : "))
temperature_celsius = temperature_kelvin - 273.15
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print("{:.2f} K = {:.2f} °F = {:.2f} °C".format(temperature_kelvin, temperature_fahrenheit, temperature_celsius))

