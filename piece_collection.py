import numpy as np

piece_list_small = [
    np.array(
        [[1]]
    ),
    np.array(
        [[1, 1]]
    ),
    np.array(
        [[1, 0],
         [0, 1]]
    )
]

piece_list_medium = [
    np.array(
        [[1, 1, 1]]
    ),
    np.array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    ),
    np.array(
        [[1, 1, 1],
         [0, 0, 1],
         [0, 0, 1]]
    ),
    np.array(
        [[1, 1, 1, 1]]
    ),
    np.array(
        [[0, 1, 1],
         [1, 1, 0]]
    ),
    np.array(
        [[0, 1, 0],
         [1, 1, 1]]
    ),
    np.array(
        [[1, 1],
         [1, 1]]
    )
]

piece_list_large = [
    np.array(
        [[1, 1, 1, 1]]
    ),
    np.array(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    ),
    np.array(
        [[1, 1, 1, 1, 1]]
    ),
    np.array(
        [[1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1]]
    )
]

all_pieces = [piece_list_small, piece_list_medium, piece_list_large]


def get_random_piece(iteration: int):
    size_probability = np.array([max(50 - iteration, 25), 25, min(iteration, 25)], dtype=np.float64)
    size_probability /= np.sum(size_probability)
    index_piece_size = np.random.choice(3, p=size_probability)
    piece_list = all_pieces[index_piece_size]
    piece = piece_list[np.random.randint(len(piece_list))]
    if np.random.uniform() > 0.5:
        piece = piece.T
    if np.random.uniform() > 0.5:
        piece = np.flipud(piece)
    if np.random.uniform() > 0.5:
        piece = np.fliplr(piece)
    return piece
