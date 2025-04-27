import pygame
from circleshape import *
from constants import *
import random

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle_offset = random.uniform(20, 50)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = self.velocity.rotate(random_angle_offset)
            asteroid_1.velocity *= 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = self.velocity.rotate(-random_angle_offset)
            asteroid_2.velocity *= 1.2
            self.kill()

Asteroid.containers = (asteroids, updatable, drawable)
