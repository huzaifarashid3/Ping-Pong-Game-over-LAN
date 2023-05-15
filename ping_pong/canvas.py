import pygame


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
        font = pygame.font.SysFont("freesansbold", size)
        render = font.render(text, 1, pygame.Color("grey25"))

        self.screen.blit(render, (x, y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill(self.bg_color)
