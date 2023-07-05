
import os
import random
import sys

from cap6635.agents.informed.hill_climbing import (
    HillClimbing
)
from cap6635.environment.queens import NQueens
from cap6635.utilities.plot import QueensAnimator


board = NQueens(20)
agent = HillClimbing(board)

last_cost = agent._cost
i = 0
animator = QueensAnimator(os.getcwd(), '/hill_climbing.gif')
animator.temp = '/temp/'
animator.save_state(i, agent._board, agent._cost)
while not agent._solution_located:
    print(i)
    result = agent.climb()
    if result == 'Failed':
        animator.save_state(i, agent._board, agent._cost)
        agent.random_init()
        i += 1
    last_cost = agent._cost

animator.make_gif()
del animator.temp

print(agent._answer)
