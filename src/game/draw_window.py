import pygame

from src.game.draw_grid import draw_grid


def draw_window(surface, grid, params):
    [play_width, play_height, top_left_x, top_left_y] = params
    surface.fill((0, 0, 0))

    # Tetris Title
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("TETRIS", 1, (255, 255, 255))
    surface.blit(
        label,
        (top_left_x + play_width / 2 - (label.get_width() / 2), 30)
    )

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)

    # draw grid and border
    draw_grid(surface, 20, 10, params)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x,
                     top_left_y, play_width, play_height), 5)
    pygame.display.update()
