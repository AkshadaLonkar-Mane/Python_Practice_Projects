# Guess the Number
#A fun game where the user tries to guess a randomly generated number within a specified range.


# 1. Import Module:
# To generate random number, we will need to import Python's random module.

import random

# 2. Create a loop for user to Guess:
def guess_the_number():
    number = random.randint(1, 10)  # number = random number between 1 to 10
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number between 1 to 10:   "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
        
        except ValueError:
            print("Please enter a valid integer.")


# 3. Run the Game: Call the guess_the_number() function to start the game.
guess_the_number()

# Output:
"""
Guess the number between 1 to 10:   5
Too low! Try again.
Guess the number between 1 to 10:   8
Too high! Try again.
Guess the number between 1 to 10:   6
Congratulations! You've guessed the number 6 in 3 attempts.
"""