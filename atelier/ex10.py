#!/usr/bin/python

nbreUser = int(input("Entrez un nombre de secondes : "))

nbreSemaines = nbreUser // 604800
nbreJours = (nbreUser % 604800) // 86400 
nbreHeures = ((nbreUser % 604800) % 86400) // 3600
nbreMinutes =  (((nbreUser % 604800) % 86400) % 3600) // 60
nbreSecondes = ((((nbreUser % 604800) % 86400) % 3600) % 60 ) % 60

print("{} secondes = {} semaines {} jours {} heure {} minutes {} secondes".format(nbreUser, nbreSemaines, nbreJours, nbreHeures, nbreMinutes, nbreSecondes))
