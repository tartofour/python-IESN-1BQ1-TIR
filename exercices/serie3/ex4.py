#!/usr/bin/python

### FONCTION ###
def affiche_ip(octet1, octet2, octet3, octet4):
    print(octet1, octet2, octet3, octet4, sep='.')

### MAIN ###
nb1 = int(input("Entrez un premier nombre : "))
nb2 = int(input("Entrez un deuxième nombre : "))
nb3 = int(input("Entrez un troisième nombre : "))
nb4 = int(input("Entrez un quatrième nombre : "))

affiche_ip(nb1, nb2, nb3, nb4)
