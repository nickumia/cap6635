
import os
import random
import sys

from cap6635.agents.blindsearch.vacuum import (
    ReflexVacuum, ModelVacuum, GoalVacuum
)
from cap6635.environment.map import Carpet
from cap6635.utilities.plot import VacuumAnimator


if len(sys.argv) > 1:
    agent_type = sys.argv[1]
else:
    agent_type = random.choice(['1', '2', '3'])

try:
    if len(sys.argv) == 4:
        world_height = int(sys.argv[2])
        world_width = int(sys.argv[3])
except ValueError:
    pass

try:
    world_height
except NameError:
    world_height = random.randint(5, 12)
try:
    world_width
except NameError:
    world_width = random.randint(5, 12)


world = Carpet(world_height, world_width)
if agent_type == '1':
    agent = ReflexVacuum(world)
elif agent_type == '2':
    agent = ModelVacuum(world)
elif agent_type == '3':
    agent = GoalVacuum(world)

print('World dimensions (%d, %d)' % (world_height, world_width))
print('Agent: %s' % (agent.__class__))

i = 0

animator = VacuumAnimator(os.getcwd(), '/vacuum%s.gif' % (agent_type))
animator.temp = '/temp/'
animator.save_state(i, world, agent)
while world.dirtPresent():
    i += 1
    agent.move()
    animator.save_state(i, world, agent)

animator.make_gif()
del animator.temp

print('All dirt has been cleaned :)')
print('Agent time: %d, utility: %d' % (agent.time, agent.utility))
