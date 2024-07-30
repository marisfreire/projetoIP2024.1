import pygame as py
from config import *
from mapa import *


mapa = ["00000000400000000000000000000000",
        "01111110100011011101101111010110",
        "00010010111111111101101000010110",
        "01110010100000000111101000010100",
        "01111110101111100111111011111110",
        "01000110111111110000111000010000",
        "01101110101111111110101111111110",
        "00001010101111111010100000000010",
        "01111011101111100010101111111110",
        "00000000101111111010101000010010",
        "00000000101111111110111111111110",
        "01111100100000000110100111000010",
        "01001100111111111111110111111110",
        "01001111100100111111110100001110",
        "01111001100100111111110111111110",
        "01011001100100111111110110000010",
        "01011111111111110000011111111110",
        "00000000000000000000001100000000"]


class Jogo:
    def __init__(self):
        # Setup geral do jogo
        py.init()
        self.tela = py.display.set_mode((largura, altura))  # tamanho da tela
        self.nome_oficial = 'CinEncontre'
        self.nome = py.display.set_caption(self.nome_oficial)
        self.clock = py.time.Clock()


    def mostrar_tela(self):
        while True:
            key = py.key.get_pressed()
            
            if key[py.K_LEFT]:
                player.move(-2, 0)
            if key[py.K_RIGHT]:
                player.move(2, 0)
            if key[py.K_UP]:
                player.move(0, -2)
            if key[py.K_DOWN]:
                player.move(0, 2)
            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    py.quit()

            [teste, player, teste2] = mapa_jogo(mapa)
            rect_fundo = mapa.get_rect(topleft=(0, 100))
            self.tela.fill('white')
            self.tela.blit(mapa, rect_fundo)
            py.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':  # jogo só será iniciado a partir do arquivo main
    jogo = Jogo()
    jogo.mostrar_tela()
