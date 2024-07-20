import pygame
class Joint(pygame.sprite.Sprite):
    def __init__(self, chain1, chain2 = None, coordinate = pygame.math.Vector2(), groups = []):
        super().__init__(groups)
        self.chain1 = chain1
        if chain2:
            self.chain2 = chain2
        self.coordinates = coordinate
        self.image = pygame.surface.Surface((5,5))
        self.rect = self.image.get_frect(center = self.coordinates)
    
    def update(self):
        ...