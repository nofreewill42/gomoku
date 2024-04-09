from env import GomokuEnv

# initialize the environment
env = GomokuEnv.make(13)
observation = env.reset()
env.render()

print(observation.keys())

# take a random action
import random

action = random.choice(list(observation["possible_actions"]))
print(f'Action taken: {action} by player {observation["player"]}. Number of possible actions: {len(observation["possible_actions"])}')
observation = env.step(action)

print(observation.keys())

action = random.choice(list(observation["possible_actions"]))
print(f'Action taken: {action} by player {observation["player"]}. Number of possible actions: {len(observation["possible_actions"])}')
observation = env.step(action)

action = random.choice(list(observation["possible_actions"]))
print(f'Action taken: {action} by player {observation["player"]}. Number of possible actions: {len(observation["possible_actions"])}')
observation = env.step(action)

env.render()