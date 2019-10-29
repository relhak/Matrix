# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:19:19 2019

@author: Harold
"""

import sys
import pygame
from random import randint
from random import random

X = 720
Y = 640

black = (0, 0, 0)
green = (0, 255, 0)

pygame.init()
display = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Digital Rain')
font = pygame.font.SysFont('consolas',32)

display.fill(black)

class rain():
    black = (0, 0, 0)
    green = (0, 255, 0)
    
    def __init__(self,x):
        self.array = [str(0)]
        self.speed = (random() + 1 )/2
        self.y = 0 - 32
        self.y_a = 0 - 32
        self.x = x
        self.g_curr = randint(200,255)
        self.g_prev = self.g_curr
        self.length = randint(15,35)
        
    def updatePos(self):
        self.y_a += 7.5 * self.speed 
        
        if (self.y_a - self.y) >= 32:
            self.updateDrop()
            self.y = self.y + 32
        
        if int(self.y_a - self.y) % 2 == 0:
            self.array[0] = str(randint(0,9))
        
        if self.y_a > Y + 32 * self.length :
            self.array = [str(0)]
            self.y_a = 0 - 32
            self.y = self.y_a
            self.speed = (random() + 1)/2
    
    def updateDrop(self):
        if len(self.array)<self.length :
            self.array.insert(1,self.array[0])
            
        if len(self.array)>=self.length :
            self.array.pop(-1)
            
        if len(self.array)>15:
            if randint(0,10) <= 3:
                self.array[randint(0,8)] = str(' ')
        
    def draw(self):
        offset = 0
        for c in self.array:
            if offset == 0:
                v = 255
                g = v
                r = v
                b = v 
            else:
                g = self.g_prev - (offset / 32 + 2) / self.length * self.g_prev
                r = 0
                b = 0
            
            s = font.render(c, True, (r,g,b), black)
            display.blit(s, (self.x,self.y-offset))
            offset += 32   
            

def storm():
    drops = []
    for j in range(0,40):
        drops.append(rain(18*j))
    return drops
 
storm = storm()        

while True: # main game loop
    for drop in storm:
        drop.updatePos()
        drop.draw()
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()


        


