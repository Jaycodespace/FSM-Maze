import pygame


class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0) 

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
