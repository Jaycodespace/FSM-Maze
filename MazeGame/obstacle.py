import pygame


class Obstacle:
    def __init__(self, x, y, width, height, image_path):

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def render(self, screen):
        screen.blit(self.image, self.rect)