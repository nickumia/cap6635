
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
        try:
            # Order with the best survivors last
            best_last = [x for _, x in sorted(zip(survival_rates, pop))]
        except TypeError:
            # None are better than each other
            print("failed")
            best_last = pop

        if len(best_last) < x:
            return best_last
        return best_last[-x:]

    def reproduce(self, x, y):
        c = random.randint(0, x._n - 1)
        offspring = NQueensGeneticEncoding(x._n)
        offspring.sequence = x.sequence[0:c] + y.sequence[c:y._n]
        return offspring

    def fix_missing(self, x):
        # if repeated queens, swap repeats with missing queens
        missing = set(range(1, x._n + 1)) - set(x.sequence)
        for j in x.permutation:
            x.sequence[j] = missing.pop()

    def mutate(self, x):
        # if perfect permutation, swap any random pair of queens
        # print(x.permutation)
        if x.permutation == []:
            c1 = random.randint(0, x._n - 1)
            c2 = random.randint(0, x._n - 1)
            x.swap(c1, c2)
            return x

    def evolve(self):
        new_pop = []
        X, Y = self.best_chromosome(self._population)
        print(X.sequence, Y.sequence)
        for j in range(self._generation_size):
            child = self.reproduce(X, Y)
            if child.permutation:
                self.fix_missing(child)
            elif random.random() < self._mutation_probability:
                self.mutate(child)
            new_pop.append(child)
            if child.survival_rate == self._perfect_form:
                return new_pop
        return new_pop
