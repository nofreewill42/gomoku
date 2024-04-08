from env import GomokuEnv

# initialize the environment
env = GomokuEnv.make(13)
observation, player, possible_actions = env.reset()
env.render()

# take a random action
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