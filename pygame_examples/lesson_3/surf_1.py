import pygame

screen = pygame.display.set_mode((400, 400))
surf = pygame.Surface((400, 200))
surf.fill((255, 255, 255))
surf.set_alpha(200)

game = True

while game is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((255, 0, 0))
    pygame.draw.rect(surf, (0, 255, 0), (0, 0, 30, 30))
    screen.blit(surf, (0, 100))
    pygame.display.update()

pygame.quit()
