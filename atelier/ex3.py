#!/usr/bin/python
temperatureKelvin = float(input("Entrez une t° en Kelvin : "))
temperatureCelsius = temperatureKelvin - 273.15
temperatureFahrenheit = (temperatureCelsius * 9/5) + 32

print("{:.2f} K = {:.2f} °F = {:.2f} °C".format(temperatureKelvin, temperatureFahrenheit, temperatureCelsius))

