import pygame
import sys
from BlockClass import *
from DebugFunction import *
from itertools import count
pygame.init()
current_block_id = count(0,1)
running = True
blocks = pygame.sprite.Group()
blocks.add(block(next(current_block_id)))
blocks.add(block(next(current_block_id), coordinates=pygame.math.Vector2(x=100,y=100)))
blocks.sprites()[0].add_neighbor(blocks.sprites()[1], pygame.math.Vector2(10,10))

clock = pygame.time.Clock()
window = pygame.display.set_mode(size=(1000,500))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()


    window.fill((30,40,50))

    blocks.update()
    blocks.draw(window)

    pygame.display.update()

    
    clock.tick(120)