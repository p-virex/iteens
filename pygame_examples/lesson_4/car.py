import pygame

WIDTH, HEIGHT = SIZE = (1000, 1000)

screen = pygame.display.set_mode(SIZE)

screen.fill((255, 255, 255))

CAR = pygame.image.load('car.png')
SMALL_CAR = pygame.transform.scale(CAR, (100, 50))
angle = 0
game = True
rect_car = SMALL_CAR.get_rect(center=(WIDTH/2, HEIGHT/2))
while game is True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    image = pygame.transform.rotate(SMALL_CAR, angle)
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT]:
        angle = 180
        rect_car.x -= 1
    elif pressed_keys[pygame.K_RIGHT]:
        angle = 0
        rect_car.x += 1
    elif pressed_keys[pygame.K_DOWN]:
        angle = 270
        rect_car.y += 1
    elif pressed_keys[pygame.K_UP]:
        angle = 90
        rect_car.y -= 1

    screen.fill((255, 255, 255))
    screen.blit(image, rect_car)
    pygame.display.update()

    pygame.time.delay(20)
