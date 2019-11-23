#!/usr/bin/python
from math import pi

def aire_disque(rayon : float) -> float:
    """Retourne l'aire du cercle de rayon x

    Args :
        rayon(float): rayon du cercle

    Return :
        aire_cercle(float)

    """
    return pi * rayon**2

rayon_cercle = float(input("Entrez le rayon du cercle : "))
print(aire_disque(rayon_cercle))

