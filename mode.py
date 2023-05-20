from checkers.algorithm import *


# Simulating moves
def alphabeta_play(game, depth):
    value, new_board = alphabeta(game.get_board(), depth, WHITE, game)
    game.ai_move(new_board)


def minimax_play(game, depth):
    value, new_board = minimax(game.get_board(), depth, WHITE, game)
    game.ai_move(new_board)


def computer_play(game):
    value, new_board = computer(game.get_board(), RED, game)
    game.ai_move(new_board)


# Ai and Computer moves function in case of Computer vs Ai agent
def computer_mode(level, algorithm, game):
    if level == "Easy" and algorithm == "Alphabeta" and game.turn == WHITE:
        alphabeta_play(game, 2)
    elif level == "Easy" and algorithm == "Alphabeta" and game.turn != WHITE:
        computer_play(game)

    elif level == "Easy" and algorithm == "Minimax" and game.turn == WHITE:
        minimax_play(game, 2)
    elif level == "Easy" and algorithm == "Minimax" and game.turn != WHITE:
        computer_play(game)

    elif level == "Medium" and algorithm == "Alphabeta" and game.turn == WHITE:
        alphabeta_play(game, 4)
    elif level == "Medium" and algorithm == "Alphabeta" and game.turn != WHITE:
        computer_play(game)

    elif level == "Medium" and algorithm == "Minimax" and game.turn == WHITE:
        minimax_play(game, 4)
    elif level == "Medium" and algorithm == "Minimax" and game.turn != WHITE:
        computer_play(game)

    elif level == "Hard" and algorithm == "Alphabeta" and game.turn == WHITE:
        alphabeta_play(game, 8)
    elif level == "Hard" and algorithm == "Alphabeta" and game.turn != WHITE:
        computer_play(game)

    elif level == "Hard" and algorithm == "Minimax" and game.turn == WHITE:
        minimax_play(game, 8)
    elif level == "Hard" and algorithm == "Minimax" and game.turn != WHITE:
        computer_play(game)


# Ai moves function in case of Human vs Ai agent
def human_mode(level, algorithm, game):
    if level == "Easy" and algorithm == "Alphabeta" and game.turn == WHITE:
        alphabeta_play(game, 2)
    elif level == "Easy" and algorithm == "Minimax" and game.turn == WHITE:
        minimax_play(game, 2)

    elif level == "Medium" and algorithm == "Alphabeta" and game.turn == WHITE:
        alphabeta_play(game, 4)

    elif level == "Medium" and algorithm == "Minimax" and game.turn == WHITE:
        minimax_play(game, 4)

    elif level == "Hard" and algorithm == "Alphabeta" and game.turn == WHITE:
        alphabeta_play(game, 8)

    elif level == "Hard" and algorithm == "Minimax" and game.turn == WHITE:
        minimax_play(game, 8)
