import pygame
from player import Player
from obstacle import Obstacle


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


class State:
    def __init__(self, fsm):
        self.fsm = fsm

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass


class MenuState(State):
    def render(self, screen):
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Press Space to Start", True, BLACK)
        screen.blit(text, (240, 250))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.fsm.change_state(PlayingState(self.fsm))


class PlayingState(State):
    def __init__(self, fsm):
        super().__init__(fsm)
        self.player = Player()
        
        self.obstacles = [
            Obstacle(150, 180, 20, 450), 
            Obstacle(300, 0, 20, 450),
            Obstacle(450, 180, 20, 450),
            Obstacle(600, 0, 20, 450)
           ]
        self.finish_line = pygame.Rect(750, 0, 10, 600) 

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            self.fsm.change_state(MenuState(self.fsm))

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                print("Collision! Back to menu.")
                self.fsm.change_state(MenuState(self.fsm))

       
        if self.player.rect.colliderect(self.finish_line):
            print("Finished!")
            self.fsm.change_state(FinishState(self.fsm))

    def render(self, screen):
        screen.fill(WHITE)
        self.player.render(screen)
        for obstacle in self.obstacles:
            obstacle.render(screen)

        
        pygame.draw.rect(screen, GREEN, self.finish_line)


class FinishState(State):
    def render(self, screen):
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 48)
        text = font.render("You Finished! Press R to Restart", True, BLACK)
        screen.blit(text, (150, 250))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            self.fsm.change_state(MenuState(self.fsm))
