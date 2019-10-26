#!/usr/bin/python

prix_htva = int(input("Entrez le prix de l'article : "))
categorie = int(input("Entrez la catégorie de l'articles (1 : normal, 2 : important, 3 : nécessaire) : "))

if categorie == 2:
    print(prix_htva * 1.12)
elif categorie == 3:
    print(prix_htva * 1.06)
else:
    print(prix_htva * 1.21)
