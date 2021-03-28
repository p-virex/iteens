from random import randint, choice

import pygame

WIDTH, HEIGHT = SIZE = (800, 800)


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Rectangle, self).__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(15, WIDTH-15), randint(15, HEIGHT-15))
        self.speed_x = choice([-1, 1])
        self.speed_y = choice([-1, 1])
        self.screen = screen

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH or self.rect.right < 0:
            self.speed_x *= -1
        if self.rect.bottom + 15 > HEIGHT or self.rect.top < 0:
            self.speed_y *= -1
        list_rect = pygame.sprite.spritecollide(self, rect_sprites, False)
        if len(list_rect) > 1:
            for spr in list_rect:
                spr.speed_y *= -1
                spr.speed_x *= -1


def rand_color():
    return [randint(0, 255) for _ in range(3)]


screen = pygame.display.set_mode(SIZE)

game = True

screen.fill((255, 255, 255))
pygame.display.update()

rect_sprites = pygame.sprite.Group()

for _ in range(150):
    rect_sprites.add(Rectangle(rand_color()))

while game is True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    screen.fill((255, 255, 255))
    rect_sprites.update()
    rect_sprites.draw(screen)
    pygame.display.update()

    pygame.time.delay(10)
