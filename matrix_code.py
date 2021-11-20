import pygame
from pygame.locals import *
import random
import math

pygame.init()
dim = (1920, 1080)
surface = pygame.display.set_mode(dim)
fps = 60

objects = []
paused = False
pause_key_latch = (False, False)


class MatrixText(object):
    _use_text = True

    def __init__(self, x=random.randint(0, dim[0]), y=0.0, size=random.randint(8, 24),
                 alphabet=None, length=10):
        self._length = length
        self._x = x
        self._y = y
        self._size = size
        self._font = pygame.font.Font('fake_receipt.ttf', size)
        self._text = ''
        self._last_alpha = 255
        self._alphabet = alphabet
        self._seq = 0
        if not self._alphabet:
            self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz1234567890`~!@#$%^&*()_+-={}[];\':"\\/?,.<>'

    def _draw_char(self, ch, x, y, color):
        img = self._font.render(ch, True, color)
        surface.blit(img, (x, y))

    def tick(self):
        step = self._size + 2
        self._y += 0.7
        if self._y - step * self._length > dim[1]:
            objects.remove(self)  # Self destruction

    def display(self):
        step = self._size + 2
        fade_in_alpha = int((self._y % step) * 255 / step)
        if fade_in_alpha < self._last_alpha:
            self._text = self._alphabet[self._seq] + (
                self._text[:-1] if len(self._text) >= self._length else self._text)
            self._seq += 1
            self._seq %= len(self._alphabet)
        self._last_alpha = fade_in_alpha

        bot = math.ceil(self._y / float(step)) * step
        self._draw_char(self._text[0], self._x, bot, (0, fade_in_alpha, 0))
        for i in range(1, len(self._text)):
            curr_y = bot - i * step
            calpha = (1.0 - (float(i) / (self._length - 1)))
            nalpha = (1.0 - (float(i + 1) / (self._length - 1)))
            prog = 1.0 - fade_in_alpha / 255.0
            dalph = prog * (calpha - nalpha) + nalpha
            alpha = int(dalph * 255)
            if alpha < 0:
                alpha = 0
            elif alpha > 255:
                alpha = 255
            self._draw_char(self._text[i], self._x, curr_y, (0, alpha, 0))


def event_handler():
    global pause_key_latch, paused
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit(0)
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause_key_latch = (True, pause_key_latch[1])
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                pause_key_latch = (False, pause_key_latch[1])

    if pause_key_latch[0] and not pause_key_latch[1]:
        paused = not paused
        pause_key_latch = (True, True)
    elif not pause_key_latch[0] and pause_key_latch[1]:
        pause_key_latch = (False, False)


count = top = 100


def loop(alphabet=None):
    global objects, count
    surface.fill((0, 0, 0))
    if count >= top:
        for _ in range(6):
            objects.append(MatrixText(x=random.randint(0, dim[0]), y=0.0, size=random.randint(8, 30),
                                      alphabet=alphabet, length=random.randint(10, 20)))
        count = 0

    for o in objects:
        if not paused:
            o.tick()
        o.display()

    count += 1


def main():
    alpha = 'GAMERS HEAVEN '
    pygame.display.set_caption('The Matrix')
    clk = pygame.time.Clock()
    while True:
        event_handler()
        loop(alphabet=alpha)

        pygame.display.update()
        clk.tick(fps)


if __name__ == '__main__':
    main()
