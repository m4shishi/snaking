import pygame
from pygame.locals import *

pygame.init()

dimensions=(450, 550)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (127, 127, 127)
background = RED
screen = pygame.display.set_mode(dimensions)
running = True

screen.fill(background)
pygame.display.update()

while running:
    for eve in pygame.event.get():
        if(eve.type == pygame.QUIT):
            running = False
        if(eve.type == K_SLASH):
            background = GRAY
        print(eve)
    screen.fill(background)
    pygame.display.update()

pygame.quit()