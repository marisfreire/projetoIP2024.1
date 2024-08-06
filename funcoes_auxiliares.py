import pygame as py
from collision import check_collision
from config import *


def centralizar(surface):
    pos_x = (largura - (surface.get_width())) / 2
    pos_y = (altura - (surface.get_height())) / 2

    return pos_x, pos_y


def gerar_fonte(fonte, tamanho):
    return py.font.Font(fonte, tamanho)


def desenhar_menu(objeto):
    objeto.tela.fill('#c83333')
    fonte_titulo = gerar_fonte(fonte_upheav, 210)
    fonte_subtitulo = gerar_fonte(fonte_2, 30)

    surface_titulo = fonte_titulo.render('CINCONTRE', True, white)
    pos_x_titulo, pos_y_titulo = centralizar(surface_titulo)
    titulo_rect = surface_titulo.get_rect(topleft=(pos_x_titulo, pos_y_titulo - 50))

    objeto.tela.blit(surface_titulo, titulo_rect)

    surface_subtitulo = fonte_subtitulo.render('Pressione ENTER para iniciar um novo jogo', True, white)
    pos_x_subtitulo, pos_y_subtitulo = centralizar(surface_subtitulo)
    subtitulo_rect = surface_subtitulo.get_rect(topleft=(pos_x_subtitulo, pos_y_subtitulo + 50))

    objeto.tela.blit(surface_subtitulo, subtitulo_rect)


def desenhar_instrucoes(objeto):
    objeto.tela.fill('#c83333')

    fonte_titulo = gerar_fonte(fonte_upheav, 150)
    surface_titulo = fonte_titulo.render('Parabéns!', True, white)
    pos_x_titulo, pos_y_titulo = centralizar(surface_titulo)
    titulo_rect = surface_titulo.get_rect(topleft=(pos_x_titulo, pos_y_titulo - 270))

    objeto.tela.blit(surface_titulo, titulo_rect)

    # Paragrafo

    paragrafo = ['Passar no Cin é um grande feito! Será que você consegue Cincontrar?',
                 'Encontre todos os arquivos necessários para completar ', 'seu código antes que o tempo acabe!',
                 'Desvie da procrastinação e não deixe seu crachá desaparecer!',
                 'Use o café para ganhar energia e superar os desafios',
                 'Boa sorte!', 'Complete seu código e prove que você', 'pode vencer a Procrastinação!']

    gap = 190
    tam_paragrafo = 25
    for elemento in paragrafo:
        fonte_paragrafo = gerar_fonte(fonte_2, tam_paragrafo)

        if paragrafo.index(elemento) >= 5:
            fonte_paragrafo.set_bold(True)

        surface_paragrafo = fonte_paragrafo.render(elemento,
                                                   True, white)
        pos_x_paragrafo, pos_y_paragrafo = centralizar(surface_paragrafo)

        paragrafo_rect = surface_paragrafo.get_rect(topleft=(pos_x_paragrafo, pos_y_paragrafo - gap))

        objeto.tela.blit(surface_paragrafo, paragrafo_rect)
        if paragrafo.index(elemento) == 0:
            gap -= 150
        elif paragrafo.index(elemento) == 4:
            gap -= 80
            tam_paragrafo += 5
        else:
            gap -= 40

    return True

def desenhar_derrota(objeto, tempo_esgotado):
    fonte = gerar_fonte(fonte_upheav, 220)
    surface_titulo = fonte.render('GAME OVER', True, white)
    pos_x_titulo, pos_y_titulo = centralizar(surface_titulo)
    titulo_rect = surface_titulo.get_rect(topleft=(pos_x_titulo, pos_y_titulo - 210))

    objeto.tela.blit(surface_titulo, titulo_rect)

    fonte2 = gerar_fonte(fonte_2, 24)

    if tempo_esgotado:
        mensagem = 'Poxaaaa.. parece que você ficou sem tempo e perdeu seu crachá!'
    else:
        mensagem = 'A procrastinação te dominou! Você não conseguiu entregar o código!'

    surface_subtitulo = fonte2.render(mensagem, True, white)
    pos_x_subtitulo, pos_y_subtitulo = centralizar(surface_subtitulo)
    subtitulo_rect = surface_subtitulo.get_rect(topleft=(pos_x_subtitulo, pos_y_subtitulo))

    objeto.tela.blit(surface_subtitulo, subtitulo_rect)


def desenhar_vitoria(objeto):
    fonte_titulo = gerar_fonte(fonte_upheav, 200)
    surface_titulo = fonte_titulo.render('VITÓRIA !', True, white)
    pos_x_titulo, pos_y_titulo = centralizar(surface_titulo)
    titulo_rect = surface_titulo.get_rect(topleft=(pos_x_titulo, pos_y_titulo - 230))
    objeto.tela.blit(surface_titulo,titulo_rect)

    fonte_subtitulo = gerar_fonte(fonte_2, 30)
    surface_subtitulo1 = fonte_subtitulo.render('Parabéns! Você entregou o código a tempo!', True, white)
    pos_x_subtitulo1, pos_y_subtitulo1 = centralizar(surface_subtitulo1)
    subtitulo1_rect = surface_titulo.get_rect(topleft=(pos_x_subtitulo1, pos_y_subtitulo1 - 50))
    objeto.tela.blit(surface_subtitulo1, subtitulo1_rect)

    surface_subtitulo2 = fonte_subtitulo.render(
        'Agora você mostrou que pegou o ritmo do Cin!', True, white)
    pos_x_subtitulo2, pos_y_subtitulo2 = centralizar(surface_subtitulo2)
    subtitulo2_rect = surface_titulo.get_rect(topleft=(pos_x_subtitulo2, pos_y_subtitulo2))
    objeto.tela.blit(surface_subtitulo2, subtitulo2_rect)

    fonte_subtitulo.set_bold(True)
    surface_subtitulo3 = fonte_subtitulo.render(
        ' Boa sorte nas próximas aventuras!', True, white)
    pos_x_subtitulo3, pos_y_subtitulo3 = centralizar(surface_subtitulo3)
    subtitulo3_rect = surface_titulo.get_rect(topleft=(pos_x_subtitulo3, pos_y_subtitulo3 + 50))
    objeto.tela.blit(surface_subtitulo3, subtitulo3_rect)

def desenhar_coracoes(objeto, lista_imagens):
    x = 0
    img = 0
    for y in range(3):
        rect = py.Rect(40 + x, 40, 40, 40)
        image = py.image.load(lista_imagens[img])
        objeto.tela.blit(image, rect)
        x += 45
        img += 1


def novos_coletaveis(objeto, lista_coletaveis, item, player, qtde_coletaveis):
    novos_itens = []
    for e in lista_coletaveis:
        if check_collision(e, player[0]):
            if not e.coletado:
                e.coletado = True
                if qtde_coletaveis[item] > 0:
                    qtde_coletaveis[item] -= 1
                    novos_itens.append(e.randomizar())  # Adiciona novo item à lista temporária
                if e.tipo == 'cafe':
                    acelerar(player[0])

        if not e.coletado and qtde_coletaveis[item] > 0:
            objeto.tela.blit(e.image, e.rect)

    # Adicionar novos itens à lista original
    lista_coletaveis.extend(novos_itens)


def botoes(objeto):

    background = py.image.load("mapa_cincontre.png")
    background = py.transform.scale(background, (1280, 820))
    objeto.tela.blit(background, (0, 0))

    # Criar uma superfície preta com a mesma dimensão da tela
    escurecimento = py.Surface((1280, 820))
    escurecimento.fill((0, 0, 0))  # Preto
    escurecimento.set_alpha(200)  # 0 é totalmente transparente, 255 é totalmente opaco
    # Desenhar a camada de escurecimento sobre a imagem
    objeto.tela.blit(escurecimento, (0, 0))
    # Desenhar os botões

    fonte = gerar_fonte(fonte_upheav, 30)
    largura_botao = 80
    altura_botao = 60
    reiniciar_text = fonte.render('JOGUE NOVAMENTE', True, white)
    altura_reiniciar = reiniciar_text.get_height()
    largura_reiniciar = reiniciar_text.get_width()

    x, y = centralizar(reiniciar_text)
    x -= 200
    y += 120
    while largura_botao < (largura_reiniciar + 15):
        largura_botao += 5

    while altura_botao < (altura_reiniciar + 15):
        altura_botao += 5

    reiniciar_button = py.draw.rect(objeto.tela, green, (x, y, largura_botao, altura_botao))

    reiniciar_rect = reiniciar_text.get_rect(topleft=(x + ((largura_botao - largura_reiniciar)/2), y + (altura_reiniciar/2)))
    objeto.tela.blit(reiniciar_text, reiniciar_rect)

    sair_text = fonte.render('SAIR', True, white)
    largura_sair = sair_text.get_width()
    altura_sair = sair_text.get_height()
    x += 360

    while largura_botao < (largura_sair + 10):
        largura_botao += 5

    sair_button = py.draw.rect(objeto.tela, red, (x, y, largura_botao, altura_botao))  # vermelho

    sair_rect = sair_text.get_rect(topleft=(x + ((largura_botao - largura_sair)/2), y + (altura_sair / 2)))
    objeto.tela.blit(sair_text, sair_rect)

    return reiniciar_button, sair_button


def acelerar(objeto):
    objeto.speed += 1



