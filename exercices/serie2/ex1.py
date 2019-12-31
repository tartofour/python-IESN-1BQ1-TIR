#!/usr/bin/env python3

# 1
nb = 12.0
print(nb // 1 == nb)

#2
print(0x00 <= nb <= 0xFF)

#3
st = "bonjour"
print("b" < st > "bouton")

#4
print(nb > 0 and ((nb % 2 == 1) and nb > 100) or (nb % 2 == 0 and not(nb > 100)))

#5
nb1 = 17
nb2 = 16
print(abs(nb1-nb2) == 1)
