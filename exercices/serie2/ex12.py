#!/usr/bin/python
from random import randrange

nb_mystere = randrange(0,100)
nb_user = -1

while nb_user != nb_mystere:
    nb_user = int(input("Entrez un nombre compris en 1 et 100 : "))

    if nb_user > nb_mystere:
        print("Trop grand !\n")
    elif nb_user < nb_mystere:
        print("Trop petit !\n")
    else:
        print("Gagné !")
