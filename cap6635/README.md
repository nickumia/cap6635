# CAP6635 Artificial Intelligence
A summary of the AI techniques explored in Dr. Zhu's AI class

## Structure of Package

- `cap6635.agents` define the different search and decision-making algorithms.
    - See sub-directories for more details on the agents
- `cap6635.environment` creates and populates the world with various obstacles or other states.
- `cap6635.utilities` hosts various helper functions for searching, environment manipulation, animation and more.

### Development setup

```bash
pip install -r requirements.txt cap6635
```

## AI Examples

### Vacuums

Run the `vacuums.py` example with the optional paramters.  The output gets saved as a `vacuum?.gif` animation.

```bash
# Type of agent defaults to random type (if not provided)
# 1 --> Simple Reflex Vacuum
# 2 --> Model-based Vacuum
# 3 --> Goal-based Vacuum
# World Height & Width defaults to random int (if not provided)

python vacuums.py [type_of_agent] [height_of_world] [width_of_world]
```

### n-Queens

```bash
# Hill Climbing
python hill_climbing.py [number_of_queens]

# Simulated Annealing
python simulated_annealing.py [number_of_queens]

# Genetic Algorithm
python genetic.py [number_of_queens]
```
