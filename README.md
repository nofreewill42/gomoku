Just run

>python main.py

```
from env import GomokuEnv

\# initialize the environment
env = GomokuEnv.make(13)
observation, player, possible_actions = env.reset()
env.render()

\# take some random actions
import random
action = random.choice(list(possible_actions))
print(f'Action taken: {action} by player {player}. Number of possible actions: {len(possible_actions)}')
observation, player, possible_actions, winner, done = env.step(action)
action = random.choice(list(possible_actions))
print(f'Action taken: {action} by player {player}. Number of possible actions: {len(possible_actions)}')
observation, player, possible_actions, winner, done = env.step(action)
action = random.choice(list(possible_actions))
print(f'Action taken: {action} by player {player}. Number of possible actions: {len(possible_actions)}')
observation, player, possible_actions, winner, done = env.step(action)
env.render()
```

and you'll see.

![image](https://github.com/nofreewill42/gomoku/assets/14865017/b522a788-78de-44ea-99b7-360443b2cf5e)
