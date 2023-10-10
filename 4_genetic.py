
import collections
import os
import random
import sys

from cap6635.agents.localsearch.genetic import GeneticSearch
from cap6635.environment.queens import NQueensGeneticEncoding
from cap6635.utilities.plot import QueensAnimator


try:
    board = NQueensGeneticEncoding(int(sys.argv[1]))
    board2 = NQueensGeneticEncoding(int(sys.argv[1]))
except IndexError:
    size = random.randint(4, 30)
    board = NQueensGeneticEncoding(size)
    board2 = NQueensGeneticEncoding(size)

pop = [board, board2]
agent = GeneticSearch(0.05, pop, gen_size=100)

i = 0
animator = QueensAnimator(os.getcwd(), '/genetic_%d.gif' % (board._n))
animator.temp = '/temp/'
animator.save_state(i, pop[-1], pop[-1].survival_rate)

while agent.population[-1].survival_rate != 1:
    print('=== Generation %d ===' % (i))
    agent.population = agent.evolve()
    costs = collections.Counter([i.survival_rate for i in agent.population])
    print(costs)
    # animator.save_state(i, agent.population[-1], costs.values())
    animator.save_state(i, agent.population[-1], costs, bar=True)
    i += 1
    print('Best Survivor: %0.2f' % (
        max([k.survival_rate for k in agent.population])))

animator.make_gif()
del animator.temp

print(pop[-1].sequence)
