#!/usr/bin/python
commande_user = input("Quelle commande souhaitez-vous utiliser ? \n\nO : ouverture d'un fichier, \nX : sortie d'un programme, \nF : fermeture d'un fichier, \nP : impression d'un fichier) \n\nVotre choix : ").capitalize()

if commande_user == "O":
    fichier = input("\nTapez le nom du fichier : ")
    print("\nOuverture du fichier {}.".format(fichier))
elif commande_user == "X":
    confirmation = input("\nÊtes-vous sûr de vouloir quitter le programme ? (o/n) : ")
    if confirmation.lower() == "o":
        print("Aurevoir !")
elif commande_user == "F":
    print("\nLe fichier a bien été fermé !")
elif commande_user == "P":
    nb_exemplaire = int(input("\nCombien d'exemplaire(s) de ce fichier voulez-vous imprimer ? : "))
    print("Impression de {} exemplaire(s).".format(nb_exemplaire))
else:
    print("\nParamètre invalide !")
