import pygame
from helper_functions import *


class Player():

    def __init__(self, startx, starty, color=yellow, width=15, height=60):

        self.p = pygame.Rect(startx, starty, width, height)
        self.vel = 0
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.p)

    def move(self):
        self.p.y += self.vel
        self.p.top = max(0, self.p.top)
        self.p.bottom = min(self.p.bottom, 480)
