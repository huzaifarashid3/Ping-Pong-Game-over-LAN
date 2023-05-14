import pygame
from network import Network

pygame.init()


def input_handling():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


def read_pos(spos):
    spos = spos.split(",")
    return int(spos[0]), int(spos[1])


def make_pos(ipos):
    return str(ipos[0] + "," + ipos[1])


class Canvas():
    def __init__(self, w, h, bg_color, name="None"):
        self.width = w
        self.height = h
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0, 0, 0))

        self.screen.draw(render, (x, y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill(self.bg_color)


class Player():
    width = height = 50

    def __init__(self, startx, starty, color=(200, 150, 20)):
        self.x = startx
        self.y = starty
        self.vel = 0
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y,
                         self.width, self.height), 0)

    def move(self):
        pass


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p1 = Player(startPos[0], startPos[1])
    canvas = Canvas(720, 480, pygame.Color("grey20"), "testing")
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        input_handling()

        canvas.draw_background()
        p1.draw()
        canvas.update()


main()
