import pygame
from circleshape import *
from constants import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print("asteroid initialised")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        print("asteroid drawn")

    def update(self, dt):
        self.position += self.velocity * dt
        print("asteroid updated")
    
Asteroid.containers = (asteroids, updatable, drawable)
