#!/usr/bin/python

nb_user = int(input("Entrez un nombre de secondes : "))

nb_semaines = nb_user // 604800
nb_jours = (nb_user % 604800) // 86400 
nb_heures = ((nb_user % 604800) % 86400) // 3600
nb_minutes =  (((nb_user % 604800) % 86400) % 3600) // 60
nb_secondes = ((((nb_user % 604800) % 86400) % 3600) % 60 ) % 60

print("{} secondes = {} semaines {} jours {} heure {} minutes {} secondes".format(nb_user, nb_semaines, nb_jours, nb_heures, nb_minutes, nb_secondes))
