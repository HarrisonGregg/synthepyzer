import pygame
from pygame.locals import *
import globs
from globs import *

class Button:
    def __init__(self, x, y, width=30, height=100, text="", id="", fontsize = 30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.id = id
        self.depressed = False
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        self.myfont = pygame.font.SysFont("Arial", fontsize)
        self.text_surface = self.myfont.render(self.text, 1, BLACK)
    def change_text(self, text):
        self.text = text
        self.text_surface = self.myfont.render(self.text, 1, BLACK)
    def draw(self, screen):
        text_surface = self.myfont.render(self.text, True, BLACK)
        text_width, text_height = self.myfont.size(self.text)
        if self.depressed:
            pygame.draw.rect(screen, BLACK, self.rectangle)
            shifted_rect = pygame.Rect(self.x+1, self.y+1, self.width, self.height)
            pygame.draw.rect(screen, GREY, shifted_rect)
            screen.blit(self.text_surface, (self.x+self.width/2-text_width/2+1, self.y+self.height/2-text_height/2+1))
        else:
            # pygame.draw.rect(screen, , self.rectangle)
            screen.blit(self.text_surface, (self.x+self.width/2-text_width/2, self.y+self.height/2-text_height/2))
    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            mouse_rect = pygame.Rect(mousex, mousey, 1, 1)
            if mouse_rect.colliderect(self.rectangle):
                self.depressed = True    
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouse_rect = pygame.Rect(mousex, mousey, 1, 1)
            if mouse_rect.colliderect(self.rectangle) and self.depressed:
                d = {"depressed":self.depressed, "text":self.text, "id":self.id}
                e = pygame.event.Event(BUTTON_DEPRESSED, d)
                pygame.event.post(e)
            self.depressed = False    
