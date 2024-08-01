import pygame
import pygame as py
from config import *
from player import *
from monster import *

mapa = ["00000000400000000000000000000000",
        "01111110100011011101101111010110",
        "00010010111111111101101000010110",
        "01110010100000000111101000010100",
        "01111110101111100111111011111110",
        "01000110111111110000111000010000",
        "01101110101111111110101111311110",
        "00001010101111111010100000000010",
        "01111011101111100010101111111110",
        "00000000101131111010101000010010",
        "00000000101111111110111111111110",
        "01111100100000000110100111000010",
        "01001100111111111111110111111110",
        "01001111100100111111110100001110",
        "01111001100100111111110111111110",
        "01011001100100111111110110000010",
        "01011111111111110000011111311110",
        "00000000000000000000011000000000"]


# Função que determina se houve ou não uma colisão entre o player e algum inimigo
def check_collision(player, monster):
    return player[0].rect.colliderect(monster.rect)


# Função que desenha as paredes do jogo
class Wall(object):
    def __init__(self, pos):
        self.rect = py.Rect(pos[0], pos[1], 40, 40)
        self.image = py.image.load('wall.png')


class Jogo:
    def __init__(self):
        # Setup geral do jogo
        self.fonte = None
        py.init()
        self.tela = py.display.set_mode((largura, altura))  # tamanho da tela
        self.nome_oficial = 'CinEncontre'
        py.display.set_caption(self.nome_oficial)
        self.clock = py.time.Clock()

        self.clock.tick(FPS)

    def mensagem_tela(self, mensagem, pos_x, pos_y, cor, tam_fonte):
        self.fonte = pygame.font.Font(fonte_file, tam_fonte)
        msg = self.fonte.render(f'{mensagem}', True, cor)
        msg_rect = msg.get_rect(topleft=(pos_x, pos_y))
        self.tela.blit(msg, msg_rect)

    def menu(self, lista_walls, lista_player, lista_monsters):
        # Loop do jogo
        while True:
            key = py.key.get_pressed()
            self.tela.fill('white')
            self.mensagem_tela('CINCONTRE', 375, 20, 'Black', 100)

            self.mensagem_tela('Pressione ENTER para jogar', 150, 500, black, 70)
            pygame.display.update()

            if key[py.K_RETURN]:
                self.play(lista_walls, lista_player, lista_monsters)

            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    quit()

    def play(self, lista_walls, lista_player, lista_monsters):
        while True:
            # Desenho dos elementos: paredes, jogador e inimigos
            background = py.image.load('mapa_cincontre.png')
            self.tela.fill('white')
            self.tela.blit(background, (0, 100))

            # Player e uma lista de objetos Player()
            for jog in player:
                py.draw.rect(self.tela, 'purple', jog.rect)

            # Walls e uma lista de objetos Wall()
            for wall in walls:
                self.tela.blit(wall.image, wall.rect)

            # Monsters e uma lista de objetos Monster()
            for monster in monsters:
                py.draw.rect(self.tela, 'blue', monster.rect)
                monster.move()
                if check_collision(player, monster):  # Detecta as colisões entre os inimigos e os players
                    self.derrota()

            key = py.key.get_pressed()
            if key[py.K_LEFT] or key[py.K_a]:
                player[0].move(-2, 0)
            if key[py.K_RIGHT] or key[py.K_d]:
                player[0].move(2, 0)
            if (key[py.K_UP] or key[py.K_w]) and player[0].rect.top > 120:
                player[0].move(0, -2)
            if (key[py.K_DOWN] or key[py.K_s]) and player[0].rect.bottom < 770:
                player[0].move(0, 2)

            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    quit()
            pygame.display.update()

    def derrota(self):
        # tela de derrota
        while True:
            self.tela.fill(black)
            self.mensagem_tela("game over", 100, 300, white, 200)

            key = py.key.get_pressed()
            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    quit()
            pygame.display.update()


def mapa_jogo(mapa):
    walls = []
    player = []
    monsters = []

    # Análise da sequência de nível acima. 0 = parede, 3 = inimigo, 4 = player
    x = 0
    y = 100
    for row in mapa:
        for col in row:
            col = int(col)
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


walls, player, monsters = mapa_jogo(mapa)

if __name__ == '__main__':  # jogo só será iniciado a partir do arquivo main
    jogo = Jogo()
    jogo.menu(walls, player, monsters)
