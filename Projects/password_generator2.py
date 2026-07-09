########## Welcome to the PyPassword Generator! ##########

import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(length))

print("Have a nice day!")