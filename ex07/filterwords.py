import sys
import string

if len(sys.argv) != 3 or sys.argv[2].isdigit() is False:
    print("ERROR")
    sys.exit(1)


def is_longer(word):
    return False if len(word) <= int(sys.argv[2]) else True


translator = str.maketrans('', '', string.punctuation)
texte = sys.argv[1].translate(translator)
liste = texte.split()
liste = list(filter(is_longer, liste))
print(liste)
