#!/usr/bin/python
nbreUser = float(input("Entrez une nombre entier positive : "))
partieEntiere = int(nbreUser / 1)
partieDecimale = nbreUser % 1

print("{} = {} + {}".format(nbreUser, partieEntiere, partieDecimale))
