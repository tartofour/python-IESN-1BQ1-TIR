#!/usr/bin/python

def is_palindrome(s: str) -> bool:
    string_to_compare = "" 
    length = len(s) - 1
    while length >= 0:
        string_to_compare += s[length]
        length -= 1
    return string_to_compare == s

mot = input("Entrez un mot pour vérifier s'il s'agit d'un palindrome : ")
print(is_palindrome(mot))


