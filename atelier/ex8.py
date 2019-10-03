#!/usr/bin/python
nbreUser = float(input("Entrez un nombre entier positif : "))
partieEntiere = int(nbreUser)
partieDecimale = nbreUser - int(nbreUser) 

print("{} = {} + {}".format(nbreUser, partieEntiere, partieDecimale))

# Bug, je sais pas pourquoi. 
