# Based of "Big Book of Small Python Projects" by Al Sweigert
#
# Project 01
#
# Description:
# ------------
# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.
# The game offers one of the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the wrong place,
# “Fermi” when your guess has a correct digit in the correct place,
# and “Bagels” if your guess has no correct digits.
# You have 10 tries to guess the secret number.

import random

def get_input():
    tries_remaining = 10
    guess = '000'
    guessed_correct = False
    print("Please enter in a number between 1 and 100")
    while tries_remaining > 0:
        print("You have " + str(tries_remaining) + " guesses remaining")
        tries_remaining -= 1
        guess = input("Your guess?")
        if guess == answer:
            guessed_correct = True
            print("You guessed correctly!")
            tries_remaining = 0

# Driver
answer = random.randint(1, 100)

get_input()





