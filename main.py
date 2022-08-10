import environment
import piece_collection
import agent
import visualize

if __name__ == '__main__':
    num_games = 10

    for i in range(num_games):
        my_agent = agent.Agent()
        env = environment.Env()
        next_piece = piece_collection.get_random_piece(i)
        while True:
            if env.last_piece_placed:
                if my_agent.counter > 0:
                    visualize.draw_board(env, my_agent.counter, next_piece)
                next_piece = piece_collection.get_random_piece(i)
            if env.game_lost(next_piece):
                visualize.draw_board(env, my_agent.counter, next_piece, is_last=True)
                print()
                print('Game Over')
                break
            my_agent.select_position(next_piece, env)

