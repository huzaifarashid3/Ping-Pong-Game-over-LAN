import pygame
from network import Network
from player import Player
from ball import Ball
from canvas import Canvas
from helper_functions import *

pygame.init()


class Game():
    def __init__(self, w, h):
        self.n = Network("172.21.122.101")
        self.run = True
        self.canvas = Canvas(w, h, bg_color, "client side")
        self.player = Player(w - 35, 30, yellow, 15, 80)
        self.player2 = Player(w - 35, 20, yellow, 15, 80)
        self.ball = Ball(w/2, h/2, 30, 10, 10, red)
        self.inputs = [0, 0, 0, 0, 0, 0]

    def start(self):
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(60)

            self.input_handling()
            self.n.send(self.inputs)
            self.modify()
            self.render()

        pygame.quit()

    def render(self):
        self.canvas.draw_background()
        self.player.draw(self.canvas.get_canvas())
        self.player2.draw(self.canvas.get_canvas())
        self.ball.draw(self.canvas.get_canvas())
        self.canvas.update()

    def input_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                self.inputs[4] = pygame.KEYDOWN

                if event.key == pygame.K_DOWN:
                    self.inputs[5] = pygame.K_DOWN

                if event.key == pygame.K_UP:
                    self.inputs[5] = pygame.K_UP

            if event.type == pygame.KEYUP:
                self.inputs[4] = pygame.KEYUP

    def modify(self):
        data = self.n.rvc()
        self.player.p.x = data[0]
        self.player.p.y = data[1]
        self.ball.b.x = data[2]
        self.ball.b.y = data[3]


def main():
    game = Game(720, 480)
    game.start()


main()
