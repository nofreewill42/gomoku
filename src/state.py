from dataclasses import dataclass
from typing import List

import matplotlib.pyplot as plt
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

    def render(
        self, figsize_factor=0.7, marker_size=500, cmap="binary", probs=None
    ):
        plt.figure(
            figsize=(
                int(self.board.shape[1] * figsize_factor),
                int(self.board.shape[0] * figsize_factor),
            )
        )
        if probs is None:
            img = np.zeros_like(self.board)
        else:
            assert probs.shape == self.board.shape
            img = probs

        plt.imshow(img, cmap=cmap, interpolation="none", vmin=0.0, vmax=1.0)

        # Adding grid lines
        plt.grid(which="major", color="k", linestyle="-", linewidth=2)
        plt.xticks(np.arange(-0.5, self.board.shape[1], 1), [])
        plt.yticks(np.arange(-0.5, self.board.shape[0], 1), [])

        r, c = np.where(self.board == 1)
        plt.scatter(c, r, marker="x", s=marker_size, c="k")
        r, c = np.where(self.board == -1)
        plt.scatter(
            c, r, marker="o", facecolors="none", edgecolors="k", s=marker_size
        )

        plt.show()
