from checkers.board import *
from checkers.constants import *


class Game:
    def __init__(self, win):
        self._init()  # call the function initial the attribute
        self.win = win  # to select the window we will play in bec if we're playing many plays

    def _init(self):  # initialization
        self.selected = None
        self.turn = RED  # the red its turn to play
        self.board = Board()  # object from Board
        self.valid_moves = {}  # it for tell us what the valid move allow for you

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)  # draw valid moves
        pygame.display.update()  # display the change of board

    def reset(self):  # play from first
        self._init()

    def winner(self):
        return self.board.winner()

    def select(self, row, col):  # the selected place - the row and col is selected
        if self.selected:  # if already selected piece
            result = self._move(row, col)  # try to move it to row, col
            if not result:  # if we can't move
                self.selected = None  # remove the selected to None
                self.select(row, col)  # then recall this method with the row, col

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  # selected piece is done

        return False  # No selected piece

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True  # move is done

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    # Ai agent
    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
