from typing import List
from typing import Tuple
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from src.state import Action
from src.state import GameState


class GomokuEngine:
    """
    A gym-like environment for Gomoku.
    """

    def __init__(
        self, grid_size: Union[int, Tuple[int, int]], win_len: int = 5
    ):
        """initialize the game.
        Players: 1 and -1.

        Args:
            grid_size (Union[int, Tuple[int, int]]):
                size of the grid (e.g. 15x15).
            win_size (int, optional):
                Number of signs in a row to win the game. Defaults to 5.
        """
        if isinstance(grid_size, int):
            self._grid_size = (grid_size, grid_size)
        else:
            assert len(grid_size) == 2
            self._grid_size = (grid_size[0], grid_size[1])
        self._win_size = int(win_len)

        self.reset()

    @property
    def state(self) -> GameState:
        return self._state

    @property
    def history(self) -> List[GameState]:
        return self._history

    @property
    def win_len(self) -> int:
        return self._win_size

    @property
    def active_player(self) -> int:
        return self.state.active_player

    def reset(self) -> GameState:
        """reset the game. Player 1 starts.

        Returns:
            GameState:
        """

        self._state = GameState(
            board=np.zeros(self._grid_size, dtype=np.int8),
            active_player=1,
            winner=0,
        )
        self._history: List[GameState] = [self.state]

        return self.state

    def step(self, action: Action, check_action: bool = False) -> GameState:
        """take action

        Args:
            action (Action):
            check_action (bool, optional): Defaults to False.

        Returns:
            GameState: the next state.
        """

        if check_action:
            assert not self.state.is_over
            assert (
                action in self.state.get_possible_actions()
            ), f"invalid action {action}"

        next_state = self.state.copy()
        next_state.board[action.row, action.col] = self.state.active_player
        if self.has_game_ended(
            next_state.board, action.row, action.col, self._win_size
        ):
            next_state.winner = self.state.active_player
        else:
            next_state.active_player = -self.state.active_player

        self._state = next_state
        self._history.append(self.state)

        return self.state

    @staticmethod
    def has_game_ended(
        board: np.ndarray, row: int, col: int, win_size: int
    ) -> bool:
        """check whether a player won or not.

        Args:
            board (np.ndarray): the game board
            row (int): row location of latest action
            col (int): col location of latest action
            win_size (int): number of consecutive marks needed to win.

        Returns:
            bool:
        """
        board_mod = board * board[row, col]
        board_mod[board_mod == -1] = 0

        vecs_to_check = [
            board_mod[row],
            board_mod[:, col],
            np.diag(board_mod, col - row),
            np.diag(board_mod[:, ::-1], board_mod.shape[1] - 1 - col - row),
        ]

        for vec in vecs_to_check:
            if GomokuEngine.longest_consecutive_len(vec) >= win_size:
                return True

        return False

    @staticmethod
    def longest_consecutive_len(vec: np.ndarray) -> int:
        """_summary_

        Args:
            vec (np.ndarray): vector of 0s and 1s

        Returns:
            int: length of longest consecutive 1s
        """
        if np.all(vec == 0):
            return 0

        vec = np.concatenate([[0], vec, [0]])
        diff = np.diff(vec)
        start = np.where(diff == 1)[0]
        end = np.where(diff == -1)[0]
        len_1s = end - start
        max_len = int(np.max(len_1s))
        return max_len

    def render(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.state.board, cmap="viridis", interpolation="none")

        # Adding grid lines
        plt.grid(which="major", color="w", linestyle="-", linewidth=2)
        plt.xticks(np.arange(-0.5, 20, 1), [])
        plt.yticks(np.arange(-0.5, 20, 1), [])

        plt.colorbar()

        plt.show()
