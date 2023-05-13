from pygame.locals import *
import pygame
import sys


def input_routine():
    global player1_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            elif event.key == pygame.K_UP:
                player1_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 3
            elif event.key == pygame.K_UP:
                player1_speed += 3


def drawing():
    screen.fill(bg_color)
    pygame.draw.rect(screen, my_color, player1)
    pygame.draw.rect(screen, my_color, player2)
    pygame.draw.ellipse(screen, my_color, ball)

    pygame.draw.aaline(screen, my_color, (screen_width/2, 0),
                       (screen_width/2, screen_height))

    pygame.display.flip()


def ball_animation():
    global ball_speed_x, ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    ball.x += ball_speed_x
    ball.y += ball_speed_y


def player_animation():
    player1.y += player1_speed
    player1.top = max(0, player1.top)
    player1.bottom = min(screen_height, player1.bottom)


def player2_animation():
    global player2_speed
    if ball.y < player2.bottom:
        player2_speed -= 3
    if ball.y > player2.top:
        player2_speed += 3

    player2.y += player2_speed
    player2.top = max(0, player2.top)
    player2.bottom = min(screen_height, player2.bottom)


pygame.init()

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
my_color = (200, 150, 100)

while True:

    input_routine()

    ball_animation()
    player_animation()
    player2_animation()

    drawing()

    clock.tick(60)
