import pygame
from constants import *
from circleshape import *



def update(screen, clock, delta):
    while True:
        # Check if the the window have closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill it with white
        screen.fill((255, 255, 255), rect = None, special_flags = 0)
        pygame.display.flip()

        # Set FPS
        delta[0] = clock.tick(60) / 1000 # 60 FPS


def main():
    # Initialize pygame
    pygame.init()
    # Setup FPS
    pyClock = pygame.time.Clock()
    delta = [0]

    # Setup the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    update(screen, pyClock, delta)
    

if __name__ == "__main__":
    main()