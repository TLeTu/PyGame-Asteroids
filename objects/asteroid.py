import pygame
import random
from constants import *
from objects.circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, delta):
        self.position += self.velocity * delta
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        
        randomAngle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(randomAngle)
        velocity2 = self.velocity.rotate(-randomAngle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)

        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
        self.kill()