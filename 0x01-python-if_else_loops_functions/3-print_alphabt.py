#!/usr/bin/python3

for letter in range (97, 1223):
    if chr(letter) is not  'q' and chr(letter) is not 'e':
        print("{}".format(letter), end="")
