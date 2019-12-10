#!/usr/bin/python

def print_mail(contacts: dir, name:str) -> None:
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact introuvable")

contacts = {"benjamin" : "benjamin.verjus@gmail.com", "jean" : "jean@gmail.com"}
name = input("Entrez le nom du contact dont vous souhaitez récupérer l'adresse mail : ")
print_mail(contacts, name)
