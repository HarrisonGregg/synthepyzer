import pygame
from pygame.locals import *
import keyboard
from keyboard import *
import slider
from slider import *
import button
from button import *

pygame.init()
fpsClock = pygame.time.Clock()

size = [600,400]

screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

k = keyboard(20, 100)

sliders = [Slider((400+50*i, 100), 200) for i in range(1,5)]

b = Button(20, 20, 100, 30, "Button")

while True:
    for event in pygame.event.get():
        k.update(event)
        b.update(event)
        for s in sliders:
            s.update(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYBOARD_EVENT:
            print(event.selected)
            print(event.octave)
    k.draw(screen)
    b.draw(screen)
    for s in sliders:
        s.draw(screen)
    pygame.display.flip()
    screen.fill(BLACK)
    fpsClock.tick(30)