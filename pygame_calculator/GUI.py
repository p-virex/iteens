import pygame


class Label():

    def __init__(self, screen, text, x=0, y=0, text_color=(255, 255, 255), bg_color=None, font_size=25):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.text_color = text_color
        self.bg_color = bg_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)

        self.text_blit = self.font.render(self.text, True, self.text_color, self.bg_color)

    def set_text(self, text):
        self.text = text
        self.font = pygame.font.Font(None, self.font_size)
        self.text_blit = self.font.render(self.text, True, self.text_color, self.bg_color)

    def add_text(self, text):
        self.text += text
        self.font = pygame.font.Font(None, self.font_size)
        self.text_blit = self.font.render(self.text, True, self.text_color, self.bg_color)

    def set_text_color(self, text_color):
        self.text_color = text_color
        self.text_blit = self.font.render(self.text, True, self.text_color, self.bg_color)

    def set_bg_color(self, bg_color):
        self.bg_color = bg_color
        self.text_blit = self.font.render(self.text, True, self.text_color, self.bg_color)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move_x(self, x):
        self.x += x

    def move_y(self, y):
        self.y += y

    def get_text(self):
        return self.text

    def update(self):
        self.screen.blit(self.text_blit, (self.x, self.y))


class Button():

    def __init__(self, screen, text, x=0, y=0, text_color=(0, 0, 0), bg_color=(200, 200, 200), font_size=25, width=100,
                 height=50, hover_color=(100, 100, 100)):

        self.pygame = pygame
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.text_color = text_color
        self.bg_color = bg_color
        self.font_size = font_size
        self.width = width
        self.height = height
        self.hover_color = hover_color

        self.button = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.Font(None, self.font_size)

        self.text_blit = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def set_text(self, text):
        self.text = text
        self.font = pygame.font.Font(None, self.font_size)
        self.text_blit = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def set_text_color(self, text_color):
        self.text_color = text_color
        self.text_blit = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def set_bg_color(self, bg_color):
        self.bg_color = bg_color

    def set_x(self, x):
        self.x = x
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def set_y(self, y):
        self.y = y
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def move_x(self, x):
        self.x += x
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def move_y(self, y):
        self.y += y
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.button.centerx - self.text_rect.centerx, self.button.centery - self.text_rect.centery)

    def set_hover_color(self, hover_color):
        self.hover_color = hover_color

    def active(self, key):
        if self.button.collidepoint(self.pygame.mouse.get_pos()) and key == 1:
            return True
        else:
            return False

    def update(self):
        if self.button.collidepoint(self.pygame.mouse.get_pos()):
            self.pygame.draw.rect(self.screen, self.hover_color, self.button)
        else:
            self.pygame.draw.rect(self.screen, self.bg_color, self.button)

        self.screen.blit(self.text_blit, self.xy)


class Input():

    def __init__(self, screen, text='', x=0, y=0, text_color=(0, 0, 0), circuit_color=(200, 200, 200), font_size=25,
                 width=100, height=50, bg_color=(100, 100, 100)):

        self.pygame = pygame
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.text_color = text_color
        self.circuit_color = circuit_color
        self.font_size = font_size
        self.width = width
        self.height = height
        self.bg_color = bg_color

        self.input_text = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.Font(None, self.font_size)

        self.text_blit = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def active(self, key):
        # active(key = event.unicode)
        if key == "":
            self.text = self.text[0:-1]
        else:
            self.text += key

            self.text_blit = self.font.render(self.text, True, self.text_color)
            self.text_rect = self.text_blit.get_rect()
            self.xy = (
            self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def set_text_color(self, text_color):
        self.text_color = text_color
        self.text_blit = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def set_bg_color(self, circuit_color):
        self.circuit_color = circuit_color

    def set_x(self, x):
        self.x = x
        self.input_text = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def set_y(self, y):
        self.y = y
        self.input_text = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def move_x(self, x):
        self.x += x
        self.input_text = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def move_y(self, y):
        self.y += y
        self.input_text = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def set_hover_color(self, bg_color):
        self.bg_color = bg_color

    def set_text(self, text):
        self.text = text
        self.text_blit = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

    def get_text(self):
        return self.text

    def update(self):
        if self.input_text.collidepoint(self.pygame.mouse.get_pos()):

            self.text_blit = self.font.render(self.text + '|', True, self.text_color)
            self.text_rect = self.text_blit.get_rect()
            self.xy = (
            self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)
        else:
            self.text_blit = self.font.render(self.text, True, self.text_color)
            self.text_rect = self.text_blit.get_rect()
            self.xy = (
            self.input_text.centerx - self.text_rect.centerx, self.input_text.centery - self.text_rect.centery)

        self.pygame.draw.rect(self.screen, self.bg_color, self.input_text)
        self.pygame.draw.rect(self.screen, self.circuit_color, self.input_text, 3)

        self.screen.blit(self.text_blit, self.xy)


class Image():

    def __init__(self, screen, img, x=0, y=0):
        self.pygame = pygame
        self.screen = screen
        self.img = img
        self.x = x
        self.y = y

        self.image = self.pygame.image.load(self.img)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move_x(self, x):
        self.x += x

    def move_y(self, y):
        self.y += y

    def set_img(self, img):
        self.img = img
        self.image = self.pygame.image.load(self.img)

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))


class Toggle():

    def __init__(self, screen, value=False, x=0, y=0, width=60, height=25):

        self.screen = screen
        self.pygame = pygame
        self.value = value
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.toggle = pygame.Rect(self.x, self.y, self.width, self.height)

    def active(self, key):
        if self.toggle.collidepoint(self.pygame.mouse.get_pos()) and key == 1:

            if self.value:
                self.value = False
            else:
                self.value = True

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_x(self, x):
        self.x = x
        self.toggle = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_y(self, y):
        self.y = y
        self.toggle = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_x(self, x):
        self.x += x
        self.toggle = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_y(self, y):
        self.y += y
        self.toggle = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        if self.value:
            self.value_rect = pygame.Rect(self.x + self.width / 2, self.y, self.width / 2, self.height)
            self.value_color = (100, 255, 100)
        else:

            self.value_rect = pygame.Rect(self.x, self.y, self.width / 2, self.height)
            self.value_color = (255, 100, 100)

        self.pygame.draw.rect(self.screen, (100, 100, 100), self.toggle, 3)
        self.pygame.draw.rect(self.screen, (100, 100, 100), self.toggle)
        self.pygame.draw.rect(self.screen, self.value_color, self.value_rect)


class ProgressBar():

    def __init__(self, screen, progress=0, x=0, y=0, width=300, height=30):
        self.screen = screen
        self.pygame = pygame
        self.progress = progress
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.progressbar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.progressbar_line = pygame.Rect(self.x, self.y, self.progress * self.width / 100, self.height)

        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.progress) + ' %', True, (0, 0, 0))

        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.progressbar.centerx - self.text_rect.centerx, self.progressbar.centery - self.text_rect.centery)

    def move_progress(self, progress):
        if self.progress < 100:
            self.progress += progress

            self.text_blit = self.font.render(str(self.progress) + ' %', True, (0, 0, 0))

        self.progressbar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.progressbar_line = pygame.Rect(self.x, self.y, self.progress * self.width / 100, self.height)

    def set_x(self, x):
        self.x = x
        self.progressbar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.progressbar_line = pygame.Rect(self.x, self.y, self.progress * self.width / 100, self.height)

        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.progress) + ' %', True, (0, 0, 0))

        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.progressbar.centerx - self.text_rect.centerx, self.progressbar.centery - self.text_rect.centery)

    def set_y(self, y):
        self.y = y
        self.progressbar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.progressbar_line = pygame.Rect(self.x, self.y, self.progress * self.width / 100, self.height)

        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.progress) + ' %', True, (0, 0, 0))

        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.progressbar.centerx - self.text_rect.centerx, self.progressbar.centery - self.text_rect.centery)

    def move_x(self, x):
        self.x += x
        self.progressbar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.progressbar_line = pygame.Rect(self.x, self.y, self.progress * self.width / 100, self.height)

        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.progress) + ' %', True, (0, 0, 0))

        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.progressbar.centerx - self.text_rect.centerx, self.progressbar.centery - self.text_rect.centery)

    def move_y(self, y):
        self.y += y
        self.progressbar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.progressbar_line = pygame.Rect(self.x, self.y, self.progress * self.width / 100, self.height)

        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.progress) + ' %', True, (0, 0, 0))

        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.progressbar.centerx - self.text_rect.centerx, self.progressbar.centery - self.text_rect.centery)

    def update(self):
        self.pygame.draw.rect(self.screen, (100, 100, 100), self.progressbar)
        self.pygame.draw.rect(self.screen, (100, 255, 100), self.progressbar_line)

        self.screen.blit(self.text_blit, self.xy)


class Stepper():

    def __init__(self, screen, value=0, step=1, height=25, width=120, x=0, y=0):

        self.screen = screen
        self.pygame = pygame
        self.value = value
        self.height = height
        self.width = width
        self.step = step
        self.x = x
        self.y = y

        self.stepper = pygame.Rect(self.x, self.y, self.width, self.height)

        self.up = pygame.Rect(self.x + self.width * 2 / 3, self.y, self.width / 3, self.height)
        self.down = pygame.Rect(self.x, self.y, self.width / 3, self.height)

        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))

        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)

    def active(self, key):
        if self.down.collidepoint(self.pygame.mouse.get_pos()) and key == 1:
            self.value -= self.step

            self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))
            self.text_rect = self.text_blit.get_rect()
            self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)
        elif self.up.collidepoint(self.pygame.mouse.get_pos()) and key == 1:
            self.value += self.step

            self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))
            self.text_rect = self.text_blit.get_rect()
            self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)

    def set_x(self, x):
        self.x = x
        self.stepper = pygame.Rect(self.x, self.y, self.width, self.height)
        self.up = pygame.Rect(self.x + self.width * 2 / 3, self.y, self.width / 3, self.height)
        self.down = pygame.Rect(self.x, self.y, self.width / 3, self.height)
        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)

    def set_y(self, y):
        self.y = y
        self.stepper = pygame.Rect(self.x, self.y, self.width, self.height)
        self.up = pygame.Rect(self.x + self.width * 2 / 3, self.y, self.width / 3, self.height)
        self.down = pygame.Rect(self.x, self.y, self.width / 3, self.height)
        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)

    def move_x(self, x):
        self.x += x
        self.stepper = pygame.Rect(self.x, self.y, self.width, self.height)
        self.up = pygame.Rect(self.x + self.width * 2 / 3, self.y, self.width / 3, self.height)
        self.down = pygame.Rect(self.x, self.y, self.width / 3, self.height)
        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)

    def move_y(self, y):
        self.y += y
        self.stepper = pygame.Rect(self.x, self.y, self.width, self.height)
        self.up = pygame.Rect(self.x + self.width * 2 / 3, self.y, self.width / 3, self.height)
        self.down = pygame.Rect(self.x, self.y, self.width / 3, self.height)
        self.font = pygame.font.Font(None, 32)
        self.text_blit = self.font.render(str(self.value), True, (0, 0, 0))
        self.text_rect = self.text_blit.get_rect()
        self.xy = (self.stepper.centerx - self.text_rect.centerx, self.stepper.centery - self.text_rect.centery)

    def update(self):

        self.pygame.draw.rect(self.screen, (100, 100, 100), self.stepper)
        self.pygame.draw.rect(self.screen, (255, 100, 100), self.down)
        self.pygame.draw.rect(self.screen, (100, 255, 100), self.up)

        self.screen.blit(self.text_blit, self.xy)