import pygame
from DebugFunction import *

class block(pygame.sprite.Sprite):
    def __init__(self, name, height = 100, length = 100, depth = 0, coordinates = pygame.math.Vector2(50,50), groups : list = [], locked = False):
        super().__init__(groups)
        self.name = name
        self.image = pygame.surface.Surface((length, height))
        self.rect = self.image.get_frect(topleft = coordinates)
        self.image.fill((255,255,255))
        self.depth = depth
        self.locked = locked
        self.mouse_offset = pygame.math.Vector2(pygame.mouse.get_pos()[0]-self.rect.centerx,pygame.mouse.get_pos()[1]-self.rect.centery)
        self.neighbors = {} #dictionary object using a id as the key and a list containing the object and a vector containing the distances between the center points 
        

    def move(self, affected_blocks, to_neighbor = False):
        mouse_pos = pygame.mouse.get_pos()
        affected_blocks.append(self)
        if not self.locked and not to_neighbor:
            if True in pygame.mouse.get_just_pressed():
                self.mouse_offset.x = mouse_pos[0]-self.rect.centerx
                self.mouse_offset.y = mouse_pos[1]-self.rect.centery
            if not(self.locked) and True in pygame.mouse.get_pressed() and self.rect.collidepoint(mouse_pos):
                self.rect.center = mouse_pos-self.mouse_offset
                for neighbor in self.neighbors.values():
                    if not neighbor[0] in affected_blocks:
                        neighbor[0].move(affected_blocks,self.name)
                
      
        elif not self.locked:
            neighbor_pos = self.neighbors.get(to_neighbor)[0].rect.center
            self.rect.center = neighbor_pos - self.neighbors.get(to_neighbor)[1]
            for neighbor in self.neighbors.values():
                if not neighbor[0] in affected_blocks:
                    neighbor[0].move(affected_blocks,self.name)
        else:
            ...
            
    def add_neighbor(self, neighbor : object, center_offset : pygame.math.Vector2):
        self.neighbors[neighbor.name] = (neighbor, center_offset)
        neighbor.recieve_neighbor(self, -center_offset)

    def recieve_neighbor(self, neighbor : object, center_offset : pygame.math.Vector2):
        self.neighbors[neighbor.name] = (neighbor, center_offset)

    def update(self):
        self.move([])
