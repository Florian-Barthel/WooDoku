import numpy as np


class Env:
    def __init__(self):
        self.game_board = np.zeros([9, 9], dtype=np.int)
        self.total_reward = 0
        self.last_piece_placed = True
        self.last_position_x = 0
        self.last_position_y = 0
        self.game_score = 0

    def place_piece(self, piece: np.ndarray, x: int, y: int):
        """Places a given piece at coordinates x and y

        :param piece: numpy array consisting of 0 and 1
        :param x: x coordinate of the upper left corner to place the piece
        :param y: y coordinate of the upper left corner to place the piece
        """
        height, width = piece.shape
        if width + x > 9 or height + y > 9:
            self.last_piece_placed = False
        elif np.any(self.game_board[y:y + height, x:x + width] + piece > 1):
            self.last_piece_placed = False
        else:
            self.game_board[y:y + height, x:x + width] += piece
            self.last_piece_placed = True
            self.last_position_x = x
            self.last_position_y = y
            self.game_score += np.sum(piece)

    def calculate_reward(self) -> int:
        game_board_remove = self.game_board.copy()
        current_reward = 0
        for i in range(3):
            for j in range(3):
                if np.sum(self.game_board[3 * i:3 * i + 3, 3 * j:3 * j + 3]) == 9:
                    current_reward += 1
                    self.game_score += 9
                    game_board_remove[3 * i:3 * i + 3, 3 * j:3 * j + 3] = 0

        for i in range(9):
            if np.sum(self.game_board[i]) == 9:
                current_reward += 1
                self.game_score += 9
                game_board_remove[i] = 0
            if np.sum(self.game_board.T[i]) == 9:
                current_reward += 1
                self.game_score += 9
                game_board_remove.T[i] = 0
        self.game_board = game_board_remove
        self.total_reward += current_reward
        return current_reward

    def game_lost(self, next_piece: np.ndarray):
        height_piece, width_piece = next_piece.shape
        for i in range(9 - (height_piece - 1)):
            for j in range(9 - (width_piece - 1)):
                if np.all(self.game_board[i:i + height_piece, j:j + width_piece] + next_piece < 2):
                    return False
        return True
