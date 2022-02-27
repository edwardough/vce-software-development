import random
randNum = random.randint(1,10)
guess = False
while guess != True:
    try:
        pGuess = int(input("Guess my number between 1 and 10 inclusive: "))
        if pGuess == randNum:
            print("Winner winner chicken dinner!")
            guess = True
        elif pGuess < randNum:
            print("Too low Bozo!")
        else:
            print("Too high, wanna cry?")
    except ValueError:
        print("Please enter a number.")
input("Thanks for playing, [ENTER] to end.")
