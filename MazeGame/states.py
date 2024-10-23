import pygame
from player import Player
from obstacle import Obstacle


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0, 0)


class State:
    def __init__(self, fsm):
        self.fsm = fsm

    def handle_event(self):
        pass

    def update(self):
        pass

    def render(self):
        pass


class MenuState(State):
    def render(self, screen):
        self.background_image = pygame.image.load('MazeGame/Images/background.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

        self.banner_image = pygame.image.load('MazeGame/Images/banner.png').convert_alpha()  
        self.banner_image = pygame.transform.scale(self.banner_image, (400, 250))
        self.banner_rect = self.banner_image.get_rect(center=(395, 260))
        
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.banner_image, self.banner_rect)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Press Space to Start", True, WHITE)
        screen.blit(text, (235, 250))
        

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.fsm.change_state(PlayingState(self.fsm))


class PlayingState(State):
    def __init__(self, fsm):
        super().__init__(fsm)
        self.player = Player()

        self.background_image = pygame.image.load('MazeGame/Images/ground.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))
        
        font = pygame.font.SysFont(None, 30)
        self.text = font.render("(ESC) MAIN MENU", True, WHITE)
        self.obstacles = [
            Obstacle(150, 180, 40, 450, 'MazeGame/Images/obstacle.png'), 
            Obstacle(300, 0, 40, 450, 'MazeGame/Images/obstacle.png'),
            Obstacle(450, 180, 40, 450, 'MazeGame/Images/obstacle.png'),
            Obstacle(600, 0, 40, 450, 'MazeGame/Images/obstacle.png')
           ]
        
        self.finish_line = pygame.Rect(750, 0, 10, 600) 

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.fsm.change_state(MenuState(self.fsm))
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.fsm.change_state(PauseState(self.fsm))

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.fsm.change_state(GameOverState(self.fsm))

       
        if self.player.rect.colliderect(self.finish_line):
            print("Finished!")
            self.fsm.change_state(FinishState(self.fsm))

    def render(self, screen):
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.text,(0,0))
        self.player.render(screen)
        for obstacle in self.obstacles:
            obstacle.render(screen)

        
        pygame.draw.rect(screen, RED, self.finish_line)


class FinishState(State):
    def render(self, screen):
        self.background_image = pygame.image.load('MazeGame/Images/background.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))
        
        self.banner_image = pygame.image.load('MazeGame/Images/banner.png').convert_alpha()  
        self.banner_image = pygame.transform.scale(self.banner_image, (700, 450))
        self.banner_rect = self.banner_image.get_rect(center=(410, 230))

        font = pygame.font.SysFont(None, 48)
        text = font.render("IMBAHA BAI! press SPACE to play again", True, WHITE)
        menutext = font.render("Press M to go back to main menu",True,WHITE)
        screen.blit(self.background_image,(0,0))
        screen.blit(self.banner_image, self.banner_rect) 
        screen.blit(text, (90, 190))
        screen.blit(menutext,(150,255))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.fsm.change_state(PlayingState(self.fsm))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            self.fsm.change_state(MenuState(self.fsm))
        

class GameOverState(State):
    def render(self,screen):
        self.background_image = pygame.image.load('MazeGame/Images/background.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

        self.banner_image = pygame.image.load('MazeGame/Images/gameover.png').convert_alpha()  
        self.banner_image = pygame.transform.scale(self.banner_image, (700, 300))
        self.banner_rect = self.banner_image.get_rect(center=(410, 240))

        font = pygame.font.SysFont(None,48)
        text = font.render("GAME OVER!",True,WHITE)
        menutext = font.render("PRESS M TO GO BACK TO MAIN MENU",True,WHITE)
        playtext = font.render("PRESS SPACE TO PLAY AGAIN",True,WHITE)
        screen.blit(self.background_image,(0,0))
        screen.blit(self.banner_image, self.banner_rect) 
        screen.blit(text, (300, 150))
        screen.blit(menutext, (100, 225))
        screen.blit(playtext, (150, 300))
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            self.fsm.change_state(MenuState(self.fsm))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.fsm.change_state(PlayingState(self.fsm))
    

class PauseState(State):
    def render(self,screen):
        self.background_image = pygame.image.load('MazeGame/Images/background.png')
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

        self.banner_image = pygame.image.load('MazeGame/Images/banner.png').convert_alpha()  
        self.banner_image = pygame.transform.scale(self.banner_image, (700, 600))
        self.banner_rect = self.banner_image.get_rect(center=(395, 225))

        font = pygame.font.SysFont(None,48)
        text = font.render("RELAX PAUSE SA TA!",True,WHITE)
        resumetext = font.render("PRESS SPACE TO RESUME GAME",True,WHITE)
        menutext = font.render("PRESS M TO GO BACK TO MAIN MENU",True,WHITE)
        screen.blit(self.background_image,(0,0))
        screen.blit(self.banner_image, self.banner_rect)
        screen.blit(text,(220,150))
        screen.blit(resumetext,(130,225))
        screen.blit(menutext,(85,300))


        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.fsm.change_state(self.fsm.previous_state)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            self.fsm.change_state(MenuState(self.fsm))

