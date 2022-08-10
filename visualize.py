import numpy as np

import environment


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def draw_board(env: environment.Env, iteration, last_piece: np.ndarray, is_last=False):
    print('-----------WOODOKU-----------')
    print('Iteration {}, Score: {}'.format(iteration, env.game_score))
    print('Current piece:')
    for i in range(last_piece.shape[0]):
        for j in range(last_piece.shape[1]):
            if last_piece[i, j] > 0:
                print(bcolors.OKCYAN + '■' + bcolors.ENDC, end='  ')
            else:
                print(' ', end='  ')
        print()
    print()

    for i in range(env.game_board.shape[0]):
        if i % 3 == 0 and i > 0:
            print('═'*30)
        for j in range(env.game_board.shape[1]):
            if j % 3 == 0 and j > 0:
                print('║ ', end='')

            if i in np.arange(last_piece.shape[0]) + env.last_position_y and not is_last:
                if j in np.arange(last_piece.shape[1]) + env.last_position_x:
                    if last_piece[i - env.last_position_y, j - env.last_position_x] > 0:
                        print(bcolors.OKCYAN + '■' + bcolors.ENDC, end='  ')
                    else:
                        if env.board_diff[i, j] != 0:
                            print(bcolors.FAIL + '■' + bcolors.ENDC, end='  ')
                        elif env.game_board[i, j] > 0:
                            print('■', end='  ')
                        else:
                            print('☐', end='  ')
                    continue
            if env.board_diff[i, j] != 0:
                print(bcolors.FAIL + '■' + bcolors.ENDC, end='  ')
                continue
            if env.game_board[i, j] > 0:
                print('■', end='  ')
            else:
                print('☐', end='  ')
        print()
    print()
