import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 500, 50, 50) 
        self.color = (0, 0, 255) 
        self.speed = 20

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
