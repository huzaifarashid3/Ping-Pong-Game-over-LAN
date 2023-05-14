import pygame
from network import Network
from player import Player
from ball import Ball
from canvas import Canvas
from helper_functions import *

pygame.init()


class Game():
    def __init__(self, w, h):
        self.n = Network()
        self.run = True
        self.canvas = Canvas(w, h, bg_color, "testing")
        self.player = Player(w - 35, 30, yellow, 15, 80)
        self.ball = Ball(w/2, h/2, 30, 10, 10, red)

    def start(self):
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(60)

            data = self.n.send_n_rcv(make_pos((0, 0, 0, 0)))

            self.player.p.x, self.player.p.y = (data[0], data[1])
            self.ball.b.x, self.ball.b.y = (data[2], data[3])

            self.render()
        pygame.quit()

    def render(self):
        self.canvas.draw_background()
        self.player.draw(self.canvas.get_canvas())
        self.ball.draw(self.canvas.get_canvas())
        self.canvas.update()


def main():
    game = Game(720, 480)
    game.start()


main()
