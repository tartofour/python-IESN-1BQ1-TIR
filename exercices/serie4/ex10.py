#!/usr/bin/python

def reverse_str(s: str) -> str:
    reversed_string = ""
    i = len(s) - 1  
    while i >= 0:
        reversed_string += (s[i])
        i -= 1
    return reversed_string 
   
s = input("Entrez une chaine de caractères : ")
print(reverse_str(s))
