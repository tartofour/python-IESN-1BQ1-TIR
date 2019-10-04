#!/usr/bin/python

nb_user = int(input("Entrez un nombre de secondes : "))

nb_heures = nb_user // 3600
nb_minutes = (nb_user % 3600) // 60
nb_secondes = (nb_user % 3600) % 60

print("{} secondes = {} heure {} minutes {} secondes".format(nb_user, nb_heures, nb_minutes, nb_secondes))
