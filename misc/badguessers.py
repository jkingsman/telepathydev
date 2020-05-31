class DifferenceGuesser:
    def __init__(self):
        self.board = getBoardAsList()
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

    # naive from unguessed
    def getGuess(self):
        if len(self.board) == 1:
            return (self.board[0], True)

        unguessedOptions = [cell for cell in self.board if cell not in self.yes + self.no]
        if len(unguessedOptions) == 0:
            # it's something we already guessed
            random.shuffle(self.yes)
            return (self.yes[0], True)

        # set degree of difference from previous yesses to eliminate as much as possible
        mostDifferent = unguessedOptions[0]
        degreesDifferent = 0

        for option in unguessedOptions:
            optionDegreesDifferent = 0

            rows = [yes['row'] for yes in self.yes]
            cols = [yes['col'] for yes in self.yes]
            colors = [yes['color'] for yes in self.yes]
            symbols = [yes['symbol'] for yes in self.yes]

            if option['row'] not in rows:
                optionDegreesDifferent += 1

            if option['col'] not in cols:
                optionDegreesDifferent += 1

            if option['color'] not in colors:
                optionDegreesDifferent += 1

            if option['symbol'] not in symbols:
                optionDegreesDifferent += 1

            if optionDegreesDifferent > degreesDifferent:
                mostDifferent = option

        return (mostDifferent, False)

    def getCommonElementCount(self, cell1, cell2):
        commonalities = 0
        if cell1['row'] == cell2['row']:
            commonalities += 1

        if cell1['col'] == cell2['col']:
            commonalities += 1

        if cell1['color'] == cell2['color']:
            commonalities += 1

        if cell1['symbol'] == cell2['symbol']:
            commonalities += 1

        return commonalities

    def getFirstCommonElement(self, cell1, cell2):
        if cell1['row'] == cell2['row']:
            return ('row', cell1['row'])

        if cell1['col'] == cell2['col']:
            return ('col', cell1['col'])

        if cell1['color'] == cell2['color']:
            return ('color', cell1['color'])

        if cell1['symbol'] == cell2['symbol']:
            return ('symbol', cell1['symbol'])

    def removeCellWhereElementDoesntMatch(self, elementName, value):
        newBoard = []
        for cell in self.board:
            if cell[elementName] != value:
                continue
            newBoard.append(cell)
        self.board = newBoard

    def feedback(self, guess, isYes):
        if isYes:
            self.stripBoardOfItemsWithNothingInCommon(guess)
            self.yes.append(guess)
        else:
            self.stripBoardOfItemsWithAnythingInCommon(guess)
            self.no.append(guess)

        # let's hunt for commonalities in our confirmeds
        if len(self.yes) > 1:
            for cell1 in self.yes:
                for cell2 in self.yes:
                    if self.getCommonElementCount(cell1, cell2) == 1:
                        elementName, value = self.getFirstCommonElement(cell1, cell2)
                        self.removeCellWhereElementDoesntMatch(elementName, value)

class RandomGuesser:
    def __init__(self):
        self.board = getBoardAsList()
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

    # naive from unguessed
    def getGuess(self):
        if len(self.board) == 1:
            return (self.board[0], True)

        unguessedOptions = [cell for cell in self.board if cell not in self.yes + self.no]
        if len(unguessedOptions) > 0:
            return (random.choice(unguessedOptions), False)
        else:
            print("Out of available options; it's one of these:")
            print(self.yes + self.board)
            return (random.choice(self.yes), True)

    def feedback(self, guess, isYes):
        if isYes:
            self.stripBoardOfItemsWithNothingInCommon(guess)
            self.yes.append(guess)
        else:
            self.stripBoardOfItemsWithAnythingInCommon(guess)
            self.no.append(guess)

    def isSolving(self):
        if len(self.board) <= 1:
            return True

class TestGuesser:
    def __init__(self):
        self.board = getBoardAsList()
        self.yes = []
        self.no = []
        self.known = {
            'row': None,
            'col': None,
            'color': None,
            'symbol': None,
        }

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

    def cellHasValueThatWeAreCertainOf(self, cell):
        for key in self.known.keys():
            if self.known[key] and self.known[key] == cell[key]:
                return True
        return False

    # naive from unguessed
    def getGuess(self):
        if self.known['row'] and self.known['col'] and self.known['color'] and self.known['symbol']:
            print("certainty!")
            return (self.known['row'], self.known['col'], self.known['color'], self.known['symbol'])

        if len(self.board) == 1:
            return (self.board[0], True)

        unguessedOptions = [cell for cell in self.board if cell not in self.yes + self.no]
        unguessedOptionsWithoutCertainty = [cell for cell in unguessedOptions if not self.cellHasValueThatWeAreCertainOf(cell)]
        if len(unguessedOptionsWithoutCertainty) > 0:
            print("using non-certain option")
            return (random.choice(unguessedOptionsWithoutCertainty), False)

        if len(unguessedOptions) > 0:
            print("using option with certainty or we have no certainty")
            return (random.choice(unguessedOptions), False)

        print("Out of options but I know it's one of these!")
        print(self.yes + self.board)

    def intersectDicts(self, d1, d2):
        commonalities = {}
        for key in set(d1).intersection(set(d2)):
            if d1[key] == d2[key]:
                commonalities[key] = d1[key]
        return commonalities

    def removeElementsWithout(self, element):
        newBoard = []
        for option in self.board:
            if option[list(element.keys())[0]] != list(element.values())[0]:
                continue
            newBoard.append(option)
        self.board = newBoard

    def feedback(self, guess, isYes):
        if isYes:
            self.stripBoardOfItemsWithNothingInCommon(guess)
            self.yes.append(guess)
        else:
            self.stripBoardOfItemsWithAnythingInCommon(guess)
            self.no.append(guess)

        # get common elements when all others are different
        if len(self.yes) > 1:
            for one in self.yes:
                for two in self.yes:
                    if one == two:
                        continue

                    intersection = self.intersectDicts(one, two)
                    if len(intersection) >= 1:
                        print(intersection)
                        for key in list(intersection.keys()):
                            self.known[key] = intersection[key]
                            self.removeElementsWithout({key: intersection[key]})
        print(self.known)
