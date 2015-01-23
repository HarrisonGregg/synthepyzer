import globs
from globs import * 
import pygame
import time
from pygame.locals import *

class Slider:
    def __init__(self, xy=[0,0], slide_height=100, id=""):
        self.width = 30
        self.height = 30
        self.id = id
        self.slide_height = slide_height
        self.top_y = xy[1]-self.height/2
        self.bot_y = self.top_y + self.slide_height
        self.x = xy[0]
        self.y = xy[1] - self.height/2
        self.color = [233,111,000]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = False
        self.myfont = pygame.font.SysFont("Arial", 20)
        self.label = self.myfont.render("", 1, WHITE)
    def bind(self):
        if self.y >= self.bot_y:
            self.y = self.bot_y
        if self.y <= self.top_y:
            self.y = self.top_y
    def get_value(self):
        self.bind()
        a = 1-min(1.0, float(self.y - self.top_y) / float(self.bot_y - self.top_y))
        # print(a)
        return(a)
    def set_value(self, value):
        self.temp_val = value
        self.y = self.top_y + int(self.slide_height * (1 - self.temp_val))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self, event):
        # print(pygame.mouse.get_pos())
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(0)[0]:
                mousex, mousey = event.pos
                mouserect = pygame.Rect(mousex,mousey, 1,1)
                wholerect = pygame.Rect(self.x, self.top_y, 30, self.slide_height + self.height)
                if wholerect.colliderect(mouserect):
                    self.active = True
        if event.type == MOUSEBUTTONUP:
            self.active = False
        if event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            mouserect = pygame.Rect(mousex,mousey, 1,1)
            wholerect = pygame.Rect(self.x, self.top_y, 30, self.slide_height)
            if pygame.mouse.get_pressed(0)[0] and self.active:
                self.y = mousey - self.height/2
                self.bind()
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                d = {"value":self.get_value(), "id": self.id}
                e = pygame.event.Event(SLIDER_MOTION, d)
                pygame.event.post(e)
                self.label = self.myfont.render("{0}".format(str(self.get_value())[:4]), 1, WHITE)
    def draw(self, screen):
        text_width, text_height = self.myfont.size(str(self.get_value()))
        pygame.draw.line(screen, [100,100,100], [self.x+self.width/2,self.top_y+self.height/2], [self.x+self.width/2, self.bot_y+self.height/2], 5)
        pygame.draw.rect(screen, self.color, self.rect)
        if self.active:
            screen.blit(self.label, (self.x + self.width/2 - text_width/2, self.y + self.height/2 - text_height/2))
# size = [600,400]
# screen = pygame.display.set_mode(size)
# pygame.init()

# sliders = [slider([70,70], 200), slider([200, 50], 30)]
# clock = pygame.time.Clock()
# while(1):
    # #pygame.event.pump()
    # for s in sliders:
        # s.update(1)
        # s.draw()
    # sliders[0].get_value()
    # pygame.display.flip()
    # screen.fill([0,0,0])
    # clock.tick(10)


# """
# self.rects.append(pygame.Rect(self.left, self.top, self.rect_width, self.rect_height))
        # for r in self.rects:
            # pygame.draw.rect(SCREEN,GRAY, r)
# """

"""
myfont = pg.font.SysFont("Comic Sans MS", 30)
# apply it to text on a label
label = myfont.render("Python and Pygame are Fun!", 1, yellow)
# put the label object on the screen at point x=100, y=100
screen.blit(label, (100, 100))
"""
