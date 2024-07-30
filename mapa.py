import pygame
from player import *
from monster import *
# Criacao do mapa em nivel de jogo real

class Wall(object):
    def __init__(self, pos):
        self.rect(pos[0], pos[1], 40, 40)
        self.image = pygame.image.load('wall.png')

#player = 4
#parede = 0
#chao = 1
def mapa_jogo(mapa):
    walls = []
    player = []
    monsters = []

    #Parse the level string above. W = wall, F = exit, P = player
    x = y = 0
    for row in mapa[mapa]:
        for col in row:
            if col == 0:
                walls.append(Wall((x, y)))
            if col == 4:
                player.append(Player((x, y)))
            if col == 3:
                monsters.append(Monster((x, y)))
            x += 40
        y += 40
        x = 0
    return walls, player, monsters