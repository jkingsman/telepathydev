#!/usr/bin/env python3

import random

# import matplotlib.pyplot as plt

from guesser import FitnessGuesser as Guesser
from responder import Responder
from helpers import getCellTuple, n2l

ITERATIONS = 100
guessesToWin = []
losses = 0

for i in range(ITERATIONS):
    guesser = Guesser()

    # guesser.fitnessFunc = lambda yes, no: 1 # 14
    # guesser.fitnessFunc = lambda yes, no: yes / (no + .000000001) # 93
    guesser.fitnessFunc = lambda yes, no: abs(yes - no) # 8.6

    responder = Responder(getCellTuple(n2l(random.randint(1, 18)), random.randint(1, 18)))
    print(f"Iteration {i}: {responder.cell}")

    turns = 0
    gameOver = False

    while not gameOver:
        guess = guesser.getGuess()
        # print(f"Turn {turns} of iteration {i}: {guess}")
        if guess[1]:
            if responder.checkSolve(guess[0]):
                guessesToWin.append(turns)
                break
            else:
                losses += 1
                break

        guesser.feedback(guess[0], responder.check(guess[0]))
        turns += 1

print(f"Mean turns to win: {sum(guessesToWin) / len(guessesToWin)}")
print(f"{losses/ITERATIONS * 100}% loss rate ({losses} losses)")

# if len(guessesToWin) > 0:
#     print("Rendering plot...")
#     plt.hist(guessesToWin)
#     plt.ylabel('Occurences')
#     plt.xlabel('Turns to Win');
#     meanTurnsToWin = sum(guessesToWin) / len(guessesToWin)
#     plt.title('Mean Turns to Win: ' + str(meanTurnsToWin));
#     plt.savefig('histo.png')
