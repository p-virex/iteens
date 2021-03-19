import pygame

screen = pygame.display.set_mode((400, 400))
rect = pygame.Rect((0, 0, 50, 50))
surf = pygame.Surface((50, 50))
surf.fill((255, 255, 255))

game = True
while game is True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    rect.x += 1
    screen.fill((0, 0, 0))
    screen.blit(surf, rect)
    pygame.display.update()
    pygame.time.delay(30)
