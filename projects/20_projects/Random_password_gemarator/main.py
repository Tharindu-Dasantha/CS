import string
import random

def main():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    order = input("If you want to generate a password press Y: ").lower()
    if order != "y":
        print("BYE!")
    else:
        password = generate_password(characters)
        print(password)
    
def generate_password(characters):
    password_length = int(input("Enter the length of your password: "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    return "".join(password)

main()