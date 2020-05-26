import sys

argc = len(sys.argv)
if argc == 1:
    pass
elif argc > 2 or sys.argv[1].isdigit() is False:
    print("ERROR")
else:
    if int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
