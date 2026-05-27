import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rnd_angle = random.uniform(20.0, 50.0)
            new_velocity_a = self.velocity.rotate(rnd_angle)
            new_velocity_b = self.velocity.rotate(rnd_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_a = Asteroid(self.position.x, self.position.y, new_radius)
            split_b = Asteroid(self.position.x, self.position.y, new_radius)
            split_a.velocity = new_velocity_a * 1.2
            split_b.velocity = new_velocity_b * 1.2
