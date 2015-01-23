import globs
from globs import * 
import pygame
import time
from pygame.locals import *

class Grid:
    def __init__(self, xy=[285,35], hw=[24,32], sq=22):
        self.size_w = hw[1]
        self.size_h = hw[0]
        self.square = sq
        self.cell_width =  self.square #int(self.size_w / 32)
        self.cell_height = self.square #int(self.size_h / 24)
        self.color = [233,111,100]
        self.active = False
        self.top = xy[1]
        self.bot = self.top + self.size_h * sq
        self.top_lines = []
        self.left_lines = []
        self.left = xy[0]
        self.list_2d = [[0] * hw[1] for i in range(hw[0])]
        self.right = self.left + self.size_w * sq
        for x in range(hw[1] + 1):
            self.top_lines.append([[x*sq + xy[0], self.top], [x*sq+xy[0], self.bot]])
        for y in range(hw[0]+ 1):
            self.left_lines.append([[self.left, y*sq+xy[1]], [self.right, y*sq + xy[1]]])
        self.lines = self.left_lines + self.top_lines
        self.list_2d[0][1] += 1
    def update(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
            if pygame.mouse.get_pressed(0)[0]:
                self.mousex, self.mousey = event.pos
                #self.cellx = self.mousexy[0] // self.rect_width
                self.cellx = int((self.mousex - self.left) / self.square)
                self.celly = int((self.mousey - self.top) / self.square)
                # print(self.mousex, self.mousey, self.celly, self.cellx)
                if (self.cellx < 0 or self.celly < 0):
                    pass
                elif (self.cellx >= self.size_w or self.celly >= self.size_h):
                    pass
                else:
                    self.list_2d[self.celly][self.cellx] = 1
            if pygame.mouse.get_pressed(0)[2]:
                self.mousex, self.mousey = event.pos
                self.cellx = int((self.mousex - self.left) / self.square)
                self.celly = int((self.mousey - self.top) / self.square)
                if (self.cellx < 0 or self.celly < 0):
                    pass
                elif (self.cellx >= self.size_w or self.celly >= self.size_h):
                    pass
                else:
                    self.list_2d[self.celly][self.cellx] = 0
    def draw(self, screen):
        self.rects = []
        for y, row in enumerate(self.list_2d):
            for x, val in enumerate(row):
                if val:
                    self.leftc = (x * self.square) + self.left
                    self.topc = (y * self.square) + self.top
                    self.rects.append([(pygame.Rect(self.leftc, self.topc, self.square, self.square)), [val*10, 255,0]])
        for rect in self.rects:
            pygame.draw.rect(screen, rect[1], rect[0])
        for line in self.left_lines:
            pygame.draw.line(screen, [100,100,100], line[0], line[1], 2)
        for i, line in enumerate(self.top_lines):
            if i % 4 > 0:
                pygame.draw.line(screen, [100,100,100], line[0], line[1], 2)
            else:
                pygame.draw.line(screen, [150,150,150], line[0], line[1], 2)
    def getPoints(self):
        output = []
        for i in range(len(self.list_2d[0])):
            for j in range(len(self.list_2d)):
                if self.list_2d[j][i]:
                    output.append([j,i])
        # for y, row in enumerate(self.list_2d):
        #     for x, val in enumerate(row):
        #         if val:
        #             output.append([y,x])
        return output