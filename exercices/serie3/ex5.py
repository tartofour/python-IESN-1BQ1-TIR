#!/usr/bin/python

def affiche_message_bienvenue(nom, formule_politesse="Bonjour"):
    print(formule_politesse, nom)

nom_user = input("Entrez votre nom : ")
affiche_message_bienvenue(nom_user) 

