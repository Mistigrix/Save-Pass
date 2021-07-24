import string

all_letters = list(string.ascii_letters + string.punctuation + string.digits + ' ') # creation d'une liste de carractere
alphabets = {}
i = 0

while i != len(all_letters):
    alphabets[i] = all_letters[i]
    i+=1
