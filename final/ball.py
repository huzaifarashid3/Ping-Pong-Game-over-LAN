import pygame
from helper_functions import *


class Ball():
    def __init__(self, x, y, diameter, velx=10, vely=10, color=red):
        self.b = pygame.Rect(x, y, diameter, diameter)
        self.velx = velx
        self.vely = vely
        self.color = color

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color,
                            self.b)

    def move(self):
        self.b.x += self.velx
        self.b.y += self.vely

    def collision(self, player):
        if self.b.top <= 0 or self.b.bottom >= 480:
            self.vely *= -1
        if self.b.left <= 0 or self.b.right >= 720:
            self.velx *= -1
        if self.b.colliderect(player):
            self.velx *= -1
