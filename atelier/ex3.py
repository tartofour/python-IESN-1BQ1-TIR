#!/usr/bin/python
temperatureKelvin = int(input("Entrez une t° en Kelvin : "))
temperatureCelsius = temperatureKelvin - 273.15
temperatureFahrenheit = (temperatureCelsius * 9/5) + 32


print("{} K = {} °F = {} °C".format(temperatureKelvin, temperatureFahrenheit, temperatureCelsius))
