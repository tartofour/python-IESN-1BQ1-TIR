#!/usr/bin/python

total_secondes = int(input("Entrez un nombre de secondes : "))

nb_semaines = total_secondes // 604800
nb_jours = (total_secondes % 604800) // 86400 
nb_heures = ((total_secondes % 604800) % 86400) // 3600
nb_minutes =  (((total_secondes  % 604800) % 86400) % 3600) // 60
nb_secondes = ((((total_secondes % 604800) % 86400) % 3600) % 60 ) % 60

print("{} secondes = {} semaines {} jours {} heure {} minutes {} secondes".format(total_secondes, nb_semaines, nb_jours, nb_heures, nb_minutes, nb_secondes))
