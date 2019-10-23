#!/usr/bin/python
# Je n'ai pas utilisé de variable globale car ces merdes faisaient tout planter.

### FONCTION ###
def controleur_volume(volume, user_input):
    if user_input is "+":
        volume += 10
    
    elif user_input is "-":
        volume -= 10

    return volume

### MAIN ### 
volume = 50 
user_input = ""

while user_input.lower() != "x":
    user_input = input("+ : Augmenter le volume\n- : Diminuer le volume\nx : Quitter \n\nVotre choix : ")
    volume = controleur_volume(volume, user_input)
    print("Volume : {}%".format(volume))
