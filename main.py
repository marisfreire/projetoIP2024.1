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
        "01mn1122111111111111112111111110",
        "01op1111122122111111112122221110",
        "01111mn1122122111111112111111110",
        "03211op1122122111111112112222210",
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

        self.soundtrack = pygame.mixer.Sound('music/jazzyfrenchy.mp3')
        self.botao_sound = pygame.mixer.Sound('music/botao.mp3')
        self.botao_sound.set_volume(0.4)

        self.clock = py.time.Clock()
        self.clock.tick(FPS)

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
        time_seg = 30
        lista_imagens = ['imagens_pixel/heart.png', 'imagens_pixel/heart.png', 'imagens_pixel/heart.png']
        lista_imagens_puzzle = ['puzzle/Hello-World-1.png',
                                'puzzle/Hello-World-2.png',
                                'puzzle/Hello-World-3.png',
                                'puzzle/Hello-World-4.png',
                                'puzzle/Hello-World-5.png']
        cont = 0
        piscar = False
        qtde_coletaveis = {"cafe": 4, "pasta": 4, "vida": 1}
        dano.clear()  # Limpa a lista de danos para reiniciar as vidas
        lista_player[0].reset_position()  # Implementar o método reset_position() na classe Player
        lista_player[0].speed = 2
        for monster in lista_monsters:
            monster.reset_position()

        self.soundtrack.play(-1)
        self.soundtrack.set_volume(0.3)
        opacidade = 0
        while True:

            # Atualiza o temporizador de invencibilidade
            if opacidade == 255:
                opacidade = 0
            else:
                opacidade = 255
            if invincible_timer > 0:
                invincible_timer -= 1
            if 1 <= invincible_timer <= 30:
                lista_player[0].image.set_alpha(opacidade)
            else:
                lista_player[0].image.set_alpha(255)

            # Contador
            if seg > 0:
                seg -= 1

            # Desenho do background
            background = py.image.load('mapa_cincontre.png')
            self.tela.fill('white')
            self.tela.blit(background, (0, 100))

            desenhar_coracoes(self, lista_imagens)
            desenhar_puzzle(self, lista_imagens_puzzle, cont)

            if seg % 60 == 0:  # Significa que passaram-se 60 frames, ou seja, um segundo
                time_seg -= 1

            self.fonte = py.font.Font(fonte_upheav, 100)

            if time_seg < 10:
                if seg % 15 == 0:
                    if piscar:
                        piscar = False
                    else:
                        piscar = True

                    if piscar:
                        cor = red_time
                    else:
                        cor = black

                text_timer = self.fonte.render(f'00:0{time_seg}', True, cor)
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
                        lista_imagens[2] = 'imagens_pixel/heart.png'
                    else:
                        lista_imagens[1] = 'imagens_pixel/heart.png'
                    qtde_coletaveis['vida'] += 1
                    dano.pop(-1)

            # Desenho das pastas
            novos_coletaveis(self, lista_pasta, 'pasta', player, qtde_coletaveis)
            if qtde_coletaveis['pasta'] == 0:

                self.vitoria(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
            elif qtde_coletaveis['pasta'] == 3:
                cont = 1
            elif qtde_coletaveis['pasta'] == 2:
                cont = 2
            elif qtde_coletaveis['pasta'] == 1:
                cont = 3

            # Monsters e uma lista de objetos Monster()
            for monster in monsters:
                self.tela.blit(monster.image, monster.rect)
                monster.move()
                if check_collision(player[0], monster) and invincible_timer == 0:  # Detecta as colisões entre os
                    # inimigos e os players
                    dano.append('dano')
                    invincible_timer = 30  # 30 frames = 0.5 segundo de invicibilidade

                    # efeito sonoro
                    tomou_dano = pygame.mixer.Sound('music/monstro.mp3')
                    tomou_dano.play(0)
                    tomou_dano.set_volume(0.3)

                    # efeito visual
                    if len(dano) == 1:
                        desenhar_coracoes(self, lista_imagens)
                        lista_imagens[2] = 'imagens_pixel/damage.png'

                    elif len(dano) == 2:
                        desenhar_coracoes(self, lista_imagens)
                        lista_imagens[1] = 'imagens_pixel/damage.png'

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

            fonte = gerar_fonte(fonte_upheav, 60)
            text = fonte.render('JOGAR', True, black)
            largura_text = text.get_width()
            altura_text = text.get_height()

            x, y = centralizar(text)
            y += 300
            play_button = py.draw.rect(self.tela, white, (x - 10, y + 20, largura_text + 20, altura_text + 20), 0, 5)
            play_rect = text.get_rect(topleft=(x, y + 25))
            self.tela.blit(text, play_rect)

            for event in py.event.get():
                if event.type == py.QUIT:
                    quit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:  # Reinicia o jogo ao pressionar Enter
                        self.play(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                if event.type == py.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        self.botao_sound.play(0)
                        self.play(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)

            pygame.display.update()

    def derrota(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        # tela de derrota
        self.soundtrack.stop()
        falhou = pygame.mixer.Sound('music/fail.mp3')
        falhou.play(0, 0, 200)
        falhou.set_volume(0.3)
        while True:

            # Imagem de fundo

            reinicio_button, sair_button = botoes(self)
            for event in py.event.get():
                if event.type == py.QUIT:
                    quit()

                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        self.botao_sound.play(0)
                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                    if event.key == py.K_ESCAPE:  # Sai do jogo ao pressionar Escape
                        quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reinicio_button.collidepoint(event.pos):
                        self.botao_sound.play(0)
                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                    if sair_button.collidepoint(event.pos):
                        self.botao_sound.play(0)
                        quit()

            # Título
            desenhar_derrota(self, self.tempo_esgotado)

            pygame.display.update()

    # tela de vitoria
    def vitoria(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida):
        self.soundtrack.stop()
        vitoria_sound = pygame.mixer.Sound('music/vitoria.mp3')
        vitoria_sound.play(0)
        vitoria_sound.set_volume(0.5)
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
                        self.botao_sound.play(0)

                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta, lista_vida)
                    if sair_button.collidepoint(event.pos):
                        self.botao_sound.play(0)
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
            if col in ['0', '2', '6', '7', '8', '9', '.','m','n','o','p']:
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
