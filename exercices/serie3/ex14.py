#!/usr/bin/python
from math import pi

def aire_disque(rayon : float) -> float:
    return pi * rayon**2

rayon_cercle = float(input("Entrez le rayon du cercle : "))
print(aire_disque(rayon_cercle))

