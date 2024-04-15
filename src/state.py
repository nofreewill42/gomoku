from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class Action:
    row: int
    col: int


@dataclass
class GameState:
    board: np.ndarray
    active_player: int
    winner: int

    def get_possible_actions(self) -> List[Action]:
        w = np.where(self.board == 0)
        actions = [Action(row, col) for (row, col) in zip(*w)]
        return actions

    @property
    def is_over(self) -> bool:
        return self.winner != 0 or not np.any(self.board == 0)

    def copy(self) -> "GameState":
        return GameState(
            board=self.board.copy(),
            active_player=self.active_player,
            winner=self.winner,
        )
