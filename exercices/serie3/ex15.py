#!/usr/bin/python
from random import randint
from time import sleep

### FONCTIONS ###
def affiche_menu():
    print("1. Affichez une blague\n2. Jouer au nombre mystère\n3. Minuteur")

def affiche_blague():
    liste_blagues = ["\nQu'est-ce qui est blanc, tombe du ciel et fini par 'ard' ?\nLa neige connard !\n", "\nQuelle est la différence entre une BMW et une LADA ?\nDans la BWM t'as l'air-co et dans la LADA t'as l'air con.\n", "\nPourquoi la petite fille tombe-t-elle de la balançoire ?\nParce qu'elle n'a pas de bras.\n", "\nQue faire lorsqu'un geek pleure ?\nOn le console.\n"]
    choix_blague = randint(1, len(liste_blagues))
    print(liste_blagues[choix_blague-1])

def jeu_nb_mystere(): 
    nb_mystere = randint(1, 100)
    nb_essais = 5
    nb_user = None
    
    while nb_user != nb_mystere and nb_essais != 0:
        print("Il vous reste  {} essai(s)".format(nb_essais))
        nb_user = int(input("Entrez un nombre compris entre 1 et 100 : "))

        if nb_user > nb_mystere:
            print("Trop grand !")
            nb_essais -= 1
        elif nb_user < nb_mystere:
            print("Trop petit !")
            nb_essais -= 1
        else:
            print("Gagné !")
    
    if nb_essais == 0:                                                                                                                                             
        print("Perdu")    

def minuteur(nb_secondes: int):
    while nb_secondes > 0:
        print(nb_secondes)
        nb_secondes -= 1
        sleep(1)


### MAIN ###
continuer = True

while continuer:
    affiche_menu()
    choix_user = int(input("Que voulez vous faire ? (1-2-3): "))

    if choix_user == 1:
        affiche_blague()
        continuer == False
    elif choix_user == 2:
        jeu_nb_mystere()
        continuer == False
    elif choix_user == 3:
        nb_secondes = int(input("Combien de secondes doit durer le minuteur ? : "))
        minuteur(nb_secondes)
