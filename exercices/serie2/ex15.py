#!/usr/bin/python

### FONCTIONS ###
def ouvrir():
    fichier = input("\nTapez le nom du fichier : ")
    print("\nOuverture du fichier {}.".format(fichier))

def sortir():
    confirmation = input("\nÊtes-vous sûr de vouloir quitter le programme ? (o/n) : ")
    if confirmation.lower() == "o":
        print("Aurevoir !")

def fermer():
    print("\nLe fichier a bien été fermé !")

def imprimer():
    nb_exemplaire = int(input("\nCombien d'exemplaire(s) de ce fichier voulez-vous imprimer ? : "))
    print("Impression de {} exemplaire(s).".format(nb_exemplaire))

def invalid_parameter():
    print("\nParamètre invalide !")

### MAIN ###    
commande_user = input("Quelle commande souhaitez-vous utiliser ? \n\nO : ouverture d'un fichier, \nX : sortie d'un programme, \nF : fermeture d'un fichier, \nP : impression d'un fichier) \n\n").capitalize()

if commande_user == "O":
    ouvrir()
elif commande_user == "X":
    sortir()
elif commande_user == "F":
    fermer()
elif commande_user == "P":
    imprimer()
else:
    invalid_parameter()
