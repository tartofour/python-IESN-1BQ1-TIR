#!/usr/bin/python

continuer = True
print("Bonjour")

while continuer:
    age = input("Quel est votre âge ? : ")

    if age.isdigit():
        print(age)
        print(int(age)+10)
        continuer = False
    else: 
        print("Entrez un nombre !")
