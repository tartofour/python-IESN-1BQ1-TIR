#!/usr/bin/python
from math import cos, sin, acos, fabs, radians

def distance_on_earth(coord1: tuple, coord2: tuple) -> float:
    distance = 6378 * acos(sin(coord1[0]) * sin(coord2[0]) \
    + cos(coord1[0]) * cos(coord2[0]) * cos(fabs(coord1[1]-coord2[1])))
    
    print("{:.3f}km".format(distance))


latitude1 = radians(float(input("Entrez une latitude en degrés : ")))
longitude1 = radians(float(input("Entrez une longitude en degrés : ")))
latitude2 = radians(float(input("Entrez une latitude : ")))
longitude2 = radians(float(input("Entrez une longitude : ")))
coordonnee_gps1 = (latitude1, longitude1)
coordonnee_gps2 = (latitude2, longitude2)

distance_on_earth(coordonnee_gps1, coordonnee_gps2)
