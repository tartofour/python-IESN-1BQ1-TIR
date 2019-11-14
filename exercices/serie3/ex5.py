#!/usr/bin/python

### FONCTION ###
def affiche_message_bienvenue(nom, formule_politesse="Bonjour"):
    print(formule_politesse, nom)

### MAIN ### 
nom_user = input("Entrez votre nom : ")
affiche_message_bienvenue(nom_user) 

