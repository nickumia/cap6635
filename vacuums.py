
import matplotlib.pyplot as plt
import matplotlib
import random
import sys

from cap6635.agents.blind.vacuum import (
    ReflexVacuum, ModelVacuum, GoalVacuum
)
from cap6635.environment.map import Carpet


matplotlib.use('TkAgg', force=True)


if len(sys.argv) > 1:
    agent_type = sys.argv[1]
else:
    agent_type = random.choice([1, 2, 3])

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

while world.dirtPresent():
    label = "Time Elapsed:%d; Utility: %.1f" % (agent.time, agent.utility)
    plt.text(0, 0, label)
    plt.imshow(world.map, 'pink')
    plt.show(block=False)
    plt.plot(agent.y_path, agent.x_path, 'r:', linewidth=1)
    if len(agent.x_path) > 0:
        plt.plot(agent.y_path[-1], agent.x_path[-1], '*r', 'Robot field', 5)
    plt.pause(0.5)
    agent.move()
    plt.clf()

print('All dirt has been cleaned :)')
print('Agent time: %d, utility: %d' % (agent.time, agent.utility))
