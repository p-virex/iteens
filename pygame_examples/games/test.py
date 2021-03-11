from itertools import combinations
from copy import deepcopy
from math import sqrt
import pygame
from random import randint

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

NUM_BALLS = 1000
MARKED = RED  # Color used to indicte ball collided.
WIDTH, HEIGHT = 800, 800
M, N = 8, 8  # Number of screen sub-divisions in each dimension.

MARGIN = 5  # Size of space around edges.
MAX_SPEED = 10
MAX_DELTA = round(sqrt(2 * MAX_SPEED**2))
MAX_DELTAX_X, MAX_DELTAX_Y = MAX_DELTA, MAX_DELTA
MAX_X, MAX_Y = WIDTH-MARGIN, HEIGHT-MARGIN
EMPTY_BINS = [[[] for i in range(M)] for j in range(N)]
WM, WN = WIDTH // M, HEIGHT // N  # Dimensions of each sub-division.


class Ball(object):
    def __init__(self, x, y, delta_x, delta_y, color=WHITE):
        self.x, self.y = x, y
        self.delta_x, self.delta_y = delta_x, delta_y
        self.color = color

    def draw(self, display):
        # Using Surface.fill() can be faster than pygame.draw.rect().
        display.fill(self.color, (self.x, self.y, 1, 1))

    def update(self):
        self.x += self.delta_x
        self.y += self.delta_y

        if self.x < 0:
            self.x = 0
            self.delta_x = -self.delta_x
        elif self.x > MAX_X:
            self.x = MAX_X
            self.delta_x = -self.delta_x

        if self.y < 0:
            self.y = 0
            self.delta_y = -self.delta_y
        elif self.y > MAX_Y:
            self.y = MAX_Y
            self.delta_y = -self.delta_y


def classify(balls):
    """ Sort balls in bins. """
    bins = deepcopy(EMPTY_BINS)
    for ball in balls:
        m, n = ball.x // WM, ball.y // WN
        try:
            bins[m][n].append(ball)
        except IndexError:
            raise IndexError(f'bins[{m}][{n}] -> {ball.x}, {ball.y}')
    return bins

def detect_collisions(balls):
    """ Find all colliding balls and return whether any were found.
    """
    bins = classify(balls)  # Separate balls into bins.
    collisions = False
    for m in range(M):
        for n in range(N):
            if bins[m][n]:  # Non-empty?
                for a, b in (pair for pair in combinations(bins[m][n], 2)):
                    if(a.x == b.x and a.y == b.y and (a.color != MARKED or
                                                      b.color != MARKED)):
                        a.color = b.color = MARKED
                        collisions = True
    return collisions

def main():
    pygame.init()
    display = pygame.display.set_mode((HEIGHT, WIDTH))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    balls = [
        Ball(randint(MARGIN, MAX_X), randint(MARGIN, MAX_Y),
             randint(-MAX_DELTAX_X, MAX_DELTAX_X), randint(-MAX_DELTAX_Y, MAX_DELTAX_Y))
           for _ in range(NUM_BALLS)
    ]

    # Main loop.
    remove_collisions = False  # No collisions first iteration.
    while len(balls):
        display.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Remove any collisions found.
        if remove_collisions:
            balls[:] = [ball for ball in balls if ball.color != MARKED]

        # Update display.
        for ball in balls:
            ball.draw(display)
            ball.update()

        # Check after ball updates.
        remove_collisions = detect_collisions(balls)

        pygame.display.flip()
        clock.tick(60)

main()