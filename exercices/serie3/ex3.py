#!/usr/bin/python
from time import sleep

def affiche_tic_tac(nb_secondes):
    while nb_secondes > 0:
        if nb_secondes % 2 == 1:
            print("Tic")
        else:
            print("Tac")
        nb_secondes -= 1
        sleep(1)

affiche_tic_tac(6)
