import sys

if len(argv) > 1:
    line = " ".join(reversed(sys.argv[1:]))
    print(line[::-1].swapcase())
