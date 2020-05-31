#!/usr/bin/env python3

from helpers import getBoardAsList
import random

# all guessers must implement getGuess() which returns a tuple of (guess, boolIndicatingIsSolving) and feedback(guess, bool) to indicate yes or no and
class FitnessGuesser:
    def __init__(self):
        self.board = getBoardAsList()

        self.usedInAnnealing = []
        self.yes = []
        self.no = []

        # used for testing different fitness functions
        # default finds yes and no with lowest range
        # i.e. closest to .5
        # i.e. gives most balanced performance for either a yes or no answer
        self.fitnessFunc = lambda yes, no: abs(yes - no) # 8.6

        # how bold we want to be -- randomly pick an answer when we have this or fewer options left
        # 1 == certainty
        self.answerAtNOptions = 1

        self.weightingTuple = (0, 0, 0)

    # used when we get a yes
    # we can discard any cell that doesn't have at least one thing in common with the confirmed cell
    def stripBoardOfItemsWithNothingInCommon(self, guess, board):
        return [cell for cell in board if
                cell['row'] == guess['row'] or
                cell['col'] == guess['col'] or
                cell['color'] == guess['color'] or
                cell['symbol'] == guess['symbol']]

    # used when we get a no
    # we can discard any cell thathas at least one thing in common with the rejected cell
    def stripBoardOfItemsWithAnythingInCommon(self, guess, board):
        return [cell for cell in board if
                cell['row'] != guess['row'] and
                cell['col'] != guess['col'] and
                cell['color'] != guess['color'] and
                cell['symbol'] != guess['symbol']]

    def getGuessFitnessScores(self):
        guessesAndFitness = []
        currentOptionCount = len(self.board)

        for option in getBoardAsList():
            # calculate how much a yes or no would reduce our option set, then apply the fitness function to that
            noReduction = len(self.stripBoardOfItemsWithAnythingInCommon(option, self.board)) / currentOptionCount
            yesReduction = len(self.stripBoardOfItemsWithNothingInCommon(option, self.board)) / currentOptionCount

            if len(self.board) > self.weightingTuple[0]:
                noReduction += self.weightingTuple[1]
            else:
                yesReduction += self.weightingTuple[2]

            guessesAndFitness.append({
                'cell': option,
                'fitness': self.fitnessFunc(yesReduction, noReduction),
            })
        # for guess in guessesAndFitness:
        #     print(guess)
        return guessesAndFitness

    def getGuess(self):
        # choose an answer if we're at the threshold
        if len(self.board) <= self.answerAtNOptions:
            return (random.choice(self.board), True)

        # otherwise get the fitness scores and choose the lowest score
        # deterministic
        fitnessScores = self.getGuessFitnessScores()
        return (sorted(fitnessScores, key=lambda x: x['fitness'])[0]['cell'], False)

    def feedback(self, guess, isYes):
        if isYes:
            self.board = self.stripBoardOfItemsWithNothingInCommon(guess, self.board)
            self.yes.append(guess)
        else:
            self.board = self.stripBoardOfItemsWithAnythingInCommon(guess, self.board)
            self.no.append(guess)
