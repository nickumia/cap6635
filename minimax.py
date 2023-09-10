
import random
import sys
import time

from cap6635.agents.adversarialsearch.minimax import MiniMax
from cap6635.environment.map import TicTacToe
from cap6635.utilities.constants import TTT_NONE, TTT_X, TTT_O

board = TicTacToe(3, 3)
agent = MiniMax(board)

i = 0
totalTime = 0

try:
    starter = int(sys.argv[1])
except IndexError:
    starter = random.choice([TTT_X, TTT_O])


def evaluate(agent, turn):
    global totalTime
    start = time.time()
    (m, pqx, pqy) = agent._minimax(turn)
    end = time.time()
    totalTime = totalTime + (end - start)
    print('Evaluation time: {}s'.format(round(end - start, 7)))
    print('Recommended move: X = {}, Y = {}'.format(pqx, pqy))
    return (m, pqx, pqy)


while not agent._board.is_win():
    agent._board.print_board()

    if starter == TTT_X:
        while True:
            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
            if agent._board.is_valid(px, py):
                agent._board.map[px, py] = starter
                break
        (m, pqx, pqy) = evaluate(agent, [TTT_O, TTT_X, TTT_NONE])
        agent._board.map[pqx, pqy] = TTT_O
    else:
        (m, pqx, pqy) = evaluate(agent, [TTT_X, TTT_O, TTT_NONE])
        agent._board.map[pqx, pqy] = TTT_X
        while True:
            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
            if agent._board.is_valid(px, py):
                agent._board.map[px, py] = starter
                break
