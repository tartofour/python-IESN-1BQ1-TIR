#!/usr/bin/python
import math

rayon = float(input("Entrez un rayon en mètre : "))
circonference = 2 * math.pi * rayon
aire = math.pi * rayon**2

print("Circonférence : {} \n Aire : {}".format(circonference, aire))

