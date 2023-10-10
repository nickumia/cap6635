
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
    auto = int(sys.argv[1])
except IndexError:
    auto = 0

totalTime=0
while True:
    if agent._board.is_win():
        break

    # If it's player's turn
    if agent.player_turn == TTT_X:

        while True:

            start = time.time()
            (m, qx, qy) = agent.min()
            end = time.time()
            totalTime=totalTime+(end-start)
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            print('Recommended move: X = {}, Y = {}'.format(qx, qy))

            px = int(input('Insert the X coordinate: '))
            py = int(input('Insert the Y coordinate: '))

            (qx, qy) = (px, py)

            if agent._board.is_valid(px, py):
                agent._board.map[px][py] = TTT_X
                agent.player_turn = TTT_O
                break
            else:
                print('The move is not valid! Try again.')

    # If it's AI's turn
    else:
        (m, px, py) = agent.max()
        agent._board.map[px][py] = TTT_O
        agent.player_turn = TTT_X

    agent._board.print_board()

