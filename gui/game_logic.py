import time
import messagebox
from game.config import *
from checkers.game import Game
from game.mode import *

FPS = 60


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def start_game(level, algorithm, mode):
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    time.sleep(1)
    start_time = time.time()

    while run:
        # wait
        clock.tick(FPS)

        if mode == modes[2]:
            pygame.display.set_caption("Checkers: Computer vs Ai")
            computer_mode(level, algorithm, game)

        elif mode == modes[1]:
            pygame.display.set_caption("Checkers: Human vs Ai")
            human_mode(level, algorithm, game)

            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        if game.winner() is not None:
            end_time = time.time()
            time.sleep(1)
            elapsed_time = end_time - start_time
            print(f"Elapsed Time: {elapsed_time} seconds")
            winner_color = game.winner()
            winner_message = "Red player wins!" if winner_color == RED else "White player wins!"
            print("Winner: ", winner_message)
            messagebox.showinfo("Game Over", winner_message)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.update()
