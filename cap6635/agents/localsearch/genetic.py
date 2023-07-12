
import random

from cap6635.environment.queens import NQueensGeneticEncoding


class GeneticSearch:

    def __init__(self, mp, initial_sequences, gen_size=100):
        self._population = initial_sequences
        self._mutation_probability = mp
        self._generation_size = gen_size
        self._perfect_form = initial_sequences[0].perfect_form

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, val):
        self._population = val

    def best_chromosome(self, pop, x=2):
        survival_rates = [i.survival_rate for i in pop]
        populationWithProbabilty = zip(pop, survival_rates)
        total = sum(w for c, w in populationWithProbabilty)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(pop, survival_rates):
            if upto + w >= r:
                return c
            upto += w

    def reproduce(self, x, y):
        c = random.randint(0, x._n - 1)
        offspring = NQueensGeneticEncoding(x._n)
        offspring.sequence = x.sequence[0:c] + y.sequence[c:y._n]
        return offspring

    def fix_missing(self, x):
        # if repeated queens, swap repeats with missing queens
        missing = set(range(1, x._n + 1)) - set(x.sequence)
        old_seq = x.sequence
        for j in x.permutation:
            old_seq[j] = missing.pop()
        x.sequence = old_seq

    def mutate(self, x):
        # if perfect permutation, swap any random pair of queens
        if x.permutation == []:
            c1 = random.randint(1, x._n)
            c2 = random.randint(1, x._n)
            x.swap(c1, c2)

    def evolve(self):
        new_pop = []
        for j in range(self._generation_size):
            X = self.best_chromosome(self._population)
            Y = self.best_chromosome(self._population)
            child = self.reproduce(X, Y)
            if child.permutation:
                self.fix_missing(child)
            elif random.random() < self._mutation_probability:
                self.mutate(child)
            new_pop.append(child)
            if child.survival_rate == 1:
                return new_pop
        return new_pop
