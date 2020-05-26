import sys
import string


def ispunctuation(c):
    punctuation = string.punctuation
    if c in punctuation:
        return True
    else:
        return False


def text_analyzer(*args):
    '''This function counts the number of upper characters, lower characters, \
    punctuation and spaces in a given text.'''
    if len(args) > 1:
        print("ERROR")
        return
    if args == 1:
        texte = args[0]
    else:
        texte = ""
    if not texte:
        print("What is the text to analyse ?")
        texte = input()
    print("The text contains {0} characters :".format(len(texte)))
    print("-", sum(1 for c in texte if c.isupper()), "upper letters")
    print("-", sum(1 for c in texte if c.islower()), "lower letters")
    print("-", sum(1 for c in texte if ispunctuation(c)), "punctuation marks")
    print("-", sum(1 for c in texte if c.isspace()), "spaces")
