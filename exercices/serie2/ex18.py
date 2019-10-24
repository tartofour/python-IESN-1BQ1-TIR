#!/usr/bin/python
from math import pi

### FONCTION ###
def calcul_circonference():
    global rayon 
    circonference = 2 * pi * rayon
    print("La circonférence du cercle est de {:.2f}".format(circonference))

### MAIN ###
rayon = float(input("Entrez le rayon du cercle : "))
calcul_circonference()
