#!/usr/bin/env python3

def affiche_echiquier():
    i = 8
    while i > 0:
        if i % 2 == 0:
            print("_ # " * 4)
        else: 
            print("# _ " * 4)
        i-=1

affiche_echiquier()
