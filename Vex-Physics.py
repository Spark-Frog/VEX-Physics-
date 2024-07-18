import pygame
import sys
from BlockClass import *
pygame.init()
running = True
blocks = pygame.sprite.Group()
blocks.add(block())
clock = pygame.time.Clock()

while running:
    window = pygame.display.set_mode(size=(1000,500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    blocks.draw(window)
    pygame.display.flip()
    
    clock.tick(60)