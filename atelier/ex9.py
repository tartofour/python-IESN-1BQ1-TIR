#!/usr/bin/python

nbreUser = int(input("Entrez un nombre de secondes : "))

nbreHeures = nbreUser // 3600
nbreMinutes = (nbreUser % 3600) // 60
nbreSecondes = (nbreUser % 3600) % 60

print("{} secondes = {} heure {} minutes {} secondes".format(nbreUser, nbreHeures, nbreMinutes, nbreSecondes))
