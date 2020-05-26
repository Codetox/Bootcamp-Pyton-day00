import sys


def usage(error=""):
    if (error):
        print(error)
        print()
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
    sys.exit(1)


if (len(sys.argv) == 1):
    usage()
elif (len(sys.argv) > 3):
    usage("InputError: too many arguments")
try:
    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])
except ValueError:
    usage("InputError: only numbers")
print("{0:<12}".format("Sum:"), nb1 + nb2)
print("{0:<12}".format("Difference:"), nb1 - nb2)
print("{0:<12}".format("Product:"), nb1 * nb2)
try:
    print("{0:<12}".format("Quotient:"), nb1 / nb2)
    print("{0:<12}".format("Remainder:"), nb1 % nb2)
except ZeroDivisionError:
    print("{0:<12}".format("Quotient:"), "ERROR (div by zero)")
    print("{0:<12}".format("Product:"), "ERROR (modulo by zero)")
