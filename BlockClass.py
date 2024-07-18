import pygame
class block(pygame.sprite.Sprite):
    def __init__(self, height = 100, length = 100, depth = 0, coordinates = pygame.math.Vector2(50,50), groups = []):
        super().__init__(groups)
        self.image = pygame.surface.Surface((length, height))
        self.rect = self.image.get_frect(topleft = coordinates)
        self.image.fill((255,255,255))
        self.depth = depth

    def update():
        pass
