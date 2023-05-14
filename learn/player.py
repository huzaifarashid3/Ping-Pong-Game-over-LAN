import pygame


class Player():
    width = height = 50

    def __init__(self, startx, starty, color=(200, 150, 20)):
        self.x = startx
        self.y = starty
        self.vel = 0
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y,
                         self.width, self.height), 0)

    def move(self):
        self.y += self.vel
