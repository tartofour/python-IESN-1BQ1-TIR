#!/usr/bin/python

nb_user = float(input("Entrez un nombre entier positif : "))
partie_entiere = nb_user // 1
partie_decimale = nb_user % 1 

print("{} = {} + {}".format(nb_user, partie_entiere, partie_decimale))
