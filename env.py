"""
A gym-like environment for Gomoku.

env = GomokuEnv.make(N(,M))  # N x N is the board size if M is not provided, otherwise N x M
"""

import numpy as np

class GomokuEnv:
    def __init__(self, N, M=None):
        """
        (N x N) board if M is not provided, otherwise (N x M)
        player 1: 1, player 2: -1
        board is from player 1's perspective (return board and player, board*player might or might not be advantageous to do with them regarding the neural network architecture's perspective)
        done: True if the game is over
        action_history: list of (n, m, player) tuples in the order of the actions taken
        possible_actions: set of (n, m) tuples; to make it easier to check if an action is valid

        1. Create an instance either by calling GomokuEnv(N) or GomokuEnv(N, M) or GomokuEnv.make(N) or GomokuEnv.make(N, M)
        2. Then call reset() to get the initial observation and player
        """
        self.N = N
        self.M = M if M else N
    
    def make(N, M=None):
        return GomokuEnv(N, M)

    def reset(self):
        """
        Return:
        - observation: {'board': np.array, 'possible_actions': set}
        - player: 1 (let's say player 1 always starts first)
        """

        self.board = np.zeros((self.N, self.M), dtype=np.int8)
        self.player = 1
        self.done = False
        self.winner = 0

        self.action_history = []
        self.possible_actions = set((i, j) for i in range(self.N) for j in range(self.M))

        # Construct observation
        observation = {'board': self.board.copy(),
                       'possible_actions': self.possible_actions.copy(),
                       'player': self.player,
                       'winner': self.winner,
                       'done': self.done}
        
        return observation
    
    def step(self, action):
        """
        action: (n, m) tuple
        Return:
        - observation: {'board': np.array, 'possible_actions': set}
        - winner: +1, -1, 0
        - done: True, False
        """
        # Assert that the game is not over and the action is valid, complain otherwise
        assert not self.done, "Game is already over"
        assert action in self.possible_actions, "Invalid action"

        # Put 1/-1 on the board
        self.board[action] = self.player
        # Update possible actions
        self.possible_actions.remove(action)
        # Update action history
        self.action_history.append((action, self.player))

        # Check action outcome {1,-1,0,None}
        outcome = self._check_action_outcome(action)
        if outcome is not None:
            self.done = True
            self.winner = outcome
        else:
            self.winner = 0

        # Construct observation
        observation = {'board': self.board.copy(),
                       'possible_actions': self.possible_actions.copy(),
                       'player': self.player,
                       'winner': self.winner,
                       'done': self.done}
        
        # Switch player
        self.player *= -1

        # Return observation, player, possible actions, winner and done
        return observation
    

    def _check_action_outcome(self, action):
        """
        action: (n, m) tuple
        Check if the game is over:
        - 5 in a row
        - No more possible actions
        Return:
        - +1: Player 1 won
        - -1: Player 2 won
        - 0: Draw
        - None: Game is not over yet
        """
        # Check if the current player has won
        def check_if_current_player_won(action):
            '''
            Check if the current player has won
            '''
            n, m = action
            player = self.player

            def check_row_won(n, m, player):
                """
                Grows to the left and right
                """
                count = 1
                # Check left
                left = m - 1
                while left >= 0 and self.board[n, left] == player:
                    count += 1
                    left -= 1
                # Check right
                right = m + 1
                while right < self.M and self.board[n, right] == player:
                    count += 1
                    right += 1
                return count >= 5
            
            def check_col_won(n, m, player):
                """
                Grows up and down
                """
                count = 1
                # Check up
                up = n - 1
                while up >= 0 and self.board[up, m] == player:
                    count += 1
                    up -= 1
                # Check down
                down = n + 1
                while down < self.N and self.board[down, m] == player:
                    count += 1
                    down += 1
                return count >= 5
            
            def check_diag_won(n, m, player):
                """
                Grows diagonally up-left and down-right
                """
                count = 1
                # Check up-left
                up, left = n - 1, m - 1
                while up >= 0 and left >= 0 and self.board[up, left] == player:
                    count += 1
                    up -= 1
                    left -= 1
                # Check down-right
                down, right = n + 1, m + 1
                while down < self.N and right < self.M and self.board[down, right] == player:
                    count += 1
                    down += 1
                    right += 1
                return count >= 5
            
            def check_anti_diag_won(n, m, player):
                """
                Grows diagonally up-right and down-left
                """
                count = 1
                # Check up-right
                up, right = n - 1, m + 1
                while up >= 0 and right < self.M and self.board[up, right] == player:
                    count += 1
                    up -= 1
                    right += 1
                # Check down-left
                down, left = n + 1, m - 1
                while down < self.N and left >= 0 and self.board[down, left] == player:
                    count += 1
                    down += 1
                    left -= 1
                return count >= 5

            # Won if any of the four directions has 5 in a row
            if check_row_won(n, m, player) or\
                check_col_won(n, m, player) or\
                check_diag_won(n, m, player) or\
                check_anti_diag_won(n, m, player):
                return True
            return False
        
        # Did current player win?
        if check_if_current_player_won(action):
            return self.player  # {1,-1}
        # No more possible actions remaining without winning?
        if len(self.possible_actions) == 0:
            return 0
        # If neither, the game is not over yet
        return None

    def render(self):
        print(self.board)