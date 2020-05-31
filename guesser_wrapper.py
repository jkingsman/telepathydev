#!/usr/bin/env python3

import random
import sys

from guesser import FitnessGuesser as Guesser
from helpers import getCellTuple, n2l, formatCell

guesser = Guesser()
print(f"Board initialized; {len(guesser.board)} possibilities remain")

while True:
    guess = guesser.getGuess()

    if guess[1]:
        print("Making solve attempt!")
        print(formatCell(guess[0]))
        break

    response = input(formatCell(guess[0]) + '? ')
    guesser.feedback(guess[0], response.upper() in ['Y', 'YES'])

    print(f"{len(guesser.board)} possibilities remain")
