#!/usr/bin/env python3
from math import pi

rayon = float(input("Entrez un rayon en mètre : "))
circonference = 2 * pi * rayon
aire = pi * rayon**2
print("Circonférence : {:.2f}m \nAire : {:.5f}m²".format(circonference, aire))

