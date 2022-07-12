from interface import *
import constants

if __name__ == '__main__':
    print("\t\t>>>>>>>>>>>>>>>Save your password with SavePass<<<<<<<<<<<<<<<<<<<<<\n")

    running = True

    while running:
        print(constants.MENU)

        option = 0

        while option == 0:
            try:
                option = int(input("\nOption:  "))
            except ValueError:
                print("Please enter a number")

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
            get_passwords_in_file()
        elif option == 5:
            print("Exit")
            exit()
        else:
            print("This option is not recognized")
