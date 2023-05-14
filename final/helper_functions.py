import pygame

bg_color = pygame.Color("grey20")
yellow = (200, 150, 20)
red = (200, 60, 20)


def read_pos(spos):
    spos = spos.split(",")
    return int(spos[0]), int(spos[1]), int(spos[2]), int(spos[3])


def make_pos(ipos):
    return str(ipos[0]) + "," + str(ipos[1])+str(ipos[2]) + "," + str(ipos[3])
