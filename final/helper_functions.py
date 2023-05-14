import pygame

bg_color = pygame.Color("grey20")
yellow = (200, 150, 20)
red = (200, 60, 20)


def read_pos(spos):
    spos = spos.split(",")
    return int(spos[0]), int(spos[1])


def make_pos(ipos):
    return str(ipos[0]) + "," + str(ipos[1])
