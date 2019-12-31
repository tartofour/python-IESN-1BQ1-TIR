#!/usr/bin/env python3

def tic():
    global nb_secondes
    if nb_secondes > 0:
        print("Tic")
        nb_secondes -= 1
        tac()

def tac():
    global nb_secondes
    if nb_secondes > 0:
        print("Tac")
        nb_secondes -= 1
        tic()

nb_secondes = int(input("Entrez un nombre de seconde(s) : "))
tic()
