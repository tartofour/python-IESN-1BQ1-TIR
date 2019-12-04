#!/usr/bin/python

def print_antipode(coord: tuple) -> None:
    if (coord[0] > 180 or coord[0] < -180) or \
        (coord[1] > 90 or coord[1] < -90):
            print("Erreur dans les coordonnées !")
    else:
        latitude = coord[0] * -1
        if coord[1] >= 0:
            longitude = coord[1] - 180
        else:
            longitude = coord[1] + 180
    
        coordonnées = (latitude, longitude)
        print(coordonnées)

latitude = float(input("Entrez une latitude : "))
longitude = float(input("Entrez une longitude : "))
coordonnee_gps = (latitude, longitude)

print_antipode(coordonnee_gps)
