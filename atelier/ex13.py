#!/usr/bin/python
# Je suis pas certain d'avoir compris les consignes.


nb_batiments = int(input("Combien de bâtiment(s) à contruire ? : "))
ressources_necessaires = int(input("Combien de ressources nécessaires par bâtiment ? : "))
ressources_disponibles = int(input("Combien de ressources possèdons-nous ? : "))

if nb_batiments != 0 and nb_batiments <= 15:
    nb_batiments_valide = True
    print("Nombre de bâtiment(s) valide")

if nb_batiments * ressources_necessaires > ressources_disponibles:
    ressources_insuffisantes = True
    print("Ressources insuffisantes.")

if nb_batiments != 0 and nb_batiments <= 15 and nb_batiments * ressources_necessaires <= ressources_disponibles:
    peut_construire = True
    print("On peut construire.")

