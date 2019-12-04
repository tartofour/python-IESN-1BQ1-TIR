#!/usr/bin/python

def str_to_low(s: str) -> str:
    lower_list = ""
    length = len(s)
    i = 0
    while i < length:
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            lower_list += chr(ord(s[i]) + 32)
        else:
            lower_list += s[i]
        i += 1
    return lower_list 

s = "HelLO, It'S Me"
print(str_to_low(s))
