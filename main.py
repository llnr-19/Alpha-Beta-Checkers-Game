import pygame_gui
from pygame_gui.elements import *
from pygame_gui.windows import *
from checkers.game import *
from checkers.algorithm import *
from mode import *
import pygame
import time

pygame.init()

# Game settings
difficulty_levels = ["Difficulty", "Easy", "Medium", "Hard"]
algorithm_types = ["Algorithm", "Minimax", "Alphabeta"]
modes = ["Mode", "User vs AI agent", "Computer vs AI agent"]
FPS = 60


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def start_game(level, algorithm, mode):
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkers")

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        # wait
        clock.tick(FPS)

        if mode == modes[2]:
            pygame.display.set_caption("Computer vs Ai")
            computer_mode(level, algorithm, game)
            # Ai turn
            # Alpha beta , Minimax
            # if game.turn == WHITE:
            #     value, new_board = alphabeta(game.get_board(), 7, WHITE, game)
            #     game.ai_move(new_board)
            #
            # # Human/ Computer
            # else:
            #     value, new_board = computer(game.get_board(), RED, game)
            #     game.ai_move(new_board)

        elif mode == modes[1]:
            pygame.display.set_caption("Human vs Ai")
            human_mode(level, algorithm, game)
            # if game.turn == WHITE:
            #     value, new_board = alphabeta(game.get_board(), 1, WHITE, game)
            #     game.ai_move(new_board)

            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.update()

    pygame.quit()


########################################################################################################################

def main():
    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    window_surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Game Settings")

    # Create the UI manager
    manager = pygame_gui.UIManager((400, 300))

    # UI elements
    difficulty_dropdown = UIDropDownMenu(
        options_list=difficulty_levels,
        starting_option="Difficulty",
        relative_rect=pygame.Rect(50, 50, 300, 50),
        manager=manager
    )

    algorithm_dropdown = UIDropDownMenu(
        options_list=algorithm_types,
        starting_option="Algorithm",
        relative_rect=pygame.Rect(50, 110, 300, 50),
        manager=manager
    )

    mode_dropdown = UIDropDownMenu(
        options_list=modes,
        starting_option="Mode",
        relative_rect=pygame.Rect(50, 170, 300, 50),
        manager=manager
    )

    start_button = UIButton(
        relative_rect=pygame.Rect(150, 230, 100, 40),
        text="Start",
        manager=manager
    )

    # Game settings variables
    selected_difficulty = None
    selected_algorithm = None
    selected_mode = None

    # Game loop
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Process GUI events
            manager.process_events(event)

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == difficulty_dropdown:
                    selected_difficulty = difficulty_dropdown.selected_option
                elif event.ui_element == algorithm_dropdown:
                    selected_algorithm = algorithm_dropdown.selected_option
                elif event.ui_element == mode_dropdown:
                    selected_mode = mode_dropdown.selected_option
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    # Handle start button press
                    if selected_difficulty and selected_algorithm and selected_mode:
                        print("Difficulty Level:", selected_difficulty)
                        print("Algorithm Type:", selected_algorithm)
                        print("Mode:", selected_mode)
                        time.sleep(1)
                        start_time = time.time()
                        start_game(selected_difficulty, selected_algorithm, selected_mode)
                        end_time = time.time()
                        time.sleep(1)
                        elapsed_time = end_time - start_time
                        print(f"Elapsed Time: {elapsed_time} seconds")
                        running = False
                        # Add your game logic here to start the game based on the selected settings

        # Update the UI manager
        manager.update(time_delta)

        # Draw the UI elements
        window_surface.fill((255, 255, 255))
        manager.draw_ui(window_surface)

        pygame.display.update()

    pygame.quit()


main()
