#!/usr/bin/env python3
import re
from pprint import pprint

# board generation
# f = open("rawboard.txt", "r")
# lines = f.read().split('\n')
# board = []
# for line in lines[:-1]:
#     board.append(re.findall("(\w+\s\w+)\s", line))
#
# print(board)

board = [
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


# correctness proofing
colorcount = {}
symbolcount = {}
colorsymbolcount = {}
total = 0

def addOrIncrement(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

for row in board:
    for cell in row:
        color, symbol = cell.split(' ')

        addOrIncrement(colorcount, color)
        addOrIncrement(symbolcount, symbol)
        addOrIncrement(colorsymbolcount, cell)
        total += 1

boardDim = 18
colors = 9
symbols = 9


if boardDim * boardDim == total:
    print('Cell count pass')
else:
    print('CELL COUNT FAIL')
    print('got ' + str(total) + ', expected ' + str(boardDim * boardDim))

colorsOK = True
for color in colorcount.keys():
    if colorcount[color] != (boardDim * boardDim / colors):
        print('COLOR COUNT FAIL')
        print(color + ' had ' + str(colorcount[color]) + ', expected ' + str(boardDim * boardDim / colors))
        colorsOK = False
if colorsOK:
    print('Color count pass')

symbolsOK = True
for symbol in symbolcount.keys():
    if symbolcount[symbol] != (boardDim * boardDim / symbols):
        print('SYMBOL COUNT FAIL')
        print(symbol + ' had ' + str(symbolcount[symbol]) + ', expected ' + str(boardDim * boardDim / symbols))
        colorsOK = False
if symbolsOK:
    print('Symbol count pass')

colorSymbolOK = True
for colorSymbol in colorsymbolcount.keys():
    if colorsymbolcount[colorSymbol] != (boardDim * boardDim / symbols / colors):
        print('COLOR-SYMBOL COUNT FAIL')
        print(colorSymbol + ' had ' + str(colorsymbolcount[colorSymbol]) + ', expected ' + str(boardDim * boardDim / symbols / colors))
        colorSymbolOK = False
if colorSymbolOK:
    print('Symbol count pass')

# mistake hunting
# for row in range(len(board)):
#     for col in range(len(board[row])):
#         if board[row][col] == 'yellow sun':
#             print(row + 1 , col + 1)
