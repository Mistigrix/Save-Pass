from functions import *


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
        save(passwords)
    print("Le mot de passe à bien été modifier")


def display_pass():
    passwords = return_passwords()
    i = 1
    print("\n")
    if len(passwords) > 0:
        for mdp in passwords:
            print(f"{i}->{mdp[0]}: {decrypt.unLockMess(mdp[1], KEY)}")
            i += 1
    else:
        print("\n\nNo password saved")

    print("\n")
    print("")
