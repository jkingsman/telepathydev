#!/usr/bin/env python3

import random
import sys

from responder import Responder
from helpers import getCellTuple, n2l, formatCell

if len(sys.argv) == 3:
    cell = getCellTuple(sys.argv[1].upper(), int(sys.argv[2]))
else:
    cell = getCellTuple(n2l(random.randint(1, 18)), random.randint(1, 18))

responder = Responder(cell)
print(formatCell(responder.cell))

while True:
    guess = input('Input guess (prefix with s if solving): ').upper()
    if guess[0] == 'S':
        guessCell = getCellTuple(guess[1:2].upper(), int(guess[2:]))
        if responder.checkSolve(guessCell):
            print('You win!')
        else:
            print('You lose!')
            print('Correct answer: ' + formatCell(responder.cell))
        break

    guessCell = getCellTuple(guess[0:1].upper(), int(guess[1:]))
    if responder.check(guessCell):
        print(formatCell(guessCell) + ': Yes')
    else:
        print(formatCell(guessCell) + ': No')
