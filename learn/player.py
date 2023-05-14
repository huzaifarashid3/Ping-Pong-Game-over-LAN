import pygame


class Player():

    def __init__(self, startx, starty, color=(200, 150, 20), width=50, height=50):
        self.x = startx
        self.y = starty
        self.vel = 0
        self.color = color
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y,
                         self.width, self.height), 0)

    def move(self):
        self.y += self.vel
