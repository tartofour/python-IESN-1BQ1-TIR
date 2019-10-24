#!/usr/bin/python

def bonjour():
    global nom_user
    print("Bonjour {} !".format(nom_user))

nom_user = input("Veuillez entrer votre nom : ")
bonjour()
