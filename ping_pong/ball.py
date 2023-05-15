import pygame
from helper_functions import *


class Ball():
    def __init__(self, x, y, diameter, velx=10, vely=10, color=red, sw=720, sh=480):
        self.sw = sw
        self.sh = sh
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
        if self.b.top <= 0 or self.b.bottom >= self.sh:
            self.vely *= -1
        if self.b.left <= 0 or self.b.right >= self.sw:
            self.velx *= -1
        if self.b.colliderect(player):
            self.velx *= -1
