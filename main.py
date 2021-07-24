import os
import pickle
from crypt import Cryptage
from decrypt import Decryptage

cryptage = Cryptage()
decryptage = Decryptage()
KEY = 10122004


def generate_key(password):
    """Generer un clé pour chaque mot de passe"""
    pass


def add_pass():
    ref = input("Entrer la reference du mot de passe: ")
    new_pass = input("Entrer le mot de passe: ")

    new_pass = cryptage.lockMess(new_pass, KEY)
    passwords = return_passwords()
    passwords.append([ref, new_pass])

    save(passwords)

    print("\a>>>>>>>>>>>>>>>>>>>>>>>Le mot de passe à bien été ajouter:)\n")


def return_passwords():
    """Retourne,le dictionnaire contenant tous les mots de passe enregistrer"""
    with open('.pass', 'rb') as file:
        my_pickler = pickle.Unpickler(file)
        try:
            passwords = my_pickler.load()
        except EOFError:
            passwords = []
        finally:
            return passwords


def save(passwords):
    # sauvegarder le mdp dans un fichier
    with open('.pass', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(passwords)


def display_pass():
    passwords = return_passwords()
    i = 1
    print("\n")
    if len(passwords) > 0:
        for mdp in passwords:
            print(f"{i}->{mdp[0]}: {decryptage.unLockMess(mdp[1], KEY)}")
            i += 1
    else:
        print("\n\nAucun mot de passe n'a été enregistrer")

    print("\n")
    os.system('pause')


def save_in_file():
    passwords = return_passwords()
    content_file = ''

    for password in passwords:
        content_file += password[0] + ': ' + decryptage.unLockMess(password[1], KEY) + '\n'

    with open('passwords.txt', 'w') as file:
        file.write(content_file)

    print("\n\t\a---------------------------------Les mots de passe ont été copier vers le fichier passwords.txt:)\n")


def update_pass():
    """Modifier un mot de passe ou plusieur"""
    print("\tModifier un mot de passe en entrant son numero")

    number = 0
    while number == 0:
        try:
            number = int(input("\nNumero du mdp: "))
        except ValueError:
            print("Veillez entrer un nombre")
            continue

    passwords = return_passwords()
    print(f"\nModifier le mot de passe de la reference {passwords[number-1][0]}")
    new_pass = input("Entrer le nouveau mot de passe: ")
    confirm = input(f"Êtes vous sûr de vouloir modifier le mot de passe de {passwords[number-1][0]} Y / N: ")

    afirms = ['y', 'Y', 'YES', 'yes', 'Yes', 'yEs', 'yeS']
    new_pass = cryptage.lockMess(new_pass, KEY)

    for afirm in afirms:
        if confirm == afirm:
            passwords[number-1][1] = new_pass
            save(passwords)
    print("Le mot de passe à bien été modifier")


if __name__ == '__main__':
    print("\t\t>>>>>>>>>>>>>>>Sauvegarder vos mot de passe avec SavePass<<<<<<<<<<<<<<<<<<<<<\n")

    running = True

    while running:
        print("1.\tAjouter un mot de passe")
        print("2.\tModifier un mot de passe")
        print("3.\tLister tous les mots de passe")
        print("4\tCopier tous les mots de passe")
        print("5.\tQuitter")

        option = 0

        while option == 0:
            try:
                option = int(input("\nOption:  "))
            except ValueError:
                print("Veillez entrer un nombre")
                continue

        if option == 1:
            add_pass()
            continue
        elif option == 2:
            update_pass()
            continue
        elif option == 3:
            display_pass()
            continue
        elif option == 4:
            save_in_file()
        elif option == 5:
            print("Exit")
            exit()
        else:
            print("Cette option n'est pas reconnu")
