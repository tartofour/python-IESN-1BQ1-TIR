#!/usr/bin/python

def count_chars(chars: str, s: str) -> int:
    length = len(s)
    i = 0
    compteur = 0
    while i < length:
        if s[i] in chars:
            compteur += 1
        i += 1
    return compteur

print(count_chars("ac", "abbcccddd"))
