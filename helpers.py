#!/usr/bin/env python3

boardData = [
    ['blue bolt', 'pink circle', 'green diamond', 'white hand', 'yellow moon', 'purple eye', 'red star', 'orange heart', 'silver sun', 'green eye', 'silver star', 'white circle', 'red moon', 'purple sun', 'yellow bolt', 'orange diamond', 'blue hand', 'pink heart'],
    ['pink hand', 'green heart', 'silver eye', 'orange circle', 'white bolt', 'red sun', 'blue moon', 'purple diamond', 'yellow star', 'purple hand', 'red heart', 'pink star', 'yellow diamond', 'silver circle', 'blue eye', 'green bolt', 'white sun', 'orange moon'],
    ['silver heart', 'yellow eye', 'white star', 'red diamond', 'purple circle', 'pink moon', 'green hand', 'blue sun', 'orange bolt', 'yellow star', 'white bolt', 'purple diamond', 'pink hand', 'blue moon', 'orange circle', 'red sun', 'green heart', 'silver eye'],
    ['white eye', 'orange star', 'purple bolt', 'pink sun', 'blue diamond', 'silver hand', 'yellow heart', 'green moon', 'red circle', 'pink diamond', 'green sun', 'yellow hand', 'purple star', 'orange eye', 'silver moon', 'white heart', 'red bolt', 'blue circle'],
    ['purple star', 'red bolt', 'blue circle', 'silver moon', 'green sun', 'white heart', 'orange eye', 'yellow hand', 'pink diamond', 'silver sun', 'yellow moon', 'orange heart', 'blue bolt', 'red star', 'white hand', 'purple eye', 'pink circle', 'green diamond'],
    ['green circle', 'silver diamond', 'yellow sun', 'purple heart', 'orange hand', 'blue star', 'pink bolt', 'red eye', 'white moon', 'orange bolt', 'purple circle', 'blue sun', 'silver heart', 'green hand', 'red diamond', 'pink moon', 'yellow eye', 'white star'],
    ['red moon', 'blue hand', 'pink heart', 'yellow bolt', 'silver star', 'orange diamond', 'purple sun', 'white circle', 'green eye', 'white moon', 'orange hand', 'red eye', 'green circle', 'pink bolt', 'purple heart', 'blue star', 'silver diamond', 'yellow sun'],
    ['orange sun', 'purple moon', 'red hand', 'green star', 'pink eye', 'yellow circle', 'white diamond', 'silver bolt', 'blue heart', 'red circle', 'blue diamond', 'green moon', 'white eye', 'yellow heart', 'pink sun', 'silver hand', 'orange star', 'purple bolt'],
    ['yellow diamond', 'white sun', 'orange moon', 'blue eye', 'red heart', 'green bolt', 'silver circle', 'pink star', 'purple hand', 'blue heart', 'pink eye', 'silver bolt', 'orange sun', 'white diamond', 'green star', 'yellow circle', 'purple moon', 'red hand'],
    ['pink moon', 'green hand', 'blue sun', 'purple circle', 'orange bolt', 'white star', 'red diamond', 'yellow eye', 'silver heart', 'white sun', 'purple hand', 'red heart', 'silver circle', 'orange moon', 'yellow diamond', 'blue eye', 'pink star', 'green bolt'],
    ['silver hand', 'yellow heart', 'green moon', 'blue diamond', 'red circle', 'purple bolt', 'pink sun', 'orange star', 'white eye', 'blue hand', 'green eye', 'silver star', 'purple sun', 'pink heart', 'red moon', 'yellow bolt', 'white circle', 'orange diamond'],
    ['yellow circle', 'white diamond', 'silver bolt', 'pink eye', 'blue heart', 'red hand', 'green star', 'purple moon', 'orange sun', 'red bolt', 'pink diamond', 'green sun', 'orange eye', 'blue circle', 'purple star', 'silver moon', 'yellow hand', 'white heart'],
    ['white heart', 'orange eye', 'yellow hand', 'green sun', 'pink diamond', 'blue circle', 'silver moon', 'red bolt', 'purple star', 'pink circle', 'silver sun', 'yellow moon', 'red star', 'green diamond', 'blue bolt', 'white hand', 'orange heart', 'purple eye'],
    ['green bolt', 'silver circle', 'pink star', 'red heart', 'purple hand', 'orange moon', 'blue eye', 'white sun', 'yellow diamond', 'purple moon', 'blue heart', 'pink eye', 'white diamond', 'red hand', 'orange sun', 'green star', 'silver bolt', 'yellow circle'],
    ['purple eye', 'red star', 'orange heart', 'yellow moon', 'silver sun', 'green diamond', 'white hand', 'pink circle', 'blue bolt', 'silver diamond', 'white moon', 'orange hand', 'pink bolt', 'yellow sun', 'green circle', 'purple heart', 'red eye', 'blue star'],
    ['blue star', 'pink bolt', 'red eye', 'orange hand', 'white moon', 'yellow sun', 'purple heart', 'silver diamond', 'green circle', 'orange star', 'red circle', 'blue diamond', 'yellow heart', 'purple bolt', 'white eye', 'pink sun', 'green moon', 'silver hand'],
    ['red sun', 'blue moon', 'purple diamond', 'white bolt', 'yellow star', 'silver eye', 'orange circle', 'green heart', 'pink hand', 'yellow eye', 'orange bolt', 'purple circle', 'green hand', 'white star', 'silver heart', 'red diamond', 'blue sun', 'pink moon'],
    ['orange diamond', 'purple sun', 'white circle', 'silver star', 'green eye', 'pink heart', 'yellow bolt', 'blue hand', 'red moon', 'green heart', 'yellow star', 'white bolt', 'blue moon', 'silver eye', 'pink hand', 'orange circle', 'purple diamond', 'red sun']
]

l2nTable = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
}


def l2n(l):
    return l2nTable[l.upper()]


def n2l(n):
    n2lTable = {v: k for k, v in l2nTable.items()}
    return n2lTable[int(n)]


def getCell(row, col):
    row = l2n(row)
    return boardData[row - 1][col - 1]

def getCellTuple(row, col):
    rowNum = l2n(row)
    return {
        'row': row.upper(),
        'col': col,
        'color': boardData[rowNum - 1][col - 1].split(' ')[0],
        'symbol': boardData[rowNum - 1][col - 1].split(' ')[1]
    }

def formatCell(cell):
    return f"{cell['row']}{cell['col']}, {cell['color'].capitalize()} {cell['symbol'].capitalize()}"

def getBoardAsList():
    boardList = []
    for row in range(len(boardData)):
        for col in range(len(boardData[row])):
            color, symbol = getCell(n2l(row + 1), col + 1).split(' ')
            boardList.append({
                'row': n2l(row + 1),
                'col': col + 1,
                'color': color,
                'symbol': symbol
            })
    return boardList
