import pygame

from src.game.draw_window import draw_window
from src.game.helpers.convert_shape_format import convert_shape_format
from src.game.helpers.create_grid import create_grid
from src.game.helpers.is_game_lost import is_game_lost
from src.game.helpers.is_valid_space import is_valid_space
from src.game.shapes import get_shape


def game_loop():
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
    s_width = 1000
    s_height = 700
    play_width = 300  # meaning 300 // 10 = 30 width per block
    play_height = 600  # meaning 600 // 20 = 20 height per block
    block_size = 30
    top_left_x = (s_width - play_width) // 2
    top_left_y = s_height - play_height

    pygame.init()
    win = pygame.display.set_mode((s_width, s_height), 0, 32)
    pygame.display.set_caption("Tetris")

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        fall_speed = 0.27
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # PIECE FALLING
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (is_valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not is_valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not is_valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_UP:  # rotate shape
                    current_piece.rotation = current_piece.rotation + \
                        1 % len(current_piece.shape)
                    if not is_valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - \
                            1 % len(current_piece.shape)
                if event.key == pygame.K_DOWN:  # move shape down
                    current_piece.y += 1
                    if not is_valid_space(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        # add color of piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:  # If we are not above the screen
                grid[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(
            win, grid, [play_width, play_height, top_left_x, top_left_y])

        if is_game_lost(locked_positions):
            run = False
