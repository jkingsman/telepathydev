#!/usr/bin/env python3

import random

# import matplotlib.pyplot as plt

from guesser import FitnessGuesser as Guesser
from responder import Responder
from helpers import getCellTuple, n2l, formatCell

thresholds = [1, 2, 4, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]  # 17
weights = [.05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, -.05, -.1, -.15, -.2, -.25, -.3, -.35, -.4, -.45, -.5, -.55, -.6] # 24

weightTuples = [(x, y, z) for x in thresholds for y in weights for z in weights]

for weightTuple in weightTuples:
    def runIters(procNum):
        ITERATIONS = 100
        guessesToWin = []
        losses = 0

        for i in range(ITERATIONS):
            guesser = Guesser()
            guesser.weightingTuple = weightTuple

            responder = Responder(getCellTuple(n2l(random.randint(1, 18)), random.randint(1, 18)))
            # print(f"Iteration {i}: {formatCell(responder.cell)}")

            turns = 0
            gameOver = False

            while not gameOver:
                guess = guesser.getGuess()
                # print(f"Turn {turns} of iteration {i}: {formatCell(guess[0])}")
                if guess[1]:
                    if responder.checkSolve(guess[0]):
                        guessesToWin.append(turns)
                        break
                    else:
                        losses += 1
                        break

                guesser.feedback(guess[0], responder.check(guess[0]))
                turns += 1

        return (guessesToWin, losses, ITERATIONS)

    # meanTurnsToWin, lossRate = runIters()


    import multiprocessing
    pool = multiprocessing.Pool()
    results = pool.map(runIters, range(10))

    turnCountsToWin = []
    lossCount = 0
    totalTurns = 0
    for result in results:
        turnCountsToWin += result[0]
        lossCount += result[1]
        totalTurns += result[2]

    print(f"# {totalTurns} iterations run for weightTuple {weightTuple}. Mean turns to win: {round(sum(turnCountsToWin) / len(turnCountsToWin), 2)}; {round(lossCount / totalTurns * 100, 2)}% loss rate")
    print(f"{totalTurns}, {weightTuple}, {round(sum(turnCountsToWin) / len(turnCountsToWin), 2)}")

# print("Rendering plot...")
# plt.hist(turnCountsToWin, bins=[4, 5, 6, 7, 8, 9, 10, 11, 12])
# plt.ylabel('Frequency')
# plt.xlabel('Turns to Win');
# meanTurnsToWin = round(sum(turnCountsToWin) / len(turnCountsToWin), 2)
# plt.title(f"Turns to Win: {meanTurnsToWin} ({round(lossCount / totalTurns * 100, 2)}% loss rate)");
# plt.savefig('histo.png')
