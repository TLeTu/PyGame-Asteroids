import pygame
from constants import *
from objects.circleshape import CircleShape
from objects.player import Player
from objects.asteroid import Asteroid
from objects.bullet import Bullet
from asteroidfield import AsteroidField



def update(screen, clock, updatables, drawables, bullets, asteroids, player, gameOver):
    while not gameOver:
        # Check if the the window have closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill it with black
        screen.fill((0, 0, 0), rect = None, special_flags = 0)

        # Draw the player
        for obj in drawables:
            obj.draw(screen)
        
        # Set FPS
        delta = clock.tick(60) / 1000 # 60 FPS

        # Objects update
        updatables.update(delta)
        # Check collisions
        for asteroid in asteroids:
            # if asteroid.collide(player):
            #     gameOver = True
            #     print("Game over dude")
            for bullet in bullets:
                if asteroid.collide(bullet):
                    asteroid.kill()
                    bullet.kill()

        pygame.display.flip()


def main():
    # Initialize pygame
    pygame.init()
    # Initalize group
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    # Setup FPS
    pyClock = pygame.time.Clock()

    # Setup the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Bullet.containers = (bullets, updatables, drawables)
    asteroidField = AsteroidField()
    playerObj = Player(x, y)

    gameOver = False

    # Game loop
    update(screen, pyClock, updatables, drawables, bullets, asteroids, playerObj, gameOver)
    

if __name__ == "__main__":
    main()