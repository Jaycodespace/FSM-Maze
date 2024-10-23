import pygame
import sys
from states import MenuState
from fsm import FSM


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('FSM Game - MazeCrawl')


WHITE = (255, 255, 255)


clock = pygame.time.Clock()


def main():
    fsm = FSM(MenuState(fsm=None)) 
    fsm.state.fsm = fsm 

    running = True
    while running:
        screen.fill(WHITE)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            fsm.handle_event(event)

        fsm.update()
        fsm.render(screen)

        pygame.display.flip()

        clock.tick(30)

   
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
