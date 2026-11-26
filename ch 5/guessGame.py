from random import randint, random


num = randint(1, 100)

print("Welcome to the Guessing Game!")
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
        break