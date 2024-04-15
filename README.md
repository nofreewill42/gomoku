# Gomoku engine

### set up the environment

```bash
$ conda create --name gomoku python=3.10 -y

$ conda activate gomoku

$ python -m pip install -r requirements.txt
```

### Development

Running the tests:

```bash
$ python -m unittest discover
```

Running pre-commit for all files (recommended before commit):

```bash
$ pre-commit run --all
```

Running pre-commit for given files:

```bash
$ pre-commit run --files some_file.py some_file_2.py
```

### Using the engine

```bash
>>> from src.engine import GomokuEngine
>>> from src.state import Action
>>>
>>> engine = GomokuEngine(3, win_len=3)
>>> engine.render()
[[0 0 0]
 [0 0 0]
 [0 0 0]]
>>> actions = engine.state.get_possible_actions()
>>> len(actions)
9
>>> actions[0]
Action(row=0, col=0)
>>>
>>> state = engine.step(actions[0])
>>> engine.render()
[[1 0 0]
 [0 0 0]
 [0 0 0]]
>>>
>>> actions = engine.state.get_possible_actions()
>>> state = engine.step(actions[0])
>>> engine.render()
[[ 1 -1  0]
 [ 0  0  0]
 [ 0  0  0]]
>>>
>>> actions = engine.state.get_possible_actions()
>>> state = engine.step(actions[2])
>>>
>>> engine.render()
[[ 1 -1  0]
 [ 0  1  0]
 [ 0  0  0]]
>>>
>>> engine.step(Action(row=1, col=0))
>>> engine.state.is_over
False
>>>
>>> engine.step(Action(row=2, col=2))
>>> engine.render()
[[ 1 -1  0]
 [-1  1  0]
 [ 0  0  1]]
>>>
>>> engine.state.is_over
True
>>> engine.state.winner
1
```
