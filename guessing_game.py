"""Chooses a random integer between 0 and 100 and asks user to guess it."""

import random

number = random.randint(0, 100)
guesses = 3

while True:
    user_number = int(input(f"What do you think the number is? You have {guesses} guesse(s): "))
    if user_number == number:
        print("Good job! You guessed the number!")
        break
    elif user_number > number:
        print("Too high. Try again.")
    elif user_number < number:
        print("Too low. Try again.")

    guesses -= 1
    if guesses == 0:
        print(f"That's three guesses. Oh well! The number was {number}.") 
        break

        
