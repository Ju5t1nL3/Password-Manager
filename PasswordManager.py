"""
Cryptography
"""
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    """
    Loads the already created key for encryption/decryption
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()

def add():
    """
    Adds a new entry
    """
    global f
    name = input("Which website is this password for? ")
    username = input("What is your username? ")
    password = input("What is your password? ")
    encrypted = f.encrypt(password.encode())
    with open("passwords.txt", "a") as text_file:
        text_file.write(f"{name}\nusername: {username} | password: {encrypted.decode()}\n\n")

def view():
    """
    Views all previous entries
    """
    global f
    with open("passwords.txt", "r") as text_file:
        print("")
        for line in text_file.readlines():
            temp = line.rstrip()
            if "|" in line:
                user,password = temp.split("|")
                encrypted = password[11:].encode()
                print(f"{user} | password: {f.decrypt(encrypted).decode()}")
            else:
                print(temp)

#starts program
f = Fernet(load_key())

while True:
    mode = input("Would you like to view your passwords or add a new one? (view/add/quit): ").lower().strip()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "quit":
        break


