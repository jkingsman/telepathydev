#!/usr/bin/env python3

from helpers import getBoardAsList, getCellTuple, n2l, formatCell, formatCell

class Reducer:
    def __init__(self):
        self.board = getBoardAsList()
        print(len(self.board))
        self.yes = []
        self.no = []

    def stripBoardOfItemsWithNothingInCommon(self, guess):
        newBoard = []
        for option in self.board:
            if option['row'] != guess['row'] and option['col'] != guess['col'] and option['color'] != guess['color'] and option['symbol'] != guess['symbol']:
                # it's got nothing in common so don't include it
                continue
            newBoard.append(option)
        self.board = newBoard

    def stripBoardOfItemsWithAnythingInCommon(self, guess):
        newBoard = []
        for option in self.board:
            if option['row'] == guess['row'] or option['col'] == guess['col'] or option['color'] == guess['color'] or option['symbol'] == guess['symbol']:
                # it's got something in common so don't include it
                continue
            newBoard.append(option)
        self.board = newBoard

    def fromCoords(self):
        guess = input('Input guess: ').upper()
        response = input('Was hit? ')
        guessCell = getCellTuple(guess[0:1].upper(), int(guess[1:]))
        self.feedback(guessCell, response.upper() in ['Y', 'YES'])

    def feedback(self, guess, isYes):
        if isYes:
            self.stripBoardOfItemsWithNothingInCommon(guess)
            self.yes.append(guess)
        else:
            self.stripBoardOfItemsWithAnythingInCommon(guess)
            self.no.append(guess)
        for cell in self.board:
            print(formatCell(cell))
        print(len(self.board))

r = Reducer()
while True:
    r.fromCoords()
