
import random
import sys
import time

from cap6635.agents.adversarialsearch.minimax import MiniMax
from cap6635.environment.map import TicTacToe
from cap6635.utilities.constants import TTT_NONE, TTT_X, TTT_O


try:
    starter = int(sys.argv[1])
except IndexError:
    starter = random.choice([TTT_X, TTT_O])

try:
    auto = int(sys.argv[2])
except IndexError:
    auto = 0

totalTime = 0
board = TicTacToe(3, 3)
agent = MiniMax(board, starter)


def human(recommend, valid):
    global totalTime
    start = time.time()
    (m, qx, qy) = recommend()
    end = time.time()
    totalTime = totalTime + (end - start)
    print('Evaluation time: {}s'.format(round(end - start, 7)))
    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

    agent._board.print_board()
    while True:
        if not auto:
            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
        else:
            px = random.choice([0, 1, 2])
            py = random.choice([0, 1, 2])
        if valid(px, py):
            break
        else:
            print('The move is not valid! Try again.')

    return px, py


while True:
    if agent._board.is_win():
        break

    if starter == TTT_X:
        # If the player starts
        px, py = human(agent.min, agent._board.is_valid)
        agent._board.map[px][py] = TTT_X
        agent._turn = TTT_O
        (m, px, py) = agent.max()
        agent._board.map[px][py] = TTT_O
        agent._turn = TTT_X
    else:
        # If the AI starts
        (m, px, py) = agent.max()
        agent._board.map[px][py] = TTT_X
        agent._turn = TTT_O
        px, py = human(agent.min, agent._board.is_valid)
        agent._board.map[px][py] = TTT_O
        agent._turn = TTT_X
