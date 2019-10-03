#! /usr/bin/python

passwd = ""
alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    char1 = letter

    for letter in alphabet:
        char2 = letter

        for letter in alphabet:
            char3 = letter

            for letter in alphabet:
                char4 = letter

                for letter in alphabet:
                    char5 = letter

                    for letter in alphabet:
                        char6 = letter

                        for letter in alphabet:
                            char7 = letter

                            for letter in alphabet:
                                char8 = letter  
                                passwd = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
                                print(passwd + "\n")
