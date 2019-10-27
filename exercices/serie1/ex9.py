#!/usr/bin/python

total_secondes = int(input("Entrez un nombre de secondes : "))

nb_heures = total_secondes // 3600
nb_minutes = (total_secondes % 3600) // 60
nb_secondes = (total_secondes % 3600) % 60

print("{} secondes = {} heure {} minutes {} secondes".format(total_secondes, nb_heures, nb_minutes, nb_secondes))
