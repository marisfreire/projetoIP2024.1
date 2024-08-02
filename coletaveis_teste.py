import pygame
import random

class Coletaveis():
    def __init__(self) -> None:
        self.coletaveis = {"cafe" : 4, "pasta" : 4, "vida" : 1}
        pass

    # verifica colisão entre dois retângulos
    def check_collision(rect1, rect2):
        return rect1.colliderect(rect2)
    
    # coletaveis
    def decrease(elemento):
        if self.coletaveis[elemento] > 0:
            self.coletaveis[elemento] -= 1

# cafe
cafe_static_width = 30
cafe_static_height = 30
cafe_x = random.randint(0, LARGURA_TELA - cafe_static_width)
cafe_y = random.randint(0, ALTURA_TELA - cafe_static_height)
# pasta
pasta_static_width = 30
pasta_static_height = 30
pasta_x = random.randint(0, LARGURA_TELA - pasta_static_width)
pasta_y = random.randint(0, ALTURA_TELA - pasta_static_height)


    # atualiza a posição do jogador
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    static_cafe = pygame.Rect(cafe_x, cafe_y,  cafe_static_width, cafe_static_height)
    static_pasta = pygame.Rect(pasta_x, pasta_y, pasta_static_width, pasta_static_height)

    # verifica colisão
    if check_collision(player_rect, static_cafe):
        
        cafe_x = random.randint(0, LARGURA_TELA - cafe_static_width)
        cafe_y = random.randint(0, ALTURA_TELA - cafe_static_height)
        
    if check_collision(player_rect, static_pasta):

        pasta_x = random.randint(0, LARGURA_TELA - pasta_static_width)
        pasta_y = random.randint(0, ALTURA_TELA - pasta_static_height)
        
    # preenche a tela 
    tela.fill(BLACK)

    # player e puzzles
    jogador = pygame.draw.rect(tela, BLUE, player_rect)
    cafe = pygame.draw.rect(tela, BRONW, static_cafe)
    pasta = pygame.draw.rect(tela, WHITE, static_pasta)
    
    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de frames por segundo
    pygame.time.Clock().tick(60)

pygame.quit()
