import pickle
from crypt import Cryptage
from decrypt import Decrypt
import getpass


crypt = Cryptage()
decrypt = Decrypt()
KEY = 10122004


def generate_key():
    """Generate key of password"""
    pass


def add_pass():
    ref = input("Enter reference of password: ")
    new_pass = getpass.getpass("Enter password: ")

    new_pass = crypt.lockMess(new_pass, KEY)
    passwords = return_passwords()
    passwords.append([ref, new_pass])

    save_passwords(passwords)

    print("\a>>>>>>>>>>>>>>>>>>>>>>>The password is very good added :)\n")


def return_passwords():
    with open('.pass', 'rb') as file:
        my_pickler = pickle.Unpickler(file)
        try:
            passwords = my_pickler.load()
        except EOFError:
            passwords = []
        finally:
            return passwords


def save_passwords(passwords):
    with open('.pass', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(passwords)  # save passwords


def get_passwords_in_file():
    passwords = return_passwords()
    content_file = ''

    for password in passwords:
        content_file += password[0] + ': ' + decrypt.unlock_message(password[1], KEY) + '\n'

    with open('passwords.txt', 'w') as file:
        file.write(content_file)

    print("\n\t\a---------------------------------The passwords have been saved in passwords.txt file :)\n")
