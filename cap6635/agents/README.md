
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

### Genetic Algorithm

Code Adapted by Dr. Zhu's class code

- Genetic Programming: Two sequences are put through the (reproduction + mutation) processes to generate offspring.  These offspring are assessed by a fitness function to choose the best candidates to (reproduce + mutate) further.
- This algorithm depends on an adaptation of the n-Queens environment that Hill Climbing uses.  It extends the class and converts the traditional N x N board into a 1 x N sequence, with each element in the sequence correlating to the row that is holding the Queen for that column.
- Limitations: sequence representation of the environment, (sequence must remain the same length on mutation?)
- Benefits: agent can jump to a different part of the search space at will.
- Useful on some (small?) set of problems but no convincing evidence that Genetic Algorithms are better than hill-climbing w/random restarts in general

Optimizations
- In the case of the n-Queens problem, two queens cannot be in the same row/column, so duplicated row/colum offspring can automatically be invalidated.

## Adversarial Search

### MiniMax

Code Adapted from Dr. Zhu's adaptation of: https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

- MiniMax: Within a state-space search tree, two players take turns until a final state is reached.  The `max` player attempts to find the next move that maximizes their chance of winning.  The `min` player attempts to find the next move that minimizes their opponent's chance of winning.
- Minimax Alpha-Beta Pruning: An optimization of Minimax where `alpha` represents the "lower-bound on the actual value of a `max` node, maximum across seen children" and `beta` represents the "upper-bound on actual value of a `min` node, minimum across seen children".
  - For a `min` node whose `beta` value is lower than or equal to the `alpha` value of its ancestor, PRUNE
    - Reasoning: The `alpha` node will not choose any node in the `beta` branch because it is lower than itself.
  - For a `max` node whose `alpha` value is greater than or equal to the `beta` value of its ancestor, PRUNE
    - Reasoning: the `beta` node will not choose any node in the `alpha` branch because it is higher than itself. 
