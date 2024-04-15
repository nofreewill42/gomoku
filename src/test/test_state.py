import unittest

import numpy as np

from src.state import Action
from src.state import GameState


class TestGameState(unittest.TestCase):
    def test_possible_actions(self):
        board = np.zeros((2, 2), dtype=np.int8)
        board[0, 0] = 1
        board[1, 1] = -1
        state = GameState(
            board=board,
            active_player=1,
            winner=0,
        )
        actions = state.get_possible_actions()
        assert len(actions) == 2
        assert Action(0, 1) in actions
        assert Action(1, 0) in actions


if __name__ == "__main__":
    unittest.main()
