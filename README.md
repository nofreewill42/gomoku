# Gomoku engine

### set up the environment

```bash
$ conda create --name gomoku python=3.10 -y

$ conda activate gomoku

$ python -m pip install -r requirements.txt
```

### Using the engine

```bash
>>> from src.engine import GomokuEngine
>>>
>>> engine = GomokuEngine.make(3)
>>> observation = engine.reset()
>>> list(observation.keys())
['board', 'possible_actions', 'player', 'winner', 'done']
>>>
>>> # render the board
>>> engine.render()
[[0 0 0]
 [0 0 0]
 [0 0 0]]
>>>
>>> actions = observation["possible_actions"]
>>> actions
{(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
>>> obs = engine.step((0, 1))
>>>
>>> engine.render()
[[0 1 0]
 [0 0 0]
 [0 0 0]]
>>>
>>> obs["done"]
False
>>>
>>> obs = engine.step((0, 0))
>>> engine.render()
[[-1  1  0]
 [ 0  0  0]
 [ 0  0  0]]
>>>
>>> obs = engine.step((1, 1))
>>>
>>> engine.render()
[[-1  1  0]
 [ 0  1  0]
 [ 0  0  0]]
>>>
>>> obs = engine.step((0, 2))
>>> obs = engine.step((2, 1))
>>> engine.render()
[[-1  1 -1]
 [ 0  1  0]
 [ 0  1  0]]
>>>
>>> obs["done"]
True
```

