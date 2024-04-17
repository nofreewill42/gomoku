# Gomoku engine

### set up the environment

```bash
$ conda create --name gomoku python=3.10 -y

$ conda activate gomoku

$ python -m pip install -r requirements.txt
```

### Develop your model

To develop your model, rewrite the `take_action` function in your `main.py` file under `src/competition/competitors/<YourName>/main.py`.

### Competition

To run a competition, this command should be run:

```bash
python -m src.competition.run_competition
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
>>> print(engine.state.board)
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
>>> print(engine.state.board)
[[1 0 0]
 [0 0 0]
 [0 0 0]]
>>>
>>> actions = engine.state.get_possible_actions()
>>> state = engine.step(actions[0])
>>> print(engine.state.board)
[[ 1 -1  0]
 [ 0  0  0]
 [ 0  0  0]]
>>>
>>> actions = engine.state.get_possible_actions()
>>> state = engine.step(actions[2])
>>>
>>> print(engine.state.board)
[[ 1 -1  0]
 [ 0  1  0]
 [ 0  0  0]]
>>>
>>> engine.step(Action(row=1, col=0))
>>> engine.state.is_over
False
>>>
>>> engine.step(Action(row=2, col=2))
>>> print(engine.state.board)
[[ 1 -1  0]
 [-1  1  0]
 [ 0  0  1]]
>>>
>>> engine.state.is_over
True
>>> engine.state.winner
1
```

### Competition 2024-04-17

Balazs vs Jona. Balazs won 53 times, Jona won 47 times, draw 0 times.

Balazs vs David. Balazs won 46 times, David won 54 times, draw 0 times.

Jona vs Balazs. Jona won 53 times, Balazs won 47 times, draw 0 times.

Jona vs David. Jona won 43 times, David won 57 times, draw 0 times.

David vs Balazs. David won 45 times, Balazs won 55 times, draw 0 times.

David vs Jona. David won 53 times, Jona won 47 times, draw 0 times.

## *** Final results ***
### 1. Balazs: 395
### 2. Jona: 394
### 3. David: 383
