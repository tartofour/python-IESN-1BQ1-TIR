#!/usr/bin/python

def lettres_count(word: str) -> dict:
    dict_counter = {}
    for letter in word:
        if letter not in dict_counter:
            dict_counter[letter] = 1
        else:
            dict_counter[letter] += 1 
    return dict_counter

word = input("Entrez un mot : ")
print(lettres_count(word))
