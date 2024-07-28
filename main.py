import pygame as py
from config import *


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

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()

            mapa = py.image.load('mapa_cincontre.png')
            rect_fundo = mapa.get_rect(topleft=(0, 100))
            self.tela.fill('white')
            self.tela.blit(mapa, rect_fundo)
            py.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':  # jogo só será iniciado a partir do arquivo main
    jogo = Jogo()
    jogo.mostrar_tela()
