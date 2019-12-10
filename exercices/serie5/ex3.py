#!/usr/bin/python

def print_all(contacts: dict) -> None:
    for contact in contacts:
        nom, email = contact, contacts[contact]
        print("Nom: {} - Email : {}".format(nom, email))

contacts = {"Benjamin" : "benjamin.verjus@gmail.com", "Jean" : "jean@gmail.com"}
print_all(contacts)
