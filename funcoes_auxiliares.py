import pygame as py
from collision import check_collision


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
    reinicio_button = py.draw.rect(objeto.tela, '#307225', (300, 480, 250, 100))  # verde
    reinicio_text = objeto.fonte.render('JOGAR', True, 'black')
    objeto.tela.blit(reinicio_text, (365 + 10, 475 + 30))
    reinicio_text = objeto.fonte.render('NOVAMENTE', True, 'black')
    objeto.tela.blit(reinicio_text, (330 + 10, 500 + 30))
    sair_button = py.draw.rect(objeto.tela, '#a93535', (750, 480, 250, 100))  # vermelho
    sair_text = objeto.fonte.render('SAIR', True, 'black')
    objeto.tela.blit(sair_text, (835 + 10, 488 + 30))

    return reinicio_button, sair_button


def desenhar_puzzle(objeto, puzzle):
    objeto.tela.blit()


def acelerar(objeto):
    objeto.speed += 1
