#!/usr/bin/python
# Virer le for i in range et le remplacer par un while. Bisou bisou.
# Full bugué

def split_even_odd(lst: list) -> tuple:
    lst_even = []
    lst_odd = []
    length = len(lst)
    for i in range(length):
        if i % 2 == 0:
            lst_even.append(lst[i])
        else:
            lst_odd.append(lst[i])
    return (lst_even,lst_odd)

liste = [22, 21, 35, 53, 22, 24]
print(liste)
print(split_even_odd(liste))




