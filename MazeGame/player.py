import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load('MazeGame/images/player.png').convert_alpha()  
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.rect = self.image.get_rect(topleft=(10, 470))  
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
        screen.blit(self.image, self.rect)