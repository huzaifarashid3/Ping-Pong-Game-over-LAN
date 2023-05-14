from pygame.locals import *
import pygame
import sys
from network import Network


client_number = 0

# pygame.init()

clock = pygame.time.Clock()

screen_height = 480
screen_width = 720

ball_speed_x = 7
ball_speed_y = 7

player1_speed = 0
player2_speed = 0

screen = pygame.display.set_mode((720, 480))

pygame.display.set_caption("wow")

ball_radius = 20

ball = pygame.Rect(screen_width/2 - ball_radius/2,
                   screen_height/2 - ball_radius/2, ball_radius, ball_radius)

player1 = pygame.Rect(20, 20, 10, 50)
player2 = pygame.Rect(screen_width - 20 - 10, 20, 10, 50)

bg_color = pygame.Color("grey20")
yellow = (200, 150, 100)


def read_pos(strp):
    strp = strp.split(",")
    return int(strp[0]), int(strp[1])


def make_pos(tup):
    return str(tup[0]+","+tup[1])


def input_routine():
    global player1_speed, run, player1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed = 7
            elif event.key == pygame.K_UP:
                player1_speed = -7

        if event.type == pygame.KEYUP:
            player1_speed = 0


def drawing():
    screen.fill(bg_color)
    pygame.draw.rect(screen, yellow, player1)
    pygame.draw.rect(screen, yellow, player2)
    pygame.draw.ellipse(screen, yellow, ball)

    pygame.draw.aaline(screen, yellow, (screen_width/2, 0),
                       (screen_width/2, screen_height))

    pygame.display.flip()


def ball_animation():
    global ball_speed_x, ball_speed_y, ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    ball.x += ball_speed_x
    ball.y += ball_speed_y


def player_animation():
    global player1
    player1.y += player1_speed
    player1.top = max(0, player1.top)
    player1.bottom = min(screen_height, player1.bottom)


def player2_animation():
    global player2_speed, player2
    player2.y += player2_speed

    if ball.y < player2.bottom:
        player2_speed = -5
    if ball.y > player2.top:
        player2_speed = 5

    player2.top = max(0, player2.top)
    player2.bottom = min(screen_height, player2.bottom)


def main():
    n = Network()
    start_pos = read_pos(n.getPos())
    print(start_pos)
    run = True
    # while run:
    #     input_routine()

    #     ball_animation()
    #     player_animation()
    #     player2_animation()

    #     drawing()

    #     clock.tick(60)

    # print("game over")


main()
