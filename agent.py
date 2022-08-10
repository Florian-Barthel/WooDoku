import numpy as np


class Agent:
    def __init__(self):
        self.counter = 0

    def select_position(self, piece, env):
        env.place_piece(piece=piece, x=np.random.randint(9), y=np.random.randint(9))
        env.calculate_reward()
        self.counter += 1

