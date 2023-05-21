
from game.config import *
import pygame
import pygame_gui
from pygame_gui.elements import *
from checkers.constants import GREY
from gui.game_logic import start_game


def start():
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
                        start_game(selected_difficulty, selected_algorithm, selected_mode)
                        running = False

        # Update the UI manager
        manager.update(time_delta)

        # Draw the UI elements
        window_surface.fill(GREY)
        manager.draw_ui(window_surface)

        pygame.display.update()

    pygame.quit()
