import pygame
from DebugFunction import *

class block(pygame.sprite.Sprite):
    def __init__(self, name, height = 100, length = 100, depth = 0, coordinates = pygame.math.Vector2(50,50), groups : list = [], neighbors : dict = {}):
        super().__init__(groups)
        self.name = name
        self.image = pygame.surface.Surface((length, height))
        self.rect = self.image.get_frect(topleft = coordinates)
        self.image.fill((255,255,255))
        self.depth = depth
        self.locked = False
        self.mouse_offset = pygame.math.Vector2(pygame.mouse.get_pos()[0]-self.rect.centerx,pygame.mouse.get_pos()[1]-self.rect.centery)
        self.neighbors = neighbors #dictionary object using a id as the key and a list containing the object and a vector containing the distances between the center points 

    def move(self, to_neighbor = None):
        mouse_pos = pygame.mouse.get_pos()
        if not self.locked:
            if True in pygame.mouse.get_just_pressed():
                self.mouse_offset.x = mouse_pos[0]-self.rect.centerx
                self.mouse_offset.y = mouse_pos[1]-self.rect.centery
            if not(self.locked) and True in pygame.mouse.get_pressed() and self.rect.collidepoint(mouse_pos):
                self.rect.center = mouse_pos-self.mouse_offset
                debug(self.name)
                debug(self.neighbors, y = 30)
                
      
        elif not self.locked:
            neighbor_pos = self.neighbors.get(to_neighbor)[0].rect.center
            self.rect.center = neighbor_pos - self.neighbors.get(to_neighbor)[1]
        
        else:
            ...
            
    def add_neighbor(self, neighbor : object, center_offset : pygame.math.Vector2):
        print(neighbor.neighbors)
        self.neighbors[neighbor.name] = (neighbor, center_offset)
        print(neighbor.neighbors)
        
        perpendicular_vector = pygame.math.Vector2(1, -(center_offset.x/center_offset.y))
        neighbor.recieve_neighbor(self, center_offset.reflect(perpendicular_vector))

        


    def recieve_neighbor(self, neighbor : object, center_offset : pygame.math.Vector2):
        self.neighbors[neighbor.name] = (neighbor, center_offset)


    def update(self):
        self.move()
