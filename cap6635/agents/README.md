
## Blind Methods

### Vacuums

Code Adapted from Dr. Zhu's adaptation of: https://github.com/mawippel/python-vacuum

- Simple Reflex Agents: Agents react to environment based on pre-programmed rules

  ex. `ReflexVacuum`
  - I will randomly choose a new location which may or may not have dirt and I may or may not have been to before
  
- Model-based Agents: Agents maintains an internal representation of the world.  Remembers it's own past actions. 

  ex. `ModelVacuum`
  - My path is preprogrammed, I will not revisit locations

- Goal-based Agents: Agents 'look for' goal and makes decisions based on a single utility function.

  ex. `GoalVacuum`
  - Where is the closest dirt?

- Utility-based Agents: Agents 'look for' goal while considering other factors.  The utility function is an optimization of many variables.

  (not yet implemented)

## Local Search

### Hill Climbing + Simulated Annealing (n-Queens)

Code Adapted from Dr. Zhu's adaptation of: https://github.com/TranDatDT/n-queens-simulated-annealing/blob/master/main.py

- Hill Climbing: Agents look at all of it's successors and always chooses the best next move.  If there are multiple 'best' moves, choose randomly between them.  Downfalls: local max/min, plateaus, ridges

- Simulated Annealing: Agents pick a random successor.  If it is 'within reason', then choose it; otherwise, check the next random successor.  Successors are evaluated against the temperature.  A higher temperature increases the likelihood of a bad move.  As the temperature cools with each iteration, simulated annealing tends toward hill climbing naturally.

Necessary features of the environment:
- `random_init`: Allows for random restart to cover downfalls
- `eval_cost`: Decides if a solution was reached
- `successors`: Enumerates all of the next moves
