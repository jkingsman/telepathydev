#!/usr/bin/env python3

class Responder():
    def __init__(self, cell):
        self.cell = cell

    def check(self, guess):
        if guess['row'] == self.cell['row'] or \
           guess['col'] == self.cell['col'] or \
           guess['color'] == self.cell['color'] or \
           guess['symbol'] == self.cell['symbol']:
            return True
        return False

    def checkSolve(self, guess):
        if guess == self.cell:
            return True
        return False
