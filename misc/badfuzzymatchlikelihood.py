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
        self.fitnessFunc = lambda yes, no, knownWrong, knownRight: abs(yes - no) # 8.6
        # self.fitnessFunc = lambda yes, no, knownWrong, knownRight: abs(yes - min(no * knownWrong, no)) # 12.13
        # self.fitnessFunc = lambda yes, no, knownWrong, knownRight: abs(yes - (no * knownWrong)) # 12.09
        # self.fitnessFunc = lambda yes, no, knownWrong, yesFuzzy: abs((yes * yesFuzzy) - (no * knownWrong)) # 9.49

        # how bold we want to be -- randomly pick an answer when we have this or fewer options left
        # 1 == certainty
        self.answerAtNOptions = 4

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

    def getKnownWrongAttributes(self, cell):
        knownWrongAttributes = 0
        if cell['row'] in map(lambda cell: cell['row'], self.no):
            knownWrongAttributes += 1

        if cell['col'] in map(lambda cell: cell['col'], self.no):
            knownWrongAttributes += 1

        if cell['color'] in map(lambda cell: cell['color'], self.no):
            knownWrongAttributes += 1

        if cell['symbol'] in map(lambda cell: cell['symbol'], self.no):
            knownWrongAttributes += 1
        return knownWrongAttributes

    def getYesLikelihoodFuzzy(self, cell):
        knownRightAttributes = 0
        totalInCommon = list(map(lambda cell: cell['row'], self.yes)).count(cell['row']) + \
                        list(map(lambda cell: cell['col'], self.yes)).count(cell['col']) + \
                        list(map(lambda cell: cell['color'], self.yes)).count(cell['color']) + \
                        list(map(lambda cell: cell['symbol'], self.yes)).count(cell['symbol'])

        maximumMatches = 4 * len(self.yes)

        try:
            return totalInCommon/maximumMatches
        except ZeroDivisionError:
            return 0

    def getGuessFitnessScores(self):
        guessesAndFitness = []
        currentOptionCount = len(self.board)

        for option in getBoardAsList():
            # calculate how much a yes or no would reduce our option set, then apply the fitness function to that
            noReduction = len(self.stripBoardOfItemsWithAnythingInCommon(option, self.board)) / currentOptionCount
            yesReduction = len(self.stripBoardOfItemsWithNothingInCommon(option, self.board)) / currentOptionCount
            knownWrong = self.getKnownWrongAttributes(option) / 4
            yesLikelihoodFuzzy = self.getYesLikelihoodFuzzy(option) / 4

            guessesAndFitness.append({
                'cell': option,
                'fitness': self.fitnessFunc(yesReduction, noReduction, knownWrong, yesLikelihoodFuzzy),
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
