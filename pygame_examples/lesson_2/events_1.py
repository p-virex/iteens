import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

game = True
x, y = 50, 100
while game:
    clock.tick(60)
    pygame.display.set_caption(str(int(clock.get_fps())))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                x += 10
            if i.key == pygame.K_LEFT:
                x -= 10
            if i.key == pygame.K_UP:
                y -= 10
            if i.key == pygame.K_DOWN:
                y += 10
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 50)
    pygame.display.update()

pygame.quit()
