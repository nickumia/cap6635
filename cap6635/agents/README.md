
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
