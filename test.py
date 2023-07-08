from utilities.timer import Timer
from environment.map import Map2D
from itertools import combinations

import numpy as np


with Timer():
    test_list = list(range(1000))
    z = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]

with Timer():
    test_list = list(range(10))
    res = list(combinations(test_list, 2))
    print(res)
