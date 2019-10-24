#!/usr/bin/python

### FONCTION ###
def controleur_volume():
    global volume
    global user_input

    if user_input is "+":
        volume += 10
    elif user_input is "-":
        volume -= 10

### MAIN ### 
volume = 50 
user_input = ""

while user_input.lower() != "x":
    user_input = input("+ : Augmenter le volume\n- : Diminuer le volume\nx : Quitter \n\nVotre choix : ")
    controleur_volume()
    print("Volume : {}%".format(volume))
