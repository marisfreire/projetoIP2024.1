import random
import pygame
from mapa import walls

class Monster(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
        self.direction = random.randint(1,4)
        self.dist = 3
        #self.moves = random.randint(100,200)
        #self.moveCount = 0

    def move(self, x, y):
        xMove, yMove = 0,0

        if self.direction == 1:
            xMove = -self.dist
        elif self.direction == 2:
            yMove = -self.dist
        elif self.direction == 3:
            xMove = self.dist
        elif self.direction == 4:
            yMove = self.dist

        self.rect.move_ip(xMove, yMove)
        #self.moveCount += 1

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x > 0: #Moving right, hit the left side of wall
                    self.rect.right = wall.rect.left
                if x < 0: #Moving left, hit the right side of wall
                    self.rect.left = wall.rect.right
                if y > 0: #Moving down, hit the top side of wall
                    self.rect.bottom = wall.rect.top
                if y < 0: #Moving up, hit the bottom side of wall
                    self.rect.top = wall.rect.bottom
                self.rect.move_ip(-xMove, -yMove)
                self.direction = random.randint(1,4)
