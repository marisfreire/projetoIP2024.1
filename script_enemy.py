# Módulo que contém as classes dos inimigos que serão implementados ao jogo
import pygame
import random


class enemy(object):
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = random.randint(0, 3)

def drawEnemy():
    pygame.draw.rect(self.tela, (255, 255, 102), (man.x, man.y, man.width, man.height))