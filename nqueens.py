
import os
import random
import sys

from cap6635.agents.informed.queens import (
    HillClimbingQueens
)
from cap6635.utilities.plot import VacuumAnimator


agent = HillClimbingQueens(32)

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
