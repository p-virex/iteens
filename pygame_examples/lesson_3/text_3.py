import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
BASE_FONT = pygame.font.SysFont('calibry', 40)
y = 0
game = True
while game is True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    text = BASE_FONT.render('Привет!', True, (255, 0, 0))
    screen.blit(text, (30, y))
    y += 1
    pygame.display.update()
    pygame.time.delay(30)
