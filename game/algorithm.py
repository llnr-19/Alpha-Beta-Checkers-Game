import random
from copy import deepcopy
from checkers.constants import *
import pygame


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    # pygame.time.delay(100)


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def alphabeta(board, depth, max_player, game, cond=float('inf')):
    if depth == 0 or board.winner() != None:
        return board.evaluate(), board

    if max_player:
        max_evaluation = float('-inf')
        best_move = None
        for move in get_all_moves(board, WHITE, game):
            evaluation = alphabeta(move, depth - 1, False, game, max_evaluation)[0]
            if evaluation >= cond:
                break
            max_evaluation = max(max_evaluation, evaluation)
            if max_evaluation == evaluation:
                best_move = move
        return max_evaluation, best_move
    else:
        min_evaluation = float('inf')
        best_move = None
        for move in get_all_moves(board, RED, game):
            evaluation = alphabeta(move, depth - 1, True, game, min_evaluation)[0]
            if evaluation <= cond:
                break
            min_evaluation = min(min_evaluation, evaluation)
            if min_evaluation == evaluation:
                best_move = move
        return min_evaluation, best_move


def computer(board, color, game):
    moves = get_all_moves(board, color, game)
    if len(moves) == 0:
        return None, None
    random_choice = random.choice(moves)
    return None, random_choice
