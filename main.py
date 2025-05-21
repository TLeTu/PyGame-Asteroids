import pygame
from constants import *
from objects.circleshape import CircleShape
from objects.player import Player
from objects.asteroid import Asteroid
from objects.bullet import Bullet
from asteroidfield import AsteroidField


import builtins

try:
    import js
    def save_highscore_js(score):
        js.localStorage.setItem("highscore", str(score))

    def load_highscore_js():
        stored = js.localStorage.getItem("highscore")
        return int(stored) if stored else 0
except ImportError:
    # fallback for desktop
    def save_highscore_js(score):
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    def load_highscore_js():
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0



def update(screen, clock, updatables, drawables, bullets, asteroids, player, gameOver, score, font, highscore):
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
            if asteroid.collide(player):
                if player.outOfLives():
                    game_over(score, highscore)
                    gameOver = True
                    print("Game over dude")
                else:
                    player.delLive()
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            for bullet in bullets:
                if asteroid.collide(bullet):
                    score += 1
                    asteroid.split()
                    bullet.kill()
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
        screen.blit(score_text, (10, 10))  # Draw it at top-left corner

        live_text = font.render(f"Lives: {player.lives}", True, (255, 255, 255))  # White color
        screen.blit(live_text, (10, 50))  # Draw it at top-left corner

        pygame.display.flip()

def game_over(score, highscore):
    if score > highscore:
        highscore = score
        save_highscore_js(highscore)
    return highscore

async def main():
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
    score = 0
    highscore = highscore = load_highscore_js()
    font = pygame.font.SysFont(None, 36)  # Font type and size

    # Game loop
    update(screen, pyClock, updatables, drawables, bullets, asteroids, playerObj, gameOver, score, font, highscore)


import asyncio
asyncio.run(main())
