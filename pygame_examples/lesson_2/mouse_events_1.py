import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

game = True
screen.fill((30, 30, 30))
while game:
    clock.tick(60)

    pygame.display.set_caption(str(int(clock.get_fps())))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            print(i.pos)
            if i.button == 1:
                pygame.draw.circle(screen, (255, 255, 255), i.pos(), 50)
            elif i.button == 2:
                screen.fill((30, 30, 30))

    pygame.display.update()

pygame.quit()
