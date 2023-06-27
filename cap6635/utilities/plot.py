
from cap6635.utilities.location import generateNumber

import matplotlib.pyplot as plt
import imageio
import os
import shutil


class Animator:

    def __init__(self, path, name):
        self._input_path = path
        self._name = name
        self._temp_dir = '/temp'

    @property
    def temp(self):
        return self._temp_dir

    @temp.setter
    def temp(self, path):
        self._temp_dir = self._input_path + path
        try:
            os.mkdir(self._temp_dir)
        except OSError:
            pass

    @temp.deleter
    def temp(self):
        shutil.rmtree(self._temp_dir)
        del self._temp_dir

    def make_gif(self):
        images = []
        image_files = [self._temp_dir + f for f in os.listdir(self._temp_dir)]
        image_files.sort()
        for filename in image_files:
            images.append(imageio.imread(filename))
        imageio.mimsave(self._input_path + self._name, images, duration=300)


class VacuumAnimator(Animator):

    def save_state(self, i, world, agent):
        label = "Time Elapsed:%d; Utility: %.1f" % (agent.time, agent.utility)
        plt.text(0, 0, label)
        plt.imshow(world.map, 'pink')
        plt.plot(agent.y_path, agent.x_path, 'r:', linewidth=1)
        plt.plot(agent.y_path[-1], agent.x_path[-1], '*r', 'Robot field', 5)
        plt.savefig(self._temp_dir + '%s.png' % (generateNumber(i)))
        plt.clf()
