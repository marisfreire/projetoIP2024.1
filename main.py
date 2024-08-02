import pygame
import pygame as py
from config import *
from player import *
from monster import *
from coletaveis import *
from collision import check_collision
mapa = [".000000040000000000000000000000.",
        "01111112100011111121121111212110",
        "07717712111111111121121211212110",
        "01118812122222222111121222212120",
        "011111,2121111122111111211111110",
        "01777112111111112222111222212220",
        "01191112121111111112121111311110",
        "08881612121111111212122222222210",
        "01111611121111122212121111111110",
        "02222221121131111212121222212210",
        "022222221211111#1112111111111110",
        "01111122122222222112122111222210",
        "01001122111111111111112111111110",
        "01001111122122111111112122221110",
        "01111001122122111111112111111110",
        "01211001122122111111112112222210",
        "0121#111111111112222211111311110",
        ".000000000000000000001100000000."]



# Função que desenha as paredes do jogo
class Wall(object):
    def __init__(self, pos, wall_type):
        self.rect = py.Rect(pos[0], pos[1], 40, 40)
        if wall_type == "0":
            self.image = py.image.load('wall.png')
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

    def menu(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta):
        # Loop do jogo
        while True:
            key = py.key.get_pressed()
            self.tela.fill('white')
            self.mensagem_tela('CINCONTRE', 375, 20, 'Black', 100)

            self.mensagem_tela('Pressione ENTER para jogar', 150, 500, black, 70)
            pygame.display.update()

            if key[py.K_RETURN]:
                self.play(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta)

            for event in py.event.get():
                if event.type == py.QUIT or key[py.K_ESCAPE]:
                    quit()

    def play(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta):
        invincible_timer = 0  # Inicializa o temporizador de invencibilidade
        seg = 45 * 60
        time_seg = 45
        lista_imagens = ['heart.png', 'heart.png', 'heart.png']
        while True:
            # Atualiza o temporizador de invencibilidade
            if invincible_timer > 0:
                invincible_timer -= 1
            
            if seg > 0:
                seg -= 1

            # Desenho dos elementos: paredes, jogador e inimigos
            background = py.image.load('mapa_cincontre.png')
            self.tela.fill('white')
            self.tela.blit(background, (0, 100))

            xaxis = 0
            image = 0
            for i in range(3):
                self.rect = py.Rect(40 + xaxis, 40, 40, 40)
                self.image = py.image.load(lista_imagens[image])
                self.tela.blit(self.image, self.rect)
                image += 1
                xaxis += 40

            
            if seg % 60 == 0: # Significa que passaram-se 60 frames, ou seja, um segundo
                time_seg -= 1
            
            if time_seg < 10:
                text_timer = self.fonte.render(f'00:0{time_seg}', True, black)
            else:
                text_timer = self.fonte.render(f'00:{time_seg}', True, black)          
            timer_rect = text_timer.get_rect(topleft=(800,30))
            self.tela.blit(text_timer, timer_rect)

            if time_seg == 0:
                self.derrota(lista_walls, lista_player, lista_monsters)

            # Player e uma lista de objetos Player()
            for jog in player:
                # MUDAR ISSO AQUI PARA
                # self.tela.blit(jog.image, jog.rect)
                py.draw.rect(self.tela, 'purple', jog.rect)

            # Walls e uma lista de objetos Wall()
            for wall in walls:
                self.tela.blit(wall.image, wall.rect)

            # Desenho dos cafes
            
            for elemento in lista_cafe:
                
                if check_collision(elemento, player[0]):
                    elemento.coletado = True
                    if elemento.coletaveis['cafe'] > 0:
                        lista_cafe.append(elemento.randomizar())
                        elemento.decrease('cafe')
                    # Aumentar a velocidade do player quando é coletado
                
                if not elemento.coletado:
                    self.tela.blit(elemento.image, elemento.rect)


            for elemento in lista_pasta:

                if check_collision(elemento, player[0]):
                    elemento.coletado = True
                    if elemento.coletaveis['pasta'] > 0:
                        lista_cafe.append(elemento.randomizar())
                        elemento.decrease('pasta')
                    # else:
                       # vitoria()
                
                if not elemento.coletado:
                    self.tela.blit(elemento.image, elemento.rect)




            # Monsters e uma lista de objetos Monster()
            for monster in monsters:
                # MUDAR ISSO AQUI PARA
                # self.tela.blit(monster.image, monster.rect)
                py.draw.rect(self.tela, 'blue', monster.rect)
                monster.move()
                if check_collision(player[0], monster) and invincible_timer == 0:  # Detecta as colisões entre os inimigos e os players
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

    def derrota(self, lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta):
        # tela de derrota
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    quit()
                    
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:  # Reinicia o jogo ao pressionar Enter
                        self.menu(lista_walls, lista_player, lista_monsters, lista_cafe, lista_pasta)
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
    cafe = []
    pasta = []

    # Análise da sequência de nível acima. 0 = parede, 3 = inimigo, 4 = player, # = cafe, , = pasta
    for row in mapa:
        for col in row:
            if col in ['0','2','6','7','8','9','.']:
                walls.append(Wall((x, y), col))
            if col == '4':
                player.append(Player((x, y)))
            if col == '3':
                monsters.append(Monster((x, y)))
            if col == '#':
                cafe.append(Coletaveis('cafe',(x,y)))
            if col == ',':
                pasta.append(Coletaveis('pasta', (x,y)))
            x += 40
        y += 40
        x = 0
    return walls, player, monsters, cafe, pasta


walls, player, monsters, cafe, pasta = mapa_jogo(mapa)



if __name__ == '__main__':  # jogo só será iniciado a partir do arquivo main
    jogo = Jogo()
    jogo.menu(walls, player, monsters, cafe, pasta)
