#!/usr/bin/env python3
from math import pi

def calcul_circonference():
    global rayon 
    circonference = 2 * pi * rayon
    print("La circonférence du cercle est de {:.2f}".format(circonference))

rayon = float(input("Entrez le rayon du cercle : "))
calcul_circonference()
