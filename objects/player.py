import pygame
from objects.circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.max_speed = PLAYER_SPEED
        self.acceleration_rate = 400   # pixels per second²
        self.friction = 300            # pixels per second²
    
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta

    def update(self, delta):
        keys = pygame.key.get_pressed()
        
        # Reset acceleration each frame
        self.acceleration = pygame.Vector2(0, 0)
        
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        
        # Apply acceleration based on input
        if keys[pygame.K_w]:
            self.acceleration += forward * self.acceleration_rate
        if keys[pygame.K_s]:
            self.acceleration -= forward * self.acceleration_rate
        
        # Apply friction (slow down when no input)
        if self.acceleration.length() == 0 and self.velocity.length() > 0:
            friction_accel = -self.velocity.normalize() * self.friction
            # Prevent friction from reversing velocity direction
            if friction_accel.length() * delta > self.velocity.length():
                self.velocity = pygame.Vector2(0, 0)
            else:
                self.acceleration += friction_accel
        
        # Update velocity and clamp speed
        self.velocity += self.acceleration * delta
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        
        # Update position
        self.position += self.velocity * delta
        
        # Rotate
        if keys[pygame.K_a]:
            self.rotate(-delta)
        if keys[pygame.K_d]:
            self.rotate(delta)