import pygame
from constants import *


def update(screen):
    while True:
        # Check if the the window have closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill it with black
        screen.fill((255, 255, 255), rect = None, special_flags = 0)
        pygame.display.flip()


def main():
    # Initialize pygame
    pygame.init()

    # Setup the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    update(screen)
    

if __name__ == "__main__":
    main()