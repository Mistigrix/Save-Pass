from constants import *


class Decrypt:

    def __init__(self):
        pass

    def unlock_message(self, message, clef):
        """Methode permettant de crypter un message et retourne le message crypter
        Paramètre: message à crypter et la clé de chiffrement"""

        return self.unLock(message, clef)

    def unLockFile(self, path, key):

        try:
            key = int(key)
            file = open(path, 'r+')
            content = file.readlines()
            list_crypt = []
            file.close()

            # recupere chaque ligne, la crypte et l'ajoute a liste crypter
            for line in content:
                line_crypt = self.unLock(line, key)
                list_crypt.append(line_crypt)

            return list_crypt

        except FileNotFoundError:
            return None
        except ValueError:
            raise ValueError("The clef is not int ")
        except:
            raise Exception

    def unLock(self, message, key):

        message_decrypter = ''

        key = int(key)  # conversion de la clé en entier (etait en chaine de carrctère au paravant)

        # on verifie les numeros des lettres et on les additionnent avec la clef
        for lettre in message:
            # recuperation des lettres et leurs indices dans la variables alphabets
            for numero_lettre, lettre_alpha in alphabets.items():
                # on verifie si on a la bonne lettre
                if lettre == lettre_alpha:
                    # on soustrait sa clé
                    numero_decrypte = numero_lettre - key
                    while numero_decrypte < 0:
                        numero_decrypte = numero_decrypte + len(alphabets)

                    message_decrypter += alphabets[numero_decrypte]

        return message_decrypter


if __name__ == '__main__':
    decryptage_object = Decrypt()
    message = ''
    while message != 'exit':
        message = input("Entrer le message: ")
        clef = int(input("Entrer la clé de dechiffrement: "))
        decrypt = decryptage_object.unlock_message(message, clef)
        print(decrypt)
