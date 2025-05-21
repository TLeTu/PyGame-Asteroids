import pygame
from constants import *
from objects.circleshape import CircleShape
from objects.player import Player



def update(screen, clock, player):
    while True:
        # Check if the the window have closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill it with black
        screen.fill((0, 0, 0), rect = None, special_flags = 0)

        # Draw the player
        player.draw(screen)
        
        # Set FPS
        delta = clock.tick(60) / 1000 # 60 FPS
        
        # Player update
        player.update(delta)

        pygame.display.flip()


def main():
    # Initialize pygame
    pygame.init()
    # Setup FPS
    pyClock = pygame.time.Clock()

    # Setup the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    playerObj = Player(x, y)

    # Game loop
    update(screen, pyClock, playerObj)
    

if __name__ == "__main__":
    main()