"""
projekt_01.py: první projekt do Engeto Online Python Akademie

author: Pavel Křivan
email: paja6700@gmail.com
discord: pavel007111
"""

import re

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

def user_authentification():
    name = input("username: ").strip()
    password = input("password: ").strip()
    if users.get(username) == password:
        print("Welcome to the app, {username}")
        return True
    else:
        print("Unregistered user, terminating the program...")
        return False
    
def text_selection():
    print("We have 3 texts to be analyzed.")
    try:
        selection = int(input("Enter a number btw. 1 and 3 to select: "))
        if 1 <= selection <= 3:
            return texts[selection - 1]
        else:
            print("Wrong selection, close the program...")
            exit()
    except ValueError:
        print("Input must be a number! Close the program...")
        exit()
