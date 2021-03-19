import pygame

WIDTH, HEIGHT = SIZE = (1000, 1000)

screen = pygame.display.set_mode(SIZE)

screen.fill((255, 255, 255))

ball = pygame.image.load('soccer_ball.png')
ball_rect = ball.get_rect()
screen.blit(ball, ball_rect)
pygame.display.update()

G = 10
x, y = 10, 1

game = True
while game is True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    y += G
    ball_rect = ball_rect.move(x, y)
    if ball_rect.left < 0 or ball_rect.right > WIDTH:
        x = -x
    if ball_rect.bottom > HEIGHT:
        y = -y
    ball_rect.bottom = min(ball_rect.bottom, HEIGHT)
    screen.fill((255, 255, 0))
    screen.blit(ball, ball_rect)
    pygame.display.update()
    pygame.time.delay(40)
