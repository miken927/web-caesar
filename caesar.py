alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(letter):
    position = alphabet.find(letter.lower())
    return position

def rotate_character(char, rot):
    if char.isalpha() == True:
        new_let = alphabet[(alphabet_position(char) + rot) % 26]
        if char == char.upper():
            new_let = new_let.upper()
    else:
        new_let = char
    return new_let

def encrypt(text, rot):
    encrypted = ""
    for char in text:
        newchar = rotate_character(char, rot)
        encrypted = encrypted + newchar
    return encrypted
