
import os
import random
import sys

from cap6635.agents.informed.hill_climbing import (
    HillClimbing
)
from cap6635.environment.queens import NQueens
from cap6635.utilities.plot import VacuumAnimator


board = NQueens(20)
agent = HillClimbing(board)

last_cost = agent._cost
repetitions = 0
while not agent._solution_located:
    print(repetitions)
    result = agent.climb()
    if result == 'Failed':
        agent.random_init()
        repetitions += 1
    last_cost = agent._cost

print(agent._answer)
