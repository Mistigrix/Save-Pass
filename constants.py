import string

all_letters = list(string.ascii_letters + string.punctuation + string.digits + ' ')
alphabets = {}
i = 0

while i != len(all_letters):
    alphabets[i] = all_letters[i]
    i += 1


MENU = """
    1.\tAdd a new Password
    2.\tSet Password
    3.\tShow all Passwords
    4\tCopied all passwords to file
    5.\tExit
"""

HELP = """
    Save-Pass version 2.0.1
    
    Save your passwords in a file 
"""