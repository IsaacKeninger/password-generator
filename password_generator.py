# https://www.cisa.gov/secure-our-world/require-strong-passwords

# In this project, I have created a password generator that complies with the CISA's (cybersecurity & infrastructure security agency)
# rules for creating strong and unique passwords using python.

# Requirements

# 1. Long: at least 16 characters long.
# 2. Random: a string of mixed-case letters, numbers, and symbols 
# 3. Unique: used for one and only one account


import random

created_passwords = set()

uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
digits = list("0123456789")
special_characters = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")

all_characters = uppercase_letters + lowercase_letters + digits + special_characters

def create_password():
    # creates length of the password
    length = random.randint(16,24)

    # This ensures that the password has one of each type of character
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # This will find and fill in the remaining spaces in the password
    remaining_spaces = length - len(password)
    password += random.choices(all_characters, k = remaining_spaces)

    random.shuffle(password) # This ensures so the first 4 chars are different each time 
    password = ''.join(password) # This converts the list of chars to a string

    if password in created_passwords:
        print("Password already in use. Try again.")
        return

    return password

password = create_password()
