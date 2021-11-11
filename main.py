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

answer = random.randint(1, 100)

print(answer)
