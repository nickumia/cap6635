
import os
import random
import sys

from cap6635.agents.localsearch.simulated_annealing import SimulatedAnnealing
from cap6635.environment.queens import NQueens
from cap6635.utilities.plot import QueensAnimator


try:
    board = NQueens(int(sys.argv[1]))
except IndexError:
    board = NQueens(random.randint(4, 30))
agent = SimulatedAnnealing(board, temperature=40)

last_cost = agent._cost
i = 0
animator = QueensAnimator(os.getcwd(),
                          '/simulated_annealing_%d.gif' % (board._n))
animator.temp = '/temp/'
animator.save_state(i, agent._board, agent._cost)
while not agent._solution_located:
    result = agent.anneal()
    if result:
        if agent._solution_located:
            print(i)
            animator.save_state(i, agent._board, agent._cost)
            break
        result = agent.anneal()
    else:
        print(i)
        animator.save_state(i, agent._board, agent._cost)
        agent.random_init()
        i += 1
    last_cost = agent._cost

animator.make_gif()
del animator.temp

print(agent._answer)
