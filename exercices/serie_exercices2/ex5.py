#!/usr/bin/python

nb1 = int(input("Entrez un premier nombre : "))
nb2 = int(input("Entrez un deuxième nombre : "))
nb3 = int(input("Entrez un troisième nombre : "))

if nb1 == nb2 or nb1 == nb3 or nb2 == nb3:
    print("Au moins deux nombres sont égaux !")
