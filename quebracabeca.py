import pygame
import random
from config import *


def desenhar_puzzle(objeto, puzzle_elemento):
    # Puzzle completo => frase propriamente dita
    objeto.fonte = pygame.font.Font(fonte_file, 40)
    puzzle_completo = objeto.fonte.render(puzzle_elemento, True, black)  # Isto é uma Surface

    palavra_vazia = ''
    tamanho = len(puzzle_elemento)

    while tamanho > 0:
        tamanho -= 1
        if puzzle_elemento[tamanho - 1] != ' ':
            palavra_vazia += '_ '

    palavra_display = objeto.fonte.render(palavra_vazia, True, black)

    puzzle_rect = puzzle_completo.get_rect(center=(430, 55))
    objeto.tela.blit(palavra_display, puzzle_rect)
    return palavra_vazia

def coletou_peca(puzzle_elemento):
    letras = list(puzzle_elemento)
    partes_a_revelar = []
    partes = len(letras) // 4
    resto = len(letras) % 4
    parte = ''

    for letra in letras:
        if len(parte) == partes and letras.index(letra) != len(letras) - (1 + resto):
            partes_a_revelar.append(parte)
        else:
            parte += letra
            if len(parte) > partes:
                partes_a_revelar.append(parte)

    random_index = random.randint(0, len(partes_a_revelar) - 1)

    adivinhou = partes_a_revelar[random_index]
    partes_a_revelar.remove(adivinhou)

    # display a nova palavra



def atualizar_puzzle(objeto, palavra_display):
    nova_palavra = palavra_display
    return nova_palavra