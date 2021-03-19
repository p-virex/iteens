import sys
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))

ORIG_IMAGE = pg.image.load('soccer_ball.png')



def main():
    clock = pg.time.Clock()
    rect = ORIG_IMAGE.get_rect(center=(300, 220))
    angle = 0

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        angle += 2
        image = pg.transform.rotozoom(ORIG_IMAGE, angle, 2)
        # image = pg.transform.rotate(ORIG_IMAGE, angle)
        screen.fill((0, 0, 0))
        screen.blit(image, rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()