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


dano = []
morreu = False
lista_imagens = ['heart.png', 'heart.png', 'heart.png']

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
        # Reiniciando variáveis
        global morreu
        morreu = False # Reiniciando
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
        invincible_timer = 0  # Inicializa o temporizador de invencibilidade
        while True:
            # Atualiza o temporizador de invencibilidade
            if invincible_timer > 0:
                invincible_timer -= 1

            # Desenho dos elementos: paredes, jogador e inimigos
            background = py.image.load('mapa_cincontre.png')
            self.tela.fill('white')
            self.tela.blit(background, (0, 100))

            xaxis = 0
            image = 0
            for i in range(3):
                self.rect = py.Rect(40 + xaxis, 20, 40, 40)
                self.image = py.image.load(lista_imagens[image])
                self.tela.blit(self.image, self.rect)
                image += 1
                xaxis += 40


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
                if check_collision(player, monster) and invincible_timer == 0:  # Detecta as colisões entre os inimigos e os players
                    dano.append('dano')
                    invincible_timer = 30 # 60 frames = 1 segundo de invicibilidade
                    if len(dano) == 1:
                        xaxis = 0
                        image = 0
                        lista_imagens[2] = 'damage.png'
                        for i in range(3):
                            self.rect = py.Rect(40 + xaxis, 20, 40, 40)
                            self.image = py.image.load(lista_imagens[image])
                            self.tela.blit(self.image, self.rect)
                            xaxis += 40
                            image += 1
                    elif len(dano) == 2:
                        xaxis = 0
                        image = 0
                        lista_imagens[1] = 'damage.png'
                        for i in range(3):
                            self.rect = py.Rect(40 + xaxis, 20, 40, 40)
                            self.image = py.image.load(lista_imagens[image])
                            self.tela.blit(self.image, self.rect)
                            xaxis += 40
                            image += 1

        

                    if len(dano) == 3:
                        self.morreu = True
                        self.derrota(lista_walls, lista_player, lista_monsters)
                        

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

    def derrota(self, lista_walls, lista_player, lista_monsters):
        # tela de derrota
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    quit()
                    
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:  # Reinicia o jogo ao pressionar Enter
                        self.menu(lista_walls, lista_player, lista_monsters)
                        # Sai da tela de derrota e retorna ao loop principal
                        #colocar para voltar para a tela inicial 
                    if event.key == py.K_ESCAPE:  # Sai do jogo ao pressionar Escape
                        quit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reinicio_button.collidepoint(event.pos):
                            self.menu(lista_walls, lista_player, lista_monsters)
                    if tela_inicial_button.collidepoint(event.pos):
                            quit()

            # Imagem de fundo
            background = py.Surface(self.tela.get_size())
            background.fill('black')
            self.tela.blit(background, (0, 0))

            # Desenhar o retângulo verde diretamente na tela
            reinicio_button = pygame.draw.rect(self.tela, '#307225', (280, 480, 250, 100))
            #fonte = pygame.font.Font(None, 30)
            #reinicio_text = fonte.render(f'{'PLAY AGAIN'}',True,'red')
            #self.tela.blit(reinicio_text, reinicio_button)


            tela_inicial_button = pygame.draw.rect(self.tela, '#a93535', (750, 480, 250, 100)) #(x,y (do canto superior do retangulo), width, height)
            #fonte = pygame.font.Font(None, 30)
            #tela_inicial_text = fonte.render(f'{'TELA INICIAL'}',True,'green')
            #self.tela.blit(tela_inicial_text, tela_inicial_button)

        
            # Título
            self.mensagem_tela('GAME OVER', 375, 120, '#ffffff', 100)
                    
            self.mensagem_tela(
                'Poxaaa...Infelizmente você perdeu seu crachá',
                640, 270, 'White', 40
            )

            self.mensagem_tela(
                'Pressione ENTER para reiniciar ou ESC para sair',
                640, 400, 'White', 30
            )
            pygame.display.update()


def mapa_jogo(mapa, x=0, y=100):
    walls = []
    player = []
    monsters = []

    # Análise da sequência de nível acima. 0 = parede, 3 = inimigo, 4 = player
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
