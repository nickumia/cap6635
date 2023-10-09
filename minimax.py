
import random
import sys
import time

from cap6635.agents.adversarialsearch.minimax import MiniMax
from cap6635.environment.map import TicTacToe
from cap6635.utilities.constants import TTT_NONE, TTT_X, TTT_O

board = TicTacToe(3, 3)

i = 0
totalTime = 0

try:
    starter = int(sys.argv[1])
except IndexError:
    starter = random.choice([TTT_X, TTT_O])

if starter == TTT_X:
    agent = MiniMax(board, starter, TTT_O, TTT_NONE)
else:
    agent = MiniMax(board, starter, TTT_X, TTT_NONE)


def evaluate(agent):
    global totalTime
    start = time.time()
    (m, pqx, pqy) = agent()
    end = time.time()
    totalTime = totalTime + (end - start)
    print('Evaluation time: {}s'.format(round(end - start, 7)))
    print('Move: X = {}, Y = {}'.format(pqx, pqy))
    print('Can the computer win? %s' %
          (lambda x: 'YES' if x < 0 else 'NO')(m))
    return (m, pqx, pqy)


while not agent._board.is_win():

    # X plays
    (m, pqx, pqy) = evaluate(agent._min)
    if starter == TTT_X:
        agent._board.print_board()
        while True:
            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
            if agent._board.is_valid(px, py):
                agent._board.map[px, py] = starter
                break
    else:
        if not agent._board.is_valid(pqx, pqy):
            (m, pqx, pqy) = evaluate(agent._max)
        agent._board.map[pqx, pqy] = TTT_X

    if agent._board.is_win():
        break

    # O plays
    if starter == TTT_X:
        (m, pqx, pqy) = evaluate(agent._min)
        agent._board.map[pqx, pqy] = TTT_O
    else:
        agent._board.print_board()
        while True:
            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
            if agent._board.is_valid(px, py):
                agent._board.map[px, py] = starter
                break
            if agent._board.is_win():
                break

agent._board.print_board()
