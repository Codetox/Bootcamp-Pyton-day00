import sys

morse = {
    "A": "di-dah",
    "B": "dah-di-di-dit",
    "C": "dah-di-dah-dit",
    "D": "dah-di-dit",
    "E": "dit",
    "F": "di-di-dah-dit",
    "G": "dah-dah-dit",
    "H": "di-di-di-dit",
    "I": "di-dit",
    "J": "di-dah-dah-dah",
    "K": "dah-di-dah",
    "L": "di-dah-di-dit",
    "M": "dah-dah",
    "N": "dah-dit",
    "O": "dah-dah-dah",
    "P": "di-dah-dah-dit",
    "Q": "dah-dah-di-dah",
    "R": "di-dah-dit",
    "S": "di-di-dit",
    "T": "dah",
    "U": "di-di-dah",
    "V": "di-di-di-dah",
    "W": "di-dah-dah",
    "X": "dah-di-di-dah",
    "Y": "dah-di-dah-dah",
    "Z": "dah-dah-di-dit",
    "0": "dah-dah-dah-dah-dah",
    "1": "di-dah-dah-dah-dah",
    "2": "di-di-dah-dah-dah",
    "3": "di-di-di-dah-dah",
    "4": "di-di-di-di-dah",
    "5": "di-di-di-di-dit",
    "6": "dah-di-di-di-dit",
    "7": "dah-dah-di-di-dit",
    "8": "dah-dah-dah-di-dit",
    "9": "dah-dah-dah-dah-dit"
}

text = ' '.join(sys.argv[1:])
text = text.upper()
code = ""
if (len(sys.argv) > 1):
    for c in text:
        if c in morse:
            msg = morse[c].split('-')
            for i in msg:
                if i == "dah":
                    code += "-"
                elif i == "di":
                    code += "."
                elif i == "dit":
                    code += "."
            code += " "
        elif c == " ":
            code += "/ "
        else:
            print("ERROR")
            sys.exit(1)
    print(code)
