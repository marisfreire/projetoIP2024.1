import pygame
import random


class Coletaveis(object):
    def __init__(self, tipo_coletavel, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30).move(5, 5)
        self.coletado = False

        self.tipo = tipo_coletavel
        if tipo_coletavel == 'cafe':
            self.image = pygame.image.load('imagens_pixel/cafezinho.png')
        elif tipo_coletavel == 'pasta':
            self.image = pygame.image.load('imagens_pixel/pasta.png')
        else:
            self.image = pygame.image.load('imagens_pixel/vida.png')

    def randomizar(self):
        from main import mapa

        # A posição do coletável deve mudar aleatoriamente
        def gerar_random_int():
            row_random = random.randint(0, 30)
            col_random = random.randint(0, 16)
            return row_random, col_random

        new_row, new_col = 0, 0

        while mapa[new_col][new_row] != '1':
            new_row, new_col = gerar_random_int()
            if mapa[new_col][new_row] == '1':
                # Deve colocar o coletável nessa nova posição
                return Coletaveis(self.tipo, (new_row * 40, 100 + new_col * 40))
