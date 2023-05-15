import pygame
from player import Player
from ball import Ball
from canvas import Canvas
from helper_functions import *
from server import *

pygame.init()


class Game():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.server = Server()
        self.player = Player(10, 20, yellow, 15, 80)
        self.player2 = Player(w - 25, 20, yellow, 15, 80, w, h)
        self.ball = Ball(w/2, h/2, 30, 10, 10, red, w, h)
        self.canvas = Canvas(w, h, bg_color, "server side")
        self.run = True
        self.inputs = (0, 0, 0, 0, 0, 0, 0, 0)
        self.clock = pygame.time.Clock()

    def start(self):
        while self.run:
            self.clock.tick(60)

            self.inputs = (0, 0, 0, 0, 0, 0, 0, 0)

            self.inputs = self.server.rcv()

            self.input_handling()

            self.modify()

            self.server.send((self.player.p.x, self.player.p.y, self.player2.p.x, self.player2.p.y,
                              self.ball.b.x, self.ball.b.y, 0, 0))

            self.render()
        pygame.quit()

    def input_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player.vel = 10
                if event.key == pygame.K_UP:
                    self.player.vel = -10
            if event.type == pygame.KEYUP:
                self.player.vel = 0

        if self.inputs[6] == 1:
            if self.inputs[7] == 1:
                self.player2.vel = 10
            if self.inputs[7] == 2:
                self.player2.vel = -10
        if self.inputs[6] == 2:
            self.player2.vel = 0

    def render(self):
        self.canvas.draw_background()
        self.canvas.draw_text(("FPS:" +
                               str(int(self.clock.get_fps()))), 50, 40, self.h - 80)

        self.canvas.draw_text(("Ping"), 200, self.w/6, self.h/3)
        pygame.draw.aaline(self.canvas.get_canvas(),
                           yellow, (self.w/2, 0), (self.w/2, self.h))
        self.player.draw(self.canvas.get_canvas())
        self.player2.draw(self.canvas.get_canvas())
        self.ball.draw(self.canvas.get_canvas())
        self.canvas.update()

    def modify(self):
        self.player.move()
        self.player2.move()
        self.ball.collision(self.player.p)
        # self.ball.collision(self.player2.p)
        self.ball.move()


def server_main():
    game = Game(480, 480)
    game.start()

server_main()