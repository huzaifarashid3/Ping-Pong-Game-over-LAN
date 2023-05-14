import pygame


class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.diameter = 20
        self.velx = 0
        self.vely = 0

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color,
                            (self.x, self.y, self.diameter, self.diameter))

    def move(self):
        self.x += self.velx
        self.y += self.vely
