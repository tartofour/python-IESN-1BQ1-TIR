#!/usr/bin/python

def update_contact(contacts: dict, name:str, mail: str) -> None:
    contacts[name] = mail
    print(contacts)

contacts = {"benjamin" : "benjamin.verjus@gmail.com", "Jean" : "jean@gmail.com"}
name = input("Entrez le nom du contact : ")
mail = input("Entrez l'adresse mail du contact : ")
update_contact(contacts, name, mail)

