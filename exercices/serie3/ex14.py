#!/usr/bin/python

### FONCTION ###
def aire_disque(rayon : float) -> float:
    from math import pi

    return pi * rayon**2

### MAIN ###

rayon_cercle = float(input("Entrez le rayon du cercle : "))
print(aire_disque(rayon_cercle))

