import pygame
import itertools
import nqueens
import time
import sys

try:
    n = int(sys.argv[1])
except Exception:
    n = 8
try:
    speed = int(sys.argv[2])
except Exception:
    speed = 0

# set up background surface
pygame.init()
pygame.display.set_caption('The {}-Queens Problem'.format(n))

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

screen = pygame.display.set_mode((680, 680))
clock = pygame.time.Clock()

colors = itertools.cycle((WHITE, BLACK))
tile_size = 640 // n
width, height = n * tile_size, n * tile_size
background = pygame.Surface((width, height))

for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pygame.draw.rect(background, next(colors), rect)
    if n % 2 == 0:
        next(colors)


# display loop ###############################################################
queen_events = nqueens.lazy_n_queens(n)
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    try:
        sol, result = next(queen_events)
    except StopIteration:
        quit()
    foreground = pygame.Surface((width, height), pygame.SRCALPHA)
    foreground.fill((0, 0, 0, 0))
    marker_radius = int(tile_size * 0.4)
    color = (0, 200, 0) if result else pygame.Color('red')
    for col, pos in enumerate(sol):
        x = col * tile_size + tile_size // 2
        y = pos * tile_size + tile_size // 2
        pygame.draw.circle(foreground, color, (x, y), marker_radius)

        line_width = 2
        pygame.draw.line(foreground, color,
                         (x, y), (x + width, y + height), line_width + 2)
        pygame.draw.line(foreground, color,
                         (x, y), (x + width, y - height), line_width + 2)
        pygame.draw.line(foreground, color, (x, y), (x + width, y), line_width)

    screen.fill((60, 70, 90))
    screen.blit(background, (20, 20))
    screen.blit(foreground, (20, 20))

    pygame.display.flip()

    if result:
        time.sleep(1)
    clock.tick(speed)

pygame.quit()
