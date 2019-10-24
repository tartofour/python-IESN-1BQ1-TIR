#!/usr/bin/python

### FONCTION ###
def bonjour():
    global nom_user
    print("Bonjour {} !".format(nom_user))

### MAIN ###
nom_user = input("Veuillez entrer votre nom : ")
bonjour()
