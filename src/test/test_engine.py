import unittest

import numpy as np

from src.engine import GomokuEngine
from src.state import Action


class TestEngine(unittest.TestCase):
    def test_step(self):
        engine = GomokuEngine(3, win_len=2)
        state = engine.step(Action(1, 1))
        np.testing.assert_array_equal(
            state.board,
            np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.int8),
        )
        assert state.active_player == -1
        assert state.winner == 0

    def test_longest_consecutive_len_case_0(self):
        row = np.array([0, 0, 0])
        max_1s = GomokuEngine.longest_consecutive_len(row)
        assert max_1s == 0

    def test_longest_consecutive_len_case_1(self):
        row = np.array([1])
        max_1s = GomokuEngine.longest_consecutive_len(row)
        assert max_1s == 1

    def test_longest_consecutive_len_case_2(self):
        row = np.array([1, 1])
        max_1s = GomokuEngine.longest_consecutive_len(row)
        assert max_1s == 2

    def test_longest_consecutive_len_case_3(self):
        row = np.array([1, 1, 0, 1, 1, 1])
        max_1s = GomokuEngine.longest_consecutive_len(row)
        assert max_1s == 3

    def test_longest_consecutive_len_case_4(self):
        row = np.array([0, 1, 1, 0, 0, 1])
        max_1s = GomokuEngine.longest_consecutive_len(row)
        assert max_1s == 2

    def test_has_game_ended_case0(self):
        board = np.array([[0, 1, 0], [-1, -1, -1], [1, 0, 1]])
        has_ended = GomokuEngine.has_game_ended(
            board,
            1,
            2,
            win_size=3,
        )
        assert has_ended

    def test_has_game_ended_case1(self):
        board = np.array([[0, 1, 0], [-1, 1, -1], [1, 0, 1]])
        has_ended = GomokuEngine.has_game_ended(
            board,
            1,
            2,
            win_size=3,
        )
        assert not has_ended

    def test_has_game_ended_case2(self):
        board = np.array([[1, 1, 0, 0, 0], [1, 1, -1, 0, 0], [1, 0, 1, 0, 0]])
        has_ended = GomokuEngine.has_game_ended(
            board,
            2,
            0,
            win_size=3,
        )
        assert has_ended

    def test_has_game_ended_case3(self):
        board = np.array([[1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 1, -1]])
        has_ended = GomokuEngine.has_game_ended(
            board,
            0,
            1,
            win_size=3,
        )
        assert has_ended

    def test_has_game_ended_case4(self):
        board = np.array([[1, 1, 0, -1], [1, 0, -1, 0], [1, -1, 1, 0]])
        has_ended = GomokuEngine.has_game_ended(
            board,
            1,
            2,
            win_size=3,
        )
        assert has_ended


if __name__ == "__main__":
    unittest.main()
