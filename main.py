import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping pong game")

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

paddle_width, paddle_height = 15, 150  # Increase paddle height
ball_size = 20

player1_x, player1_y = 50, screen_height // 2 - paddle_height // 2
player2_x, player2_y = screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2

ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += 5

    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += 5

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y = -ball_speed_y

    if (
        (player1_x < ball_x < player1_x + paddle_width and
         player1_y < ball_y < player1_y + paddle_height) or
        (player2_x < ball_x + ball_size < player2_x + paddle_width and
         player2_y < ball_y < player2_y + paddle_height)
    ):
        ball_speed_x = -ball_speed_x

    if ball_x < 0 or ball_x > screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x = -ball_speed_x

    screen.fill(black)
    pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.flip()
    clock.tick(60)
