import pygame as py
# Função que desenha as paredes do jogo
class Wall(object):
    def __init__(self, pos, wall_type):
        self.rect = py.Rect(pos[0], pos[1], 40, 40)
        if wall_type == "0":
            self.image = py.image.load('imagens_pixel/wall.png')
        elif wall_type == "2":
            self.image = py.Surface((40, 40))
            self.image.fill((80, 76, 76))
        elif wall_type == ".":
            self.image = py.image.load('imagens_pixel/image.png')
        elif wall_type == "6":
            self.image = py.image.load('imagens_pixel/pc left.png')
        elif wall_type == "7":
            self.image = py.image.load('imagens_pixel/pc front.png')
        elif wall_type == "8":
            self.image = py.image.load('imagens_pixel/pc back.png')
        elif wall_type == "9":
            self.image = py.image.load('imagens_pixel/pc right.png')
        else:
            self.image = None
