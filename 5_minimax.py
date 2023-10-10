
import random
import sys
import time

from cap6635.agents.adversarialsearch.minimax import MiniMax, MiniMaxAlphaBeta
from cap6635.environment.map import TicTacToe
from cap6635.utilities.constants import TTT_X, TTT_O


totalTime = 0
board = TicTacToe(3, 3)

# Determine which algorithm to use
try:
    algo = int(sys.argv[1])
except IndexError:
    algo = 0

# Determine who plays first
try:
    starter = int(sys.argv[2])
except IndexError:
    starter = random.choice([TTT_X, TTT_O])

# Is there a Human? Or should it be AI vs. AI?
try:
    auto = int(sys.argv[3])
except IndexError:
    auto = 0
algorithm = MiniMaxAlphaBeta if algo == 0 else MiniMax
agent = algorithm(board, starter)


def human(recommend, valid):
    global totalTime
    start = time.time()
    (m, qx, qy) = recommend(-2, 2)
    end = time.time()
    totalTime = totalTime + (end - start)
    print('Evaluation time: {}s'.format(round(end - start, 7)))
    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

    if agent._board.is_win():
        return 0, 0
    agent._board.print_board()
    while True:
        if not auto:
            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))
        else:
            px = qx
            py = qy
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
        (m, px, py) = agent.max(-2, 2)
        agent._board.map[px][py] = TTT_O
        agent._turn = TTT_X
    else:
        # If the AI starts
        (m, px, py) = agent.max(-2, 2)
        agent._board.map[px][py] = TTT_X
        agent._turn = TTT_O
        px, py = human(agent.min, agent._board.is_valid)
        agent._board.map[px][py] = TTT_O
        agent._turn = TTT_X

agent._board.print_board()
winner = 'X' if agent._board.win == 1 else 'O'
winner = 'O' if agent._board.win == 2 else 'No one'

print("%s wins!" % (winner))
