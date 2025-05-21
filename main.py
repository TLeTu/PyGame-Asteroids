import pygame
from constants import *
from objects.circleshape import *
from objects.player import *



def update(screen, clock, delta, player):
    while True:
        # Check if the the window have closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill it with black
        screen.fill((0, 0, 0), rect = None, special_flags = 0)
        pygame.display.flip()

        # Draw the player
        player.draw(screen)

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

    # Initialize player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = player(x, y)

    # Game loop
    update(screen, pyClock, delta, player)
    

if __name__ == "__main__":
    main()