from random import randint
import random
import string

def generateRandomNumber():
    value = randint(0,9)
    return str(value)

def generateRandomLowerCaseLetter():
    lower_upper_alphabet = string.ascii_lowercase
    random_letter = random.choice(lower_upper_alphabet)
    return random_letter

def generateRandomUpperCaseLetter():
    lower_upper_alphabet = string.ascii_uppercase
    random_letter = random.choice(lower_upper_alphabet)
    return random_letter

def generateRandomValue():
    value = randint(0,2)
    if value == 0:
        return generateRandomNumber()
    elif value == 1:
        return generateRandomLowerCaseLetter()
    else:
        return generateRandomUpperCaseLetter()

def generatePassword():
    value = input("Enter a password length :")
    i = 0
    password = ''
    while i < value:
        i+= 1
        password += generateRandomValue()
    return password

print(generatePassword())
