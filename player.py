import pygame


class Player(object):
    def __init__(self, pos):
        self.initial_position = pos  # Armazena a posição inicial
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30).move(5, 5)  # X , Y , Largura, Altura
        self.image = pygame.image.load('damage.png')
        self.speed = 2

    def reset_position(self):
        # Redefine a posição do jogador para a posição inicial
        self.rect.topleft = self.initial_position

    def move(self, dx, dy):
        # Move cada eixo separadamente
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        from main import walls
        # Mover o retângulo
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Se você colide com uma parede, você muda de direção
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Move pra direita, bateu no lado esquerdo da parede
                    self.rect.right = wall.rect.left
                if dx < 0:  # Move para esquerda, bateu no lado direito da parede
                    self.rect.left = wall.rect.right
                if dy > 0:  # Move para baixo, bateu no lado de cima da parede
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Move para cima, bateu no lado de baixo da parede
                    self.rect.top = wall.rect.bottom
