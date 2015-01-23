import sys
import globs
from globs import *
import pygame
from pygame.locals import *

class keyboard:
    def __init__(self, x=0, y=0, width=400, height=200):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = -1
        self.last_key = -1
        self.octave = 3
        self.rects = []
        self.rectColors = []
        for i in [1, 2, 4, 5, 6]:
            self.rectColors.append(BLACK)
            self.rects.append(pygame.Rect((self.x+self.width/8*i-15, self.y, self.width*30/400, self.height/2)))
        for i in range(7):
            self.rectColors.append(WHITE)
            self.rects.append(pygame.Rect((self.x + self.width/8*i, self.y, self.width/8-2, self.height)))
        self.rectColors.append(WHITE)
        self.rectColors.append(WHITE)
        self.rects.append(pygame.Rect((self.x + self.width*7/8, self.y + 1, self.width/8, self.height/2-2)))
        self.rects.append(pygame.Rect((self.x + self.width*7/8, self.y + self.height/2+1, self.width/8, self.height/2-2)))
    def get_octave_xy():
        pass
    def get_key(self, x, y):
        pointRect = pygame.Rect(x,y,1,1)
        return pointRect.collidelist(self.rects)
    def draw(self, screen):
        for i, rect in enumerate(reversed(self.rects)):
            rect_color = self.rectColors[len(self.rects)-i-1]
            if self.selected == len(self.rects)-i-1:
                rect_color = [233,111,000]
            pygame.draw.rect(screen, rect_color, rect)
        pygame.draw.polygon(screen, BLACK, ((self.x + self.width*15/16, self.y + self.height*3/16), (self.x + self.width*31/32, self.y + self.height*5/16), (self.x + self.width*29/32, self.y + self.height*5/16)))
        pygame.draw.polygon(screen, BLACK, ((self.x + self.width*15/16, self.y + self.height*13/16), (self.x + self.width*31/32, self.y + self.height*11/16), (self.x + self.width*29/32, self.y + self.height*11/16)))
    def update(self, event):
        if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            self.selected = self.get_key(mouseX, mouseY)
            index = [1, 3, 6, 8, 10, 0, 2, 4, 5, 7, 9, 11]
            mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)
            keyboardRect = pygame.Rect(self.x, self.y, self.width*7/8, self.height)
            if pygame.mouse.get_pressed(0)[0] and mouseRect.colliderect(keyboardRect) and self.selected < 12 and self.selected != self.last_key:
                d = {"selected":index[self.selected], "octave":self.octave}
                e = pygame.event.Event(KEYBOARD_EVENT, d)
                pygame.event.post(e)
                self.last_key = self.selected
        elif event.type == MOUSEBUTTONUP:
            mouseX, mouseY = event.pos
            self.last_key = -1
            mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)
            octaveUpRect = pygame.Rect(self.x + self.width*7/8, self.y, self.width/8, self.height/2)
            if mouseRect.colliderect(octaveUpRect):
                self.octave = min(7, self.octave+1)
            octaveDownRect = pygame.Rect(self.x + self.width*7/8, self.y+self.height/2, self.width/8, self.height/2)
            if mouseRect.colliderect(octaveDownRect):
                self.octave = max(0, self.octave-1)
            
            
            
            
            
            
            
