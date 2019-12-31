#!/usr/bin/env python3

def tic():
    print("Tic")

def tac():
    print("Tac")

nb_secondes = int(input("Entrez un nombre de seconde(s) : "))
while nb_secondes > 0:
    if nb_secondes % 2 == 0:
        tic()
    else: 
        tac()
    nb_secondes -= 1
