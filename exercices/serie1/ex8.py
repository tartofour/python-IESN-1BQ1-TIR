#!/usr/bin/python

nb = float(input("Entrez un nombre entier positif : "))
partie_entiere = nb // 1
partie_decimale = nb % 1 

print("{} = {} + {}".format(nb, partie_entiere, partie_decimale))
