import pygame
from helper_functions import *


class Ball():
    def __init__(self, x, y, diameter, velx=10, vely=10, color=red):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.velx = velx
        self.vely = vely
        self.color = color

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color,
                            (self.x, self.y, self.diameter, self.diameter))

    def move(self):
        self.x += self.velx
        self.y += self.vely
