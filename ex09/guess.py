import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99\
to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print("")

secretWord = random.randint(1, 99)
answer = ""
test = 0

while (answer != str(secretWord) and answer != "exit"):
    print("What's your guess between 1 and 99 ?")
    answer = input()
    if answer == "exit":
        print("Goodbye!")
    elif answer.isdigit() is False:
        print("That's not a number.")
    elif int(answer) < secretWord:
        print("Too low!")
    elif int(answer) > secretWord:
        print("Too high!")
    test += 1


if answer != "exit":
    if answer == "42":
        print("The answer to the ultimate question of life,\
the universe and everything is 42.")
    if test == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("You won in {} attempts!" .format(test))
