import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

game = True
screen.fill((30, 30, 30))
pygame.draw.arc(screen, (255, 255, 255), (10, 50, 280, 100), 0, 3.14)

while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    pygame.display.update()

    clock.tick(60)
    pygame.display.set_caption(str(int(clock.get_fps())))

pygame.quit()
