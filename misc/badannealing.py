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
        self.fitnessFunc = lambda yes, no: abs(yes - no)

        # how bold we want to be -- randomly pick an answer when we have this or fewer options left
        # 1 == certainty
        self.answerAtNOptions = 1

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
            guessesAndFitness.append({
                'cell': option,
                'fitness': self.fitnessFunc(yesReduction, noReduction),
            })
        return guessesAndFitness

    def getGuess(self):
        # choose an answer if we're at the threshold
        if len(self.board) <= self.answerAtNOptions:
            return (random.choice(self.board), True)

        # otherwise get the fitness scores and choose the lowest score
        # deterministic
        fitnessScores = self.getGuessFitnessScores()
        return (sorted(fitnessScores, key=lambda x: x['fitness'])[0]['cell'], False)

    def performAnnealing(self):
        def intersectDicts(d1, d2):
            commonalities = {}
            for key in set(d1).intersection(set(d2)):
                if d1[key] == d2[key]:
                    commonalities[key] = d1[key]
            return commonalities

        def removeElementsWithout(element):
            newBoard = []
            for option in self.board:
                if option[list(element.keys())[0]] != list(element.values())[0]:
                    continue
                newBoard.append(option)
            self.board = newBoard

        # go through and find any certainties we know and eliminate things that don't match
        possibles = [cell for cell in self.yes if cell not in self.usedInAnnealing]
        print("possibles: ", possibles)
        if len(possibles) > 1:
            for one in possibles:
                for two in possibles:
                    if one == two:
                        continue

                    intersection = intersectDicts(one, two)
                    if len(intersection) == 1:
                        self.usedInAnnealing.append(one)
                        self.usedInAnnealing.append(two)
                        print(one, two, intersection)
                        for key in list(intersection.keys()):
                            print("executing removal of those without", key, intersection[key])
                            removeElementsWithout({key: intersection[key]})



    def feedback(self, guess, isYes):
        if isYes:
            self.board = self.stripBoardOfItemsWithNothingInCommon(guess, self.board)
            self.yes.append(guess)
            if len(self.usedInAnnealing) == 0:
                self.performAnnealing()
        else:
            self.board = self.stripBoardOfItemsWithAnythingInCommon(guess, self.board)
            self.no.append(guess)
