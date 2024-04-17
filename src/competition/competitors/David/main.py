import random
from typing import List

from src.state import Action
from src.state import GameState

def take_action(state: GameState, history: List[GameState], player: int) -> Action:
    """overwrite this function.

    Args:
        state (GameState):
        history (List[Action]):
        player (int): current player (1 or -1)

    Returns:
        Action: the action taken by the player (model).
    """
    actions = state.get_possible_actions()
    action = random.choice(actions)
    return action
