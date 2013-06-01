__author__ = 'kartikn'
import random
import pygame
import sys
from pygame.locals import *
import bricks

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
pygame.init()
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
brick_list = []
for i in range(0, 5):
    brick = bricks.Brick(random.randrange(50, 250), random.randrange(50, 250), random.randrange(50)
        , random.randrange(50), WINDOW_WIDTH, WINDOW_HEIGHT)
    brick.x_vel = random.randrange(-1, 2)
    brick.y_vel = random.randrange(-1, 2)
    brick.color = ([random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)])
    brick.line_width = (random.randrange(0, 10))
    brick.warp = random.randrange(0, 2)
    brick_list.append(brick)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window_surface.fill((0, 0, 0))
    for brick in brick_list:
        brick.updatePosition()
        brick.bounceSelf(brick_list)
        pygame.draw.rect(window_surface, brick.color, brick, brick.line_width)
    pygame.display.update()
