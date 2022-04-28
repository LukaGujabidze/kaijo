import time
import random
import string

# Read user input. How many character the password should contain
user_choice = int(input("how many characters do you want? "))

# Function which generates any 1 random character and returns it
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

    for count in range(0, user_choice):
        password_character.append(password_gen())
    
    print("".join(password_character))



while True:
    func()
    answer = input("another password ? (y/n) ")
    if answer.lower() == "y":
        user_choice = int(input("how many characters do you want? "))
    elif answer.lower == "n":
        break
    else:
        print("you should be write 'y' or 'n'")
        

time.sleep(5)