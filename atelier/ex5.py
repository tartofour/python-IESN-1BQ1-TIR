#!/usr/bin/python
import math

rayon = float(input("Entrez un rayon en mètre : "))
circonference = 2 * math.pi * rayon
aire = math.pi * rayon**2

print("Circonférence : {:.2f}m \nAire : {:.5f}m²".format(circonference, aire))

