import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

game = True
screen.fill((30, 30, 30))

COLOR = (0, 0, 0)
OBJECT = 'circle'

while game:
    clock.tick(60)
    pygame.display.set_caption(str(int(clock.get_fps())))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
            OBJECT = 'circle'
        if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            OBJECT = 'rect'
        if keys[pygame.K_LALT] and keys[pygame.K_r]:
            COLOR = (255, 0, 0)
        if keys[pygame.K_LALT] and keys[pygame.K_c]:
            COLOR = (0, 0, 255)
        if keys[pygame.K_LALT] and keys[pygame.K_g]:
            COLOR = (0, 255, 0)
        if keys[pygame.K_RETURN]:
            screen.fill((30, 30, 30))
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if OBJECT == 'circle':
                    pygame.draw.circle(screen, COLOR, i.pos, 50)
                if OBJECT == 'rect':
                    pygame.draw.rect(screen, COLOR, (i.pos[0], i.pos[-1], 20, 20), 3)

    pygame.display.update()

pygame.quit()
