import pygame as py
from config import *
from player import *
from monster import *
from coletaveis import *
from collision import check_collision
from wall import *
from funcoes_auxiliares import *
import random

mapa = [".000000040000000000000000000000.",
        "01111112100011111121121111212110",
        "07717712111111111121121211212110",
        "01118812122222222111121222212120",
        "011111,2121111122111111211111110",
        "03777112111111112222111222212220",
        "01191112121111111112121111311110",
        "08881612121151111212122222222210",
        "01111611121111122212121111111110",
        "02222222121131111212121222212210",
        "022222221211111#1112111111111110",
        "01111122122222222112122111222210",
        "01001122111111111111112111111110",
        "01001111122122111111112122221110",
        "01111001122122111111112111111110",
        "03211001122122111111112112222210",
        "0121#111111111112222211111311110",
        ".000000000000000000001100000000."]

dano = []
morreu = False

codigos = ['print(Hello World)', 'def f(x): return x + 1', 'minha_tupla = (2, 3)',
           'for i in range(2) : print(f"Bem vindo!")']


class Jogo:
    def __init__(self):
        # Setup geral do jogo
        self.fonte = None
        py.init()
        self.tela = py.display.set_mode((largura, altura))  # tamanho da tela
        self.nome_oficial = 'Cincontre'
        py.display.set_caption(self.nome_oficial)

        self.li_instrucoes = False
        self.tempo_esgotado = False

        self.clock = py.time.Clock()
        self.clock.tick(FPS)

    def mensagem_tela(self, mensagem, pos_x, pos_y, cor, tam_fonte):
        self.fonte = pygame.font.Font(fonte_upheav, tam_fonte)
        msg = self.fonte.render(f'{mensagem}', True, cor)
        msg_rect = msg.get_rect(topleft=(pos_x, pos_y))
        self.tela.blit(msg, msg_rect)

    def menu(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        # Loop do jogo
        while True:
            key = py.key.get_pressed()
            self.fonte = gerar_fonte(fonte_upheav, 100)
            desenhar_menu(self)

            pygame.display.update()

            if key[py.K_RETURN]:
                if not self.li_instrucoes:
                    self.instrucao(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                else:
                    self.play(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)

            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    quit()

    def play(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        invincible_timer = 0  # Inicializa o temporizador de invencibilidade
        seg = 45 * 60
        time_seg = 45
        lista_imagens = ['heart.png', 'heart.png', 'heart.png']
        random_index = random.randint(0, len(codigos) - 1)
        puzzle_elemento = codigos[random_index]

        qtde_coletaveis = {"cafe": 4, "pasta": 4, "vida": 1}
        dano.clear()  # Limpa a lista de danos para reiniciar as vidas
        lista_player[0].reset_position()  # Implementar o método reset_position() na classe Player
        lista_player[0].speed = 2
        for monster in lista_monsters:
            monster.reset_position()

        while True:
            # Atualiza o temporizador de invencibilidade
            if invincible_timer > 0:
                invincible_timer -= 1

            # Contador
            if seg > 0:
                seg -= 1

            # Desenho do background
            background = py.image.load('mapa_cincontre.png')
            self.tela.fill('white')
            self.tela.blit(background, (0, 100))

            desenhar_coracoes(self, lista_imagens)

            if seg % 60 == 0:  # Significa que passaram-se 60 frames, ou seja, um segundo
                time_seg -= 1

            self.fonte = py.font.Font(fonte_upheav, 100)
            if time_seg < 10:
                text_timer = self.fonte.render(f'00:0{time_seg}', True, black)
            else:
                text_timer = self.fonte.render(f'00:{time_seg}', True, black)
            timer_rect = text_timer.get_rect(topleft=(980, 2))
            self.tela.blit(text_timer, timer_rect)

            if time_seg == 0:
                self.tempo_esgotado = True
                self.derrota(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)

            # Player e uma lista de objetos Player()
            for jog in player:
                self.tela.blit(jog.image, jog.rect)

            # Walls e uma lista de objetos Wall()
            for wall in walls:
                self.tela.blit(wall.image, wall.rect)

            # Desenho dos cafés
            novos_coletaveis(self, lista_cafe, 'cafe', player, qtde_coletaveis)

            if len(dano) != 0:
                novos_coletaveis(self, lista_vida, 'vida', player, qtde_coletaveis)
                if qtde_coletaveis['vida'] == 0:
                    if len(dano) == 1:
                        lista_imagens[2] = 'heart.png'
                    else:
                        lista_imagens[1] = 'heart.png'
                    qtde_coletaveis['vida'] += 1
                    dano.pop(-1)

            # Desenho das pastas
            novos_coletaveis(self, lista_pasta, 'pasta', player, qtde_coletaveis)
            if qtde_coletaveis['pasta'] == 0:
                self.vitoria(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)

            # Monsters e uma lista de objetos Monster()
            for monster in monsters:
                self.tela.blit(monster.image, monster.rect)
                monster.move()
                if check_collision(player[0], monster) and invincible_timer == 0:  # Detecta as colisões entre os
                    # inimigos e os players
                    dano.append('dano')
                    invincible_timer = 30  # 60 frames = 1 segundo de invicibilidade
                    if len(dano) == 1:
                        desenhar_coracoes(self, lista_imagens)
                        lista_imagens[2] = 'damage.png'

                    elif len(dano) == 2:
                        desenhar_coracoes(self, lista_imagens)
                        lista_imagens[1] = 'damage.png'

                    if len(dano) == 3:
                        self.derrota(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)

            key = py.key.get_pressed()
            if key[py.K_LEFT] or key[py.K_a]:
                player[0].move(-2, 0)
            if key[py.K_RIGHT] or key[py.K_d]:
                player[0].move(2, 0)
            if (key[py.K_UP] or key[py.K_w]) and player[0].rect.top > 120:
                player[0].move(0, -2)
            if (key[py.K_DOWN] or key[py.K_s]) and player[0].rect.bottom < 780:
                player[0].move(0, 2)

            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    quit()
            pygame.display.update()

    def instrucao(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        # Tela de instruções
        while True:

            self.li_instrucoes = desenhar_instrucoes(self)

            for event in py.event.get():
                if event.type == py.QUIT:
                    quit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:  # Reinicia o jogo ao pressionar Enter
                        self.play(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)

            pygame.display.update()

    def derrota(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        # tela de derrota
        while True:

            # Imagem de fundo

            reinicio_button, sair_button = botoes(self)
            for event in py.event.get():
                if event.type == py.QUIT:
                    quit()

                if event.type == py.KEYDOWN:

                    if event.key == py.K_ESCAPE:  # Sai do jogo ao pressionar Escape
                        quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reinicio_button.collidepoint(event.pos):
                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                    if sair_button.collidepoint(event.pos):
                        quit()

            # Título
            desenhar_derrota(self, self.tempo_esgotado)

            pygame.display.update()

    # tela de vitoria
    def vitoria(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        while True:
            # Desenho da tela
            reinicio_button, sair_button = botoes(self)
            # Títulos e mensagens
            desenhar_vitoria(self)

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                        return
                    if event.key == py.K_ESCAPE:
                        py.quit()
                        quit()

                if event.type == py.MOUSEBUTTONDOWN:
                    if reinicio_button.collidepoint(event.pos):
                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                        return
                    if sair_button.collidepoint(event.pos):
                        py.quit()
                        quit()
            py.display.update()


def mapa_jogo(elemento_mapa, x=0, y=100):
    lista_walls = []
    lista_player = []
    lista_monsters = []
    lista_cafe = []
    lista_pasta = []
    lista_vida = []

    # Análise da sequência de nível acima. 0 = parede, 3 = inimigo, 4 = player, # = cafe, , = pasta
    for row in elemento_mapa:
        for col in row:
            if col in ['0', '2', '6', '7', '8', '9', '.']:
                lista_walls.append(Wall((x, y), col))
            if col == '4':
                lista_player.append(Player((x, y)))
            if col == '3':
                lista_monsters.append(Monster((x, y)))
            if col == '#':
                lista_cafe.append(Coletaveis('cafe', (x, y)))
            if col == ',':
                lista_pasta.append(Coletaveis('pasta', (x, y)))
            if col == '5':
                lista_vida.append(Coletaveis('vida', (x, y)))
            x += 40
        y += 40
        x = 0
    return lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida


walls, player, monsters, cafe, pasta, vida = mapa_jogo(mapa)

if __name__ == '__main__':  # jogo só será iniciado a partir do arquivo main
    jogo = Jogo()
    jogo.menu(walls, player, monsters, cafe, pasta, vida)
