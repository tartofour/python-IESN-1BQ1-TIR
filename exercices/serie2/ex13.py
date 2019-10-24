#!/usr/bin/python
from random import randrange

nb_mystere = randrange(0,100)
nb_user = -1
nb_essais = 5

while nb_user is not nb_mystere and nb_essais is not 0:
    print("Il vous reste  {} essai(s)".format(nb_essais))
    nb_user = int(input("Entrez un nombre compris entre 1 et 100 : "))

    if nb_user > nb_mystere:
        print("Trop grand !\n")
        nb_essais -= 1
    elif nb_user < nb_mystere:
        print("Trop petit !\n")
        nb_essais -= 1
    else:
        print("Gagné !")

if nb_essais is 0:
    print("Perdu")
