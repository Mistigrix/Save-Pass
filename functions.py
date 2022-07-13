import getopt
import pickle
import sys

from crypt import Cryptage
from decrypt import Decrypt
import getpass
import constants


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


def update_pass():
    print("\tEdit a password to enter his number")

    number = 0
    while number == 0:
        try:
            number = int(input("\nNumber du mdp: "))
        except ValueError:
            print("Please enter a number")
            continue

    passwords = return_passwords()
    print(f"\nModifier le mot de passe de la reference {passwords[number-1][0]}")
    new_pass = input("Enter the new password: ")
    confirm = input(f"Are you sur to edit the password {passwords[number-1][0]} (Y/N): ")

    affirms = ['y', 'Y', 'YES', 'yes', 'Yes', 'yEs', 'yeS']
    new_pass = crypt.lockMess(new_pass, KEY)

    if confirm in affirms:
        passwords[number-1][1] = new_pass
        save_passwords(passwords)
    print("Le mot de passe à bien été modifier")


def display_pass():
    passwords = return_passwords()
    i = 1
    print("\n")
    if len(passwords) > 0:
        for mdp in passwords:
            print(f"{i}->{mdp[0]}: {decrypt.unlock_message(mdp[1], KEY)}")
            i += 1
    else:
        print("\n\nNo password saved")

    print("\n")
    print("")


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


def check_command_line(argv):
    short_options = 'ha'
    long_options = ['help', 'add']

    try:
        options, args = getopt.getopt(argv, short_options, long_options)
    except getopt.GetoptError:
        print("This option is not recognized")
        sys.exit(2)

    for option, arg in options:
        if option in ('-h', '--help'):
            print(constants.HELP)
            sys.exit()
        elif option in ('-a', '--add'):
            add_pass()
            sys.exit()
