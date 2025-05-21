import pygame
from constants import *
from objects.circleshape import CircleShape
from objects.player import Player



def update(screen, clock, delta, player):
    while True:
        # Check if the the window have closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill it with black
        screen.fill((0, 0, 0), rect = None, special_flags = 0)

        # Draw the player
        player.draw(screen)

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

    # Initialize player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    playerObj = Player(x, y)

    # Game loop
    update(screen, pyClock, delta, playerObj)
    

if __name__ == "__main__":
    main()