
from cap6635.agents.blind.vacuum import SimpleVacuum, ModelVacuum
from cap6635.environment.map import Carpet


world = Carpet(5,5)
# agent = SimpleVacuum(world)
agent = ModelVacuum(world)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg', force=True)


while world.dirtPresent():
    plt.text(0,0,"Time Elapsed:%d; Utility: %.1f"%(agent.time,agent.utility))
    plt.imshow(world.map, 'pink')
    plt.show(block=False)
    plt.plot(agent.y_path,agent.x_path,'r:',linewidth=1)
    if len(agent.x_path) > 0:
        plt.plot(agent.y_path[-1], agent.x_path[-1], '*r', 'Robot field', 5)
    plt.pause(0.5)
    agent.move()
    plt.clf()

print('All dirt has been cleaned :)')
print('Agent time: %d, utility: %d' % (agent.time, agent.utility))
