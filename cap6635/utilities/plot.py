
from cap6635.utilities.location import generateNumber

import matplotlib.pyplot as plt
import numpy as np
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


class MazeAnimator(Animator):

    def save_state(self, i, maze, agent):
        plt.imshow(maze.map, 'pink')
        plt.plot(agent._y_path, agent._x_path, 'r:', linewidth=1)
        plt.plot(agent._y_path[-1], agent._x_path[-1], '*r', 'Maze Runner', 5)
        plt.savefig(self._temp_dir + '%s.png' % (generateNumber(i)))


class QueensAnimator(Animator):

    def gen_grids(self, n, ax1):
        for pos in np.linspace(-n, 2*n, 3*n+1):
            ax1.vlines(pos, 0, n, color='k', linestyle='--')
            ax1.hlines(pos, 0, n, color='k', linestyle='--')
        for pos in np.linspace(-n, 2*n, 3*n*10+1):
            ax1.axline((pos, 0), slope=1,
                       color='k', linestyle='-', transform=ax1.transAxes)
            ax1.axline((pos, 0), slope=-1,
                       color='k', linestyle='-', transform=ax1.transAxes)

    def save_state(self, t, board, cost, bar=False):
        label = "Iteration: %d" % (t)
        n = board._n
        pretty = np.arange(n*n*3).reshape(n, n, 3)
        positions = [(row-1, col-1) for row, col in board._chess_board.items()]

        ax1 = plt.subplot(121)
        # self.gen_grids(n, ax1)
        for i in range(n):
            for j in range(n):
                if (i, j) in positions:
                    pretty[i][j] = (255, 0, 0)
                else:
                    pretty[i][j] = (255, 255, 255)
        ax1.imshow(pretty)
        ax2 = plt.subplot(122)
        if bar:
            ax2.bar(cost.keys(), cost.values())
            ax2.set_xlim(0, 1)
        else:
            ax2.plot(cost)
            ax2.set_xlabel('# of Moves')
            ax2.set_ylabel('# of attacked Q pairs')
        plt.title(label)
        plt.savefig(self._temp_dir + '%s.png' % (generateNumber(t)))
        plt.clf()
