
from cap6635.agents.blind.vacuum import SimpleVacuum
from cap6635.environment.map import Carpet


world = Carpet()
agent = SimpleVacuum(world)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg', force=True)


while True:
    plt.text(0,0,"Time Elapsed:%d; Utility: %.1f"%(agent.time,agent.utility))
    plt.imshow(world.map, 'pink')
    plt.show(block=False)
    plt.plot(agent.y_path,agent.x_path,'r:',linewidth=1)
    print(agent.y_path,agent.x_path)
    if len(agent.x_path) > 0:
        plt.plot(agent.y_path[-1], agent.x_path[-1], '*r', 'Robot field', 5)
    plt.pause(0.5)
    agent.move()
    plt.clf()
