t = (19, 42, 21)

print("The {0} numbers are:" .format(len(t)), end=" ")
print(*t[0:], sep=", ")
