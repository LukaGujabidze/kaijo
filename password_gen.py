import random
import string

def password_gen():
    upper_letters = random.choice(string.ascii_uppercase)
    lower_letters = random.choice(string.ascii_lowercase)
    numbers = random.choice(string.digits)
    special_char = random.choice(string.punctuation)

    # List containing 4 different types of characters
    password_list = [upper_letters, lower_letters, numbers, special_char]

    password = random.choice(password_list)
    return password


def func():    
    password_character = []

    for count in range(0, 8):
        password_character.append(password_gen())
    

    return "".join(password_character)

